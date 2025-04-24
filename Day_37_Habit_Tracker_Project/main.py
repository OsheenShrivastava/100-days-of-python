# TODO-1 - Import requests module
import requests

# TODO-6 - Import Date Time Module
from datetime import datetime

# TODO-2 - Create your user account by passing below parameters:
#  token(string of chars,numbers),username(string of your choice),agreeTermsOfService(should be yes) and
#  notMinor(should be yes)

USERNAME = "Your username"
TOKEN = "Your token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# TODO-3 - Create a graph definition by passing the below parameters:
#  id(should include chars and numbers),name(string),unit(E.g., km,calory),type(Only int or float are supported),
#  color(shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as
#  color kind).

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# TODO-4 - Create a Header (required parameter) to pass for creating a graph

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# TODO-5 - Post a pixel on graph by passing below parameters:
#  date(The date string on which the quantity is to be recorded),
#  quantity(quantity to be registered on specific date - string)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# TODO-7 - Format the date in the desired format
today = datetime.now()
Date_today = today.strftime("%Y%m%d")

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you walk today?\n"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

# TODO-8 - Use http put request to update today's datapoint to a new value

update_pixel_datapoint = f"{pixel_creation_endpoint}/{Date_today}"

update_pixel_config = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_datapoint, json=update_pixel_config, headers=headers)
# print(response.text)

# TODO-9 - Use http delete request to delete a datapoint

delete_pixel_datapoint = f"{pixel_creation_endpoint}/{Date_today}"

# response = requests.delete(url=delete_pixel_datapoint, headers=headers)
# print(response.text)