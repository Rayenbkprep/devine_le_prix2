from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def demo():
    return"Coucou l'isep"


@app.route('/coucou')
def coucou():
    return render_template("coucou.html")
app.run()