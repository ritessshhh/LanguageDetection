from flask import Flask, render_template, url_for, request, redirect
from model.model import predict_language

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST' and request.form['language'] != '':
        email = request.form['email']
        print(email)
        language = predict_language(request.form['language'])
        print(language)
        alert = '<div class="alert alert-success mt-3" role="alert"> ' + language +'! 🎉</div>'
    else:
        alert = ''

    print(alert)
    return render_template("index.html", alert=alert)

@app.route('/language')
def language():
    return render_template("language.html")

if __name__ == "__main__":
    app.run(debug=True)