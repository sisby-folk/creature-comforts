#!/usr/bin/env python3
import os
import shutil
import subprocess

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

	os.chdir(dest_pack)
	subprocess.run([packwiz, "refresh", "--build"])

if __name__ == "__main__":
	main()
