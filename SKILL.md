# minote-skill

## Purpose

`minote-skill` is the agent-facing skill layer built on top of `minote-driver`.

It packages the verified Xiaomi Cloud Notes todo automation into a capability that is easier to expose, route, and integrate than the raw browser automation runtime.

## Current Capability

Current package:

- `minote-todo`

Supported operations:

- Read pending todos
- Read completed todos
- Create a todo
- Update a todo title
- Complete a todo
- Restore a completed todo
- Delete a todo

Out of scope:

- Private notes
- Chinese natural-language parsing
- Browser-runtime implementation details

## Relationship To minote-driver

- `minote-driver` owns the runtime, CLI, and validation scripts
- `minote-skill` owns the capability definition, interface contract, and integration-facing packaging

## Package Layout

- `README.md`: showcase-oriented introduction
- `SKILL.md`: top-level skill definition
- `skills/minote-todo/`: concrete capability package

## Integration Notes

- Use this repository as the publishable skill surface
- Keep runtime implementation changes in `minote-driver`
- Sync this repository from `minote-driver` when skill docs or contracts change
