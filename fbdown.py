from __future__ import unicode_literals
import youtube_dl
import json


with youtube_dl.YoutubeDL() as ydl:
   url = ydl.extract_info('https://www.facebook.com/574719552680201/videos/743165196185314/')
print(url("fromats")[-1]["url"])
