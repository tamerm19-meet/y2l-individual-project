from flask import *
from flask import session as login_session
from model import *
from database import *

app = Flask(__name__)
app.secret_key=b'romkrtg8547854ufruh'
@app.route('/',methods=['GET','POST'])
def homepage():
    if 'Email' in login_session:
        a=login_session['FirstName']
        articles=GetAllArticles()
        
        return render_template("home.html",a=a,articles=articles)
    else:
        return redirect(url_for('choose'))


@app.route('/actualsignup',methods=['GET','POST'])
def actualsignup():
    a=""
    if request.method == 'POST':
        firstName=request.form['fname']
        lastName=request.form['lname']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm']
        available=True
        if confirm == password and '@' in email and '.com' in email:
            AddTeacher(firstName,lastName,email,password,)
            return redirect(url_for('homepage'))
        elif '@' not in email or '.com' not in email:
            a="Invalid email"
            return render_template("actualsignup.html",a=a)
        else:
            a="Passwords don't match"
            return render_template("actualsignup.html",a=a)
    else:
        return render_template("actualsignup.html")

@app.route('/login',methods=['GET','POST'])
def login():
    txt=""
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        student = GetStudentByEmail(email)
        teacher =GetTeacherByEmail(email)
        if student!=None:
            if student.Password==password:
                login_session['FirstName']=student.FirstName
                login_session['LastName']=student.LastName
                login_session['Email']=student.Email
                login_session['Password']=student.Password
                return redirect(url_for('homepage'))
            else:
                txt="Incorrect password"
        elif teacher!=None:
            if teacher.Password==password:
                login_session['FirstName']=teacher.FirstName
                login_session['LastName']=teacher.LastName
                login_session['Gender']=teacher.Gender
                login_session['Email']=teacher.Email
                login_session['Password']=teacher.Password
                return redirect(url_for('homepage'))
            else:
                txt="Incorrect password"
        else:
            txt="Account doesn't exist"
    
    return render_template("login.html",txt=txt)

@app.route('/welcome',methods=['GET','POST'])
def choose():
    
    if request.method == 'POST':
        if request.form['choice'] == "student":
            return redirect(url_for('signUp'))
        elif request.form['choice'] == "teacher":
            return redirect(url_for('actualsignup'))
        else:
            return redirect(url_for('login'))
    return render_template("welcome.html")

@app.route('/post',methods=['GET','POST'])
def post():

    if request.method == 'POST':
        
        title=request.form['atitle']
        content=request.form['content']
        name=login_session['FirstName']
        email=login_session['Email']
        articles=GetAllArticles()
        for article in articles:
            if article.Title==title:
                note="Article already exists"
                return render_template("post.html",note=note)
        AddArticle(title,content,name,email)
        return redirect(url_for('homepage'))
    else:
        return render_template("post.html")
    
@app.route('/logout',methods=['GET','POST'])
def logout():
    login_session.clear()
    return choose()
