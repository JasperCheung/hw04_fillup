#Jasper Cheung
#SoftDev1 pd 7
#Hw#04: Fill Up Yer Flask
#2017-09-24

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "my life is an error" 
@app.route("/one")
def one():
    return "Errno 10013 I LOVE IT!!!"
@app.route("/two")
def two():
    return "I disabled firewall and antivirus, still doesn't work"
@app.route("/three")
def three():
    return "what are sockets..."

if __name__ == "__main__":
    app.debug = True
    app.run()

