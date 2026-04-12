from pathlib import Path
import os


def _load_dotenv() -> None:
    env_path = Path(__file__).resolve().parents[3] / ".env"
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if " #" in line:
            line = line.split(" #", 1)[0].rstrip()
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def _resolve_path(value: str, default: Path) -> Path:
    if not value:
        return default
    candidate = Path(value)
    if candidate.is_absolute():
        return candidate
    return PROJECT_ROOT / candidate


RUNTIME_ROOT = _resolve_path(os.environ.get("MINOTE_RUNTIME_ROOT", "script"), PROJECT_ROOT / "script")
CHROMEDRIVER_EXE = _resolve_path(
    os.environ.get("MINOTE_CHROMEDRIVER_EXE", "script/bin/chromedriver.exe"),
    RUNTIME_ROOT / "bin" / "chromedriver.exe",
)
CHROME_EXE = Path(
    os.environ.get("MINOTE_CHROME_EXE", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
)
CHROME_USER_DATA_DIR = _resolve_path(
    os.environ.get("MINOTE_CHROME_USER_DATA_DIR", "script/chrome_profile"),
    RUNTIME_ROOT / "chrome_profile",
)
TARGET_URL = "https://i.mi.com/note/#/"
REMOTE_DEBUGGING_PORT = int(os.environ.get("MINOTE_REMOTE_DEBUGGING_PORT", "9222"))
