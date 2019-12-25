import base64, random

with open("frame3.jpg", "rb") as image:
    str= base64.b64encode(image.read())
    print(random.choice([str[:16], str[:32]]))

