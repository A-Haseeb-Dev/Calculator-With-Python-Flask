# Calculator-With-Python-Flask
# Simple Web Calculator using Flask

A simple web-based calculator built with **Flask, HTML, CSS, and JavaScript**.  
Supports `+ − × ÷ % **` operations and parentheses with safe evaluation.

---

## Features

- Real-time display update
- Safe expression evaluation using Python AST
- Supports:
  - Addition (`+`)
  - Subtraction (`−`)
  - Multiplication (`×`)
  - Division (`÷`)
  - Modulo (`%`)
  - Exponent (`**`)
  - Parentheses
- Keyboard support for numbers and operators

---

## Prerequisites

- Python 3.8+
- pip (Python package manager)

---

## Installation & Setup

1. **Clone or download the repository**  

```bash
git clone https://github.com/your-username/WebCalculatorUsingFlask.git
cd WebCalculatorUsingFlask
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**
 - #### Windows (cmd):
```bash
venv\Scripts\activate
```
   
- ##### Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

- ##### Mac/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install flask
```
---

# Run the Application
 1. Make sure the virtual environment is activated.
 2. Run the Flask app:
```bash
python app.py
```

 3. **Open your browser and go to:**
```bash
http://127.0.0.1:5000
```

You should see the calculator interface.

---

# Project Structure

WebCalculatorUsingFlask/  
│  
├── app.py               # Flask backend  
├── templates/  
│   └── index.html       # Frontend HTML  
├── static/  
│   └── style.css        # CSS styles  
└── README.md            # Project instructions  

---

# Notes
- This project is for learning and development purposes only.
- Do not use this in production as-is; Flask's development server is not secure for production.
- All expressions are evaluated safely using Python AST to prevent malicious code execution.

---

# License
### MIT License

```bash
If you want, I can also make a **version with screenshots of the calculator UI and example expressions included**, which is great for GitHub README presentation.  
Do you want me to do that next?
```