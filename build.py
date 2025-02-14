"""
Creates most of the files necessary for clangen simulator.
Only runs properly in the clangen-lite directory.
"""

import subprocess
from pathlib import Path
import shutil
import zipfile

subprocess.run(["hatch", "build", "-t", "wheel"], check=True)

with zipfile.ZipFile("dist/res.zip", "w") as z:
    for p in Path(".").glob("resources/**/*.json"):
        z.write(p, p)

    for p in Path(".").glob("sprites/**/*.json"):
        z.write(p, p)

shutil.copytree("sprites", "dist/sprites", dirs_exist_ok=True)
