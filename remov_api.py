"""
API for communicating with the replicate model to delete a video background
from an URL or MP4 file
"""

import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename

import modelo_ia as modelo

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
# flask files constants
UPLOAD_FOLDER = "./static/uploads/"
ALLOWED_EXTENSIONS = {"mp4","gif"}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

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
            # get the file
            file = request.files["video"]
            print("File", file)
            # if the user uploaded a empty file without a name
            if file.filename == "":
                print("No file selected")
                return jsonify({"error": "No file selected"}), 400
            # if the file is not empty and is allowed
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
                print("Filename ", filename)
                # video = open(f"./static/uploads/{filename}", "rb")
                # output = modelo.remove_background_from_video(video=video)
                # video.close()

                # no es necesario abrir el archivo, se puede pasar el nombre del archivo.
                output = modelo.remove_background_from_video(input_filename=f"./static/uploads/{filename}")
                os.remove(f"./static/uploads/{filename}")
                abs_output = os.path.abspath(output)
                return jsonify({"output_url": abs_output})
            else:
                return jsonify({"error": "Invalid video extension"}), 400
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)