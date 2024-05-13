# RemovIA_back

Crear un archivo .env y agregar la siguiente linea de codigo 
    
    REPLICATE_API_TOKEN = {your api key}

Deberan iniciar sesion en replicate para poder obtenerla, ya con esa configuracion previa podrás probarla nuestra api localmente
https://replicate.com/account

## Pasos para probar la api RemovIA 

1. Ejecutar la api usando el comando python RemovIA.py 

2. Comprobar que la api este corriendo, mostrando este mensaje en la consola de VSC http://127.0.0.1:5000

3.  Ya al estar activa la api, puede comprobar su funcionamiento con postman de la siguiente manera:

    3.1 Realizar una solicitud POST a la siguiente direccion http://127.0.0.1:5000/eliminar_fondo

     3.2 Ir al apartado Body -> raw y agregar el url del video que deseas convertir, ejemplo:

        {
          "url": "https://i.pinimg.com/originals/32/79/46/3279462667fb3498a6aa144e7cdea2ae.gif"
        }

     3.3 Dar a enviar, si la solicitud ha sido procesada correctamente, te devolvera el URL del video con el fondo ya eliminado.
    
