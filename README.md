# Autonomy Interface Lab

> A clean-room simulation of an autonomy pipeline, designed to demonstrate explicit component contracts, traceability, and acceptance testing.

## Why this project exists

Autonomous and embedded systems are rarely a single algorithm. They are systems of independently owned components that must exchange reliable information, make bounded decisions, and produce evidence that the integration works.

This repository is an independent, synthetic demonstration. It contains no employer code, datasets, vehicle configurations, customer information, or proprietary implementation details.

## The scenario

The simulation moves one synthetic pedestrian observation through four components:

```text
Sensor input → Perception → Planner → Safety monitor → Vehicle command
```

Each handoff has a defined contract. The safety monitor rejects stale or low-confidence perception results and commands a safe stop instead.

## What it demonstrates

- Message contracts with typed Python dataclasses
- Clear ownership boundaries between components
- Timestamp and confidence validation at integration boundaries
- Deterministic synthetic scenarios and acceptance tests
- A small, inspectable example of requirement-to-test traceability

## Run it

This project uses only the Python standard library.

```bash
python3 run_demo.py
python3 -m unittest discover -s tests -v
```

## Acceptance criteria

| ID | Requirement | Acceptance evidence |
| --- | --- | --- |
| AC-01 | A valid pedestrian observation must produce a braking command. | `test_valid_pedestrian_causes_braking` |
| AC-02 | Low-confidence perception must produce a safe stop. | `test_low_confidence_causes_safe_stop` |
| AC-03 | Stale perception must produce a safe stop. | `test_stale_perception_causes_safe_stop` |
| AC-04 | A clear path must permit a cruise command. | `test_clear_path_allows_cruise` |

## Structure

```text
src/contracts.py       Message definitions and interface rules
src/pipeline.py        Synthetic component implementations
run_demo.py            Executable scenarios
tests/test_pipeline.py Acceptance tests
```

## Professional context

This project illustrates the kind of systems thinking used in multi-team, multi-component product delivery: agree the interface, make timing and quality assumptions explicit, validate failures at the boundary, and retain evidence that the integrated behavior meets an agreed acceptance criterion.
