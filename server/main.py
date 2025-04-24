def app(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    if method == "GET" and path == "/ping":
        data = b"pong"
        status = "200 OK"

    elif method == "GET" and path == "/info":
        protocol = environ["SERVER_PROTOCOL"]
        info = f"Method: {method}\nURL: {path}\nProtocol: {protocol}"
        data = info.encode("utf-8")
        status = "200 OK"

    else:
        data = b"Not Found"
        status = "404 Not Found"

    headers = [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ]
    start_response(status, headers)
    return iter([data])
    
