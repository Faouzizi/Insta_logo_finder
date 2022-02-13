FROM python:3.7-slim

# define workdir
WORKDIR /app

# Copy all files, dirctory from local to docker
COPY . .

# Install packages
RUN pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org --requirement requirements.txt\
    && pip install .

# Install chromedriver on docker
# Set up the Chrome PPA
RUN apt-get update -y \
    && apt-get install -y wget \
    && apt-get install -y gnupg2 \
    && apt-get install -y unzip \
    && apt-get install -y curl

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update \
    && apt-get install -y google-chrome-stable

# Download and install Chromedriver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# Run python script
CMD ["python", "web_app/web_app.py"]
