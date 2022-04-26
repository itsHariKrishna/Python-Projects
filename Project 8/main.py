from album_files import AlbumDetails
import requests
from cred import Cred

year = input("To which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(URL)
response.raise_for_status()
data = response.text




# spotify
ENCODED_DETAILS = Cred().base64_encoded
CLIENT_REDIRECT = Cred().redirect_url

# -------------- Accessing the Access token -----------------
URL = "https://accounts.spotify.com/api/token"
method = "POST"
token_header = {
    "Authorization": f"Basic {ENCODED_DETAILS.decode()}",
    "Content-Type": "application/x-www-form-urlencoded",
}
params = {
    "grant_type": 'client_credentials',
}

r2 = requests.post(url=URL, headers=token_header, data=params)
r2.raise_for_status()
access_token = r2.json()["access_token"]

# ----------- Searching songs in spotify -------------
search_item = " https://api.spotify.com/v1/search"
album_header = {
    "Authorization": f"Bearer {access_token}"
}

song_details = []
for i in range(len(song_titles)):
    album_params = {
        "q": song_titles[i],
        "type": "track",
    }

    r3 = requests.get(url=search_item, headers=album_header, params=album_params)
    # ------ exception -----
    if 199 < r3.status_code < 300:
        album_data = r3.json()

    else:
        raise Exception("Issue with either ulr, header, or params")

    song_details.append(f"{album_data['tracks']['items'][0]['artists'][0]['uri']},"
                        f" {album_data['tracks']['items'][0]['artists'][0]['name']}")

print(song_details)
