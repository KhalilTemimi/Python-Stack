from flask import Flask,render_template, request,redirect,session

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def counter():  
    if 'visit' in session:
        print('key exists!')
        session['visit']+= 1
    else:
        print("key 'counter' does NOT exist")
        session['visit']= 0 
    if 'counter' in session:
        print('key exists!')
        session['counter']+= 1
    else:
        print("key 'counter' does NOT exist")
        session['counter']= 0
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/increment')
def increment():
    session['counter']+= 2
    return render_template('/index.html')

@app.route('/increment_num', methods=['post'])
def increment_num():
    session['counter']+=int(request.form['number'])
    return render_template('/index.html')

if __name__ == ('__main__'):
    app.run(debug=True)