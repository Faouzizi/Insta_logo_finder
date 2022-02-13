# Instagram Logo Finder
The goal of this project is to find the logo for any brand selected.
The principle is simple, we will scrap the logo url from Instagram using Selenium.

- We connect to our account
- Go to the search bar 
- Enter the brand name 
- Get the logo url


For that, follow the next steps:
- Clone the current repository using: git clone https://github.com/Faouzizi/Insta_logo_finder.git
- Go to the project directory and create a new vertual environnement using: python3 -m venv/venv
- Activate this new venv using: source venv/bin/activate
- Install all requirements: pip install -r requirements.txt
- Export your instagram credential to you venv using: 
  - export EMAIL='jon.snow@gmail.com' 
  - export PASSWORD='jonsnowpassword'
    
Finally, you need to run the main script: python3 web_app/web_app.py
Then you can use it.
Enjoy :) 
    

# Launch via Docker
- create the docker image 
sudo docker build -t logo_finder . --build-arg EMAIL=${EMAIL} --build-arg PASSWORD=${PASSWORD}
- Run the image created 
sudo docker run -e PASSWORD='password' -e EMAIL='email' -p 5000:5000 logo_finder:latest
