"""
    Model from replicate to delete background
"""

from dotenv import load_dotenv
import replicate


# load the dotenv values
load_dotenv()
# get the secret key from the env file
# SECRET_TOKEN = os.environ.get("REPLICATE_API_TOKEN")


def remove_background(video):
    """
    function to connect to deployed model
    """

    # construct the input of the model
    input_video = {"video": video}

    output = replicate.run(
        "nateraw/video-background-remover:ac5c138171b04413a69222c304f67c135e259d46089fc70ef12da685b3c604aa",
        input=input_video,
    )
    print(output)

    return output


# url = "https://i.pinimg.com/originals/32/79/46/3279462667fb3498a6aa144e7cdea2ae.gif"
# output_url = remove_background(url)
# print(output_url)
