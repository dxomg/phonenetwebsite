from flask import Flask, render_template
import psutil
app = Flask(__name__)

footername = "Dxomg"

@app.route('/')
def main():
    footername = "Dxomg"
    home = "Home"
    server = "Server"
    info = "Info"
    return render_template('index.html',footername=footername, home=home, server=server, info=info)

@app.route('/server')
def server():
    footername = "Dxomg"
    home = "Home"
    server = "Server"
    info = "Info"
    return render_template('server.html', footername=footername, home=home, server=server, info=info)

@app.route('/info')
def info():
    footername = "Dxomg"
    ram = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    total = (round(ram + swap))/2
    home = "Home"
    server = "Server"
    info = "Info"
    return render_template('info.html', ram=ram, swap=swap, total=total, footername=footername, home=home, server=server, info=info)

if __name__ == '__main__':
    app.run("0.0.0.0", 1234)
