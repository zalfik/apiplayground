import pandas as pd
from requests import request
import json
from datetime import datetime

# url = "https://api.github.com/user/zalfik"

# response = request("GET", url, timeout=(2, 5))

today_timestamp = datetime.now().strftime("%Y%m%d")
# url = "https://football98.p.rapidapi.com/seriea/results"

# headers = {
# 	"X-RapidAPI-Key": "2df78883ecmsh99bbfaf0b24898cp18aaf9jsnd2016d8a89d8",
# 	"X-RapidAPI-Host": "football98.p.rapidapi.com"
# }

# response = request("GET", url, headers=headers)

# # Check if response was successful
# if response.status_code == 200:
#     # Get the data from the API response
#     data = response.json()
    
#     # Convert data to a Pandas dataframe
#     # df = pd.DataFrame(data)
    
#     # Write the data to a JSON file
#     file_path = f"data_{today_timestamp}.json"
#     with open(file_path, "w") as file:
#         json.dump(data, file)
        
#     # Print the dataframe
#     # df.to_csv("data.csv", index=False)
# else:
#     # Handle the error
#     print('Failed to retrieve data from API. Error code:', response.status_code)

# # df = pd.read_json("data.json")

# print(type(data))

# for row in data:
#     print(row)

with open("data.json", mode="r") as data_file:
    saved_data = json.load(data_file)[0]


tester = saved_data
# print(tester)
print(type(tester))

for matchday in tester:
    print(f"\n{matchday}\n".strip())
    for game in tester[matchday]:
        # print the game result
        print(f"{game['homeTeam']} {game['homeTeamScore']}-{game['awayTeamScore']} {game['awayTeam']}\n")
        ht = tester[matchday][0]

# md21 = tester[" Matchday 21 "]
# print(md21)
# for row in md21:
#     print(row)

# print(type(response.text))

