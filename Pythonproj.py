from flask import Flask, render_template, request, json, redirect
from DinoGame import rundino
import cv2
import pyautogui
import numpy as np
from threading import Thread


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def entry_point():
    return render_template('index_2.html')

@app.route('/rundino')
def go_to_dino():
    Thread(target=rundino).start()
    url='https://chromedino.com/'
    return redirect(url, code=307)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
