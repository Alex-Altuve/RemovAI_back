"""
API for communicating with the replicate model to delete a video background
from an URL or MP4 file
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename

import replicate_api as modelo

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
# flask files constants
UPLOAD_FOLDER = "./static/uploads/"
ALLOWED_EXTENSIONS = {"mp4"}

app = Flask(__name__)
# flask app configuration
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# swagger configuration
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "RemovIA"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# helper functions for the endpoints
def allowed_file(filename):
    """
    Verify if the file is allowed
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/delete-background/url", methods=["POST"])
@cross_origin()
def remove_background_url():
    """
    function to remove the background of a video from URL
    """
    try:
        print("Hi form delete background from URL")
        print("Request data", request.data)
        # if no file exists then verify the URL
        data = request.json
        print("Data in request", data)
        video = data.get("input")
        if not video:
            print("No url data in request", data)
            return jsonify({"error": "URL missing in request body"}), 400
        # call the model
        output = modelo.remove_background(video=video)
        # return the result
        return jsonify({"output_url": output})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/delete-background/file", methods=["POST"])
@cross_origin()
def remove_background_file():
    """
    function to remove the background of a video from a file
    """
    try:
        print("Hi form delete background from file")
        print("Request data", request.data)
        print("Request files", request.files)
        # verify if the user submitted a file or a URL
        if "video" in request.files:
            print(request.files)
            file = request.files["video"]
            # if the user uploaded a empty file without a name
            if file.filename == "":
                print("No file selected")
                return jsonify({"error": "No file selected"}), 400
            # if the file is not empty and is allowed
            if file and allowed_file(file.filename):
                # create a secure file object
                filename = secure_filename(file.filename)
                # save the file to local
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                # open the video
                video = open(f"./static/uploads/{filename}", "rb")
                # call the model
                output = modelo.remove_background(video=video)
                # return the result
                return jsonify({"output_url": output})
            else:
                return jsonify({"error": "Invalid video extension"}), 400
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)