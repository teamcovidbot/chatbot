import pytest

from cloud_functions.main import get_correct_answers

class TestGetCorrectAnswers:
    def test_returns_expected_dict(self, q_and_a):
        expected = {"question1": "D",
                    "question2": "A",
                    "question3": "A"}
        actual = get_correct_answers(q_and_a)
        assert actual == expected

    def test_returns_empty_dict_when_no_true_value(self, q_and_a):
        q_a_without_true = {"questions": [{
                                "answers": [{
                                        "order": "D",
                                        "answer": "whatever_D",
                                        "correct": False
                                    }, {
                                        "order": "A",
                                        "answer": "whatever_A",
                                        "correct": False
                                    }]
                            }]
        }
        expected = {}
        actual = get_correct_answers(q_a_without_true)
        assert actual == expected

    def test_returns_empty_dict_when_2many_true_values(self, q_and_a):
        q_a_with_2many_true = {"questions": [{
                                "answers": [{
                                        "order": "D",
                                        "answer": "whatever_D",
                                        "correct": True
                                    }, {
                                        "order": "A",
                                        "answer": "whatever_A",
                                        "correct": True
                                    }]
                            }]
        }
        expected = {}
        actual = get_correct_answers(q_a_with_2many_true)
        assert actual == expected

    def test_returns_empty_dict_when_invalid_data(self, q_and_a):
        q_a_invalid = {"no questions": "here"}
        expected = {}
        actual = get_correct_answers(q_a_invalid)
        assert actual == expected
