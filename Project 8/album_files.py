from main import data
import bs4


def titles_name():
    # ------------ Get album name and artist name -------------
    album_name = soup.select(selector="div li h3.c-title")
    song_titles = [i.getText().strip("\n\t") for i in album_name]

    artist_name = soup.select(selector="div li span.c-label")
    artist_name = [i.text.strip("\n\t'NEW-123") for i in artist_name]
    return
