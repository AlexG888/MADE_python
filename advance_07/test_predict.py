import pytest

from predict import predict_message_mood, SomeModel


@pytest.fixture
def heavy_model():
    print("LOAD")
    return SomeModel()


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
