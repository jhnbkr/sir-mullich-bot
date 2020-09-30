import http
import json

def get_random_gif(tag):
    api_key = "cXMH5UVWSufhjAPppUd63yIjFtjA1CbU"
    connection = http.client.HTTPSConnection("api.giphy.com")
    connection.request("GET", f"/v1/gifs/random?api_key={api_key}&tag={tag}")
    response = connection.getresponse()
    data = json.loads(response.read().decode("utf-8")).get("data")
    return data.get("url")
