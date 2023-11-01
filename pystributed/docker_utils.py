
import os
from .config import CONFIG

def build_image():
    # Dynamically generate Dockerfile
    with open("./Dockerfile", 'w') as f:
        f.write(f'''
FROM continuumio/miniconda3:latest

WORKDIR /app

# Install Transformers
RUN pip install transformers pandas

# Copy user's code and any necessary data
COPY temp_script.py /app/temp_script.py

CMD ["python", "/app/temp_script.py"]
''')
    os.system("docker build -t {}/{} .".format(CONFIG["DOCKER_REGISTRY"], CONFIG["DOCKER_IMAGE_NAME"]))

def push_image():
    os.system("docker push {}/{}".format(CONFIG["DOCKER_REGISTRY"], CONFIG["DOCKER_IMAGE_NAME"]))