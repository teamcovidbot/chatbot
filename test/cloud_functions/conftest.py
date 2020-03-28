from flask import Flask, Request
import pytest

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
