import requests
import json
import os
from datetime import datetime

BASE_URL = "https://restcountries.com/v3.1"

HEADERS = {
    "Accept" : "application/json",
    "User-Agent" : "CountryExplorer/1.0"
    }

TIMEOUT = 5

def search_country(country_name):
    url = f"{BASE_URL}/name/{country_name}"
    print(f"\n searching for : {country_name}")

    try:
        response = requests.get(url,headers=HEADERS,timeout=TIMEOUT)
        print(f"status code : {response.status_code}")
        response.raise_for_status()
        data = response.json()
        return data

    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
    except requests.exceptions.Timeout:
        print("Request timeout :{TIMEOUT} seconds")
    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            print(f"country name {country_name} not found")
        elif response.status_code == 429:
            print("Too many requests ")
        else:
            print(f"HttpError :{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Unexpected error : {e}")
    return None

def display_country(data):
    country = data[0]

    name = country["name"]["common"]
    capital= country.get("capital",["N/A"])[0]
    population = country.get("population",0)
    region = country.get("region")

    print(f"\n Country : {name} ")
    print(f"Capital : {capital}")
    print(f"Population : {population:,}")
    print(f"Region : {region}")

def save_results(data,country_name):
    os.makedirs("results",exist_ok=True)
    filename =f"results/{country_name.lower()}_data.json"
    save_data = {
        "searchedtime" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result" : data    
        }
    with open(filename,'w') as f:
        json.dump(save_data,f,indent=4)
    
    print("Data saved successfully")

def main():
    print ("\n Country Explorer")
    print("Type 'quit' to EXIT")

    while True:
        country_name = input("Enter country name :").strip()

        if country_name.lower() == "quit":
            print("Goodbye!")
            break
        
        if not country_name:
            print("Enter a country name ")
            continue


        data = search_country(country_name)
        if data:
            display_country(data)
            choice=input("\n save data to file (y/n):").strip().lower()
            if choice == "y":
                save_results(data,country_name)
        else:
            print("Enter a different country name")

if __name__ =="__main__":
    main()



        
        

