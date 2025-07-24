from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# 在此定义纪念日日期
anniversary_date = datetime(2024, 6, 16)

@app.route('/')
def index():
    current_date = datetime.now()
    delta = current_date - anniversary_date
    days_passed = delta.days
    return render_template('index.html', days_passed=days_passed, anniversary_date=anniversary_date.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    app.run(debug=False)
