from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "app"
PACKAGE = ROOT / "app.zip"


with ZipFile(PACKAGE, "w", compression=ZIP_DEFLATED) as archive:
    for path in sorted(APP_DIR.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
            archive.write(path, path.relative_to(APP_DIR).as_posix())
