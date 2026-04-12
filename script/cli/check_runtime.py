from pathlib import Path
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = PROJECT_ROOT / "script" / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from minote.config import (
    CHROMEDRIVER_EXE,
    CHROME_EXE,
    CHROME_USER_DATA_DIR,
    PROJECT_ROOT as CONFIG_PROJECT_ROOT,
    REMOTE_DEBUGGING_PORT,
    RUNTIME_ROOT,
    TARGET_URL,
)


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    env_path = CONFIG_PROJECT_ROOT / ".env"

    checks = {
        "env_file_exists": env_path.exists(),
        "runtime_root": str(RUNTIME_ROOT),
        "runtime_root_exists": RUNTIME_ROOT.exists(),
        "chrome_exe": str(CHROME_EXE),
        "chrome_exe_exists": CHROME_EXE.exists(),
        "chromedriver_exe": str(CHROMEDRIVER_EXE),
        "chromedriver_exe_exists": CHROMEDRIVER_EXE.exists(),
        "chrome_user_data_dir": str(CHROME_USER_DATA_DIR),
        "chrome_user_data_dir_parent_exists": CHROME_USER_DATA_DIR.parent.exists(),
        "remote_debugging_port": REMOTE_DEBUGGING_PORT,
        "target_url": TARGET_URL,
    }

    errors = []
    if not checks["env_file_exists"]:
        errors.append("Missing .env file at repository root")
    if not checks["runtime_root_exists"]:
        errors.append("Configured MINOTE_RUNTIME_ROOT does not exist")
    if not checks["chrome_exe_exists"]:
        errors.append("Configured MINOTE_CHROME_EXE does not exist")
    if not checks["chromedriver_exe_exists"]:
        errors.append("Configured MINOTE_CHROMEDRIVER_EXE does not exist")
    if not checks["chrome_user_data_dir_parent_exists"]:
        errors.append("Parent directory of MINOTE_CHROME_USER_DATA_DIR does not exist")

    payload = {
        "ok": not errors,
        "checks": checks,
        "errors": errors,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
