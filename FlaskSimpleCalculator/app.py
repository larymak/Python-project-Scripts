from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    operand_1 = request.form.get("operand_1", type=int)
    operand_2 = request.form.get("operand_2", type=int)
    operator = request.form.get("operator")
    if(operand_2 == 0 and operator=='Division'):
        result='Invalid_operation'
    elif(operator == 'Addition'):
        result = operand_1 + operand_2
    elif(operator == 'Subtraction'):
        result = operand_1 - operand_2
    elif(operator == 'Multiplication'):
        result = operand_1 * operand_2
    elif(operator == 'Division'):
        result = operand_1 / operand_2
    else:
        result = 'Invalid_Choice'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)