# Define custom function directory
ARG FUNCTION_DIR="/function"

FROM python:3.10 AS build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}
COPY lambda_function.py ${FUNCTION_DIR}

# Copy the requirements.txt
COPY requirements.txt .

# Install the dependencies in FUNCTION_DIR
RUN pip install \
    --target ${FUNCTION_DIR} \
        -r requirements.txt

# Use a slim version of the base Python image to reduce the final image size
FROM python:3.10-slim

# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}

# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

RUN apt-get update && \
    apt-get install -y zip gcc g++ && \
    rm -rf /var/lib/apt/lists/*


# Set runtime interface client as default command for the container runtime
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
# Pass the name of the function handler as an argument to the runtime
CMD [ "lambda_function.handler" ]
