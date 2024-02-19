from flask import Flask , render_template,request,flash
app= Flask(__name__)
app.secret_key = "zkjzjjsjjjs3652"

@app.route("/hello")
def index():
  flash("what's your name?")
  return render_template("index.html")
@app.route("/greet", methods=["GET", "POST"])

def greet():

   flash("hi " + str(request.form['name_input']) + ", great to see you ")
   return render_template("index.html")
