# * Calling an API is one of the most common tasks in programming.
# * Implement an HTTP call to an API (of your choice) and display its
# * result through the terminal. For example: Pokémon, Marvel...
# * Here is a list of possible APIs:
# * https://github.com/public-apis/public-apis

import requests

url = "https://my-poke-api.onrender.com/random/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("API Content:")
        print(response.text)
    else:
        print(f"API request failed {response.status_code}")
except Exception as e:
    print(f"An error occurred while making the API request: {str(e)}")