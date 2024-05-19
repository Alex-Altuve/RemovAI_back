import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename

import Replicate_api as modelo

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
# flask files constants
UPLOAD_FOLDER = "/static/uploads/"
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


@app.route("/eliminar-fondo", methods=["POST"])
def remove_background_ai():
    """
    function to remove the background of a video from URL
    """
    try:
        data = request.json
        print(data)
        url = data.get("input")
        if not url:
            return jsonify({"error": "URL missing in request body"}), 400

        output_url = modelo.remove_background(url)
        return jsonify({"output_url": output_url})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/delete-background", methods=["POST"])
def remove_background_url_or_video_ai():
    """
    function to remove the background of a video from URL
    """
    try:
        # variable for the result
        video = {}
        # verify if the user submitted a file or a URL
        if "video" in request.files:
            file = request.files["file"]
            # if the user uploaded a empty file without a name
            if file.filename == "":
                return jsonify({"error": "No file selected"}), 400
            # if the file is not empty and is allowed
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # save the file to local
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                # open the video
                video = open("./static/uploads/video.mp4", "rb")
        else:
            # if no file exists then verify the URL
            data = request.json
            video = data.get("url")
            if not video:
                return jsonify({"error": "URL missing in request body"}), 400
        # call the model
        output = modelo.remove_background(video=video)
        # return the result
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
