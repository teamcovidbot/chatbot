import json
import os


def covidbot_result(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    payload = None
    # Next line is how we expect real data to come in from Twilio
    if request.form and request.form.get('Memory'):
        payload = json.loads(request.form.get('Memory'))
    else:
        # The normal way
        payload = request.get_json()

    # Real payload processing starts here
    given_answers = parse_twilio(payload)
    correct_answers = get_correct_answers(get_questions())
    score = calculate_score(given_answers, correct_answers)
    image_url = determine_image(score)
    message = determine_message(score)
    suggestions = get_suggestions()

    return json.dumps({
        "actions": [
            {
                "say": "Even if you cannot sing, you can still hum happy birthday twice. That way you are certain your hands are clean."
            },
            {
                "say": message
            },
            {
                "say": suggestions
            },
            {
                "show": {
                    "body": "Mascot",
                    "images": [
                        {
                            "label": "Mascot",
                            "url": f"{image_url}"
                        }
                    ]
                }
            }
        ]
    })


def determine_image(score):
    if score < 6:
        return os.environ["BAD_IMAGE_URL"]
    else:
        return os.environ["GOOD_IMAGE_URL"]


def determine_message(score):
    if score < 5:
        return f"That was the last question! Your score is {score} out of 7. You are a danger to humankind."
    elif score < 6:
        return f"That was the last question. Your score is {score} out of 7. An almost perfect score. If you get everything right, I have a surprise for you"
    else:
        return "That was the last question. You had a perfect score! Here is a drawing you can use on social media to raise awareness!"


def get_suggestions():
    return """Reminder:\n
- you are required to stay at home to avoid contact outside of your family as much as possible\n
- work from home if your profession allows for it\n
- Non-essential shops and retail outlets will remain closed\n
- Maintain the required distance when taking public transport.\n
            """


def get_questions():
    return QUESTIONS


QUESTIONS = {
    "questions": [{
        "name": "question1",
        "question": "I am allowed to go outside for which case?",
        "answers": [{
            "order": "D",
            "answer": "I need to pick up my medicine from the pharmacist.",
            "correct": True
        }, {
            "order": "A",
            "answer": "I'm going for a jog with my friends in the parc.",
            "correct": False
        }, {
            "order": "C",
            "answer": "We have an appointment with the bank regarding our investment plan.",
            "correct": False
        }, {
            "order": "B",
            "answer": "We are taking the kids to the beach for the day.",
            "correct": False
        }
        ]
    }, {
        "name": "question2",
        "question": "Which bike trip am I allowed to do?",
        "answers": [{
            "order": "A",
            "answer": "60 kilometers all by myself.",
            "correct": True
        }, {
            "order": "C",
            "answer": "40 kilometers with a group of cyclists.",
            "correct": False
        }, {
            "order": "B",
            "answer": "10 kilometers with the whole family on Sunday.",
            "correct": False
        }, {
            "order": "D",
            "answer": "A bike trip to the parc to enjoy a sunny picnic.",
            "correct": False
        }
        ]
    }, {
        "name": "question3",
        "question": "When do I have the obligation to wash my hands?",
        "answers": [{
            "order": "A",
            "answer": "When I come home from the store.",
            "correct": True
        }, {
            "order": "C",
            "answer": "Every half hour.",
            "correct": False
        }, {
            "order": "D",
            "answer": "In the morning when I wake up.",
            "correct": False
        }, {
            "order": "B",
            "answer": "I just have to make sure to wash them at least 10 times a day",
            "correct": False
        }
        ]
    }, {
        "name": "question4",
        "question": "Which remedies are helpful to protect yourself against COVID-19?",
        "answers": [{
            "order": "B",
            "answer": "Stricltly follow government regulations.",
            "correct": True
        }, {
            "order": "A",
            "answer": "Absorb an unusually large amount of vitamin C.",
            "correct": False
        }, {
            "order": "C",
            "answer": "Drink lots of alcohol.",
            "correct": False
        }, {
            "order": "D",
            "answer": "Smoke sigarettes.",
            "correct": False
        }
        ]
    }, {
        "name": "question5",
        "question": "Children are still allowed to ..",
        "answers": [{
            "order": "B",
            "answer": "Play in the garden with other children of the same household.",
            "correct": True
        }, {
            "order": "A",
            "answer": "Play in the garden with the neighbours' children.",
            "correct": False
        }, {
            "order": "D",
            "answer": "Play with other children on the terrains of the local youth movement.",
            "correct": False
        }, {
            "order": "C",
            "answer": "Play in a public outdoor playground with children of the same household.",
            "correct": False
        }
        ]
    }, {
        "name": "question6",
        "question": "What do you do when you see that others are not following the rules?",
        "answers": [{
            "order": "D",
            "answer": "I instruct them to behave differently and contact local authorities when they don't want to listen.",
            "correct": True
        }, {
            "order": "B",
            "answer": "I cheerfully join them.",
            "correct": False
        }, {
            "order": "C",
            "answer": "I start picking a fight.",
            "correct": False
        }, {
            "order": "A",
            "answer": "I start filming and publicly shame them on social media.",
            "correct": False
        }
        ]
    }, {
        "name": "question7",
        "question": "How long do I have to wash my hands?",
        "answers": [{
            "order": "C",
            "answer": "Until I sang 'Happy Birthday' twice.",
            "correct": True
        }, {
            "order": "B",
            "answer": "At least 60 seconds.",
            "correct": False
        }, {
            "order": "A",
            "answer": "Washing your hands for 10 seconds is long enough.",
            "correct": False
        }, {
            "order": "D",
            "answer": "Until I don't feel like washing my hands any longer.",
            "correct": False
        }
        ]
    }
    ]
}


def parse_twilio(payload: dict) -> dict:
    """Parses twilio_payload and returns answers.
    payload: {
        "twilio": {
            "messaging.whatsapp": {...},
            "collected_data": {...}
        }
    }

    RETURN: {"question1": "D",
             "question2": "A",
             ...
            }
    """
    try:
        answers = payload['twilio']['collected_data']['covid_19_questionary']['answers']
        return {q: answers[q]['answer'] for q in answers.keys()}
    except KeyError:
        return {}


def get_correct_answers(q_and_a: dict) -> dict:
    """Gets the correct answers from the reference q_and_a
    q_and_a: {
        "questions": [{
			"name": "question1",
            "question": "I am allowed to go outside for which case?",
            "answers": [...]
        },
        {...}]
    }

    RETURN: {"question1": "D",
             "question2": "A",
             ...
            }
    """
    try:
        result = {}
        for q_a in q_and_a["questions"]:
            key = q_a["name"]
            values = [a["order"] for a in q_a["answers"] if a["correct"]]
            assert len(values) == 1
            result[key] = values[0]
        return result
    except AssertionError:
        return {}
    except KeyError:
        return {}


def calculate_score(given_answers: dict, correct_answers: dict) -> int:
    """Returns the number of correct answers.
    given_answers: {"question1": "X",
                    "question2": "Y",
                    ...
                    "questionN": "Z"}

    correct_answers: {"question1": "A",
                      "question2": "B",
                      ...
                      "questionN": "C"}

    RETURN: number of correct answers
    """
    result = 0
    for q, a in given_answers.items():
        if correct_answers.get(q) == a:
            result += 1
    return result
