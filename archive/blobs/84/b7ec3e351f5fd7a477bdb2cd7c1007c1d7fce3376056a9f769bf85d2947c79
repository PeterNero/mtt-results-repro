"""Audit Route-C Weyl-pair source-provenance reduction import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "routec_weylpair_source_provenance_reduction_import.candidate.json"
CERT = ROOT / "certificates" / "routec_weylpair_source_provenance_reduction_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "RouteC_WeylPair_Source_Provenance_Reduction_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_routec_weylpair_source_provenance_reduction.py"

STATUS = "ROUTEC_WEYLPAIR_SOURCE_PROVENANCE_IMPORTED_CARRIER_CLOSED_SECTOR_CHARGE_OPEN"
NEXT = "Q79_Selected_RouteC_WeylPair_SectorCharge_or_Chirality_Certificate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(all(data["checks"].values()), "not all checks passed")

    source = data["source_level_closure"]
    require(source["carrier_proved"] is True, "carrier not closed")
    require(source["shift_X_residual"] == 0.0, "shift residual mismatch")
    require(source["phase_Z_residual"] < 1e-11, "phase residual too large")
    require(source["projective_commutator_residual"] < 1e-12, "commutator residual too large")
    require(source["active_shift"] == [[1, 1]], "active shift mismatch")

    transfer = data["conditional_transfer"]
    require(transfer["conditional_exact"] is True, "transfer not exact")
    require(transfer["phase_residual"] == 0.0, "phase transfer residual mismatch")
    require(transfer["shift_residual"] == 0.0, "shift transfer residual mismatch")
    require(transfer["selected_transfer_map_emitted"] is False, "transfer map overemitted")
    require(transfer["selected_sector_routing_emitted"] is False, "sector routing overemitted")
    require(transfer["promote_to_A_selected_allowed"] is False, "A promotion allowed too early")

    routing = data["sector_routing_reduction"]
    require(routing["proved_by_locked_columns"] is True, "locked-column route not identified")
    require(routing["source_data_independently_selects_route"] is False, "sector route overproved")
    require(routing["proved_by_selected_source"] is False, "selected sector route overproved")
    require(routing["fully_proved"] is False, "sector routing fully proved too early")
    require(len(routing["exact_rows_relative_to_locked_columns"]) == 1, "exact route count mismatch")

    closes = data["what_closes_now"]
    for key in [
        "source_level_phase_Z_carrier_provenance",
        "source_level_shift_X_carrier_provenance",
        "active_shift_1_1_provenance",
        "conditional_source_to_C1_transfer_exact",
        "sector_routing_gap_identified",
        "target_fitting_excluded",
    ]:
        require(closes[key] is True, f"closed flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "selected_sector_charge_or_chirality_certificate",
        "source_derivation_of_u_e_phase_route",
        "source_derivation_of_d_nuD_shift_route",
        "selected_transfer_normalization",
        "promote_conditional_A_to_A_selected",
        "emit_theorem_derived_b_selected",
        "full_SM_or_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining flag missing: {key}")

    guard = data["guardrails"]
    for key in [
        "claims_conditional_transfer_is_selected_C1_map",
        "claims_conditional_A_is_A_selected",
        "claims_b_selected_emitted",
        "claims_full_SM_closure",
        "uses_locked_target_columns_as_source_selector",
        "uses_observed_flavor_data",
        "uses_benchmark_flavor_entries",
    ]:
        require(guard[key] is False, f"guardrail overclaimed: {key}")

    require("source-level qutrit Weyl carrier is now closed" in note, "note missing source closure")
    require("does not promote the conditional transfer" in note, "note missing promotion guard")
    require("No observed masses" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
