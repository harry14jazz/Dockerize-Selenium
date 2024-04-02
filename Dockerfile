# Use the official Python image as a base image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY 2_simple_main.py requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install Chrome browser and chromedriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && LATEST_CHROMEDRIVER_VERSION=$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q --continue -P /tmp "https://chromedriver.storage.googleapis.com/$LATEST_CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
    && unzip -o /tmp/chromedriver_linux64.zip -d /usr/local/bin \
    && rm /tmp/chromedriver_linux64.zip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

# Run the Python script when the container launches
CMD ["python", "2_simple_main.py"]