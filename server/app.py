from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return parameter  # Return plain text

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    # Create a list of numbers from 0 to the parameter (inclusive)
    numbers = '\n'.join(str(i) for i in range(parameter + 1))  # Include the parameter in the output
    return numbers  # Return as plain text

# Math operations route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation in ['/', 'div']:  # Handle both "div" and "/" for division
        if num2 == 0:
            return 'Cannot divide by zero', 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400

    return str(result)  # Return the result as plain text

if __name__ == '__main__':
    app.run(debug=True)
