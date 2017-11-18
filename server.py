import sys

from flask import Flask, send_from_directory, jsonify, request
app = Flask(__name__, static_folder='views')

data = {
  "dreams": [
    "Find and count some sheep",
    "Climb a really tall mountain",
    "Wash the dishes"
  ]
}

def format(f, p1, p2):
  f = f.split("\n")
  w = u""
  capitalizeNext = False
  for line in f:
    line = line.strip()
    if len(line) == 23 and line.count(":") == 4 and line.count(".") == 2 and line.count(",") == 1:
      continue
    if line == "":
      continue
    if ":" in line:
      w = w + "\n\n"
  
    punctuatedLine = u""
    for c in line:
      if c == '1' or c== '2':
        name = unicode(p1) if c == '1' else unicode(p2)
        c = u"\n\n"
        c = c + name
        c = c + u": "
        capitalizeNext = True
        punctuatedLine += c
        continue
      
      if capitalizeNext and not c.isspace():
        c = c.upper()
        capitalizeNext = False
      punctuatedLine += c
      if c == ':' or c == '.' or c == '?':
        capitalizeNext = True
    w = w + (punctuatedLine + " ")
      
  return w

@app.route("/")
def hello():
  return app.send_static_file('index.html')

@app.route("/dreams", methods=["GET"])
def get_dreams():
  return jsonify(**data)

@app.route("/dreams", methods=["POST"])
def add_dream():
  #data["dreams"].append(request.args["dream"])
  output = format(request.form["sbv"], request.form["person1"], request.form["person2"])
  return u'<pre>{}</pre>'.format(output) #'"OK"'
  #return 'You entered: ' + (request.form['sbv']) + ", by " + request.form['person1']

@app.route('/<path:path>')
def send_static(path):
  return send_from_directory('public', path)

if __name__ == "__main__":
  app.run()
