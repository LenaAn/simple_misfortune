from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    count = r.incr('click_count')
    return f"CLICK COUNTER! Refresh to see the count increase! CLICK COUNT: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
