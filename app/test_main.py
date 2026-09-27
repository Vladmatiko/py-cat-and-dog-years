import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                28, 22, [3, 1], id="equal_cat_dogs_years_to_human_age"
            ),
            pytest.param(
                0, 0, [0, 0], id="cat_dog_years_zero_value"
            ),
            pytest.param(
                14, 14, [0, 0], id="cat_and_dog_14_years"
            ),
            pytest.param(
                15, 15, [1, 1], id="cat_and_dog_15_years"
            ),
            pytest.param(
                23, 23, [1, 1], id="cat_and_dog_23_years"
            ),
            pytest.param(
                24, 24, [2, 2], id="cat_and_dog_24_years"
            ),
            pytest.param(
                27, 28, [2, 2], id="cat_and_dog_next_years_before_border"
            ),
            pytest.param(
                28, 29, [3, 3], id="cat_and_dog_next_years_after_border"
            ),
            pytest.param(
                100, 100, [21, 17], id="cat_dog_years_hundred_value"
            )
        ]
    )
    def test_dog_age(self, cat_age: int, dog_age: int, expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestRaises:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (
                [], "0", TypeError
            ),
            (
                45, -1 , ValueError
            ),
            (
                -1, 33, ValueError
            )
        ]
    )
    def test_cat_dog_raises(self
                            , cat_age: int
                            , dog_age: int
                            , expected: type[Exception]) -> None:
        with pytest.raises(expected):
            get_human_age(cat_age, dog_age)
