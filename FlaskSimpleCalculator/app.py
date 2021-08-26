from flask import Flask, render_template, request
from handle_calculation import calculate

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
    result = calculate(operand_1, operand_2, operator)
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)