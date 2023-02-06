from flask import Flask, request, json

app = Flask(__name__)

@app.route("/")
def Home():
    return "This is initaial Page : Home Page"

@app.route("/about")
def About():
    return "This is about page"

@app.route("/contact" , methods=["GET", "POST"])
def Contact():
    if request.method == "GET":
        return "This is contact page -- get method"
    if request.method == "POST":
        data = json.loads(request.data)
        data['name'] = data['name'] + " " + "ramesh"
        print(data)
        return data
    

if __name__ == '__main__':
    app.run(debug=True)
    
# get method => Read
# post => Create
# put => update
# delete => delete