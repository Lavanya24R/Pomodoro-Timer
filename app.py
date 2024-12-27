from flask import Flask, render_template, send_from_directory 
app = Flask(__name__) 
import subprocess 

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/start_pomodoro') 
def start_pomodoro(): 
    # Here, you can start your Pygame app 
    try:
        subprocess.Popen(["python", "timer.py"]) 
        return "Pomodoro timer started!" 
    except Exception as e:
        return f"An error occured: {e}"
    
if __name__ == '__main__': 
    app.run(debug=True)
    