from pathlib import Path
import json
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = PROJECT_ROOT / "script" / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from minote.browser import open_mi_cloud
from check_runtime import collect_runtime_status


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    payload = collect_runtime_status()
    if not payload["ok"]:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    open_mi_cloud()


if __name__ == "__main__":
    main()
