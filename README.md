# lambda_api_example

This repo contains an example of how to build an API in AWS using a CloudFormation template, Lambda and a Docker container. The use case is to package python packages for the lambda function to access using Docker which can otherwise be hard to install in lambda.

The API triggers a lambda function which runs a docker container.
The Docker container is specified in the `container_folder` using the `Dockerfile`, `requirements.txt` and the `lambda_handler.py`.
