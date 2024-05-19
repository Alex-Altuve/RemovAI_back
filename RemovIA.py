from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

# from OpenSSL import SSL

import Replicate_api as modelo

app = Flask(__name__)
CORS(app)

# Swagger configuration
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "RemovIA"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


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


if __name__ == "__main__":
    app.run(debug=True)
