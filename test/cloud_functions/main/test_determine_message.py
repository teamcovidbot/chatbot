import pytest

from cloud_functions.main import determine_message

class TestDetermineMessage:
    @pytest.mark.parametrize('test_score', range(0,6))
    def test_returns_message_with_score_if_lower_than_six(self, test_score):
        expected_substring = f"Your score is {test_score}"
        actual = determine_message(test_score)
        assert expected_substring in actual

    @pytest.mark.parametrize('test_score', range(6,8))
    def test_returns_message_with_congrats_for_score_gte_six(self, test_score):
        expected_substring = f"You had a perfect score!"
        actual = determine_message(test_score)
        assert expected_substring in actual
