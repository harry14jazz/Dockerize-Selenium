# FROM alpine:latest
# WORKDIR /app
# RUN echo "https://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
# 	&& apk update\
# 	&& apk add --no-cache python3 py3-pip firefox dbus-x11 ttf-freefont curl unzip py3-zstandard geckodriver\
# 	&& pip3 install selenium requests selenium-requests selenium-wiredo

FROM alpine:latest
WORKDIR /app

# Add Alpine testing repository
RUN echo "https://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# Update package lists and install dependencies
RUN apk update \
    && apk add --no-cache \
        python3 \
        py3-pip \
        firefox \
        dbus-x11 \
        ttf-freefont \
        curl \
        unzip \
        py3-zstandard \
    && pip3 install selenium requests selenium-requests selenium-wire

# Install geckodriver separately
RUN apk add --no-cache geckodriver

# Clean up
RUN rm -rf /var/cache/apk/*

# Copy your application code
COPY . /app

# Set the entrypoint (if needed)
# ENTRYPOINT ["python3", "your_script.py"]
