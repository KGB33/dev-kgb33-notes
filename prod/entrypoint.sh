#!/bin/bash
exec gunicorn --config gunicorn_config.py notes.__main__:app
