"""Acceptance tests linked to the criteria in the README."""

import unittest

from src.contracts import Command, ObjectClass, SensorObservation
from src.pipeline import execute


class PipelineAcceptanceTests(unittest.TestCase):
    def test_valid_pedestrian_causes_braking(self) -> None:
        command = execute(
            SensorObservation(1000, 8.0, ObjectClass.PEDESTRIAN), 0.96, 1080
        )
        self.assertEqual(command.command, Command.BRAKE)

    def test_low_confidence_causes_safe_stop(self) -> None:
        command = execute(
            SensorObservation(1000, 8.0, ObjectClass.PEDESTRIAN), 0.58, 1080
        )
        self.assertEqual(command.command, Command.SAFE_STOP)

    def test_stale_perception_causes_safe_stop(self) -> None:
        command = execute(
            SensorObservation(1000, 30.0, ObjectClass.VEHICLE), 0.96, 1200
        )
        self.assertEqual(command.command, Command.SAFE_STOP)

    def test_clear_path_allows_cruise(self) -> None:
        command = execute(
            SensorObservation(1000, 30.0, ObjectClass.PEDESTRIAN), 0.96, 1080
        )
        self.assertEqual(command.command, Command.CRUISE)


if __name__ == "__main__":
    unittest.main()
