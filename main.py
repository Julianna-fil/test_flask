from uuid import uuid4

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/data')
def data():
    def get_data():
        rows = []
        for i in range(10_000_000):
            yield(str(uuid4()))

    res = get_data()
    return render_template('data.html', res=res, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
