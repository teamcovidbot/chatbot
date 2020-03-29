from flask import Flask, Request
import pytest

GOOD_IMAGE_URL='http://some.host/good.jpg'
BAD_IMAGE_URL='http://some.host/bad.jpg'

@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    return app

@pytest.fixture(scope='module')
def valid_req_payload():
    return {
        "twilio": {
            "messaging.whatsapp":
                {
                    "To":"whatsapp:+14155238886",
                    "From":"whatsapp:+32478585416",
                    "MessageSid":"SM53501e9374ef5279e93dc384b74f6f03"
                },
            "collected_data": {
                "covid_19_questionary": {
                    "answers": {
                        "question2": {
                            "confirm_attempts":0,
                            "answer":"A",
                            "filled":True,
                            "type":"Multiple_Choice_Value",
                            "confirmed":False,
                            "validate_attempts":1,
                            "attempts":1},
                        "question1":{
                            "confirm_attempts":0,
                            "answer":"D",
                            "filled":True,
                            "type":"Multiple_Choice_Value",
                            "confirmed":False,
                            "validate_attempts":1,
                            "attempts":1},
                        "question3":{
                            "answer":"C",
                            "type":"Multiple_Choice_Value",
                            "filled":True,
                            "attempts":1,
                            "validate_attempts":1,
                            "confirm_attempts":0,
                            "confirmed":False,
                            "media":None}
                    },
                    "date_completed":"2020-03-28T15:33:46Z",
                    "date_started":"2020-03-28T15:33:37Z",
                    "status":"complete"
                }
            }
        }
    }

@pytest.fixture(scope='module')
def q_and_a():
    return {
    "questions": [{
			"name": "question1",
            "question": "First question",
            "answers": [{
                    "order": "D",
                    "answer": "whatever_D",
                    "correct": True
                }, {
                    "order": "A",
                    "answer": "whatever_A",
                    "correct": False
                }, {
                    "order": "C",
                    "answer": "whatever_C",
                    "correct": False
                }, {
                    "order": "B",
                    "answer": "whatever-B",
                    "correct": False
                }
            ]
        }, {
			"name": "question2",
            "question": "Second question",
            "answers": [{
                    "order": "A",
                    "answer": "whatever_A",
                    "correct": True
                }, {
                    "order": "C",
                    "answer": "whatever_B",
                    "correct": False
                }, {
                    "order": "B",
                    "answer": "whatever_C",
                    "correct": False
                }, {
                    "order": "D",
                    "answer": "whatever_D",
                    "correct": False
                }
            ]
        }, {
			"name": "question3",
            "question": "Third question",
            "answers": [{
                    "order": "A",
                    "answer": "whatever_A",
                    "correct": True
                }, {
                    "order": "C",
                    "answer": "whatever_C",
                    "correct": False
                }, {
                    "order": "D",
                    "answer": "whatever_C",
                    "correct": False
                }, {
                    "order": "B",
                    "answer": "whatever_B",
                    "correct": False
                }
            ]
        }]
    }
