import pandas as pd
from requests import request
import json

url = "https://api.github.com/user/zalfik"

response = request("GET", url, timeout=(2, 5))

# url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

# querystring = {"market":"classic","iso_date":"2018-12-01","federation":"UEFA"}

# headers = {
# 	"X-RapidAPI-Key": "2df78883ecmsh99bbfaf0b24898cp18aaf9jsnd2016d8a89d8",
# 	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
# }

# response = request("GET", url, headers=headers, params=querystring)

# Check if response was successful
if response.status_code == 200:
    # Get the data from the API response
    data = response.json()
    
    # Convert data to a Pandas dataframe
    # df = pd.DataFrame(data)
    
    # Write the data to a JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)
        
    # Print the dataframe
    # print(df)
else:
    # Handle the error
    print('Failed to retrieve data from API. Error code:', response.status_code)



# print(type(response.text))

####

import requests
import pandas as pd
import json

# API endpoint
url = 'https://api.example.com/data'

# Send GET request to API endpoint
response = requests.get(url)

# Check if response was successful
if response.status_code == 200:
    # Get the data from the API response
    data = response.json()
    
    # Convert data to a Pandas dataframe
    df = pd.DataFrame(data)
    
    # Write the data to a JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)
        
    # Print the dataframe
    print(df)
else:
    # Handle the error
    print('Failed to retrieve data from API. Error code:', response.status_code)
