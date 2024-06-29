from OctopusAgile import Agile
from phue import Bridge
from datetime import datetime, timedelta
import requests
import settings
import pytz


def main():
    bridge = Bridge(settings.bridge_ip_address)
    bridge.connect()
    bridge.get_api()

    # https://en.wikipedia.org/wiki/Distribution_network_operator
    agile = Agile(settings.region_code)
    current_rate = agile.get_current_rate()
    print(f"Current rate: {current_rate}")

    response = requests.get("http://localhost:8000/price").json()

    if response["use_timer"]:
        # Use timer for charging
        local_timezone = pytz.timezone("Europe/London")
        start_charge = datetime.fromisoformat(response["start_charge"]).astimezone(
            local_timezone
        )
        end_charge = datetime.fromisoformat(response["end_charge"]).astimezone(
            local_timezone
        )
        now = datetime.now().astimezone(local_timezone)

        if now > start_charge and now < end_charge:
            # Start charging
            print("Start charging (timer)")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", True)
        elif now > end_charge:
            # Stop charging
            print("Stop charging (timer)")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", False)
    else:
        # Use price threshold for charging
        price_threshold_pence = int(response["threshold"])
        print(f"Price threshold: {price_threshold_pence}")
        if current_rate < price_threshold_pence:
            # Below threshold - start charging
            print("Start charging (threshold)")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", True)
        else:
            # Above threshold - stop charging
            print("Stop charging (threshold)")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", False)


if __name__ == "__main__":
    main()
