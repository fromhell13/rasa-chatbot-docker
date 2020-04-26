#!/bin/sh

docker build . -t fromhell13/rasa-action:latest
docker login --username fromhell13 --password P@55w0rd820922
docker push fromhell13/rasa-action:latest