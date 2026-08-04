#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
DATA="$ROOT/candidate_data/q79_Ronly_triple_fiber_min_degree"
OUT=${1:-"$ROOT/reproduced_q79_Ronly_degree9"}
PYTHON=${PYTHON:-python3}
EXPECTED_DAG_SHA256=d8146f94952d0e4013db26d155cd390541264920d413b47d0031eb9db739605d

: "${MSOLVE_BIN:?Set MSOLVE_BIN to the patched msolve 0.10.1 executable}"
mkdir -p "$OUT"

export MSOLVE_F4_PROVENANCE_DUMP="$OUT/provenance.tsv"
export MSOLVE_F4_OPERATION_DAG="$OUT/operation_dag.tsv"
"$MSOLVE_BIN" \
  -f "$DATA/selected_full14.msolve.in" \
  -o "$OUT/unit.msolve.out" \
  -t 1 -l 2 -g 2

ACTUAL_DAG_SHA256=$(sha256sum "$OUT/operation_dag.tsv" | cut -d ' ' -f 1)
if [[ "$ACTUAL_DAG_SHA256" != "$EXPECTED_DAG_SHA256" ]]; then
  echo "DAG hash mismatch: $ACTUAL_DAG_SHA256" >&2
  exit 1
fi
grep -q '^\[1\]:$' "$OUT/unit.msolve.out"

"$PYTHON" "$ROOT/scripts/expand_q79_Ronly_f4_operation_dag.py" \
  --dag "$OUT/operation_dag.tsv" \
  --input "$DATA/selected_full14.msolve.in" \
  --certificate "$OUT/explicit_degree9_multipliers.json" \
  --packet "$OUT/explicit_degree9_generation.packet.json" \
  --instrumentation-patch "$DATA/msolve_f4_operation_dag.patch"

"$PYTHON" "$ROOT/scripts/certify_q79_Ronly_explicit_minimum_degree9.py" \
  --multipliers "$OUT/explicit_degree9_multipliers.json" \
  --generation-packet "$OUT/explicit_degree9_generation.packet.json" \
  --output "$OUT/consolidated_certificate.json"

echo "Q79_RONLY_EXPLICIT_DEGREE9_FULL_REPRODUCTION_PASS"
echo "$OUT/consolidated_certificate.json"
