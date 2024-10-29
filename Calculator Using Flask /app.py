from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form.get('num1', type=float)
    num2 = request.form.get('num2', type=float)
    operation = request.form.get('operation')

    result = None
    error = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            error = "Cannot divide by zero"
        else:
            result = num1 / num2

    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
