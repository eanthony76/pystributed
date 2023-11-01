
FROM continuumio/miniconda3:latest

WORKDIR /app

# Install Transformers
RUN pip install transformers pandas

# Copy user's code and any necessary data
COPY temp_script.py /app/temp_script.py

CMD ["python", "/app/temp_script.py"]
