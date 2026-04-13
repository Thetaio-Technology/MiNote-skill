# README Writing Skill Summary

## Purpose

This document summarizes the logic used while refining the repository `README.md` for GitHub homepage rendering.

The goal was not to rewrite the entire README, but to make the existing content render correctly on GitHub, read more like a public project page, and avoid artifacts caused by writing in Typora first.

## Core Principle

When a README is intended for GitHub, GitHub's actual Markdown renderer is the source of truth.

Typora can be used as a drafting tool, but rendering decisions should be validated against GitHub Flavored Markdown behavior rather than local editor preview behavior.

## Working Logic

### 1. Fix rendering before polishing wording

The first pass focused on visible rendering problems on the GitHub page:

- text that should have been bold on separate lines but rendered inline
- blockquote content that should have been split into two lines but rendered as one paragraph
- image sizing that worked in Typora but not on GitHub

This ordering matters because homepage readability depends more on layout correctness than on wording polish.

### 2. Prefer GitHub-stable syntax over editor-specific syntax

When Typora behavior differed from GitHub behavior, the GitHub-compatible version was used.

Practical rules used in this README:

- use `<br/>` for explicit line breaks inside HTML containers
- use an empty quoted line (`>`) to separate blockquote paragraphs
- use supported HTML attributes such as `width` for image sizing
- avoid relying on inline CSS such as `style="zoom:30%;"`

## Specific Decisions

### Line breaks in centered sections

The README used `<div align="center">` blocks. Inside these blocks, plain line breaks from the source file are not reliable enough for GitHub rendering.

Decision:

- add `<br/>` between lines that must stay visually separated

Applied to:

- the two-line bold slogan near the top of the page
- the three centered question lines in the introduction

### Line breaks in blockquotes

Two quoted lines describing the division of responsibility between `minote-driver` and `minote-skill` were visually intended as two separate lines.

Decision:

- insert a blank blockquote line (`>`) between them

Reason:

- GitHub treats adjacent blockquote lines as part of the same paragraph unless a paragraph break is made explicit

### Image sizing

The original image used Typora-oriented scaling with:

```html
<img ... style="zoom:30%;" />
```

Decision:

- replace it with:

```html
<img ... width="30%" />
```

Reason:

- GitHub sanitization and renderer behavior do not reliably preserve inline CSS like `zoom`
- width attributes are more stable for README rendering

### Anchor links in badges

Some top badges linked to heading anchors that did not exist in the current README.

Decision:

- retarget badge links to real existing sections

Reason:

- homepage badges should work as navigation, not as decorative broken links

### Minimal wording cleanup

After rendering problems were fixed, only obvious wording issues were corrected.

This included:

- typo-level fixes such as `代办` -> `待办`, `模版` -> `模板`, `组建` -> `组件`
- normalization of product naming such as `Claude Code` and `OpenCode`
- completing the numbered install sequence by adding step `1. 克隆仓库`

The standard was to avoid broad rewriting and only fix what was clearly broken, incomplete, or awkward.

### Formalizing AI-sounding text

One section originally described the repository through a list of short functional bullets. While correct, it read more like generated assistant output than like a project README.

Decision:

- merge the bullet list into one formal project-description sentence

Reason:

- public README copy should read like maintainers intentionally wrote it for users
- repository positioning is often better expressed as a concise paragraph than as task-style bullets

### External link correction

The `minote-driver` repository link was updated to the actual repository URL:

`https://github.com/Thetaio-Technology/MiNote-driver`

Reason:

- README external references should point to canonical public locations

## Editorial Style Rules Inferred From This Session

The README should follow these style rules going forward:

- prioritize GitHub rendering over local editor appearance
- use explicit formatting when visual structure matters
- prefer small, corrective edits over large rewrites
- keep homepage copy direct and product-facing
- avoid wording that sounds like an assistant explaining its own reasoning
- use working links and real anchors only
- treat the README as a public landing page, not an internal note

## Recommended Future Review Checklist

When editing this README again, check the following in order:

1. Do all forced line breaks render correctly on GitHub?
2. Do blockquotes, lists, and centered sections preserve the intended spacing?
3. Do images display at the intended size?
4. Do badge anchors point to real sections?
5. Do external repository links point to canonical URLs?
6. Does the wording read like a public project page rather than an AI conversation?

## Summary

The logic used in this editing session was:

1. identify GitHub rendering failures
2. replace Typora-dependent syntax with GitHub-stable syntax
3. fix only the wording issues that were clearly worth correcting
4. rewrite the most AI-sounding section into normal project documentation language
5. keep the overall structure intact while improving public readability
