import requests
import json

country_name = input("Enter country name :")
url = "https://restcountries.com/v3.1/name/"+ country_name
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    region = country["region"]
    currency = list(country["currencies"].values())[0]["name"]

    print("\n ===Country Information===")
    print("Country :", name)
    print("Capital :", capital)
    print("Population :", population)
    print("Region :", region)
    print("Currency :", currency)

    print("\nContent type:",response.headers["Content-Type"])         # application/json
    print("Content-Length:",response.headers["Content-Length"])       # size in bytes
    print("Cache-Control:",response.headers.get("Cache-Control")) 
    result ={
        "Country" : name,
        "Capital" : capital,
        "Population" : population,
        "Region" : region,
        "Currency" : currency,
    }

    with open("Country_data.json", "w") as file:
        json.dump(result,file,indent = 4)
    print("\nData saved to country_data.json")
else:
    print("Country not found!")


