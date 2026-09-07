#!/usr/bin/env bash
# Drive the full catalog generation to a target file count.
#
# Each pass skips problem files that already exist, so the run is resumable:
# kill it, re-run it, and it picks up where it stopped. Passes repeat because
# individual agy calls fail (timeout, truncated response, missing sections) and
# those files are simply retried on the next pass.
#
# Discovery is followed by dedupe and a top-up because the topics overlap: the
# first sweep returned 1,100 candidates carrying 1,013 distinct slugs, which is
# not enough headroom over a 1,000 target once failures are subtracted.
#
#   tools/run_catalog.sh [target] [passes]
set -uo pipefail
cd "$(dirname "$0")/.."

TARGET=${1:-1000}
PASSES=${2:-6}
PER_TOPIC=${PER_TOPIC:-110}
TOPUP=${TOPUP:-25}
POOL=${POOL:-$((TARGET + 150))}     # candidates to hold, ahead of the file target
LOG=${LOG:-catalog-run.log}

count() { find topics -name '*.md' ! -name 'README.md' | wc -l | tr -d ' '; }
pool()  { python3 - <<'PY'
import glob, json
print(sum(len(json.load(open(f))) for f in glob.glob("topics/*/candidates.json")))
PY
}

echo "=== run start $(date -u +%FT%TZ) — $(count) files on disk, target ${TARGET} ===" | tee -a "$LOG"

# Stage 1: discovery, unless a pool already exists (so a restart does not re-ask).
if [ "$(pool)" -lt 100 ]; then
  python3 tools/generate_catalog_cli.py --stage discovery \
    --limit-candidates "$PER_TOPIC" 2>&1 | tee -a "$LOG"
fi
python3 tools/dedupe_candidates.py --target "$TARGET" 2>&1 | tail -5 | tee -a "$LOG"

# Stage 2: top up until the candidate pool clears the target with headroom.
for round in 1 2 3; do
  p=$(pool)
  [ "$p" -ge "$POOL" ] && break
  echo "=== topup round ${round} — pool ${p}/${POOL} ===" | tee -a "$LOG"
  python3 tools/generate_catalog_cli.py --stage topup \
    --limit-candidates "$TOPUP" 2>&1 | tail -20 | tee -a "$LOG"
  python3 tools/dedupe_candidates.py --target "$TARGET" 2>&1 | tail -3 | tee -a "$LOG"
done
echo "=== candidate pool: $(pool) ===" | tee -a "$LOG"

# Stage 3: generation, repeated until the target is met or the passes run out.
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
