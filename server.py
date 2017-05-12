from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/process', methods=['post'])
def new():
    name = request.form['name']
    print name
    return redirect('/')



app.run(debug=True) # run our server
