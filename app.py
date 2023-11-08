import requests

api_url = "https://punapi.rest/api/pun"

def blague():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data["pun"]
        else:
            return "Impossible de récupérer une blague"
    except Exception as e:
        return "Une erreur s'est produite : " + str(e)


if __name__ == "__main__":
    print(blague())
