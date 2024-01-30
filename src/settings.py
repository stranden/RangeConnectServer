import os

# RabbitMQ
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", default="localhost")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", default="rangeconnect")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", default="Uivq9ACXS49W")
RABBITMQ_URI = f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASS}@{RABBITMQ_HOST}/"

# PostgreSQL
DATABASE_HOST = os.getenv("DATABASE_HOST", default="localhost")
DATABASE_USER = os.getenv("DATABASE_USER", default="rangeconnect")
DATABASE_PASS = os.getenv("DATABASE_PASS", default="MzqGbe#o8AUn")
DATABASE_DB = os.getenv("DATABASE_DB", default="rangeconnect")
DATABASE_SCHEMA = "rcb"
DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_DB}"
