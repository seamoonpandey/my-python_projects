import requests

joke_api_url = "https://v2.jokeapi.dev/joke/Programming"

response = requests.get(joke_api_url)

if response.status_code == 200:
    joke_data = response.json()

    if joke_data["type"] == "twopart":
        joke = joke_data["setup"] + "\n" + joke_data["delivery"]
    else:
        joke = joke_data["joke"]


    print(joke)

else:
    print("Sorry mate! we are unable to give a joke for you cause you are the best of your type")
