from flask import Flask, render_template, request, jsonify
import ast
import operator as op

app = Flask(__name__)

# Allowed operators
_allowed_operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def safe_eval(expr: str):
    """
    Safely evaluate math expressions using AST.
    Supports: numbers, + - * / ** %, unary +/-, parentheses.
    """
    try:
        node = ast.parse(expr, mode='eval')
    except Exception:
        raise ValueError("Invalid expression")

    def _eval(node):
        if isinstance(node, ast.Expression):
            node = node.body
        if isinstance(node, ast.Constant):  # Python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numeric constants allowed")
        if isinstance(node, ast.BinOp):
            if type(node.op) not in _allowed_operators:
                raise ValueError(f"Operator {type(node.op).__name__} not allowed")
            left = _eval(node.left)
            right = _eval(node.right)
            return _allowed_operators[type(node.op)](left, right)
        if isinstance(node, ast.UnaryOp):
            if type(node.op) not in _allowed_operators:
                raise ValueError(f"Unary operator {type(node.op).__name__} not allowed")
            return _allowed_operators[type(node.op)](_eval(node.operand))
        raise ValueError(f"Unsupported expression element: {type(node).__name__}")

    result = _eval(node)
    # Convert float to int if whole number
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json(force=True)
    expr = (data.get("expression") or "").strip()
    if not expr:
        return jsonify({"error": "Empty expression"}), 400
    try:
        value = safe_eval(expr)
        return jsonify({"result": value})
    except ZeroDivisionError:
        return jsonify({"error": "Division by zero"}), 400
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        return jsonify({"error": "Evaluation error"}), 400

if __name__ == "__main__":
    app.run(debug=True)
