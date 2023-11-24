"""
Main module of the server file
"""

import os
# 3rd party moudles

# local modules
import config


# Get the application instance
connex_app = config.connex_app
from flask import redirect

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    return redirect("/api/ui")

if __name__ == "__main__":
    connex_app.run(host='0.0.0.0', port=int(os.getenv("PORT", default="8000")))