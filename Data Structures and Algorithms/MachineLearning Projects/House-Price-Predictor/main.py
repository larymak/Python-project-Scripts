import pickle       #pip install pickle

from flask import Flask, render_template, request   #pip install flask

from flask_sqlalchemy import SQLAlchemy #pip install Flask-SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contact.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    concern = db.Column(db.String(500), nullable=False)
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.email} - {self.concern}"

# route
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form['query']
        if query == "own":
            return render_template('form.html')
        elif query == "rent":
            # we can make two seperate form for owner and tenant but we will imrpove it
            return render_template('formrent.html')
        else:
            # we will make a seprate Error page for this in furture
            return "Page Not found please select valid input"
    return render_template('index.html')


@app.route('/about', methods=["GET", "POST"])
def about():
    if request.method == "POST":
        email = request.form['email']
        concern = request.form['con']
        detail = Contact(email=email, concern=concern)
        db.session.add(detail)
        db.session.commit()
        return render_template('about.html', res=True)
    return render_template('about.html')


@app.route('/depend', methods=["GET", "POST"])
def depend():
    return render_template('depend.html')


@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == "POST":
        bhk = int(request.form['bhk'])  # range 1 to 3
        health = int(request.form['health'])  # range  1 to 5
        school = int(request.form['school'])  # range 1 to 4
        pool = int(request.form['pool'])  # 1 for exist 0 for not
        park = int(request.form['park'])  # range 1 to 5
        tax = int(request.form['tax'])  # range  2000 to 5000
        train = int(request.form['train'])  # range 1 to 5
        bus = int(request.form['bus'])  # range 1 to 5
        market = int(request.form['market'])  # range 1 to 5
        bank = int(request.form['bank'])  # range 3 to 5
        police_Station = int(request.form['police_Station'])  # range 1 to 3
        age = int(request.form['age'])  # range 1 to 20
        area = int(request.form['area'])         # 1 for urban 0 for rural
        mall = int(request.form['mall'])  # range 1 to 3
        # range 5 to 10 for rural 10 to 20 for urban
        floor = int(request.form['floor'])
        worship = int(request.form['worship'])  # range 1 to 12

    inf = clf.predict([[pool, train, bus, school, park, 1, market, health,
                        bank, bhk, tax, age, area, police_Station, mall, floor, worship]])[0]
    inf = -inf
    if area == 0:
        tag = "Lakh"
    else:
        inf = inf * 0.1
        tag = "Crore"
    inf = round(inf, 2)
    # print(inf)
    return render_template('show.html', str="Price", inf=inf, tag=tag)


@app.route('/formRent', methods=["GET", "POST"])
def form_Rent():
    if request.method == "POST":
        bhk = int(request.form['bhk'])  # range 1 to 3
        health = int(request.form['health'])  # range  1 to 5
        school = int(request.form['school'])  # range 1 to 4
        pool = int(request.form['pool'])  # 1 for exist 0 for not
        park = int(request.form['park'])  # range 1 to 5
        tax = int(request.form['tax'])  # range  2000 to 5000
        train = int(request.form['train'])  # range 1 to 5
        bus = int(request.form['bus'])  # range 1 to 5
        market = int(request.form['market'])  # range 1 to 5
        bank = int(request.form['bank'])  # range 3 to 5
        police_Station = int(request.form['police_Station'])  # range 1 to 3
        age = int(request.form['age'])  # range 1 to 20
        area = int(request.form['area'])         # 1 for urban 0 for rural
        mall = int(request.form['mall'])  # range 1 to 3
        # range 5 to 10 for rural 10 to 20 for urban
        floor = int(request.form['floor'])
        worship = int(request.form['worship'])  # range 1 to 12

    inf = clf.predict([[pool, train, bus, school, park, 1, market, health,
                        bank, bhk, tax, age, area, police_Station, mall, floor, worship]])[0]
    inf = -inf
    if area == 1:
        inf = inf - (inf*0.1*4)
    else:
        inf = inf - (inf*0.1*8)
    inf = round(inf, 2)

    # print(inf)
    return render_template('show.html', str="Rent", inf=inf, tag="thousand")


if __name__ == "__main__":
    app.run(debug=True)
