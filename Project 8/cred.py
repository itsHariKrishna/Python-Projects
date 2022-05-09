import base64
import os


class Cred():
    user_id_spotify = os.environ.get("user_id_spotify", "1stozuq4s15h07m2bn3i9lejv")
    spotify_client_ID = os.environ.get("spotify_client_ID", "b66c55b216164b84ac1780f092fb51f2")
    spotify_client_SECRET = os.environ.get("spotify_client_SECRET", "0906f1483f5c4a28a04829a25ff97a63")
    spotify_playlist_token = os.environ.get("spotify_playlist_token",
                                            "BQCpyWvXu-ln1fJtau3UlVIEMOc9iHM94pf_MgyZSJGZUYnObN7w9CJqLlsSCyqZocBkbtHeRIRs67p1ASHDtGUuSD475zthanYchtgDtzKRxHcuBWaCpwMpXtAApmzOFf5bRT5A0myCNag-xgXYGZsLBNShjJJUg9DJ0h5C9VCtf9EHz8pioFaZdxxcKx4rD36sp-ZADg")

    def __init__(self):
        self.redirect_url = "https://example.com/callback"  # "http://localhost:9000"
        self.client_cred = f"{self.spotify_client_ID}:{self.spotify_client_SECRET}"

        # base64 encoding
        self.base64_encoded = base64.b64encode(self.client_cred.encode())
