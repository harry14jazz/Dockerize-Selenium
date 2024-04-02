# Use Alpine Linux as the base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY 2_simple_main.py requirements.txt ./

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories

RUN apk update

# Install Chromium and chromedriver using apk package manager
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    unzip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the path for chromedriver
ENV PATH="/usr/lib/chromium/:${PATH}"

# Run the Python script when the container launches
CMD ["python", "2_simple_main.py"]