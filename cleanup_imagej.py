#!/usr/bin/env python3
#
# This file is part of the GPM phenotyping scripts.
#
# Copyright (c) 2023 Jason Toney
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""This script removes the files created by AnalyzeSporesAndGermlings.ijm."""

import os


def cleanup_imagej():
    """Clean up any results files that exist."""
    print("Cleaning up ImageJ files...")
    os.chdir(os.path.dirname(__file__))
    imagej_path = "ImageJ/GPM"
    removed = 0
    for file in os.listdir(f"{imagej_path}/images"):
        if file.endswith(".tif"):
            os.remove(f"{imagej_path}/images/{file}")
            removed += 1
    for file in os.listdir(f"{imagej_path}/results"):
        if file.endswith(".csv"):
            os.remove(f"{imagej_path}/results/{file}")
            removed += 1
    print(f"Cleanup complete. Deleted {removed} files.")
    input("Press ENTER to exit.\n")


if __name__ == "__main__":
    cleanup_imagej()
