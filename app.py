from flask import Flask,render_template,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world 2'

if __name__ == '__main__':
    app.run(debug=False)
