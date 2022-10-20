import requests


# Index
# GK : 9
# Computer Science: 18
# Anime / Manga : 31
# to get all topics in one quiz , remove category from parameters
NUM_OF_QUESTIONS = 20
category = 31

parameters = {
    "category": category,
    "amount": NUM_OF_QUESTIONS,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]






