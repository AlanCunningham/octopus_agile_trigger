# Octopus Agile Trigger

A small script that turns toggles the state of Philips Hue plugs based on the current Octopus Agile price.

## Overview
This is intended to be run every half an hour on a cronjob.  When the price drops below a given threshold,
it turns on a Philips Hue plug.  I then have a Google Home automation which uses the Hue plug state as a trigger
to run other automations in the house (e.g. turn on the car charger, dishwasher, and send a broadcast via Google
speakers etc). When the price goes back above the threshold, it turns the Hue plug off.

Similarly, when the price goes below 0, the state of another Hue plug is set, which can trigger another automation.

## Installation

Clone the project and install the dependencies into a python virtual environment:
```
# Clone the repository
$ git clone git@github.com:AlanCunningham/octopus_agile_trigger.git

# Create a python virtual environment
$ python3 -m venv venv

# Activate the virtual environment
$ source venv/bin/activate

# Install the python dependencies using the requirements.txt file provided
(venv) $ pip install -r requirements.txt
```

Open the settings.py and enter:
- Your Philips Hue Bridge IP address
- You [Distribution Network Operator Code](https://en.wikipedia.org/wiki/Distribution_network_operator)
- The names of the Hue plugs you want to toggle when the price drops below a given threshold and for
plunge pricing
- You preferred price threshold in pence

Then run the application
```
(venv) $ python main.py
```
