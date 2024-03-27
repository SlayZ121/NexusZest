from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>text changed</h1>'

@app.route('/about/{user}')
def about_page():
    return '<h1> this about page is of  {user}</h1>'

if __name__=="__main__":
    app.run(debug=True)