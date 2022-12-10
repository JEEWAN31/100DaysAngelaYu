import requests as re
parameters = {
    "amount":10,
    "type":"boolean"
}
response = re.get(f"https://opentdb.com/api.php?",params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]