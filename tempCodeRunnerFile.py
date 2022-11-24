import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")
#generate image
input = openai.Image.create(
    prompt="Learning how to design a website is fun!",
    n=2,
    size="512x512"
)
print(input)