from OctopusAgile import Agile
from phue import Bridge
import settings


def main():
    bridge = Bridge(settings.bridge_ip_address)
    bridge.connect()
    bridge.get_api()

    # https://en.wikipedia.org/wiki/Distribution_network_operator
    agile = Agile(settings.region_code)
    current_rate = agile.get_current_rate()

    print(current_rate)

    if current_rate < settings.price_threshold_pence:
        bridge.set_light(settings.hue_plug_name, "on", True)
    else:
        bridge.set_light(settings.hue_plug_name, "on", False)

if __name__ == "__main__":
    main()
