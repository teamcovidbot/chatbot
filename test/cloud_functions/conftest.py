from flask import Flask, Request
import pytest

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    return app

@pytest.fixture(scope='module')
def valid_req_payload():
    return {'message': 'hello'}
