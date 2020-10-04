
# Stream : Twitter messsages, Video
# https://docs.python.org/3/library/io.html




# open(file,mode) returns a STREAM (e.g: _io.TextIOWrapper)

# Stream classes:
# BytesIO - expects binary-like obj and produces bytes objects
# StringIO - expects str obj and produces str obj



import requests
import os

# dumb way write the photo to disk
r = requests.get("https://images.unsplash.com/photo-1452857576997-f0f12cd77844?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80")
with open("photo.jpg", "wb") as f:
    f.write(r.content)



##
##requests.post(
##    "https://api.telegram.org/bot<TOKEN>/sendPhoto?chat_id=<chat_id>",
##    files={"photo": open("photo.jpg", "rb")}
##)

os.remove("photo.jpg")


################
import io

# OK way using stream to store the photo in RAM
r = requests.get("https://images.unsplash.com/photo-1452857576997-f0f12cd77844?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80")
with io.BytesIO() as buf:
    buf.write(r.content)
    buf.seek(0)

##    requests.post(
##        "https://api.telegram.org/bot<TOKEN>/sendPhoto?chat_id=<chat_id>",
##        files={"photo": buf}
##    )
