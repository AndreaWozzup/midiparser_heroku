import requests
from WebServer import start_server
from threading import Thread


def threaded_function():
    start_server()


def test_upload():

    thread = Thread(target=threaded_function)
    thread.setDaemon(True)
    thread.start()

    files = {'file': open('test.mid', 'rb')}
    request = requests.post("http://127.0.0.1:5000/upload", files=files)

    assert(request.status_code == 200)
    assert("test.mid" in request.text)


def test_root():

    thread = Thread(target=threaded_function)
    thread.setDaemon(True)
    thread.start()

    request = requests.get("http://127.0.0.1:5000")
    assert(request.status_code == 200)


def test_upload_fail():
    thread = Thread(target=threaded_function)
    thread.setDaemon(True)
    thread.start()

    request = requests.post("http://127.0.0.1:5000/upload")
    assert(request.status_code == 405)


if __name__ == "__main__":
    test_upload()
    test_upload_fail()
    test_root()


