# RemovIA_back

Crear un archivo .env y agregar la siguiente linea de codigo

    REPLICATE_API_TOKEN = {your api key}

Deberan iniciar sesion en replicate para poder obtenerla, ya con esa configuracion previa podrás probarla nuestra api localmente
https://replicate.com/account

## Pasos para probar la api RemovIA

1.  Crear un ambiente virtual con `PS> python -m venv venv`
2.  Activar el ambiente virtual con `.\venv\Scripts\activate`
3.  Instalar las dependencias usando `pip install -r ./requirements.txt`
4.  Crear el archivo `.env` utilizadno como base el archivo `.env.example` y colocar en el su token de Replicate
5.  Ejecutar la api usando el comando `python remov_ai.py` o ejectuando `flask --app remov_ai run` o si estas en modo desarrolador `flask --app remov_ai --debug run`
6.  Comprobar que la api este corriendo, mostrando este mensaje en la consola de VSC http://127.0.0.1:5000

7.  Ya al estar activa la api, puede comprobar su funcionamiento con postman de la siguiente manera:

    7.1 Realizar una solicitud POST a la siguiente direccion http://127.0.0.1:5000/eliminar_fondo

    7.2 Ir al apartado Body -> raw y agregar el url del video que deseas convertir, ejemplo:

        {
          "url": "https://i.pinimg.com/originals/32/79/46/3279462667fb3498a6aa144e7cdea2ae.gif"
        }


    7.3 Dar a enviar, si la solicitud ha sido procesada correctamente, te devolvera el URL del video con el fondo ya eliminado.

## Dependencias usadas 
    replicate
    dotenv 
    flask
    os
    flask_cors 
    flask_swagger_ui 
    werkzeug.utils 
    
De cada módulo se importa 

    dotenv -> load_dotenv
    flask_cors ->  CORS, cross_origin
    werkzeug.utils ->  secure_filename
    flask_swagger_ui -> get_swaggerui_blueprint
    flask -> Flask, request, jsonify
=======
    
     3.3 Dar a enviar, si la solicitud ha sido procesada correctamente, te devolvera el URL del video con el fondo ya eliminado.

## Dependencias usadas 
    replicate
    dotenv 
    flask

De cada módulo se importa 

dotenv -> load_dotenv

flask -> Flask, request, jsonify


## Enlace Modelo de IA usado
https://replicate.com/nateraw/video-background-remover

## Authors

- ### [@Alex Altuve](https://github.com/Alex-Altuve)  [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alex-altuve-delgado-b1a212288/)
- ### [@Alejandro Novellino](https://github.com/AlejandroNovellino) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]()

