from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

# /time
@app.route('/time')
def current_time():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return time_string

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
