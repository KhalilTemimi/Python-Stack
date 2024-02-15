from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email
from flask_app import app

@app.route('/')
def home():
    return render_template('email_validation.html')

@app.route('/process', methods=['post'])
def create():
    if not Email.validate_entry(request.form):
        return redirect('/')
    data = {
        'email' : request.form['email'],
    }
    Email.save(data)
    return redirect('/result')

@app.route('/destroy/<int:id>')
def destroy(id):
    data = {"id":id}
    Email.destroy(data)
    return redirect('/result')


@app.route('/result')
def display_info():
    emails = Email.get_all()
    last_email = Email.show_last()
    return render_template('emails_list.html', emails = emails, last_email = last_email)