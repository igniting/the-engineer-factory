#!/bin/sh
# Rebuild all Phase 3 CSVs. Usage: sh scripts/build_all.sh RAW_DIR
# RAW_DIR holds the downloaded files needed by build_reference.py (see its docstring);
# the other scripts use transcribed values only. Order matters: later scripts read earlier CSVs.
set -e
cd "$(dirname "$0")/.."
python3 -I scripts/build_reference.py "$1" .
python3 -I scripts/build_exports.py .
python3 -I scripts/build_workforce.py .
python3 -I scripts/build_firms.py .
python3 -I scripts/build_hiring.py .
python3 -I scripts/build_education.py .
python3 -I scripts/build_labour.py .
python3 -I scripts/build_migration.py .
python3 -I scripts/build_beyond.py .
