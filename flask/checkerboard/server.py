from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/<int:x>/<int:y>/<string:first>/<string:second>')
def default_checkerboard(x,y,first,second):
    return render_template("index.html", x=x, y=y, first=first, second=second)



if __name__=="__main__": 
    app.run(debug=True)