# API de Facturación - CRUDs

Este proyecto implementa un sistema de facturación para productos utilizando Python 3.11.5, FastAPI para el desarrollo del backend, y PostgreSQL como sistema de gestión de bases de datos. Está diseñado para ser ejecutado en contenedores Docker, proporcionando un entorno de desarrollo y despliegue reproducible y fácil de configurar.

## Características

- **API RESTful**: Diseño de endpoints siguiendo los principios REST para operaciones CRUD.
- **Dockerización**: Contenedorización de la aplicación y la base de datos para facilitar el despliegue.
- **Pruebas Automatizadas**: Incluye pruebas unitarias y de integración para asegurar la calidad del código.
## Tecnologías Utilizadas

- **Python 3.11.5**: Lenguaje de programación principal.
- **FastAPI**: Framework web para construir APIs con Python.
- **PostgreSQL**: Sistema de gestión de bases de datos relacionales.
- **Docker**: Plataforma de contenedorización para simplificar el despliegue y la ejecución.
- **Docker Compose**: Herramienta para definir y ejecutar aplicaciones Docker multi-contenedor.
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
│   │   └── logger.py
│   ├── db/
│   │   └── postgresql.py
│   ├── models/
│   │   ├── invoice_detail.py
│   │   ├── invoice_header.py
│   │   ├── person.py
│   │   └── product.py
│   ├── repositories/
│   │   ├── invoice_detail.py
│   │   ├── invoice_header.py
│   │   ├── person.py
│   │   └── product.py
│   ├── schemas/
│   │   ├── invoice_detail.py
│   │   ├── invoice_header.py
│   │   ├── person.py
│   │   └── product.py
│   ├── services/
│   │   ├── invoice_detail.py
│   │   ├── invoice_header.py
│   │   ├── person.py
│   │   └── product.py
│   └── util/
│       └── file_utils.py
├── tests/
│   ├── integration/
│       └── ...
│   └── unit/
│       ├──end_points/
│              └── ...
├── init_scripts/
│   └── init_db.sql
├── .env_example
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

La estructura del proyecto sigue las mejores prácticas de organización de código:

El proyecto sigue una estructura modular para facilitar su mantenimiento y escalabilidad. Incluye directorios para modelos, esquemas, operaciones CRUD, pruebas, y configuraciones de Docker.
- `app/`: Contiene el código fuente de la aplicación FastAPI.
- `tests/`: Aquí se encuentran los casos de prueba unitarios.
- `init_scripts/`: Aquí se encuentran los scripts para la db.
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
   ```bash
   # General
   ENVIRONMENT=development
   APP_NAME=real_state_company
   IMAGES_DIRECTORY="app/images"
   
   # Database
   DATABASE_URL=postgresql://user:password@localhost:5432/invoicedb

   
   Estas variables son un ejemplo para correr en un ambiente local.

5. Accede a la documentación de la API en tu navegador web:
   http://localhost:8000/docs


## Funcionalidades


## Uso

Ejemplos de cómo realizar solicitudes a los endpoints y respuestas esperadas. Esto incluye la creación, consulta, actualización y eliminación de facturas y productos.

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

