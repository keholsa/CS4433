from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
#FOR DEV PURPOSES ONLY, login.html TAKES DOMAIN '/'
@app.route('/login')
def hello():
    return render_template("login.html")
@app.route('/tutorupdate')
def tutee():
    return render_template("tutee.html")

if __name__ == '__main__':
    app.run(debug=True)
