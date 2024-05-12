import replicate
from dotenv import load_dotenv
load_dotenv()

def remove_background(url):
    input = {
        "video": url
    }

    output = replicate.run(
        "nateraw/video-background-remover:ac5c138171b04413a69222c304f67c135e259d46089fc70ef12da685b3c604aa",
        input=input
    )

    return output

# url = "https://i.pinimg.com/originals/32/79/46/3279462667fb3498a6aa144e7cdea2ae.gif"
# output_url = remove_background(url)
# print(output_url)