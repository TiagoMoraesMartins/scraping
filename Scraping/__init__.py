import os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

#Exemplo de definição de constante direto no app
app.config['TITLE'] = "Scraping"

#Definindo um secret key para poder utilizar o wtform
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

Bootstrap(app)

from Scraping import routes