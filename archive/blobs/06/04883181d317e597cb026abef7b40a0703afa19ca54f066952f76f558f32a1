"""Build CONST-EW-02 B25 internal lambda12 / physical frontier import."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
QA = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b25_internal_lambda12_physical_frontier"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LAMBDA = BASE / "internal_lambda12_import.packet.json"
PHYSICAL = BASE / "physical_anchor_rg_frontier.packet.json"
C1 = BASE / "primitive_c1_atom_cutset_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b25_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B25_InternalLambda12PhysicalFrontier_v1.md"

STATUS = "MTT_CONST_EW_02_B25_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_FRONTIER_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b24_path = DATA / "const_ew_02_weak_mixing_b24_udyn_source_derivation_import.candidate.json"
    b24_boundary_path = DATA / "const_ew_02_weak_mixing_b24_udyn_source_derivation_import" / "weak_mixing_b24_boundary.packet.json"

    lambda_candidate_path = QA / "candidate_data" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json"
    lambda_cert_path = QA / "certificates" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor_certificate.json"
    physical_candidate_path = QA / "candidate_data" / "selected_electroweak_physicalanchor_rg_and_matchingscale.candidate.json"
    physical_cert_path = QA / "certificates" / "selected_electroweak_physicalanchor_rg_and_matchingscale_certificate.json"
    c1_interface_cert_path = QA / "certificates" / "selected_u1y_routec_primitive_c1_atom_emission_interface_certificate.json"
    c1_nogo_cert_path = QA / "certificates" / "selected_u1y_routec_primitive_c1_atom_payload_fill_or_nogo_certificate.json"
    c1_missing_path = QA / "candidate_data" / "selected_u1y_routec_primitive_c1_atom_payload_missing_leaves.json"

    b24 = load(b24_path)
    b24_boundary = load(b24_boundary_path)
    lambda_candidate = load(lambda_candidate_path)
    lambda_cert = load(lambda_cert_path)
    physical_candidate = load(physical_candidate_path)
    physical_cert = load(physical_cert_path)
    c1_interface_cert = load(c1_interface_cert_path)
    c1_nogo_cert = load(c1_nogo_cert_path)
    c1_missing = load(c1_missing_path)

    lambda_packet = {
        "schema": "MTTConstEW02B25InternalLambda12Import.v1",
        "status": "INTERNAL_DIMENSIONLESS_LAMBDA12_IMPORTED_CLOSED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-LAMBDA12-SPECTRAL-TABLE-OR-THRESHOLD-POLICY",
        "inputs": {
            "B24_candidate": rel(b24_path),
            "B24_boundary": rel(b24_boundary_path),
            "qa_lambda12_candidate": rel(lambda_candidate_path),
            "qa_lambda12_certificate": rel(lambda_cert_path),
        },
        "imported_values": lambda_candidate["selected_internal_threshold_vector"],
        "closure_scope": lambda_cert["closure_scope"],
        "what_closes": {
            "internal_lambda_12": lambda_cert["lambda_12_internal_closed"],
            "internal_lambda_12_value": lambda_cert["lambda_12_internal_value"],
            "internal_Delta_G12_value": lambda_cert["Delta_G12_internal_value"],
            "same_scheme_SU2_row_or_cancellation": lambda_cert["same_scheme_SU2_row_or_cancellation_closed"],
        },
        "guardrails": lambda_candidate["guardrails"],
        "not_closed": lambda_candidate["physical_anchor_status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    physical_packet = {
        "schema": "MTTConstEW02B25PhysicalAnchorRGFrontier.v1",
        "status": "PHYSICAL_GAUGE_ANCHOR_RG_MATCHING_FRONTIER_IMPORTED_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-U-PHYS-SOURCE-DERIVATION",
        "inputs": {
            "qa_physical_frontier_candidate": rel(physical_candidate_path),
            "qa_physical_frontier_certificate": rel(physical_cert_path),
        },
        "closed_now": physical_candidate["closed_now"],
        "conditional_interface": physical_candidate["conditional_interface"],
        "still_open": physical_candidate["still_open"],
        "route_tests": physical_candidate["route_tests"],
        "decision": physical_candidate["decision"],
        "u_phys_status": {
            "u_phys_source_derived": False,
            "physical_gauge_action_anchor_closed": physical_cert["physical_gauge_action_anchor_closed"],
            "matching_scale_closed": physical_cert["matching_scale_closed"],
            "RG_scheme_closed": physical_cert["RG_scheme_closed"],
            "single_calibration_allowed_under_B23": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    c1_packet = {
        "schema": "MTTConstEW02B25PrimitiveC1AtomCutsetImport.v1",
        "status": "PRIMITIVE_C1_ATOM_INTERFACE_BUILT_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-PRIMITIVE-C1-ATOM-TABLE",
        "inputs": {
            "primitive_c1_interface_certificate": rel(c1_interface_cert_path),
            "primitive_c1_fill_nogo_certificate": rel(c1_nogo_cert_path),
            "primitive_c1_missing_leaves": rel(c1_missing_path),
        },
        "interface": {
            "assembly_theorem_proved": c1_interface_cert["assembly_theorem_proved"],
            "primitive_C1_atoms_emitted": c1_interface_cert["primitive_C1_atoms_emitted"],
            "missing_atom_count": c1_interface_cert["missing_atom_count"],
            "A_selected_computable": c1_interface_cert["A_selected_computable"],
            "b_selected_computable": c1_interface_cert["b_selected_computable"],
        },
        "fill_attempt": {
            "fill_attempt_executed": c1_nogo_cert["fill_attempt_executed"],
            "current_corpus_supplies_selected_atom_payload": c1_nogo_cert["current_corpus_supplies_selected_atom_payload"],
            "canonical_zero_branch_tested": c1_nogo_cert["canonical_zero_branch_tested"],
            "canonical_zero_branch_selected": c1_nogo_cert["canonical_zero_branch_selected"],
            "missing_leaf_count": c1_nogo_cert["missing_leaf_count"],
        },
        "minimal_closing_options": c1_missing["minimal_closing_options"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B25Boundary.v1",
        "status": "INTERNAL_LAMBDA12_AND_UDYN_CLOSED_PHYSICAL_MATCHING_AND_C1_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-BOUNDARY",
        "closed_now": {
            "B24_u_dyn_source_derived_preserved": b24["u_dyn_source_derived"],
            "internal_lambda_12_closed": True,
            "internal_lambda_12_value": lambda_cert["lambda_12_internal_value"],
            "internal_Delta_G12_value": lambda_cert["Delta_G12_internal_value"],
            "same_scheme_internal_SU2_row_closed": True,
            "physical_frontier_reduced_to_anchor_mu_RG": True,
            "primitive_C1_atom_interface_built": c1_interface_cert["assembly_theorem_proved"],
        },
        "still_open": {
            "physical_weak_angle_closure": True,
            "physical_gauge_action_anchor_or_u_phys": True,
            "matching_scale_mu_match": True,
            "RG_and_threshold_scheme": True,
            "measured_electroweak_closure": True,
            "all_24_primitive_C1_atoms": True,
            "A_selected": True,
            "b_selected": True,
            "Yukawa_magnitudes": True,
            "full_SM_closure": True,
        },
        "allowed_claim": "dimensionless internal weak-split threshold is closed in the selected internal scheme",
        "forbidden_claim": "measured/physical weak angle, alpha, or full electroweak closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B25NextWork.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_GAUGE_ANCHOR_OR_C1_ATOMS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B26-PHYSICAL-GAUGE-ANCHOR-OR-C1-ATOMS",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B26-GAUGEKINETIC-NORMALIZATION-RG-SCHEME",
            "task": "Emit same-branch physical gauge/action normalization K_phys or u_phys, selected mu_match, and fixed RG/threshold scheme.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B26-PRIMITIVE-C1-SOURCEVALUE-THEOREM",
            "task": "Emit selected noninvariant primitive C1 tensor and basis transport, prove selected zero tensor, or derive the 24 atom matrices from typed monad/Cech/HYM connection data.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB25InternalLambda12PhysicalFrontier",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B25-PHYSICAL-EW-GATES-OR-U-PHYS",
        "output_packets": {
            "internal_lambda12_import": rel(LAMBDA),
            "physical_anchor_rg_frontier": rel(PHYSICAL),
            "primitive_c1_atom_cutset_import": rel(C1),
            "weak_mixing_b25_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B25InternalLambda12PhysicalFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected internal electroweak weak-split threshold is imported "
                "as closed: lambda_12=2.6179362173268497 and Delta_G12=0.08450302790361214. "
                "Together with B24 u_dyn=1, this closes the dimensionless internal prefix. "
                "Physical weak-angle closure remains open until a physical gauge/action "
                "anchor, matching scale, and RG/threshold scheme are source-selected. "
                "The primitive C1 atom interface is built, but all 24 atom values remain open."
            ),
        },
        "internal_lambda_12_closed": True,
        "internal_lambda_12_value": lambda_cert["lambda_12_internal_value"],
        "u_dyn_source_derived": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B25_InternalLambda12PhysicalFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "internal_lambda_12_closed": True,
        "internal_lambda_12_value": lambda_cert["lambda_12_internal_value"],
        "internal_Delta_G12_value": lambda_cert["Delta_G12_internal_value"],
        "u_dyn_source_derived": True,
        "physical_gauge_action_anchor_closed": False,
        "matching_scale_closed": False,
        "RG_scheme_closed": False,
        "primitive_C1_atoms_emitted": False,
        "missing_atom_count": c1_nogo_cert["missing_atom_count"],
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B25 Internal Lambda12 Physical Frontier v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B25-PHYSICAL-EW-GATES-OR-U-PHYS`

## Closed

```text
u_dyn = 1
lambda_12_internal = {lambda_cert["lambda_12_internal_value"]}
Delta_G12_internal = {lambda_cert["Delta_G12_internal_value"]}
```

This closes the dimensionless internal weak-split threshold prefix.

## Still Open

```text
physical gauge/action anchor or u_phys
mu_match
RG and threshold scheme
measured electroweak closure
24 primitive C1 atoms
A_selected and b_selected
```

## Next

`CONST-EW-02 / WEAK-MIXING / B26-PHYSICAL-GAUGE-ANCHOR-OR-C1-ATOMS`
"""

    for path, payload in [
        (LAMBDA, lambda_packet),
        (PHYSICAL, physical_packet),
        (C1, c1_packet),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
