#flask thingy back-end
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
from tkinter import *


#Code taken from a project I coded 05.2022
def msg1():
    url = 'https://api.kanye.rest'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    soup = str(soup)
    msg = soup[10:len(soup) - 2] + " - Kayne West"
    return msg

#below code found at https://predictivehacks.com/?all-tips=how-to-add-action-buttons-in-flask
app = Flask(__name__)

@app.route('/')
def python():
    if "New Quote" in request.form:
        return msg1()
    return render_template('python.html')



