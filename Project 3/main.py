from datetime import datetime
import requests

USERNAME = "username"
AUTH_TOCKEN = "user auth tocken"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# parameters
user_params = {
    "token": AUTH_TOCKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# -------------- Registering in pixela --------------
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# ------------- creating a pixela Graph ------------------
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_id = "graph1"
graph_params = {
    "id": graph_id,
    "name": "3D modeling",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}
# ------------ Pixela Header --------------
header = {
    "X-USER-TOKEN": AUTH_TOCKEN,
}
# ------------- posting graph request to pixela ----------------
# graph_resp = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(graph_resp.text)

# ----------------- posting a pixel / adding values to pixela graph ----------------------
today = datetime.now()
date = today.strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/{graph_id}"
pixel_params = {
    "date": date,
    "quantity": input("Enter the duration of your activity in decimal: "),
}

pixel_post = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
print(pixel_post.text)

# ------------- Update pixel on the graph --------------------
update = input("Do you want to update existing entry? 'Y/N': ").upper()
if update == "Y":
    pixel_update_params = {
        "quantity": input("Enter the duration of your activity in decimal: ")
    }

    pixel_update = requests.put(url=f"{pixel_endpoint}/{date}", json=pixel_update_params, headers=header)
    print(pixel_update.text)

# pixel delete
# pixel_del = requests.delete(url=f"{pixel_endpoint}/{date}", headers=header)
# print(pixel_del.text)
