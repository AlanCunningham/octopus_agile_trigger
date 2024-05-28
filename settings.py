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
