# BlueTeamTools

Small collection of defensive security experiments and blue-team learning projects.

This repository is intentionally early-stage. It currently contains a Python honeypot proof of concept that simulates a decoy application, detects a placeholder tampering condition, displays a warning popup, and calls a defensive-action hook for future expansion.

## Current Project

### Honeypot Proof of Concept

Location: `Honeypot/ProofOfConcept.py`

The honeypot script demonstrates a basic defensive workflow:

- Runs a dummy application flow to mimic normal behavior
- Simulates tampering detection
- Displays a local warning popup using `tkinter`
- Calls a placeholder `defensive_action()` function for future response logic

The defensive action is intentionally left as a stub. Future implementations could include alerting, logging, host isolation in a lab, or integration with a monitoring pipeline.

## Why This Exists

I am using this repository to build practical blue-team tooling and document my growth in defensive security engineering. The goal is to keep projects small, readable, and focused on concepts that matter in real environments:

- Detection logic
- Defensive response design
- Safe security testing practices
- Python automation for security workflows
- Clear documentation and maintainable code

## Repository Structure

```text
BlueTeamTools/
├── Honeypot/
│   └── ProofOfConcept.py
├── README.md
├── readme.txt
└── .gitignore
```

## Running the Honeypot POC

Requirements:

- Python 3
- A desktop environment that supports `tkinter` popup windows

Run:

```bash
python Honeypot/ProofOfConcept.py
```

On some systems, `tkinter` may need to be installed separately.

## Roadmap

Planned improvements:

- Replace the hardcoded tampering flag with real detection conditions
- Add structured event logging
- Add configurable response actions
- Add safer lab-only network isolation examples
- Add unit tests around detection and response behavior
- Split reusable logic into modules as the project grows

## Responsible Use

This repository is for educational and defensive security purposes only. Use these tools only in systems, labs, and environments where you have explicit permission to test.
