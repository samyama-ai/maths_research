#!/usr/bin/env bash
# Drive the full catalog generation to a target file count.
#
# Each pass skips problem files that already exist, so the run is resumable:
# kill it, re-run it, and it picks up where it stopped. Passes repeat because
# individual agy calls fail (timeout, truncated response, missing sections) and
# those files are simply retried on the next pass.
#
#   tools/run_catalog.sh [target] [passes]
set -uo pipefail
cd "$(dirname "$0")/.."

TARGET=${1:-1000}
PASSES=${2:-6}
PER_TOPIC=${PER_TOPIC:-110}
LOG=${LOG:-catalog-run.log}

count() { find topics -name '*.md' ! -name 'README.md' | wc -l | tr -d ' '; }

echo "=== run start $(date -u +%FT%TZ) — $(count) files on disk, target ${TARGET} ===" | tee -a "$LOG"

# Stage 1: discovery. Cheap, one call per topic, and generation needs its output.
python3 tools/generate_catalog_cli.py --stage discovery \
  --limit-candidates "$PER_TOPIC" 2>&1 | tee -a "$LOG"

# Stage 2: generation, repeated until the target is met or the passes run out.
for pass in $(seq 1 "$PASSES"); do
  n=$(count)
  if [ "$n" -ge "$TARGET" ]; then
    echo "=== target met: ${n} files ===" | tee -a "$LOG"
    break
  fi
  echo "=== pass ${pass}/${PASSES} — ${n} files ===" | tee -a "$LOG"
  python3 tools/generate_catalog_cli.py --stage generation \
    --limit-generate "$PER_TOPIC" 2>&1 | tee -a "$LOG"
done

./gen_index.sh | tee -a "$LOG"
python3 tools/audit.py 2>&1 | tail -30 | tee -a "$LOG"
echo "=== run end $(date -u +%FT%TZ) — $(count) files ===" | tee -a "$LOG"
