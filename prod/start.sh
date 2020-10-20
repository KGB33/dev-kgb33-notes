#!/bin/bash
app="notes.test"
docker build -t ${app} .
docker run -d -p 3333:5000 -e FLASK_SECRET_KEY --rm --network=host ${app}
