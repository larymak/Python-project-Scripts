from flask import Flask, render_template, request, jsonify
# from handle_calculation import calculate

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('form.html')

@app.route("/results", methods=['POST','GET'])
def predict():
    if request.method == 'POST' and 'operand_1' in request.form and 'operand_2' in request.form and 'operator' in request.form:
        operand_1 = float(request.form.get('operand_1'))
        operand_2 = float(request.form.get('operand_2'))
        operator = request.form.get('operator')
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
    # result = calculate(operand_1, operand_2, operator)
    return render_template("form.html",prediction_text=str(result))

if __name__ == '__main__':
    app.run(debug=True)