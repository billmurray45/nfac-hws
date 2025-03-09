import json
import math


def ping_pong(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "")

    if path == "/ping" and method == "GET":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"pong"]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Not Found"]

def server_info(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "")
    protocol = environ.get("SERVER_PROTOCOL", "")
    url = environ.get("RAW_URI", "")

    if path == "/info" and method == "GET":
        response_body = f"Method: {method}\nURL: {url}\nProtocol: {protocol}"
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [response_body.encode()]

    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"Not Found"]

def hello(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "")

    if path == "/" and method == "GET":
        response_body = json.dumps({"message": "Hello, nfactorial!"})
        start_response("200 OK", [("Content-Type", "application/json")])
        return [response_body.encode()]

def meaning(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "")

    if path == "/meaning-of-life" and method == "GET":
        response_body = json.dumps({"meaning": "42"})
        start_response("200 OK", [("Content-Type", "application/json")])
        return [response_body.encode()]

def fact(environ, start_response):
    path = environ.get("PATH_INFO", "")
    method = environ.get("REQUEST_METHOD", "")

    if method == "GET" and path.startswith("/"):
        num = int(path[1:])
        response_body = json.dumps({"nfactorial": math.factorial(num)})
        start_response("200 OK", [("Content-Type", "application/json")])
        return [response_body.encode()]
