import pytest

from cloud_functions.main import parse_twilio

class TestParseTwilio:
    def test_returns_expect_result(self, valid_req_payload):
        expected = {"question1": "D",
                    "question2": "A",
                    "question3": "C"}
        actual = parse_twilio(valid_req_payload)
        assert actual == expected

    def test_returns_empty_dict_when_invalid_payload(self):
        wrong_payload = {'wrong': 'structure'} 
        expected = {}
        actual = parse_twilio(wrong_payload)
        assert actual == expected
