#! /bin/bash

source venv/bin/activate

export FLASK_APP=index.py
export FLASK_ENV=developement

flask run --host=0.0.0.0
