from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

notes = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=False)  # Disable debug mode for deployment

# use app.run(debug=True) for enabling the debug mode
