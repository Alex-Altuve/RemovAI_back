# RemovIA_back

## Pasos para probar la api RemovIA

1.  Crear un ambiente virtual con `PS> python -m venv venv`
2.  Activar el ambiente virtual con `.\venv\Scripts\activate`
3.  Instalar las dependencias usando `pip install -r ./requirements.txt`
5.  Ejecutar la api usando el comando `python remov_ai.py` o ejectuando `flask --app remov_ai run` o si estas en modo desarrolador `flask --app remov_ai --debug run`
6.  Comprobar que la api este corriendo, mostrando este mensaje en la consola de VSC http://127.0.0.1:5000

7.  Ya al estar activa la api, puede comprobar su funcionamiento con postman de la siguiente manera:

    7.1 Realizar una solicitud POST a la siguiente direccion http://127.0.0.1:5000/eliminar_fondo o poner en el navegador http://127.0.0.1:5000/swagger, de esza forma, se mostrara el swagger con el endpoint de subir el archivo



## Dependencias usadas 
    moviepy
    opencv-python
    rembg
    os
    Flask
    Flask_Cors
    flask_swagger_ui
    Werkzeug

   
## Enlace Modelo de IA usado -> implementado por nosotros en Colab

https://colab.research.google.com/drive/10OHII8MtGl5ATMGWrmxRNzsnDkuUMrLT#scrollTo=2HtTiaTbiL7d&uniqifier=1


## Authors

- ### [@Alex Altuve](https://github.com/Alex-Altuve)  [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alex-altuve-delgado-b1a212288/)
- ### [@Alejandro Novellino](https://github.com/AlejandroNovellino) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]()

