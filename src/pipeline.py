"""Small synthetic autonomy pipeline with explicit component boundaries."""

from __future__ import annotations

from .contracts import Command, ObjectClass, PerceptionResult, SensorObservation, VehicleCommand

MIN_CONFIDENCE = 0.80
MAX_PERCEPTION_AGE_MS = 150
BRAKE_DISTANCE_M = 12.0


def perceive(observation: SensorObservation, confidence: float) -> PerceptionResult:
    """Convert a synthetic sensor observation to a perception result."""
    return PerceptionResult(
        timestamp_ms=observation.timestamp_ms,
        object_class=observation.apparent_class,
        range_m=observation.range_m,
        confidence=confidence,
    )


def plan(perception: PerceptionResult) -> VehicleCommand:
    """Create a nominal command without overriding the safety boundary."""
    if (
        perception.object_class is ObjectClass.PEDESTRIAN
        and perception.range_m <= BRAKE_DISTANCE_M
    ):
        return VehicleCommand(Command.BRAKE, "pedestrian within braking distance")
    return VehicleCommand(Command.CRUISE, "path is clear in synthetic scenario")


def safety_gate(
    perception: PerceptionResult, proposed: VehicleCommand, now_ms: int
) -> VehicleCommand:
    """Reject stale or low-confidence messages before they reach the vehicle."""
    age_ms = now_ms - perception.timestamp_ms
    if age_ms > MAX_PERCEPTION_AGE_MS:
        return VehicleCommand(Command.SAFE_STOP, f"stale perception: {age_ms} ms old")
    if perception.confidence < MIN_CONFIDENCE:
        return VehicleCommand(
            Command.SAFE_STOP,
            f"low perception confidence: {perception.confidence:.2f}",
        )
    return proposed


def execute(
    observation: SensorObservation, confidence: float, now_ms: int
) -> VehicleCommand:
    """Run the synthetic message through perception, planning and safety."""
    perception = perceive(observation, confidence)
    proposed = plan(perception)
    return safety_gate(perception, proposed, now_ms)
