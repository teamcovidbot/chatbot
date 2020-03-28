import pytest

from cloud_functions.main import calculate_score

class TestCalculateScore:
    def test_returns_maximum_result_when_equal(self):
        same4both = {"q1": "A",
                     "q2": "B",
                     "q3": "C"}
        given = same4both
        correct = same4both
        expected = len(same4both)

        actual = calculate_score(
            given_answers=given,
            correct_answers=correct)
        
        assert actual == expected

    def test_returns_zero_when_no_answers_given(self):
        correct = {"q1": "A",
                   "q2": "B",
                   "q3": "C"}
        given = {}
        expected = 0

        actual = calculate_score(
            given_answers=given,
            correct_answers=correct)
        
        assert actual == expected

    def test_returns_correct_number_when_some_but_not_all_correct(self):
        correct = {"q1": "A",
                   "q2": "B",
                   "q3": "C"}
        given = {"q1": "A",
                 "q2": "B",
                 "q3": "WRONG"}
        expected = 2

        actual = calculate_score(
            given_answers=given,
            correct_answers=correct)
        
        assert actual == expected
