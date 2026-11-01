from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler
import sqlite3

app = Flask(__name__)


@app.route("/index.html", methods=["GET"])  # Only GET - just viewing
@app.route("/", methods=["POST", "GET"])  # Both GET and POST - can handle forms
def index():
    language = request.args.get("language")
    if language:
        data = dbHandler.listExtensionByLanguage(language)
    else:
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
        try:
            # Insert into database
            dbHandler.insertContact(email, name)

            # Render template with success message
            return render_template("/add.html", is_done=True)

        except sqlite3.IntegrityError:
            # Duplicate email - show error message
            error_message = "This email address is already subscribed. Please use a different email."
            return render_template(
                "/add.html", error=error_message, email=email, name=name
            )
    else:
        # GET request - display empty form
        return render_template("/add.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
