from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template("index.html", name=name)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/sign-up", methods=["GET"])
def sign_up():
    
    if request.method == "GET":
        key_value = request.args['key_data']
        print(key_value)
        url = "https://www.google.com/recaptcha/api/siteverify"

        myobj = {"secret": "6Ld9T-AUAAAAAN47aUFvI20gIeY75yy0bnr8cJy0", "response" : key_value}
        
        x = requests.post(url, data = myobj)

        print(x.text)


        # req = request.form
        # return redirect(request.url)
    return render_template("sign_up.html")


app.run(host='0.0.0.0', port=5000, debug=True)





