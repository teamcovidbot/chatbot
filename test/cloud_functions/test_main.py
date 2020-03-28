import pytest
import flask
import json

from cloud_functions.main import covidbot_result

class TestCovidbotResult:
    def test_returns_a_string(
            self, app, valid_req_payload):
        with app.test_request_context('/', json=valid_req_payload):
            result = covidbot_result(flask.request)
            assert isinstance(result, str)

    def test_returns_a_valid_json_serialised_dict_or_str(
            self, app, valid_req_payload):
        with app.test_request_context('/', json=valid_req_payload):
            result = covidbot_result(flask.request)
            print(result)
            assert isinstance(result, (dict, str))
