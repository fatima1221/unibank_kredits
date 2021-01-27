from flask import render_template, url_for, request, redirect
from models import *
from app import app
from forms import LoanForm
from extensions import db
from upload import save_file

@app.route('/loans')
def loans():
    loans = Loan.query.all()
    return render_template("index.html", loans=loans)

@app.route('/addloan', methods=['GET', 'POST'])
def addloan():
    form = LoanForm()
    if request.method == 'POST' and form.validate:
        title = form.title.data
        description = form.description.data
        img = save_file(form.img.data)

        loans = Loan(title, description, img)
        loans.save()

        return redirect('/loans')
    return render_template('addloan.html', form=form)