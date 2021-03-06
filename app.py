from flask import Flask, send_from_directory
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@127.0.0.1:3306/Loans'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'unibank'

BASE_DIRS = os.path.dirname(os.path.abspath(__file__))

UPLOADED_FILES_DIR = os.path.join(BASE_DIRS, 'media')
app.config ['UPLOAD_FOLDER'] = UPLOADED_FILES_DIR
 
if not os.path.isdir(UPLOADED_FILES_DIR):
    os.mkdir(UPLOADED_FILES_DIR)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOADED_FILES_DIR, filename)

from controllers import *
from extensions import *
from models import *

if __name__ == '__main__':
    app.run(port=5000, debug=True)