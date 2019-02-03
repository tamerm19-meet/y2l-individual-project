from databases import *
from flask import Flask, flash, render_template, url_for, redirect, request
from flask import session as login_session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')
    if request.method == 'POST':
        result = request.form['data']        
        matches = search(result)
        if len(matches) == 0:
            flash('No matching results for: '+result)
            return redirect(url_for('home'))
            return render_template('searchResult.html',matches=matches,log=log)







@app.route('/postmalone')
def postmalone():
    
	return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)

