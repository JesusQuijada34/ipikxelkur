import ast
from pathlib import Path

for name in ("ipikxelkur.py", "updater.py"):
    ast.parse(Path(name).read_text(encoding="utf-8"), filename=name)
source = Path("ipikxelkur.py").read_text(encoding="utf-8")
updater = Path("updater.py").read_text(encoding="utf-8")
details = Path("details.xml").read_text(encoding="utf-8")
assert "def main(args):" in source
assert "return 0" in source
assert "<platform>AlphaCube</platform>" in details
assert "safe_extract_zip" in updater
assert "MAX_UPDATE_BYTES" in updater
assert "shell=True" not in updater
assert "[\"pkill\", \"-9\", \"-x\"" in updater
print("IPIKXELKUR_STATIC_SECURITY_CHECK_OK")
