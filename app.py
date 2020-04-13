import os
from flask import Flask, render_template , flash, redirect, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask import request
import psycopg2


app = Flask(__name__ , 
            static_url_path='', 
            static_folder='static')

ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:A4notebook@localhost/nayamandi'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wuhjtupgzslvhg:bf7932ae550cdcd5d0ce67487555a1e2609af6360c83271f8c8276d38837f80b@ec2-34-233-186-251.compute-1.amazonaws.com:5432/dfoaochh60d0ct'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

#app.config['UPLOAD_FOLDER'] = 'C:\\Users\\Princekumar\\Desktop\\nayamand-flask\\upload_img'

db = SQLAlchemy(app)


class RegisterConsumer(db.Model):
    __tablename__ = 'register_consumer'
    id = db.Column(db.Integer, primary_key=True)
    regtype = db.Column(db.String(256))
    fname = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    Address = db.Column(db.String(256))
    enterdate = db.Column(db.String(256))
    pincode = db.Column(db.Integer)
    state = db.Column(db.String(256))
    distict = db.Column(db.String(256))
    tehsil = db.Column(db.String(256))
    photoid = db.Column(db.String(256))
    idno = db.Column(db.String(256), unique = True)
    mobno = db.Column(db.Integer, unique = True)
    altmobno = db.Column(db.Integer)
    emailaddr = db.Column(db.String(256), unique = True)
    altemailaddr = db.Column(db.String(256))
    bankname = db.Column(db.String(256))
    holderbankname = db.Column(db.String(256))
    bankaccno = db.Column(db.Integer, unique = True)
    cbankaccno = db.Column(db.Integer, unique = True)
    password = db.Column(db.Integer)
    cpassword = db.Column(db.Integer)
    
    
    def __init__(self,regtype, fname, gender, Address, enterdate, pincode, state, distict, tehsil, photoid, idno, mobno, altmobno, emailaddr, altemailaddr, bankname, holderbankname, bankaccno, cbankaccno, password, cpassword):
        self.regtype = regtype
        self.fname = fname
        self.gender = gender
        self.Address = Address
        self.enterdate = enterdate
        self.pincode = pincode
        self.state = state
        self.distict = distict
        self.tehsil = tehsil
        self.photoid = photoid
        self.idno = idno
        self.mobno = mobno
        self.altmobno = altmobno
        self.emailaddr = emailaddr
        self. altemailaddr = altemailaddr
        self.bankname = bankname
        self.holderbankname = holderbankname
        self.bankaccno = bankaccno
        self.cbankaccno = cbankaccno
        self.password = password
        self.cpassword = cpassword
        
        
class RegisterSeller(db.Model):
    __tablename__ = 'register_seller'
    id = db.Column(db.Integer, primary_key=True)
    regtype = db.Column(db.String(256))
    fname = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    Address = db.Column(db.String(256))
    enterdate = db.Column(db.String(256))
    pincode = db.Column(db.Integer)
    state = db.Column(db.String(256))
    distict = db.Column(db.String(256))
    tehsil = db.Column(db.String(256))
    photoid = db.Column(db.String(256))
    idno = db.Column(db.String(256), unique = True)
    mobno = db.Column(db.Integer, unique = True)
    altmobno = db.Column(db.Integer)
    emailaddr = db.Column(db.String(256), unique = True)
    altemailaddr = db.Column(db.String(256))
    bankname = db.Column(db.String(256))
    holderbankname = db.Column(db.String(256))
    bankaccno = db.Column(db.Integer, unique = True)
    cbankaccno = db.Column(db.Integer, unique = True)
    password = db.Column(db.Integer)
    cpassword = db.Column(db.Integer)
    
    
    def __init__(self,regtype, fname, gender, Address, enterdate, pincode, state, distict, tehsil, photoid, idno, mobno, altmobno, emailaddr, altemailaddr, bankname, holderbankname, bankaccno, cbankaccno, password, cpassword):
        self.regtype = regtype
        self.fname = fname
        self.gender = gender
        self.Address = Address
        self.enterdate = enterdate
        self.pincode = pincode
        self.state = state
        self.distict = distict
        self.tehsil = tehsil
        self.photoid = photoid
        self.idno = idno
        self.mobno = mobno
        self.altmobno = altmobno
        self.emailaddr = emailaddr
        self. altemailaddr = altemailaddr
        self.bankname = bankname
        self.holderbankname = holderbankname
        self.bankaccno = bankaccno
        self.cbankaccno = cbankaccno
        self.password = password
        self.cpassword = cpassword
    
    
app.config["DEBUG"] = True
app.secret_key = 'super secret key'


@app.route("/test")
def test():
    return "Server is Up & Running"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/commodity")
def commodity():
    if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else:
        return render_template('commodity.html')

@app.route("/license")
def license():
    if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else:
        return render_template('license.html')

@app.route("/catalog")
def catalog():
    return render_template('catalog.html')

@app.route("/product1_details")
def product1_details():
    return render_template('product1_details.html')

@app.route("/product2_details")
def product2_details():
    return render_template('product2_details.html')

@app.route("/product3_details")
def product3_details():
    return render_template('product3_details.html')

@app.route("/product4_details")
def product4_details():
    return render_template('product4_details.html')

@app.route("/payment_page1")
def payment_page1():
    return render_template('payment_page1.html')

@app.route("/payment_page2")
def payment_page2():
    return render_template('payment_page2.html')

@app.route("/payment_page3")
def payment_page3():
    return render_template('payment_page3.html')

@app.route("/payment_page4")
def payment_page4():
    return render_template('payment_page4.html')

@app.route("/price_details")
def price_details():
    '''if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else:'''
    return render_template('price_details.html')

@app.route("/predicted_prices")
def predicted_prices():
    '''if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else:'''
    return render_template('predicted_prices.html')

@app.route("/ml_working")
def ml_working():
    '''if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else:'''    
    return render_template('ml_working.html')

@app.route("/future_prediction")
def future_prediction():
    '''if not session.get('logged_in'):
        return render_template('login_consumers.html')
    else: '''   
    return render_template('future_prediction.html')

@app.route("/registration_consumers")
def register_consumer():
    return render_template('registration_consumers.html')

@app.route("/crop_price_pridiction_algorithm")
def crop_prediction():
    return render_template('crop_price_pridiction_algorithm.html')

@app.route("/registration_sellers")
def register_seller():
    return render_template('registration_sellers.html')

@app.route("/registration")
def register_buyer():
    return render_template('registration.html')

@app.route("/about_us")
def about_us():
    return render_template('about_us.html')

@app.route("/contact_us")
def contact_us():
    return render_template('contact_us.html')

@app.route("/features")
def features():
    return render_template('features.html')

@app.route("/login_consumers")
def login_consumers():
    return render_template('login_consumers.html')

@app.route("/login_sellers")
def login_sellers():
    return render_template('login_sellers.html')



@app.route("/register_consumer", methods=['GET','POST'])
def submit_consumer():
    if request.method == 'POST':
        regtype = 'Consumer'
        fname = request.form['fname']
        gender = request.form['gender']
        Address = request.form['Address']
        enterdate = request.form['enterdate']
        pincode = request.form['pincode']
        state = request.form['state']
        distict = request.form['distict']
        tehsil = request.form['tehsil']
        photoid = request.form['photoid']
        idno = request.form['idno']
        mobno = request.form['mobno']
        altmobno = request.form['altmobno']
        emailaddr = request.form['emailaddr']
        altemailaddr = request.form['altemailaddr']
        bankname = request.form['bankname']
        holderbankname = request.form['holderbankname']
        bankaccno = request.form['bankaccno']
        cbankaccno = request.form['cbankaccno']
        password = str(request.form['password'])
        cpassword = str(request.form['cpassword'])
       
        if db.session.query(RegisterConsumer).filter(RegisterConsumer.mobno == mobno).count() == 0:
            data = RegisterConsumer(fname,regtype,gender,Address,enterdate,pincode,state,distict,tehsil,photoid,idno,mobno,altmobno,emailaddr,altemailaddr,bankname,holderbankname,bankaccno,cbankaccno,password,cpassword)
            db.session.add(data)
            db.session.commit()
            return "submitted"
        else:
            return 'already exist'
        
        return "successfull"

@app.route("/register_seller", methods=['GET','POST'])
def submit_seller():
    if request.method == 'POST':
        regtype = 'Seller'
        fname = request.form['fname']
        gender = request.form['gender']
        Address = request.form['Address']
        enterdate = request.form['enterdate']
        pincode = request.form['pincode']
        state = request.form['state']
        distict = request.form['distict']
        tehsil = request.form['tehsil']
        photoid = request.form['photoid']
        idno = request.form['idno']
        mobno = request.form['mobno']
        altmobno = request.form['altmobno']
        emailaddr = request.form['emailaddr']
        altemailaddr = request.form['altemailaddr']
        bankname = request.form['bankname']
        holderbankname = request.form['holderbankname']
        bankaccno = request.form['bankaccno']
        cbankaccno = request.form['cbankaccno']
        password = str(request.form['password'])
        cpassword = str(request.form['cpassword'])
        #photoidimg = request.files['sign']
        #photoidimg.save(secure_filename(photoidimg.filename))
       
        if db.session.query(RegisterSeller).filter(RegisterSeller.mobno == mobno).count() == 0:
            data = RegisterSeller(regtype,fname,gender,Address,enterdate,pincode,state,distict,tehsil,photoid,idno,mobno,altmobno,emailaddr,altemailaddr,bankname,holderbankname,bankaccno,cbankaccno,password,cpassword)
            db.session.add(data)
            db.session.commit()
            return "submitted"
        else:
            return 'already exist'
        
        return "successfull"


@app.route('/login_consumer', methods=['GET','POST'])
def login_consumer():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        if db.session.query(RegisterConsumer).filter(RegisterConsumer.id == id, RegisterConsumer.password == password).first():
            session['logged_in'] = True
            flash('successful login')
            return render_template('catalog.html')
        else:
            flash('wrong password!')
            return render_template('login_consumers.html')
        

@app.route('/login_seller', methods=['GET','POST'])
def login_seller():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']
        if db.session.query(RegisterSeller).filter(RegisterSeller.id == id, RegisterSeller.password == password).first():
            session['logged_in'] = True
            flash('successful login')
            return render_template('catalog.html')
        else:
            flash('Login Failed')
            return render_template('login_sellers.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


if __name__ == '__main__':
    app.run()

