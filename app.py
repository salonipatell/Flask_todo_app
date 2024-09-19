from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.now)

with app.app_context():
    db.create_all()

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route('/')
def hello_world():
    return "<h2>Hello this is basic flask learning example</h2>"


@app.route('/products')
def products():
    return "Hello this is product page"


@app.route('/create')
def create():
    todo=Todo(title="First Title",desc="Stock invest")
    db.session.add(todo)
    db.session.commit()
    return "done"


@app.route('/alltodos',methods=['GET','POST'])
def show_todo():
    if request.method=='POST':
        print(request.form.get('title'))
    alltodo=Todo.query.all()
    return render_template('index.html',all_todo=alltodo)

if __name__=="__main__":
    # app.run(debug=True)  #---------->default it will run on 5000 port--->Running on http://127.0.0.1:5000
    app.run(debug=True,port=8000) #------>Running on http://127.0.0.1:8000