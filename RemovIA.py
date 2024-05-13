from flask import Flask, request, jsonify
import Replicate_api as modelo

app = Flask(__name__)


@app.route("/eliminar_fondo", methods=["POST"])
def remove_background_ai():
    """
    function to remove the background of a video from URL
    """
    try:
        data = request.json
        url = data.get("url")
        if not url:
            return jsonify({"error": "URL missing in request body"}), 400

        output_url = modelo.remove_background(url)
        return jsonify({"output_url": output_url})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
