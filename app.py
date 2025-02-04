from flask import Flask,render_template


app = Flask(__name__)

JOBS=[
    {
        "id":1,
        "title":"Data Analyst",
        "location":"Nepal",
        "salary":"1M"
    
},
    {
        "id":2,
        "title":"Security Engineer",
        "location":"Nepal",
        "salary":"3M"
    
},
    {
        "id":3,
        "title":"Product Engineer",
        "location":"Nepal",
        "salary":"4M"
    
}
    ]

@app.route('/')
def user():
    return render_template('home.html',jobs=JOBS)

if __name__ == '__main__':
    app.run(debug = True, port = 8000,host = 0.0) 