from OctopusAgile import Agile
from phue import Bridge
import requests
import settings


def main():
    bridge = Bridge(settings.bridge_ip_address)
    bridge.connect()
    bridge.get_api()

    # https://en.wikipedia.org/wiki/Distribution_network_operator
    agile = Agile(settings.region_code)
    current_rate = agile.get_current_rate()

    print(current_rate)

    if settings.use_flask_server:
        response = requests.get("http://localhost:8000/price")
        price_threshold_pence = response.json()
    else:
        price_threshold_pence = settings.price_threshold_pence

    # Below threshold
    if current_rate < price_threshold_pence:
        bridge.set_light(settings.threshold_price_hue_plug_name, "on", True)
    else:
        bridge.set_light(settings.threshold_price_hue_plug_name, "on", False)

    # Plunge pricing
    if current_rate < 0:
        bridge.set_light(settings.plunge_price_hue_plug_name, "on", True)
    else:
        bridge.set_light(settings.plunge_price_hue_plug_name, "on", False)


if __name__ == "__main__":
    main()
