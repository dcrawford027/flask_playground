from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def showPlayPage():
    return render_template("index.html", times=3)

@app.route("/play/<int:times>")
def displayBoxes(times):
    return render_template("index.html", times=times)

@app.route("/play/<int:times>/<color>")
def displayColoredBoxes(times, color):
    return render_template("index.html", times=times, color=color)

if __name__ == "__main__":
    app.run(debug=True)