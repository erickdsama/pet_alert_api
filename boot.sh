#!/bin/bash
flask db init
flask db migrate
flask db upgrade
if [ $FLASK_ENV = "development" ]
then
  exec gunicorn -b :5001 --access-logfile - --error-logfile - main:app  --reload
else
  exec gunicorn -b :5000 --access-logfile - --error-logfile - main:app  --reload
fi
