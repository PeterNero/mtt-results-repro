"""Audit conditional non-scalar dynamic-overlap/full-response value import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import.candidate.json"
CERT = ROOT / "certificates" / "nonscalardynamicoverlap_or_fullresponsecorrection_valueemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "NonScalarDynamicOverlap_or_FullResponseCorrection_ValueEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_nonscalardynamicoverlap_or_fullresponsecorrection_valueemission.py"

STATUS = "NONSCALAR_DYNAMIC_OVERLAP_CONDITIONAL_VALUES_IMPORTED_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_WeylPairDynamicOverlap_SourcePromotion_or_HonestGalerkinC1_ValueFill_v1"
SECTORS = ["u", "d", "e", "nuD"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    packet = data["conditional_non_scalar_value_packet"]
    require(packet["constructed"] is True, "packet not constructed")
    require(packet["selected_by_MTT"] is False, "conditional packet overselected")
    require(packet["observed_flavor_data_used"] is False, "observed flavor data used")

    responses = packet["sector_first_responses"]
    for sector in SECTORS:
        inv = responses[sector]["invariants"]
        require(inv["non_scalar"] is True, f"sector scalar: {sector}")
        require(inv["traceless_norm_sq"] > 0, f"no mass split: {sector}")
        require(inv["hermitian_residual_norm_sq"] == 0.0, f"non-Hermitian residual: {sector}")
    require(responses["u"]["source_direction"] == "phase_packet_I_plus_Z", "u route mismatch")
    require(responses["e"]["source_direction"] == "phase_packet_I_plus_Z", "e route mismatch")
    require(responses["d"]["source_direction"] == "shift_packet_I_plus_X", "d route mismatch")
    require(responses["nuD"]["source_direction"] == "shift_packet_I_plus_X", "nuD route mismatch")

    tests = packet["acceptance_tests"]
    require(tests["all_mass_split_positive"] is True, "mass split test failed")
    require(tests["ckm_commutator_positive"] is True, "CKM test failed")
    require(tests["pmns_commutator_positive"] is True, "PMNS test failed")
    require(tests["cp_odd_invariant_nonzero"] is True, "CP test failed")
    require(tests["ckm_commutator_norm_sq"] > 0, "CKM norm zero")
    require(tests["pmns_commutator_norm_sq"] > 0, "PMNS norm zero")
    require(abs(tests["cp_odd_trace_commutator_cubed_imag"]) > 0, "CP imaginary part zero")

    gate = data["promotion_gate"]
    require(gate["conditional_non_scalar_packet_available"] is True, "conditional packet unavailable")
    for key in [
        "promote_to_selected_dynamic_overlap_allowed",
        "promote_to_selected_full_response_allowed",
        "promote_to_A_selected_allowed",
        "promote_to_b_selected_allowed",
        "selected_source_to_C1_transfer_map_emitted",
        "selected_sector_routing_dynamic_map_emitted",
        "selected_Hessian_blocks_emitted",
        "selected_b_selected_emitted",
        "honest_Galerkin_C1_contractions_emitted",
    ]:
        require(gate[key] is False, f"promotion overclaimed: {key}")

    gap = data["selected_source_gap"]
    require(all(gap["source_level_closed"].values()), "source-level closed flags missing")
    require(all(gap["dynamic_level_open"].values()), "dynamic-level open flags missing")

    guardrails = data["guardrails"]
    require(guardrails["conditional_non_scalar_packet_available"] is True, "guardrail packet missing")
    require(guardrails["selected_by_MTT"] is False, "selected by MTT overclaimed")
    require(guardrails["selected_dynamic_overlap_tensor_claimed"] is False, "dynamic overlap claimed")
    require(guardrails["selected_full_response_claimed"] is False, "full response claimed")
    require(guardrails["A_selected_claimed"] is False, "A selected claimed")
    require(guardrails["b_selected_claimed"] is False, "b selected claimed")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")
    require(guardrails["full_SM_closure_claimed"] is False, "closure claimed")
    require("no observed flavor targets" in note, "note missing no-target guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
