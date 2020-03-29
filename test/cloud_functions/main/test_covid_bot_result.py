import pytest
import flask
import json
from unittest import mock
import os

from cloud_functions.main import covidbot_result
from conftest import BAD_IMAGE_URL, GOOD_IMAGE_URL

@mock.patch.dict(os.environ,
                 {'BAD_IMAGE_URL':BAD_IMAGE_URL,
                  'GOOD_IMAGE_URL':GOOD_IMAGE_URL})
class TestCovidbotResult:
    # The Twilio way of sending data in
    def test_returns_a_non_empty_str_when_given_data(
            self, app, valid_req_payload):
        with app.test_request_context(
                '/',
                data={'Memory': json.dumps(valid_req_payload)}):
            result: str = covidbot_result(flask.request)
            assert isinstance(result, str)
            assert result

    # The Google Cloud Function Testing tab (aka normal) way
    def test_returns_a_non_empty_str_when_given_json(
            self, app, valid_req_payload):
        with app.test_request_context(
                '/',
                json=valid_req_payload):
            result: str = covidbot_result(flask.request)
            assert isinstance(result, str)
            assert result

    def test_returns_a_valid_json_serialised_dict(
            self, app, valid_req_payload):
        with app.test_request_context(
                '/', 
                data={'Memory': json.dumps(valid_req_payload)}):
            result: str = covidbot_result(flask.request)
            assert isinstance(json.loads(result), (dict))

    def test_returns_result_with_expected_score_in_message(
            self, app, valid_req_payload):
        with app.test_request_context(
                '/',
                data={'Memory': json.dumps(valid_req_payload)}):
            result: str = covidbot_result(flask.request)
            loaded: dict = json.loads(result)
            i = 1 # Hardcoded
            assert 'actions' in loaded
            assert 'say' in loaded.get('actions')[i]
            assert 'Your score is 2' in loaded['actions'][i]['say']

    def test_returns_result_with_expected_image_url_in_show_images(
            self, app, valid_req_payload):
        with app.test_request_context(
                '/',
                data={'Memory': json.dumps(valid_req_payload)}):
            result: str = covidbot_result(flask.request)
            loaded: dict = json.loads(result)
            i = 3 # Hardcoded
            assert 'actions' in loaded
            assert 'show' in loaded.get('actions')[i]
            assert 'images' in loaded['actions'][i]['show']
            assert 'url' in loaded['actions'][i]['show']['images'][0]
            assert BAD_IMAGE_URL in loaded['actions'][i]['show']['images'][0]['url']
