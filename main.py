from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])  # Only GET - just viewing
@app.route("/", methods=["POST", "GET"])  # Both GET and POST - can handle forms
def index():
    data = dbHandler.listExtension()
    return render_template("/index.html", content=data)


@app.route("/add.html", methods=["POST", "GET"])
def add():
    """
    Handle the contact form page.

    GET request: Display empty form
    POST request: Process form submission and display confirmation
    """
    if request.method == "POST":
        # Form was submitted - extract data
        email = request.form["email"]
        name = request.form["name"]

        # Insert into database
        dbHandler.insertContact(email, name)

        # Render template with success message
        return render_template("/add.html", is_done=True)
    else:
        # GET request - display empty form
        return render_template("/add.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
