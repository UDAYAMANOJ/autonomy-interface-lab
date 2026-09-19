"""Run deterministic scenarios for the autonomy interface lab."""

from src.contracts import ObjectClass, SensorObservation
from src.pipeline import execute


SCENARIOS = (
    ("valid pedestrian", SensorObservation(1000, 8.0, ObjectClass.PEDESTRIAN), 0.96, 1080),
    ("low confidence", SensorObservation(2000, 8.0, ObjectClass.PEDESTRIAN), 0.58, 2080),
    ("stale perception", SensorObservation(3000, 40.0, ObjectClass.VEHICLE), 0.96, 3200),
    ("clear path", SensorObservation(4000, 30.0, ObjectClass.PEDESTRIAN), 0.96, 4070),
)


if __name__ == "__main__":
    for name, observation, confidence, now_ms in SCENARIOS:
        command = execute(observation, confidence, now_ms)
        print(f"{name:16} -> {command.command.value:9} | {command.reason}")
