#!/usr/bin/env python3
import os
import shutil
import subprocess
from typing import Any, TypeAlias, TypedDict

import tomli_w

import common


def main():
	repo_root = common.get_repo_root()
	source_pack = repo_root / "pack"
	dest_pack = common.get_generated_dir() / "pack"
	packwiz = common.check_packwiz()

	common.fix_packwiz_pack(source_pack / "pack.toml")

	if dest_pack.exists():
		shutil.rmtree(dest_pack)
	shutil.copytree(source_pack, dest_pack)
	common.fix_packwiz_pack(dest_pack / "pack.toml")

	files: dict[str, Any] = {}
	for filename, filedata in files.items():
		dst_file = dest_pack / filename
		if not dst_file.exists():
			dst_file.parent.mkdir(parents=True, exist_ok=True)
			# We want all mods to be on both sides for singleplayer compat
			filedata["side"] = "both"
			with open(dst_file, "w", encoding="utf8") as f:
				f.write(tomli_w.dumps(filedata))

	os.chdir(dest_pack)
	subprocess.run([packwiz, "refresh", "--build"])

if __name__ == "__main__":
	main()

# For type hints
class SubmissionLockfileEntry(TypedDict):
	url: str 
	files: dict[str, Any]
SubmissionLockfileFormat: TypeAlias = dict[str, SubmissionLockfileEntry]
