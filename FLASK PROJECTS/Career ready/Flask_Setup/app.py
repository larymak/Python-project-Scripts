from flask import Flask, render_template, request, session, flash, redirect, url_for, g
# from flask_bcrypt import bcrypt
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
# from models import User


app = Flask(__name__)
app.secret_key = 'somesecretkeyiknow'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLAlCHEMY_ECHO']= True

db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return f"User('{self.email})'"

# class User:
#     def __init__(self,id,email,password):
#         self.id=id
#         self.email=email
#         self.password=password
    
#     def __repr__(self):
#         return f'<User:{self.email}>'

# users=[]
# users.append(User(id=1, email='mad@gmail.com', password='madhu001'))
# print(users)



# @app.before_request
# def before_request():
#     if 'user_id' in session:
#         user = [x for x in users if x.id==session['user_id']][0]
#         g.user = user
#     else:
#         g.user = None

@app.route('/hometest')
def hometest():
    return render_template('hometest.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id',None)

        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        # user =[x for x in users if x.email==email][0]
        if user and user.password == password:
            # return render_template('hometest.html')
            return redirect(url_for('hometest'))
        else:
            flash("Wrong login details!!")
        # return redirect(url_for('login'))
    return render_template('login.html')
    

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        email = request.form['email']
        password= request.form['password']
        # hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=password)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        flash('Your registersuccesss!')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/profile')
def profile():
    # if not g.user:
    #     return redirect(url_for('login'))

    return render_template('profile.html')




@app.route('/predict',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      i = 0
      print(result)
      res = result.to_dict(flat=True)
      print("res:",res)
      arr1 = res.values()
      arr = ([value for value in arr1])

      data = np.array(arr)

      data = data.reshape(1,-1)
      print(data)
      loaded_model = pickle.load(open("careerl.pkl", 'rb'))
      predictions = loaded_model.predict(data)
     # return render_template('testafter.html',a=predictions)
      
      print(predictions)
      pred = loaded_model.predict_proba(data)
      print(pred)
      #acc=accuracy_score(pred,)
      pred = pred > 0.05
      #print(predictions)
      i = 0
      j = 0
      index = 0
      res = {}
      final_res = {}
      while j < 17:
          if pred[i, j]:
              res[index] = j
              index += 1
          j += 1
      # print(j)
      #print(res)
      index = 0
      for key, values in res.items():
          if values != predictions[0]:
              final_res[index] = values
              print('final_res[index]:',final_res[index])
              index += 1
      #print(final_res)
      jobs_dict = {0:'AI ML Specialist',
                   1:'API Integration Specialist',
                   2:'Application Support Engineer',
                   3:'Business Analyst',
                   4:'Customer Service Executive',
                   5:'Cyber Security Specialist',
                   6:'Data Scientist',
                   7:'Database Administrator',
                   8:'Graphics Designer',
                   9:'Hardware Engineer',
                   10:'Helpdesk Engineer',
                   11:'Information Security Specialist',
                   12:'Networking Engineer',
                   13:'Project Manager',
                   14:'Software Developer',
                   15:'Software Tester',
                   16:'Technical Writer'}
                
      #print(jobs_dict[predictions[0]])
      job = {}
      #job[0] = jobs_dict[predictions[0]]
      index = 1
     
        
      data1=predictions[0]
      print(data1)
      return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)




if __name__ == '__main__':
    app.run(debug=True)