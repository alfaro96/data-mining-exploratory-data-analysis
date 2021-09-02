# Práctica 1: Análisis exploratorio de datos, preprocesamiento y validación de modelos de clasificación

Para comenzar a trabajar en esta práctica se deberá tener `Docker` instalado. Para ello, se pueden seguir las instrucciones especificadas en [este enlace](https://docs.docker.com/engine/install).

Además, también se necesita la herramienta `docker-compose`, que si bien suele instalarse junto a `Docker`, puede que sea necesario instalarlo por separado. Para ello, se pueden seguir las instrucciones mostradas en [este enlace](https://docs.docker.com/compose/install).

Una vez instalado, se puede iniciar un contenedor usando el comando `docker-compose up`. En particular, usaremos la [imagen de `Docker` proporcionada por `Kaggle`](https://github.com/Kaggle/docker-python) como entorno de trabajo, pues contiene la configuración y librerías necesarias para el correcto desarrollo de la práctica.

Tras finalizar, deberemos ejecutar el comando `docker-compose down` para así eliminar los contenedores, redes, volúmemes e imágenes creadas previamente (evitando un uso de recursos excesivo).
