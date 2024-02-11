# Simple Blog API

This project is a simple blog API developed by Django to demonstrate skills of Alireza Zarei in the development of authentication and authorization, performance optimization, etc

The project
- is using python 3.10.13
- utilizes Postgres and database

## Installation

See the documentation of [Docker](https://docs.docker.com/engine/install/ubuntu/) for installation on ubuntu.

### Install Docker
#### Setup apt repository

```sh
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc]\
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") \
  stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

#### Install the Docker packages
```sh
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

#### Verify that the Docker Engine installation
Verify that the Docker Engine installation is successful by running the hello-world image
```sh
sudo docker run hello-world
```

## Run the Docker containers

Build the Dockerfile
```sh
sudo docker build .
```

Then you can start up the project

```sh
sudo docker compose up
```

> If it is the first time you are running the project or you want to migrate the database you can run the
>  command below

### Migrate the database
For migration of the database just run the command

```sh
sudo docker compose run web python manage.py migrate
```

## License

MIT

**Free Software!**