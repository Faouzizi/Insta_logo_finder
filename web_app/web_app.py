from flask import Flask, render_template
from dominate.tags import img
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap
from flask import request
from src.crawler import uplaod_logo
from src.crawler import make_logo_search
from forms import BrandNameForm
import ast
import requests

# We dfine the app logo
logo = img(src='./static/img/logo.png', height="50", width="50", style="margin-top:15px")

# We define the menu
topbar = Navbar(logo,
                View('Logo Finder', 'get_logo'),)


# Register the top menu
nav = Nav()
nav.register_element('top', topbar)

# Define the web app
app = Flask(__name__)
app.secret_key = "thjsdqjdhskqsjdhLKKJKLSDHQL:"
Bootstrap(app)

def download(image_url, logo_name):
    img_data = requests.get(image_url).content
    with open('./logos/'+str(logo_name)+'.jpg', 'wb') as handler:
        handler.write(img_data)

@app.route('/', methods=['GET', 'POST'])
def get_logo():
    brand_logo = {}
    form = BrandNameForm()
    if request.method == 'POST':
        brand_name = request.form["brand_name"]
        print(brand_name)
        attempts = 0
        while attempts < 3:
            try:
                brand_logo = make_logo_search(driver, brand_name, wait_time=2)
                break
            except:
                pass
            finally:
                attempts += 1
        print(brand_logo)
        return render_template('logo_render.html',
                               brand_name=brand_name,
                               url=brand_logo[brand_name],
                               form=form)
    else:
        return render_template('logo_render.html', form=form, brand_name='', url='')

@app.route('/api/v1/resources/logo_finder', methods=['GET'])
def categorize_trx():
    # Check if the trx label is in the url
    if 'brand_name' in request.args:
        brand_name = request.args['brand_name']
        # Define an empty results vector
        brand_name = ast.literal_eval(brand_name)
        res = []
        if isinstance(brand_name, list):
            for lab in brand_name:
                attempts = 0
                while attempts < 3:
                    try:
                        brand_logo = make_logo_search(driver, lab, wait_time=2)
                        break
                    except:
                        pass
                    finally:
                        attempts += 1
                res.append(brand_logo)
        else:
            attempts = 0
            while attempts < 3:
                try:
                    res = make_logo_search(driver, brand_name, wait_time=2)
                    break
                except:
                    pass
                finally:
                    attempts += 1
        download(res[brand_name], brand_name)
        return res
    else:
        return 'Error: No id field provided. Please specify a label.'
# ------------------------------------------------------------------------------
# Run app
if __name__ == '__main__':
    # Create driver
    driver = uplaod_logo()
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        driver.close()
