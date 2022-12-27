from time import time
from typing import Union, TextIO, TypeVar


Number = Union[int, float, None]
Str = Union[str, None]
FileObj = Union[TextIO, None]
SelfMetricTimer = TypeVar("SelfMetricTimer", bound="MetricTimer")


class BaseMetric:
    metric: Str = None

    def __init__(self, name: str):
        self.name = name
        self.value: Number = None

    def get_name(self) -> str:
        if self.metric:
            return str(self.name) + "." + str(self.metric)
        return ""

    def get_value(self) -> Number:
        return self.value

    def add(self, value):
        pass

    def clear(self):
        self.value = None


class MetricAvg(BaseMetric):
    metric: Str = "avg"

    def __init__(self, name: str):
        super().__init__(name)
        self.num_calls: int = 0

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value: Number = None):
        if not value:
            raise ValueError("No value. Enter some value")
        self.num_calls += 1
        if self.value:
            self.value = (self.value * (self.num_calls - 1) + value) / self.num_calls
        else:
            self.value = value

    def clear(self):
        super().clear()
        self.num_calls = 0


class MetricCount(BaseMetric):
    metric: Str = "count"

    def __init__(self, name: str):
        super().__init__(name)
        self.num_calls: int = 0

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value: Number = None):
        if value:
            raise ValueError("Add don't have args")
        self.num_calls += 1
        self.value = self.num_calls

    def clear(self):
        super().clear()
        self.num_calls = 0


class MetricTimer(BaseMetric):
    metric: Str = "timer"

    def __init__(self, name: str, file: FileObj = None):
        super().__init__(name)
        self.file: FileObj = file
        self.start: float = 0
        self.end: float = 0
        self.num_calls: int = 0

    def __enter__(self: SelfMetricTimer) -> SelfMetricTimer:
        self.start = time()
        self.num_calls += 1
        return self

    def __exit__(self, cls, error: str, trace_back) -> bool:
        self.end = time()
        if self.value:
            self.value += self.end - self.start
        else:
            self.value = self.end - self.start

        if self.file:
            print(error, file=self.file)
        if isinstance(error, Exception):
            return True
        return True

    def get_name(self) -> str:
        return super().get_name()

    def get_value(self) -> Number:
        return self.value

    def add(self, value=None):
        if not value:
            raise ValueError("No value. Enter some value")
        self.num_calls += 1
        if self.value:
            self.value += value
        else:
            self.value = value

    def clear(self):
        super().clear()
        self.num_calls = 0


class Stats:
    metrics: dict = dict()

    @staticmethod
    def timer(name: str, file: FileObj = None) -> MetricTimer:
        timer_metric = MetricTimer(name, file)
        metric_name = timer_metric.get_name()
        if metric_name not in Stats.metrics.keys():
            Stats.metrics[metric_name] = timer_metric
        return Stats.metrics[metric_name]

    @staticmethod
    def avg(name: str) -> MetricAvg:
        avg_metric = MetricAvg(name)
        metric_name = avg_metric.get_name()
        if metric_name not in Stats.metrics.keys():
            Stats.metrics[metric_name] = avg_metric
        return Stats.metrics[metric_name]

    @staticmethod
    def count(name: str) -> MetricCount:
        count_metric = MetricCount(name)
        metric_name = count_metric.get_name()
        if metric_name not in Stats.metrics.keys():
            Stats.metrics[metric_name] = count_metric
        return Stats.metrics[metric_name]

    @staticmethod
    def collect() -> dict:
        answer: dict = dict()
        for key, val in Stats.metrics.items():
            if val.num_calls > 0:
                answer[key] = val.get_value()
            val.clear()
        Stats.metrics = dict()
        return answer
