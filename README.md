# Práctica 1: Análisis exploratorio de datos, preprocesamiento y validación de modelos de clasificación

A continuación se especifican las instrucciones necesarias para configurar correctamente el entorno de trabajo.

## `Docker`

Para comenzar a trabajar se deberá tener `Docker` instalado. Para ello, se pueden seguir las instrucciones especificadas en [este enlace](https://docs.docker.com/engine/install).

Además, también se necesita la herramienta `docker-compose`, que si bien suele instalarse junto a `Docker`, puede que sea necesario instalarla por separado. Para ello, se pueden seguir las instrucciones mostradas en [este enlace](https://docs.docker.com/compose/install).

Una vez instalada, se puede iniciar un contenedor usando el comando `docker-compose up`. En particular, usaremos la [imagen de `Docker` proporcionada por `Kaggle`](https://github.com/Kaggle/docker-python) como entorno de trabajo, pues contiene la configuración y librerías necesarias para las tareas a desarrollar.

Tras finalizar, deberemos ejecutar el comando `docker-compose down` para así eliminar los contenedores, redes, volúmemes e imágenes creadas previamente (evitando un uso de recursos excesivo).

## `Kaggle`

Cada vez que se suben cambios a la rama `main`, la libreta de `Jupyter` (especificada en el apartado `code_file` del fichero `kernel-metadata.json`) se ejecuta y [publica](https://www.kaggle.com/alfaro96/data-mining-introduction-jupyter) en los servidores de `Kaggle` a través del flujo de trabajo `Kaggle kernel publisher`. Por tanto, se hace necesario disponer de una cuenta en `Kaggle`, que se puede crear a través de [este enlace](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F).

Tras ello, se debe [crear un *token*](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication) para poder usar la *API* pública de `Kaggle`, y posteriormente [añadir las variables secretas](https://docs.github.com/en/actions/reference/encrypted-secrets) `KAGGLE_KEY` y `KAGGLE_USERNAME` con los valores correspondientes.

Por último y antes de subir ningún cambio, se debe modificar el fichero `kernel-metadata.json` y cambiar, en el apartado `id`, `alfaro96` por el nombre de usuario de `Kaggle` correspondiente.

## `Review NB`

Dado que las libretas de `Jupyter` generan ficheros con metadatos, código fuente, texto formateado y multimedia, las soluciones convencionales para realizar un control de versiones no son las más adecuadas, pues, a pesar de tratarse de un fichero `JSON`, no siguen un formato fácilmente legible. Por ello, vamos a usar la aplicación `Review NB` que, entre otros, se encarga de proporcionar una diferencia visual para cada *commit* y *pull request*, lo que la hace ideal para nuestro entorno de trabajo.

Instalar esta aplicación es muy sencillo, pues solamente tendremos que [iniciar sesión](https://github.com/login/oauth/authorize?client_id=Iv1.b2736a9bd3b3e896) y autorizar su uso en el repositorio correspondiente (en este caso, `data-mining-exploratory-data-analysis`). Tras esto, ya tendremos acceso al [sitio web](https://app.reviewnb.com/alfaro96/data-mining-exploratory-data-analysis) correspondiente.
