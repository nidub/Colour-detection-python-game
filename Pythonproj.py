from flask import Flask, render_template, request, json
import cv2
import pyautogui
import numpy as np


app = Flask(__name__)

@app.route('/')
def entry_point():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
