#encoding:utf-8
from flask  import flash,url_for,render_template,redirect
from sayhello import app,db
from sayhello.forms import  HelloForm
from sayhello.models import Information
@app.route("/",methods=["GET","POST"])
def index():
    form=HelloForm()
    if form.validate_on_submit():
        Age=form.Age.data
        Income=form.Income.data
        Weight=form.Weight.data
        Height=form.Height.data
        Marriage=form.Marriage.data
        Sex=form.Sex.data
        Card_ID=form.Card_Id.data
        information=Information(Age=Age,Income=Income,Height=Height,Weight=Weight,Marriage=Marriage,Sex=Sex,Card_ID=Card_ID)
        db.session.add(information)
        db.session.commit()
        flash('Your message has been updated')
        return  redirect(url_for("index"))
    if not form.validate_on_submit():
        print(form.errors)
    information=Information.query.all()
    return render_template("index.html",form=form,information=information)



