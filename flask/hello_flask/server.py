from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html")  # Return the string 'Hello World!' as a response
# import statements, maybe some other routes
    
@app.route('/dojo')
def success():
    return "Hello Dojo !"

@app.route('/say/<string:name>') 
def hi(name):
    return "Hi, " + name+" !"

@app.route('/repeat/<int:id>/<string:name>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def repeat(id,name):
    return render_template("repeat.html",id = id, name = name)

@app.errorhandler(404)
def error(error):
    return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

