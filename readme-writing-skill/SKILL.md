---
name: readme-writing-skill
description: Fix GitHub README rendering and wording issues when a README drafted in local editors needs to be normalized for GitHub homepage rendering.
---

# README Writing Skill

Use this skill when a repository `README.md` renders incorrectly on GitHub, contains editor-specific formatting, or reads more like generated dialogue than public project documentation.

## Do

- Read the current README and identify visible rendering problems first.
- Follow GitHub Flavored Markdown behavior instead of local editor preview behavior.
- Apply the smallest correct fix for spacing, line breaks, images, anchors, and links.
- Rewrite only the wording that is clearly broken, awkward, or overly AI-sounding.
- Keep the existing structure unless it clearly harms homepage readability.

## Do Not

- Rewrite the whole README unless the user explicitly asks for it.
- Add decorative formatting that weakens clarity.
- Keep broken badge anchors or outdated external links.
- Rely on inline CSS that GitHub may sanitize away.

## Common Fixes

- Use `<br/>` for forced line breaks inside HTML containers.
- Use a blank `>` line to split blockquote paragraphs.
- Use supported attributes such as `width` for image sizing.
- Point badge links to real headings.
- Normalize product names, repository names, and canonical repository URLs.

## Workflow

1. Read the README and note all GitHub-visible rendering issues.
2. Replace editor-specific syntax with GitHub-stable syntax.
3. Fix broken links, anchors, typos, and numbering gaps.
4. Rewrite any section that reads like assistant-generated task output.
5. Re-read the edited README as a public project landing page.

## References

- `references/summary.md`
- `references/interface.md`
- `references/examples.md`
- `references/checklist.md`
