from flask import Flask, render_template, request


app = Flask(__name__)

price_threshold = 8


@app.route("/", methods=["GET", "POST"])
def set_price_threshold():
    """
    Interface to set the price threshold
    """
    global price_threshold
    if request.method == "POST":
        price_threshold = request.form["price"]
        print(f"New price: {price_threshold}")
        return render_template("index.html", price_threshold=price_threshold, show_toast=True)

    else:
        return render_template("index.html", price_threshold=price_threshold, show_toast=False)


@app.route("/price")
def get_price_threshold():
    """
    Returns JSON response of the currently set price threshold
    """
    response = {"threshold": price_threshold}
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
