"""
Creates most of the files necessary for clangen simulator.
"""

import argparse
import subprocess
from pathlib import Path
import shutil
import zipfile

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("clangen", help="Directory of clangen-lite")
    parser.add_argument("dist", help="Directory to place output files")
    args = parser.parse_args()

    clangen_repo = Path(args.clangen)
    output = Path(args.dist)

    subprocess.run(["hatch", "build", "-t", "wheel"], cwd=clangen_repo, check=True)

    with zipfile.ZipFile(output / "res.zip", "w") as z:
        for p in Path(clangen_repo).glob("resources/**/*.json"):
            z.write(p, p)

        for p in Path(clangen_repo).glob("sprites/**/*.json"):
            z.write(p, p)

    shutil.copytree(clangen_repo / "sprites", output / "sprites", dirs_exist_ok=True)
