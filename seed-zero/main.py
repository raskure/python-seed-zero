from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
  return "<p>Hello, World!</p>"

@app.route("/menu")
def menu():
  return render_template("menu.html")

@app.route("/app/<func>", methods=["GET", "POST"])
def assigner(func):
  if request.method == "POST":
    name = request.form["name"]
    pass
  else:
    name = request.args.get("name", "")
    pass
  print(name)
  return func

@app.route("/api/<data>")
def api(data):
  app.logger.debug(data)
  data = "" + data
  return { "a": 1, "b": 2, "c": data }