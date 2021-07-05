# AWD Data Upload Platform

## How to build & run the application

### Prerequisites

#### Ubuntu 18.04

* install docker engine using [this guide](https://docs.docker.com/engine/install/ubuntu/) Using a repository
* install docker compose using [this guide](https://docs.docker.com/compose/install/)

### running the application

* save aws credentials in aws.env file in root directory: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_BUCKET_NAME`
* run `docker-compose up -d [--build]`  
* run `docker-compose logs -f` to follow application logs
