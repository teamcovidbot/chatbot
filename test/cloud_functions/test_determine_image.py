import pytest
from unittest import mock
import os

from cloud_functions.main import determine_image
from conftest import BAD_IMAGE_URL, GOOD_IMAGE_URL

@mock.patch.dict(os.environ,
                 {'BAD_IMAGE_URL':BAD_IMAGE_URL,
                  'GOOD_IMAGE_URL':GOOD_IMAGE_URL})

class TestDetermineImage:
    @pytest.mark.parametrize('test_score', range(0,6))
    def test_returns_bad_image_when_score_lower_than_six(self, test_score):
        expected = BAD_IMAGE_URL
        actual = determine_image(test_score)
        assert actual == expected

    @pytest.mark.parametrize('test_score', range(6,8))
    def test_returns_good_image_when_score_gte_than_six(self, test_score):
        expected = GOOD_IMAGE_URL
        actual = determine_image(test_score)
        assert actual == expected
