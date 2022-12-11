from datetime import datetime

import requests
import datetime as dt
USERNAME = "NAME"
TOKEN = "lksdjfskldjslkdfjlksdjvsl"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint,json=user_param)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graphs_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(url=graph_endpoint, json=graphs_config,headers=headers)

print(response.text)

pixela_creation_endpoint = f"{graph_endpoint}/{GRAPHID}"
put_graph_header = {
   "X-USER-TOKEN": TOKEN
}
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20",

}

response = requests.post(url=pixela_creation_endpoint,json=pixel_data, headers=put_graph_header)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

update_header = {
    "X-USER-TOKEN": TOKEN
}

update_body = {
    "quantity": "10"
}

response = requests.put(url=update_endpoint,json=update_body,headers=update_header)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint,headers=TOKEN)
print(response.text)