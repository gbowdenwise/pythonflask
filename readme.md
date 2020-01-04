# Python Flask

[Flask](https://palletsprojects.com/p/flask/) Flask is a lightweight WSGI web application framework. For 
details please see the [documentation](https://flask.palletsprojects.com/en/1.1.x/). 

## Sample Flask Application

As an example, here we have a flask application with the following endpoints:

| Endpoint      |  Method | Description |
|---------------|---------|-----------------------------------------------------------------|
| /hello        | GET     | Returns a string "Hello from flask!"                            |
| /data/hello   | GET     | Returns a json object with message "Hello from DataController!" |

The application also utilizes [Blueprints](https://flask.palletsprojects.com/en/1.0.x/blueprints) 
to make promote modularity and organize your flask application into smaller, re-usable components. 

## Docker

Incluxed are docker scripts for building, running, stoping, and viewing logs. 

