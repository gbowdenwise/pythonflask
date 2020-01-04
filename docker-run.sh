#!/bin/bash

APP_NAME=pythonflask

docker run -d -p 9000:5000 --name ${APP_NAME} ${APP_NAME}
