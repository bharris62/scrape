web: gunicorn run:app -w 4 --log-file - --bind 0.0.0.0:$PORT
scheduler: python scheduler.py