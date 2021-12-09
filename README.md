# findyoursea

Small API project with Django and Nuxt

## TLDR

The idea is very simple: send back random sea coordinates to find a sailing destination. :)
It's a very simple base on which we can do more concrete things!

## Architecture

The project is built around two web services: the backend API in django (python 3.7), and the frontend site in Nuxt (NodeJs / VueJs).

The Django API communicates with a PostgreSQL database service

Finally, Nginx serves the applications as a reverse proxy.

## Install

Install [Docker and Docker-Compose](https://docs.docker.com/engine/install/ubuntu/) version 3.9+

Install the dependencies :

- `cd frontend && npm i -D`
- `python3.7 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`

> **NOTE :** If you want to dev the project, you should install the python venv locally and the npm venv locally. There are other alternatives, less interesting in my opinion

Then build the dependencies :

```sh
docker-compose build
```

Or build the services one by one :

```sh
docker-compose build <my_service> # --no-cache if needed
```

## Usage

### Developement

Run the services :

```sh
docker-compose --env-file .env up  # --force-recreate if needed
```

Run the migrations :

```sh
docker exec findyoursea-backend-1 python manage.py migrate
```

Launch bash on a container (used to migrate, run tests, etc.) :

```sh
# template :
docker exec -ti <container name> /bin/bash
# so :
docker exec -ti findyoursea-backend-1 /bin/bash  # for python
docker exec -ti findyoursea-frontend-1 /bin/bash  # for nuxt
```

#### Access to the services

- Nuxt is hosted at `localhost/`
- Django is hosted at `localhost/api/`

### Production

![no today](https://64.media.tumblr.com/85717d57dfd6495d5871418ad848a228/tumblr_mpfcipZ2kV1rliqe2o6_250.gifv)

For production, we need to :

- Configure [Django](https://docs.djangoproject.com/fr/3.2/howto/deployment/) and [Nuxt](https://nuxtjs.org/docs/get-started/commands/#production-deployment) for production
- Serve the assets [from Nginx](https://nuxtjs.org/deployments/nginx/)
- Set (and use ;) ) a [non root user](https://docs.docker.com/engine/security/rootless/) for each container
- Use a [Relational Database Service](https://aws.amazon.com/fr/rds/) (more secure)
- Hide the backend API ?
- Set [always restart](https://docs.docker.com/compose/compose-file/compose-file-v3/#restart) for each container
- [Remove the volumes](https://docs.docker.com/compose/production/)

## FAQ

Django won't connect to docker!

- Sometimes you have to delete the Docker volume, which keeps bad data cached despite us :/
