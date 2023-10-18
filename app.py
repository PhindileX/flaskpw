from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if(request.method=="POST"):
        print(request.form["submit_results"])
        match (request.form["submit_results"]):
            case "About":
                # print("in about")
                return(render_template("about.html"))

    return(render_template("index.html"))

@app.route("/about", methods=["POST"])
def about():
    return(render_template("about.html"))


if __name__=="__main__":
    app.secret_key = "If you can't love yourself, how the hell you gonna love somebody else - RuPaul"
    app.run(host="0.0.0.0", debug=True)