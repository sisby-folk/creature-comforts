#!/usr/bin/env python3
import os
import subprocess

import common


def main():
	repo_root = common.get_repo_root()
	pack_dir = repo_root / "pack"
	packwiz = common.check_packwiz()
	common.fix_packwiz_pack(pack_dir / "pack.toml")
	os.chdir(pack_dir)
	subprocess.run([packwiz, "refresh", "--build"])

if __name__ == "__main__":
	main()
