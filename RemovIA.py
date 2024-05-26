from flask import Flask, request, jsonify
import Replicate_api as modelo

app = Flask(__name__)

@app.route('/eliminar_fondo', methods=['POST'])
def remove_backgroundIA():
    try:
        data = request.json
        url = data.get('url')
        if not url:
            return jsonify({'error': 'URL missing in request body'}), 400
        
        #esto es para validar si es un URL lo que esta ingresando
        if 'http://' in url or 'https://' in url:
            output_url = modelo.remove_background(url)
            return jsonify({'output_url': output_url})
        else:
            #esto corre cuando no es un URL, es decir, un archivo local tipo Video.gif
            video= open(url, "rb")
            output_url = modelo.remove_background(video)
            return jsonify({'output_url': output_url})
        
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

