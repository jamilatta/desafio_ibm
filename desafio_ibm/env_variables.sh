#!/bin/bash

ethernet=en1

export IP=$(ifconfig $ethernet | grep inet | grep -v inet6 | awk '{print $2}')

export DATABASE_URL=postgres://VVpRIhLTIyOtJYCVEBlhmCepIecyOuNE:2OyCjLDXalhxqCdYI9TXN3T9ROIAD9ymw9wXkv0jI5tJabDcO1wT2JyY7vjYYOJv@$IP:5432/desafio_ibm
export CELERY_BROKER_URL=redis://$IP:6379/0
export USE_DOCKER=no
export IPYTHONDIR=/app/.ipython
export REDIS_URL=redis://$IP:6379/0
export CELERY_FLOWER_USER=CkJbAWgTdwXADasjUCwjdpwNgyCFIwBC
export CELERY_FLOWER_PASSWORD=XwOJHmJTPRWMHsOPXurZPEnCHxu2k60rpPc42Xw2rQfuagDfCcYuN79Rx1cvnA1D
export EMAIL_HOST=$IP
export SOLR_URL=http://$IP:8983/solr/desafio_ibm/


docker stop django
workon desafio_ibm
python manage.py runserver
