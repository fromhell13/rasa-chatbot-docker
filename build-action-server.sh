#!/bin/sh

docker build . -t fromhell13/rasa-action:latest
docker login --username xxxxx --password xxx
docker push fromhell13/rasa-action:latest