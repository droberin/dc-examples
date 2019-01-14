import time
import redis
from flask import Flask
from os import listdir, path

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello, World! I have been seen {} times.\n'.format(count)


@app.route('/shared')
def shared_folder(shared_folder_example='/app/shared'):
    if path.isdir(shared_folder_example):
        in_shared_folder = listdir(shared_folder_example)
        return 'Stuff in shared folder: {}\n'.format(in_shared_folder)
    else:
        return 'Directory {} not found in storage'.format(shared_folder_example)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
