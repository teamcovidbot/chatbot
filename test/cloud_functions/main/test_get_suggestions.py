import pytest

from cloud_functions.main import get_suggestions

class TestGetSuggestions:
    def test_returns_string_with_reminder(self):
        expected_substring = 'Reminder'
        actual = get_suggestions()
        assert expected_substring in actual
