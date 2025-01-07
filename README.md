# lambda_api_example

This repo contains an example of how to build an API in AWS using a CloudFormation template, Lambda and a Docker container. The use case is to install Python packages for the lambda function to access using a Docker image. 

The API triggers a lambda function which runs a Docker container.
The Docker container is specified in the `container_folder` using the `Dockerfile`, `requirements.txt` and the `lambda_handler.py`. The deployment of this is discussed in the post below
https://johnardavies.github.io//technical/api_lambda/

![api_schematic](/api_schematic.png)



