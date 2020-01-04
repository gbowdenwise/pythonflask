#!/bin/bash

APP_NAME=pythonflask

docker stop ${APP_NAME}
docker rm ${APP_NAME}

