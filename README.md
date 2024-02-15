# sample-flask-app

## What is this?

A small Flask application to use as a placeholder for a real application when using Kubernetes, cloud services, etc. It runs on gunicorn in a quick and dirty Alpine Linux container.

## What do I use it for?

You might want to use it if you're working with containers or something like Kubernetes and you'd like something that stands in for an actual workload. It will answer some basic queries over HTTP (just like a web server).

| Endpoint               | MIME Type | Comments                                                                                |
| ---------------------- | --------- | --------------------------------------------------------------------------------------- |
| `/`                    | text/json | returns JSON containing a simple 'hello world, a date, and the URL the client requested |
| `/err/code`            | text/html | where `<code>` is an HTTP status code of your choice                                    |
| `/help`                | text/html | returns 200 and a short message indicating what the app does                            |
| `/health`              | text/html | returns 200 and "ok" - this is a liveness check for load balancers/kubernetes           |
| `/uuid`                | text/html | returns a random UUID                                                                   |
| `/flaky/code/failrate` | text/html | has a `<failrate>` chance of returning a status code `<code>`, else returns 200         |

## How would I send requests to it?

e.g.

```bash
mdj@nostromo:~/sample-flask-app$ curl -i http://localhost/err/418
HTTP/1.1 418 I'M A TEAPOT
Server: gunicorn/20.0.4
Date: Wed, 14 Feb 2024 04:05:31 GMT
Connection: keep-alive
Content-Type: text/html; charset=utf-8
Content-Length: 0

```

That's all it does, and it's not guaranteed to be secure or suitable for anything at all :)

## Building

Here's how I build this and push it to Docker Hub. I don't use the `:latest` tag.

```bash
docker build -t mikejohnson/sample-flask-app:4 -f Dockerfile.alpine .
docker push mikejohnson/sample-flask-app:4
docker run -it -d -p 80:80 mikejohnson/sample-flask-app:4
curl -s http://localhost/health
```

## How do I run it from a shell?

`docker run -it -d -p 80:80 mikejohnson/sample-flask-app:4`

## Then what?

If you have curl on your system, try this:

`curl -i http://localhost/health`

and you might see something like this:

```bash
mdj@nostromo:~/sample-flask-app$ curl -i http://localhost/
HTTP/1.1 200 OK
Server: gunicorn/20.0.4
Date: Wed, 14 Feb 2024 04:05:02 GMT
Connection: keep-alive
Content-Type: application/json
Content-Length: 104

{"date":"Wed, 14 Feb 2024 00:00:00 GMT","greeting":["Hello","World"],"you_visited":"http://localhost/"}
```

or even something like this:

```bash
mdj@nostromo:~/sample-flask-app$ curl -i http://localhost/err/418
HTTP/1.1 418 I'M A TEAPOT
Server: gunicorn/20.0.4
Date: Wed, 14 Feb 2024 04:05:31 GMT
Connection: keep-alive
Content-Type: text/html; charset=utf-8
Content-Length: 0

```

If you have httpie, try:

`http http://localhost/err/418`

Or, if you use wget:

`wget -q -O - http://localhost/`

[You can even use a web browser](http://localhost/)
