"""Public message contracts for the synthetic autonomy interface lab."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ObjectClass(str, Enum):
    PEDESTRIAN = "pedestrian"
    VEHICLE = "vehicle"
    UNKNOWN = "unknown"


class Command(str, Enum):
    CRUISE = "cruise"
    BRAKE = "brake"
    SAFE_STOP = "safe_stop"


@dataclass(frozen=True)
class SensorObservation:
    """Input owned by the sensor adapter in this synthetic example."""

    timestamp_ms: int
    range_m: float
    apparent_class: ObjectClass


@dataclass(frozen=True)
class PerceptionResult:
    """Output contract owned by the perception component."""

    timestamp_ms: int
    object_class: ObjectClass
    range_m: float
    confidence: float


@dataclass(frozen=True)
class VehicleCommand:
    """Output contract delivered to the simulated vehicle interface."""

    command: Command
    reason: str
