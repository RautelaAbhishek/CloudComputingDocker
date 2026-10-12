# lightweight base
FROM python:3.12-alpine

# set working dir
WORKDIR /home/data

# Copy Python script and text files to the container
COPY scripts.py .
COPY data/IF.txt .
COPY data/AlwaysRememberUsThisWay.txt .

# Create output folder
RUN mkdir -p /home/data/output

# Run script when container start
CMD ["python", "scripts.py"]
