import os

# RabbitMQ
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", default="localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", default="rangeconnect")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", default="Uivq9ACXS49W")
RABBITMQ_URI = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}/"

