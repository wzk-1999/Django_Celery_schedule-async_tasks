### start the consumer: 
`celery -A app01.main worker --loglevel=info --pool=threads`

in windows, we need specify --pool= threads

### start the producer:
your Django project