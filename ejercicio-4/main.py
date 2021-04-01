import requests
import json

headers = {
    "api-key": "ea670047974b650bbcba5dd759baf1ed",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

data = {
    "shipping_order": {
        "n_packages": "1",
        "content_description": "ORDEN 255826267",
        "imported_id": "255826267",
        "order_price": "24509.0",
        "weight": "0.98",
        "volume": "1.0",
        "type": "delivery",
    },
    "shipping_origin": {"warehouse_code": "401"},
    "shipping_destination": {
        "customer": {
            "name": "Ema Alvarado Godoy",
            "email": "ema@oneninefour.cl",
            "phone": "977623070",
        },
        "delivery_address": {
            "home_address": {
                "place": "Puente Alto",
                "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto",
            }
        },
    },
    "carrier": {"carrier_code": "", "tracking_number": "9681"},
}

response = requests.post(
    "https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries",
    headers=headers,
    json=data,
)

response_data = response.json()

with open("response.json", "w") as outfile:
    json.dump(response_data, outfile, indent=4, sort_keys=True)
