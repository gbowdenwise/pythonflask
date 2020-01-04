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

Included are docker scripts for building, running, stoping, and viewing logs. 

Follow these steps:

1. Build the image
    ```text
    ./docker-build.sh
    ```
    Output:
    ```test
    Sending build context to Docker daemon  119.3kB
    Step 1/7 : FROM python:3
     ---> 4c0fd7901be8
    Step 2/7 : ENV PYTHONPATH=/app:.
     ---> Using cache
     ---> 61ed342fd451
    Step 3/7 : COPY . /app
     ---> eecfb87e47ba
    Step 4/7 : WORKDIR /app/src
     ---> Running in 796410ff4796
    Removing intermediate container 796410ff4796
     ---> ddc16f7c70f7
    Step 5/7 : RUN pip install -r ../requirements.txt
     ---> Running in be465034f7de
    Collecting flask (from -r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
    Collecting flask-cors (from -r ../requirements.txt (line 2))
      Downloading https://files.pythonhosted.org/packages/78/38/e68b11daa5d613e3a91e4bf3da76c94ac9ee0d9cd515af9c1ab80d36f709/Flask_Cors-3.0.8-py2.py3-none-any.whl
    Collecting click>=5.1 (from flask->-r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
    Collecting Werkzeug>=0.15 (from flask->-r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
    Collecting itsdangerous>=0.24 (from flask->-r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
    Collecting Jinja2>=2.10.1 (from flask->-r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl (125kB)
    Collecting Six (from flask-cors->-r ../requirements.txt (line 2))
      Downloading https://files.pythonhosted.org/packages/65/26/32b8464df2a97e6dd1b656ed26b2c194606c16fe163c695a992b36c11cdf/six-1.13.0-py2.py3-none-any.whl
    Collecting MarkupSafe>=0.23 (from Jinja2>=2.10.1->flask->-r ../requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/98/7b/ff284bd8c80654e471b769062a9b43cc5d03e7a615048d96f4619df8d420/MarkupSafe-1.1.1-cp37-cp37m-manylinux1_x86_64.whl
    Installing collected packages: click, Werkzeug, itsdangerous, MarkupSafe, Jinja2, flask, Six, flask-cors
    Successfully installed Jinja2-2.10.3 MarkupSafe-1.1.1 Six-1.13.0 Werkzeug-0.16.0 click-7.0 flask-1.1.1 flask-cors-3.0.8 itsdangerous-1.1.0
    WARNING: You are using pip version 19.1.1, however version 19.3.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    Removing intermediate container be465034f7de
     ---> 8a803bbea537
    Step 6/7 : EXPOSE 5000
     ---> Running in 399f43def38c
    Removing intermediate container 399f43def38c
     ---> ea2d49551321
    Step 7/7 : CMD python ./pythonflask/flaskAppMain.py
     ---> Running in 72aeb98fab07
    Removing intermediate container 72aeb98fab07
     ---> b449954a280b
    Successfully built b449954a280b
    Successfully tagged pythonflask:latest
    ```

2. Run

    ```text
    ./docker-run.sh
    ```
   Output:
   ```text
    d935ff492c9488d39454a2492e373745e7d71cc87797bf24aabdead8feded5eb
    ```
   
3. Check the logs

    ```text
    ./docker-logs.sh
    ```
   Outout:
    ```text
    INFO:flaskAppMain:__main__ initialized
    INFO:flaskAppMain:Starting flask server on port: 5000
     * Serving Flask app "flaskAppMain" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
    INFO:werkzeug: * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    ```
   
4. When desired, you may stop and remove the container

    ```text
    ./docker-stop.sh
    ```
   
## Test the API

Open your browser and try out the endpoints below:

Endpoint #1: ```http://localhost:9000/hello```

Response (STRING):
```text
Hello from flask!
```

Endpoint #2: ```http://localhost:9000/data/hello```

Response (JSON):
```text
{"message":"Hello from DataController!"}
```