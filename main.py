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
    local_timezone = pytz.timezone("Europe/London")
    now = datetime.now().astimezone(local_timezone)
    formatted_time = now.strftime("%c")

    # https://en.wikipedia.org/wiki/Distribution_network_operator
    if settings.octopus_go_mode:
        # Use fixed Octopus Go pricing
        cheap_night_start = now.replace(hour=0, minute=30, second=0, microsecond=0)
        cheap_night_end = now.replace(hour=5, minute=30, second=0, microsecond=0)
        if now > cheap_night_start and now < cheap_night_end:
            current_rate = settings.octopus_go_night_rate
        else:
            current_rate = settings.octopus_go_day_rate
    else:
        # Use dynamic Octopus Agile pricing
        agile = Agile(settings.region_code)
        current_rate = agile.get_current_rate()

    response = requests.get("http://localhost:8000/price").json()

    if response["use_timer"]:
        # Use timer for charging
        start_charge = datetime.fromisoformat(response["start_charge"]).astimezone(
            local_timezone
        )
        end_charge = datetime.fromisoformat(response["end_charge"]).astimezone(
            local_timezone
        )

        if now > start_charge and now < end_charge:
            # Start charging
            print(f"{formatted_time}: Timer start: {start_charge.strftime('%c')} | Start charging")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", True)
        elif now > end_charge:
            # Stop charging
            print(f"{formatted_time}: Timer stop: {end_charge.strftime('%c')} | Stop charging")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", False)
    else:
        # Use price threshold for charging
        price_threshold_pence = int(response["threshold"])
        if current_rate < price_threshold_pence:
            # Below threshold - start charging
            print(f"{formatted_time}: Current rate: {current_rate} | Threshold: {price_threshold_pence} | Start charging")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", True)
        else:
            # Above threshold - stop charging
            print(f"{formatted_time}: Current rate: {current_rate} | Threshold: {price_threshold_pence} | Stop charging")
            bridge.set_light(settings.threshold_price_hue_plug_name, "on", False)


if __name__ == "__main__":
    main()
