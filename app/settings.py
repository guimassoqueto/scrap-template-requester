from os import getenv
from dotenv import load_dotenv


load_dotenv()

RABBITMQ_DEFAULT_USER = getenv("RABBITMQ_DEFAULT_USER") or "user"
RABBITMQ_DEFAULT_PASS = getenv("RABBITMQ_DEFAULT_PASS") or "password"
RABBITMQ_DEFAULT_HOST = getenv("RABBITMQ_DEFAULT_HOST") or "localhost"
RABBITMQ_SEND_QUEUE = getenv("RABBITMQ_SEND_QUEUE") or "hello"
