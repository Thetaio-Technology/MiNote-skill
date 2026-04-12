# Install

## Overview

`minote-skill` now carries its own local runtime under `script/`.

If you want this skill to actually execute Xiaomi Cloud Notes todo operations, you need to configure the local runtime correctly through a repository-level `.env` file.

In short:

1. Clone `minote-skill`
2. Create a `.env` file from `.env.example`
3. Fill in Chrome, ChromeDriver, and runtime paths
4. Install Python dependencies
5. Initialize the local login session
6. Run verification scripts

## Environment Requirements

Current tested assumptions:

- Windows
- Python 3.9+
- Google Chrome installed
- A `chromedriver.exe` version matching the installed Chrome version
- Network access to `https://i.mi.com/note/#/`
- A Xiaomi account that can log in manually at least once

## Repository Contents

The `minote-skill` repository contains:

- skill definition
- integration contract
- usage examples
- installation guide
- local runtime under `script/`

## Installation Steps

### 1. Clone `minote-skill`

Clone the skill repository to your local machine:

```bash
git clone <MINOTE_SKILL_REPO_URL>
cd minote-skill
```

### 2. Create `.env`

Copy `.env.example` to `.env` and fill in the actual local paths.

Example:

```bash
copy .env.example .env
```

Required fields:

- `MINOTE_RUNTIME_ROOT`
- `MINOTE_CHROME_EXE`
- `MINOTE_CHROMEDRIVER_EXE`
- `MINOTE_CHROME_USER_DATA_DIR`
- `MINOTE_TARGET_URL`
- `MINOTE_REMOTE_DEBUGGING_PORT`

Typical values:

```env
MINOTE_RUNTIME_ROOT=E:\Code\TEMScript\Minote-skill\script
MINOTE_CHROME_EXE=C:\Program Files\Google\Chrome\Application\chrome.exe
MINOTE_CHROMEDRIVER_EXE=E:\Code\TEMScript\Minote-skill\script\bin\chromedriver.exe
MINOTE_CHROME_USER_DATA_DIR=E:\Code\TEMScript\Minote-skill\script\chrome_profile
MINOTE_TARGET_URL=https://i.mi.com/note/#/
MINOTE_REMOTE_DEBUGGING_PORT=9222
```

### 3. Install Python Dependencies

Create and activate a virtual environment if you want an isolated setup.

Install Selenium:

```bash
pip install selenium
```

If later the driver repository adds a `requirements.txt` or `pyproject.toml`, prefer using that instead.

### 4. Prepare ChromeDriver

Download a `chromedriver.exe` version that matches your installed Chrome version.

Place it at:

```text
bin/chromedriver.exe
```

Notes:

- `chromedriver.exe` is required for runtime execution
- It is intentionally not committed to the repository
- If the version does not match Chrome, browser startup may fail

### 5. Verify Local Runtime Assumptions

Before first execution, confirm:

- Chrome is installed in the expected location
- `bin/chromedriver.exe` exists
- Python can import `selenium`

Run the built-in runtime checker:

```bash
python script/cli/check_runtime.py
```

This checks whether:

- `.env` exists
- configured paths can be resolved
- Chrome exists
- ChromeDriver exists
- the configured profile parent directory exists

### 6. Initialize the Login Session

From the `minote-skill` repository root, run:

```bash
python script/cli/open_mi_cloud.py
```

This opens Chrome with the project-local browser profile.

On first use:

1. Log in to your Xiaomi account manually
2. Confirm the Xiaomi Cloud Notes page loads successfully
3. Close the browser after the login state is saved

The runtime reuses this local session later.

### 7. Verify Runtime Execution

Still inside `minote-skill`, run:

```bash
python script/verify/verify_todo_crud.py
python script/verify/verify_commands.py
```

If both pass, the runtime is ready for skill-level integration.

## How To Use With `minote-skill`

Once the local runtime is configured, use the skill contract documented in this repository.

Typical execution entrypoint:

```bash
python script/cli/run_skill.py minote-todo create --title "明天下午买咖啡豆"
```

Important:

- This command is executed from the `minote-skill` repository root
- Runtime configuration is resolved through `.env`

## Common Setup Problems

### Chrome opens but automation fails

Likely causes:

- Chrome version and ChromeDriver version do not match
- The page DOM changed
- The local login state is missing or expired

### Login works once but later commands fail

Likely causes:

- Session expired
- Xiaomi requested re-verification
- Local browser profile was changed or deleted

### Skill repo is cloned but nothing can execute

Likely causes:

- `.env` is missing
- `.env` paths are incorrect
- `script/bin/chromedriver.exe` is missing
- `selenium` is not installed

## Recommended Directory Relationship

Recommended local layout:

```text
E:\Code\TEMScript\Minote-skill\
├── .env
├── install.md
├── skills\
└── script\
    ├── cli\
    ├── src\
    ├── verify\
    ├── bin\
    └── chrome_profile\
```

Future automation can create missing runtime dependencies directly under `script/`.
