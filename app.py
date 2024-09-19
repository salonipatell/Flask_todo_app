from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.column(db.Integer,primary_key=True)
    title=db.column(db.String(200),nullable=False)
    desc=db.column(db.String(500),nullable=False)
    date_created=db.column(db.DateTime,default=datetime.now)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/products')
def products():
    return "Hello this is product page"

if __name__=="__main__":
    # app.run(debug=True)  #---------->default it will run on 5000 port--->Running on http://127.0.0.1:5000
    app.run(debug=True,port=8000) #------>Running on http://127.0.0.1:8000