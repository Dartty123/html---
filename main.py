from flask import Flask, render_template


app = Flask(__name__)



@app.get("/")
def index():
    return render_template("index_pizza.html",title="ПІЦЕРІЯ")


@app.get("/menu/")
def bootstrap_demo():
    return render_template("menu.html")


if __name__ == "__main__":
    app.run(debug=True)