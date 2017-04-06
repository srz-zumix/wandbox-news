import requests
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/wandbox-news-kick')
def kick():
    """Return a friendly HTTP greeting."""
    project = ''
    branch = 'master'
    token = ''
    trigger_build_url='https://circleci.com/api/v1.1/project/github/{0}/tree/{1}'.format(project, branch)
    if token:
        trigger_build_url += '?circle-token=' + token
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    parameter = { 'build_parameters': { 'RUN_NIGHTLY_BUILD': 'true'} }
    payload = json.dumps(parameter)
    r = requests.post(trigger_build_url, data=payload, headers=headers)
    r.raise_for_status()
    return r


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
