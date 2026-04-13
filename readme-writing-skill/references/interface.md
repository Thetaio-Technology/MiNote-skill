# Interface

## Input

This skill expects one or more of the following inputs:

- a repository `README.md`
- a user report describing GitHub rendering problems
- a target repository URL or section anchor that must be corrected
- a maintainer preference such as "keep changes minimal" or "make it more formal"

## Output

The expected output is:

- a corrected `README.md` or a set of focused README edits
- a short explanation of what was fixed and why
- optional follow-up notes about residual issues such as broken paths or inconsistent naming

## Decision Rules

- if GitHub rendering and local editor preview differ, follow GitHub
- if a section is structurally fine but sounds overly generated, rewrite only that section
- if a link target does not exist, retarget it to a real section or canonical URL
- if an issue is cosmetic but affects homepage readability, fix it
- if a rewrite would change project intent, stop and ask first

## Constraints

- do not rewrite the whole README unless explicitly requested
- do not add unsupported styling tricks for GitHub rendering
- do not turn a project README into a long internal design note
