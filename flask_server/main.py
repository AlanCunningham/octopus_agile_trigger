from flask import Flask, render_template, request
from datetime import datetime
import pytz


app = Flask(__name__)

use_timer = None
price_threshold = 8
start_charge_date = None
start_charge_time = None
end_charge_date = None
end_charge_time = None


@app.route("/", methods=["GET", "POST"])
def set_price_threshold():
    """
    Interface to set the price threshold
    """
    global price_threshold
    global use_timer
    global start_charge_date
    global start_charge_time
    global end_charge_date
    global end_charge_time

    print(start_charge_date)

    if request.method == "POST":
        print(request.form)
        use_timer = request.form.get("useTimer")
        price_threshold = request.form["price"]
        start_charge_date = request.form["start-date"]
        start_charge_time = request.form["start-time"]
        end_charge_date = request.form["end-date"]
        end_charge_time = request.form["end-time"]

        return render_template(
            "index.html",
            use_timer="checked" if use_timer else "",
            price_threshold=price_threshold,
            start_charge_date=start_charge_date,
            start_charge_time=start_charge_time,
            end_charge_date=end_charge_date,
            end_charge_time=end_charge_time,
            show_toast=True,
        )

    else:
        return render_template(
            "index.html",
            use_timer="checked" if use_timer else "",
            price_threshold=price_threshold,
            start_charge_date=start_charge_date,
            start_charge_time=start_charge_time,
            end_charge_date=end_charge_date,
            end_charge_time=end_charge_time,
            show_toast=False,
        )


@app.route("/price")
def get_price_threshold():
    """
    Returns JSON response of the currently set price threshold
    """

    # Convert the start/end date and times into datetimes
    datetime_format = "%a %d %b %Y %H:%M"
    start_date_time = datetime.strptime(
        f"{start_charge_date} {start_charge_time}",
        datetime_format,
    )

    end_date_time = datetime.strptime(
        f"{end_charge_date} {end_charge_time}", datetime_format
    )

    response = {
        "use_timer": use_timer,
        "threshold": price_threshold,
        "start_charge": start_date_time.isoformat(),
        "end_charge": end_date_time.isoformat(),
    }
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
