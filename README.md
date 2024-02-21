# Invoicing API

Este proyecto tiene API's relacionadas con la facturacion de productos. Utiliza Python 3.11.5, FastAPI para el desarrollo del backend y Postgresql como base de datos. Además, se ha configurado un entorno de desarrollo utilizando Docker y Docker Compose.

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:
- [Python 3.11.5](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/) (opcional, si tu proyecto está dockerizado)


## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

```
invoicing_microservice/
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── endpoints/
│   │   └── ...
│   ├── core/
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   └── validations.py
│   ├── db/
│   │   └── postgresql.py
│   ├── images/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── util/
│       └── file_utils.py
├── tests/
│   ├── integration/
│       └── ...
│   └── unit/
│       ├── test_property_api.py
│       └── ...
├── .env_example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

La estructura del proyecto sigue las mejores prácticas de organización de código:

- `app/`: Contiene el código fuente de la aplicación FastAPI.
- `tests/`: Aquí se encuentran los casos de prueba unitarios.
- `docker-compose.yml`: Define la configuración de Docker Compose para el proyecto.
- `Dockerfile`: Define la configuración del contenedor Docker para la aplicación.
- `requirements.txt`: Lista las dependencias de Python necesarias para el proyecto.

## Configuración del entorno de desarrollo

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/JorgeEduardo17/invoicing_microservice.git
   
   cd invoicing_microservice
   
2. Construir imagen, intalacion de dependencias (requirements.txt):
   ```bash
   docker-compose build

3. Inicia el entorno de desarrollo con Docker Compose:
   ```bash
   docker-compose up -d
   
   Esto configurará un contenedor de Postgresql y ejecutará la aplicación FastAPI en un servidor local.


4. Asegurate de tener variables de entorno (.env):

5. Accede a la documentación de la API en tu navegador web:
   http://localhost:8000/docs


## Funcionalidades


## Consideraciones 
Este proyecto se hizo según los siguientes criterios:

- **Arquitectura**: La estructura del proyecto y la organización del código deben seguir las mejores prácticas.
- **Documentación del Código**: El código debe estar bien documentado, incluyendo comentarios explicativos.
- **Mejores Prácticas**: Deben seguirse las mejores prácticas de desarrollo de Python y FastAPI.
- **Rendimiento**: La aplicación debe ser eficiente y responder de manera rápida a las solicitudes.
- **Pruebas Unitarias**: Se deben incluir pruebas unitarias para garantizar la calidad del código.

## Contribuciones

Si deseas contribuir a este proyecto, no dudes en enviar un pull request. Estamos abiertos a sugerencias y mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

