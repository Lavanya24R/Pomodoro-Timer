from flask import Flask, render_template, redirect, url_for
import subprocess
import webbrowser
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/end')
def index1():
    print("Received request to /end")
    return render_template('index.html')


@app.route('/start_pomodoro')
def start_pomodoro():
    try:
        subprocess.Popen(["python", "timer.py"])
        return "Pomodoro timer started!"
    except Exception as e:
        return f"An error occurred: {e}"

#@app.route('/timer_ended')
#def timer_ended():
    #return redirect(url_for('index1'))

if __name__ == '__main__':
    app.run(debug=True)
