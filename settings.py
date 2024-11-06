bridge_ip_address = ""
threshold_price_hue_plug_name = ""
plunge_price_hue_plug_name = ""

# https://en.wikipedia.org/wiki/Distribution_network_operator
region_code = "K"

# Use the local flask server to get the threshold price.
# If False, the script will use price_threshold_pence instead.
use_flask_server = True

# Ignored if use_flask_server is True
price_threshold_pence = 10

# Use fixed day/night Octopus Go prices, instead of dynamic Agile rates
octopus_go_mode = False
octopus_go_day_rate = 25.9
octopus_go_night_rate = 8.5
