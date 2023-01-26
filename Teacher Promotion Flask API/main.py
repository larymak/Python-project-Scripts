from flask import Flask, render_template, request, redirect
from load_process_prediction import label_encoder, process_and_predict

#Declaring the flask object
app = Flask(__name__)


#defining the home route
@app.route('/')
def home():
    return render_template('index.html')


#defing the result route
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':               #use args if using get method
        firstName = request.form['fname']
        lastName = request.form['lname']
        age = request.form['age']
        experience = request.form['experience']
        grade = request.form['grade']
        lastPromotion = request.form['lpromotion']
        promo1 = request.form['promo1']
        promo2 = request.form['promo2']
        promo3 = request.form['promo3']
        data = [age, experience, grade, lastPromotion, label_encoder(promo1), label_encoder(promo2), label_encoder(promo3)]
        prediction = process_and_predict(data)
       
        #redirecting the user to the  page    
        return render_template('result.html', firstName=firstName, lastName=lastName, prediction=prediction)
    else:
        return redirect('/')
        
