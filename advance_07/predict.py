class SomeModel:
    def predict(self, message: str) -> float:
        """Метод определяет качество фитбека получаемого в строке message.
        Оценка качества зависит от длины комментария.
        Структура фитбека:
        "Оценка\nкомментнарий"
        """
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


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    result = model.predict(message)
    if result < bad_thresholds:
        return "неуд"
    if result > good_thresholds:
        return "отл"
    return "норм"
