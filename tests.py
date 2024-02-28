import requests
ms_url = "http://127.0.0.1:5000"

try:
    # Get the categories
    response = requests.get(ms_url + "/categories")
    categories = response.json()
    print("Categories:", categories)

    # Get the items
    response = requests.get(ms_url + "/items")
    items = response.json()
    print("Items:", items)

    # Get the modifiers
    response = requests.get(ms_url + "/modifiers")
    modifiers = response.json()
    print("Modifiers:", modifiers)

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
