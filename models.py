from extensions import *
from app import app 

class Loan(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    img = db.Column(db.String(255), nullable=True)
   
    def __repr__(self):
        return self.title

    def __init__(self, title, description, img):
        self.title = title
        self.description = description
        self.img = img

    def save(self):
        db.session.add(self)
        db.session.commit()
       
