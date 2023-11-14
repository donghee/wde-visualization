from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    subject = 'visualization'
    return render_template('index.html', subject=subject)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5053, debug=True)
