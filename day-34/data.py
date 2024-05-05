import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
'''params for api'''

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
'''question data for the questions'''
