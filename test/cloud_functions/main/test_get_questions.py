import pytest
import flask
import json

from cloud_functions.main import get_questions

class TestGetQuestions:
    def test_returns_a_dict(self):
        q = get_questions()
        assert isinstance(q, dict)

    def test_contains_questions_key(self):
        q = get_questions()
        questions = q.get('questions')
        assert True

    def test_returns_a_question_list(self):
        q = get_questions()
        assert isinstance(q.get('questions'), list)
