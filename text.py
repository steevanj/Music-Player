import lyricsgenius
import json

# Replace this with your actual Genius API token
GENIUS_API_TOKEN = "1WjeQ2b14ecf8CStQbl76k39AXNGIo9pu2Cq_CAALCF_PVDsdCnTxIq3QZyiEdj4"

genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

query = input("Enter Song Name: ")
song = genius.search_song(query)

if song:
    lyrics_lines = song.lyrics.split('\n')
    json_data = [{"line_number": i+1, "lyrics": line} for i, line in enumerate(lyrics_lines)]

    json_string = json.dumps(json_data, indent=4)
    print(json_string)
else:
    print("Lyrics not found.")
