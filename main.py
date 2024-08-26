"""
This is a small Cloud Run app available for testing purposes.
"""

import logging
import json

import google.cloud.logging

from flask import Flask, request

app = Flask(__name__)

client = google.cloud.logging.Client()
client.setup_logging()


@app.route("/", methods=['GET'])
def index():
    content = """
    <!DOCTYPE html>
    <html lang='en'>
        <head>
            <title>Simple Cloud Run App</title>
            <meta charset='utf-8'>
        </head>
        <body>
            <h2>Cloud Run app</h2>
            <p>This is a small Cloud Run app available for testing purposes. Call the method using args or json such as below.</p>
            <p>Available endpoints / calling methods</p>
            <ul>
                <li><a href="/exec?type=road-runner&speed=10">/exec?type=road-runner&speed=10</a> - GET or POST</li>
                <li>curl "HOST/exec?type=road-runner&speed=10"</li>
                <li>curl HOST/exec -d '{"type": "coyote", "speed": "5"}' -H 'Content-Type: application/json'</li>
            </ul>
            <p>content (args or json) and some of the caller info will be logged in Cloud Logging (under jsonPayload key).</p>
        </body>
    </html>
    """
    return content


""" Calling examples
    curl "http://localhost:8080/exec?type=road-runner&speed=10"
    curl http://localhost:8080/exec -d '{"type": "coyote", "speed": "5"}' -H 'Content-Type: application/json'
"""
@app.route('/exec', methods=['GET', 'POST'])
def exec():
    type = None
    content = None

    if request.args:
        type = "args"
        content = dict(request.args)
    elif request.content_type and request.get_json():
        type = "json"
        content = request.get_json()

    """ get some of the caller info """
    log_data = {
        "content": {
            "type": type if type else "unknown",
            "data": content if content else "unknown",
        },
        "invokation_info": {
            "x-forwarded-for": request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr),
            "user-agent": request.user_agent.string,
            "host": request.host,
            "method": request.method,
            "path": request.path,
            "url": request.url
        }
    }

    # structured log entry: appears under jsonPayload in the log entry.
    logging.info(json.dumps(log_data))
    return log_data


if __name__ == "__main__":
    # Development only: run "python main.py" and open http://localhost:8080
    # When deploying to Cloud Run, a production-grade WSGI HTTP server,
    # such as Gunicorn, will serve the app.
    app.run(port=8080, debug=True)