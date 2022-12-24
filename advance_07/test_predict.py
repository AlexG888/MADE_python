import pytest

from predict import predict_message_mood


class TestModel:
    def predict(self, message: str) -> float:
        message_partition = message.partition("\n")
        if message_partition[0] == "":
            raise ValueError("Отсутствует оценка")
        if message_partition[2] == "":
            raise ValueError("Отсутствует комментарий")
        try:
            mark = int(message_partition[0])
            if 0 <= mark <= 5:
                return 1 - (1 / len(message_partition[2]) ** (1 / 2))
            return None
        except TypeError:
            raise TypeError("Оценка может быть только Int") from None
        except ValueError:
            raise ValueError("Оценка вне диапазона возможных значений") from None


@pytest.fixture
def heavy_model():
    return TestModel()


def test_predict_perfect(heavy_model):
    assert (
        predict_message_mood(
            "5\nПривет! Отличная работа, поставлю за нее максимальный балл", heavy_model
        )
        == "отл"
    )


def test_predict_norm(heavy_model):
    assert predict_message_mood("2\nПривет! Плохо!", heavy_model) == "норм"


def test_predict_bad(heavy_model):
    assert predict_message_mood("5\n..", heavy_model) == "неуд"


def test_predict_empty_mark_exeption(heavy_model):
    with pytest.raises(ValueError):
        predict_message_mood("\n..", heavy_model)


def test_predict_empty_comment_exeption(heavy_model):
    with pytest.raises(ValueError):
        predict_message_mood(
            "\nПривет! Отличная работа, поставлю за нее максимальный балл", heavy_model
        )


def test_predict_mark_not_int(heavy_model):
    with pytest.raises(ValueError):
        predict_message_mood(
            "Привет!\n Отличная работа, поставлю за нее максимальный балл", heavy_model
        )


def test_predict_mark_out_of_range(heavy_model):
    with pytest.raises(TypeError):
        predict_message_mood("100\n Отличная работа", heavy_model)


def test_predict_with_thresholds(heavy_model):
    assert predict_message_mood(
        "5\nПривет! Отличная работа, поставлю за нее максимальный балл",
        heavy_model,
        0.1,
        0.9,
    )


def test_predict_with_thresholds_int_type(heavy_model):
    assert predict_message_mood(
        "5\nПривет! Отличная работа, поставлю за нее максимальный балл",
        heavy_model,
        0,
        1,
    )


def test_predict_with_thresholds_string_type(heavy_model):
    with pytest.raises(TypeError):
        predict_message_mood("100\n Отличная работа", heavy_model, "0.1", "0.8")


def test_predict_bounds1(heavy_model):
    with pytest.raises(ValueError):
        predict_message_mood(
            "5\nПривет! Отличная работа, поставлю за нее максимальный балл",
            heavy_model,
            0,
            10,
        )


def test_predict_bounds2(heavy_model):
    with pytest.raises(ValueError):
        predict_message_mood(
            "5\nПривет! Отличная работа, поставлю за нее максимальный балл",
            heavy_model,
            -3,
            0.8,
        )
