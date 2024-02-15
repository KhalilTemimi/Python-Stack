from flask_app.controllers import emails
from flask_app.models.email import Email
from flask_app import app


if __name__ == "__main__":
    app.run(debug=True)