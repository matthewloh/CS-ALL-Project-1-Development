import openai 
import os 
import urllib.request
from PIL import Image, ImageOps, ImageTk

openai.api_key = os.getenv("OPENAI_API_KEY")
# print(openai.Model.list())
image = (openai.Image.create(
    prompt = "A cat be doing the dishes in a ultrarealistic photogenic way using 4k nikon camera",
    n = 1,
    size = "512x512"
    ))
#getting the url from the response
print(image)
# example of url received from image
# {
#   "created": 1669527956,
#   "data": [
#     {
#       "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-izj67yULpSI5MgRqaYG6db2r/user-uzoLXLVMgG87wHAwJQXu3fUl/img-mAQNRmjEwsKZtX7mgQra7k7L.png?st=2022-11-27T04%3A45%3A56Z&se=2022-11-27T06%3A45%3A56Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-11-27T01%3A47%3A06Z&ske=2022-11-28T01%3A47%3A06Z&sks=b&skv=2021-08-06&sig=aNLbqQz/tYfKmc1e2AoHo%2B7w%2BiExErYBqioVSr0p1iU%3D"
#     }
#   ]
# }
url = image["data"][0]["url"]
urllib.request.urlretrieve(url,"FILE_NAME.png")
img = Image.open("FILE_NAME.png")
img.show()