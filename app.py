from flask import Flask, render_template, request, json, redirect
from DinoGame import rundino
from threading import Thread  # From 'flask' module import 'Flask' class

app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')
def entry_point():
    return render_template('index_2.html')

@app.route('/rundino')
def go_to_dino():
    Thread(target=rundino).start()
    url='https://chromedino.com/'
    return redirect(url, code=307)

if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run(debug=True)  # Launch built-in web server and run this Flask webapp