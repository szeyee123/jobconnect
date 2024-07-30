# JobConnect Backend

Monorepo for all backend microservices.

Deployed at https://kong-service-dabaoking-kong-seanjin97.cloud.okteto.net/

## Microservices

Click on each microservice to view detailed run instructructions.

1. [Candidate](http://localhost:8081/candidate/swagger) - API Server that manages candidate accounts and details. 
    * Name: candidate.
    * Port: 8081.
    * Language: Python.
    * Framework: FastAPI. Flask example available [here](./user/src/flask_example.py) but it won't come with Swagger docs out of the box.
    * All APIs to be prefixed with `/candidate`.
2. [Job](http://localhost:8083/job/swagger) - API Server that manages creation of jobs. 
    * Name: job.
    * Port: 8083.
    * Language: Python.
    * Framework: FastAPI.
    * All APIs to be prefixed with `/job`.
3. [Company](http://localhost:8084/company/swagger) - API Server that manages company accounts and details. 
    * Name: company.
    * Port: 8084.
    * Language: Python.
    * Framework: FastAPI.
    * All APIs to be prefixed with `/company`.

## Tools

1. [MongoDB](./mongodb) - NoSQL DB. This folder serves as a docker volume to persist data on the local container instance. Delete the data folder within this folder to reset all data. 
2. [Kafka](./kafka) - Messaging broker. This folder serves as a docker volume to persist data on the local container instance. Delete the data folder within this folder to reset all data.

## Running jobconnect-backend locally

This runs all components as docker containers.

2. Run the command in the project root directory to start up all components. `$ docker compose up -d`. You should see this. ![docker compose result](./assets/DockerComposeResult.png "Docker compose result")
4. Go to the MongoDB admin console to verify that MongoDB is working. http://localhost:5000. 
`Username: admin, Password: pass`
![mongodb admin console](./assets/MongoDB.png)
5. Go to any API microservice Swagger docs to test available apis. (Only applicable for FastAPI servers.)
    * URL: `localhost:8081/candidate/swagger`
    * E.g. For `candidate` microservice's swagger docs go to http://localhost:8081/candidate/swagger. ![swagger](./assets/Swagger.png)

# Local development

## Microservices

### How to run

#### Running Python microservices locally.

##### Via docker (If you prefer to develop while the code is running in the docker container)

1. Start jobconnect-backend. [Refer to steps above](#running-jobconnect-backend-locally).
2. Modify source code, the docker container will hot reload on code change. # Note: if new env variables or dependencies are added, the docker image will need to be rebuilt. Stop the docker compose with `$ docker compose down`, followed by deleting the `jobconnect-backend_<microservice_name>-1` image. Finally, re-run the docker compose.

##### Via source code (If you prefer to develop and run the code file directly.)

1. Start jobconnect-backend. [Refer to steps above](#running-jobconnect-backend-locally)
2. Stop the `jobconnect-backend-<microservice_name>-1` container since you'll be running the server on command line.
2. `$ cd <microservice_name>`
3. `$ python3 -m venv venv`
4. Activate virtualenv.
    * `C:\> venv\Scripts\activate.bat` for Windows CMD.
    * `PS C:\> venv\Scripts\Activate.ps1` for Windows Powershell.
    * `source venv/bin/activate` for Mac/ Linux.
5. `pip install -r requirements.txt`
6. `$ python src/main.py`

### Project structure

Outline of Python microservices.

```
<microservice_name>
    src
        .env - sample .env file that will contain sensitive info.
        main.py - app entrypoint.
        config
            config.py - reads values from .env file.
            db.py - connects to DB.
        dao
            <table_name>.py - functions to interact with the DB.
        models - contains pydantic models for POST request bodies.
```

