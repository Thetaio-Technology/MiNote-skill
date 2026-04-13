---
name: minote-todo
description: Operate Xiaomi Cloud Notes todos through the existing local runtime when the user needs structured todo read and write actions without building a natural-language parser.
---

# MiNote Todo Skill

Use this skill when the user wants to operate Xiaomi Cloud Notes todos through the existing local runtime.

## Do

- Read pending todos.
- Read completed todos.
- Create a todo.
- Update a todo title.
- Complete a todo.
- Restore a completed todo.
- Delete a todo.
- Map user intent directly to existing command names.

## Do Not

- Claim support for private notes.
- Add a Chinese natural-language parser unless the user explicitly asks for it.
- Change the browser automation flow unless verification shows breakage.
- Introduce new abstractions before reusing the current command surface.

## Runtime Assumptions

- Use a Windows machine with Google Chrome installed.
- Ensure `bin/chromedriver.exe` matches the local Chrome version.
- Reuse the project-local browser profile when login state already exists.
- Run the browser launcher first if login state is missing or expired.

## Workflow

1. Run `python scripts/cli/open_mi_cloud.py` if login may be missing or expired.
2. Run `python scripts/cli/run_skill.py minote-todo <operation>` for structured execution.
3. Return backend results with minimal reshaping.
4. Treat `ok: false` as an execution failure and explain the operator-facing cause.
5. Verify login state and DOM stability first when an operation fails.

## References

- `references/interface.md`
- `references/examples.md`
- `references/checklist.md`
