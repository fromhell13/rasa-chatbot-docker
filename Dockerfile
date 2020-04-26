# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:latest

# Use subdirectory as working directory
WORKDIR /app

COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

RUN pip install -r requirements-actions.txt

# Copy actions folder to working directory
COPY ./actions /app/actions

# By best practices, don't run the code with root user
USER 1001