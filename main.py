from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024
socketio = SocketIO(app, engineio_logger=True, logger=True, max_http_buffer_size=1e8, ping_timeout=60000)


@app.route("/", methods=['GET', 'POST'])
def toy_page():
    return render_template('new.html')


@socketio.on('upload file')
def upload_file(message):
    print("in upload file")


if __name__ == '__main__':
    socketio.run(app, debug=True)
