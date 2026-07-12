"""Build CONST-EM-01 K_phys source hunt.

After internal weak-split closure, physical alpha/electroweak matching needs a
target-independent physical gauge/action anchor.  This imports the
GR/protospinor dimensional-anchor results and freezes the current boundary.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
PROTO = TEXPAPERS / "mtt-protospinor-gr-response-proof"
QA_SU3 = TEXPAPERS / "mtt-qa-su3-packet-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_em_01_alpha1_kphys_source_hunt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ANCHORS = BASE / "physical_anchor_imports.packet.json"
REDUCTION = BASE / "kphys_reduction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EM_01_Alpha1_KPhysSourceHunt_v1.md"

STATUS = "MTT_CONST_EM_01_KPHYS_SOURCE_HUNT_REDUCED_TO_ALPHA_PHYS_ANCHOR_OPEN"


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

    mtheory_candidate_path = PROTO / "certificates" / "m_theory_modal_gap_dimensional_anchor_candidate_certificate.json"
    mtheory_attempt_path = PROTO / "certificates" / "m_theory_dimensional_anchor_packet_attempt_certificate.json"
    alpha_phys_path = PROTO / "certificates" / "selected_physical_alpha_or_action_unit_theorem_certificate.json"
    anchor_search_path = PROTO / "certificates" / "target_independent_dimensional_anchor_search_certificate.json"
    qa_physical_path = QA_SU3 / "candidate_data" / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json"
    internal_path = DATA / "const_em_01_alpha1_internal_weaksplit_import.candidate.json"

    mtheory_candidate = load(mtheory_candidate_path)
    mtheory_attempt = load(mtheory_attempt_path)
    alpha_phys = load(alpha_phys_path)
    anchor_search = load(anchor_search_path)
    qa_physical = load(qa_physical_path)
    internal = load(internal_path)

    import_checks = {
        "internal_weaksplit_available": internal["internal_closure_claimed"] is True,
        "m_theory_slot_identified": mtheory_candidate["closed_tests"]["m_theory_gauge_slot_identified"] is True,
        "m_theory_physical_anchor_open": mtheory_candidate["verdict"]["physical_dimensionful_anchor_available"] is False,
        "m_theory_attempt_structural_value_open": mtheory_attempt["closure_tests"]["dimensionful_value_present"] is False,
        "alpha_phys_reduced_to_single_anchor": alpha_phys["theorem_result"]["alpha_phys_status"] == "SOLE_REMAINING_EXTERNAL_DIMENSIONFUL_ANCHOR",
        "alpha_phys_numeric_not_selected": alpha_phys["theorem_result"]["physical_numeric_alpha_selected"] is False,
        "target_independent_anchor_search_exhausted": anchor_search["status"] == "DIMENSIONAL_ANCHOR_SEARCH_EXHAUSTED_PACKET_GATE_READY",
        "best_route_mtheory_modal_gap": anchor_search["verdict"]["best_route"] == "m_theory_modal_gap_planck_anchor",
        "qa_physical_anchor_open": qa_physical["theorem"]["physical_anchor_gate"]["status"] == "OPEN",
        "no_target_backsolve": alpha_phys["guardrails"]["backsolves_alpha_phys_from_target"] is False,
    }
    kphys_open = all(import_checks.values())

    anchors = {
        "schema": "MTTConstEM01KPhysAnchorImports.v1",
        "status": "KPHYS_IMPORTS_REDUCED_TO_ALPHA_PHYS_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
        "imports": {
            "internal_weaksplit": rel(internal_path),
            "m_theory_modal_gap_anchor_candidate": rel(mtheory_candidate_path),
            "m_theory_dimensional_anchor_attempt": rel(mtheory_attempt_path),
            "selected_physical_alpha_or_action_unit": rel(alpha_phys_path),
            "target_independent_dimensional_anchor_search": rel(anchor_search_path),
            "qa_physical_gauge_anchor": rel(qa_physical_path),
        },
        "import_checks": import_checks,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    reduction = {
        "schema": "MTTConstEM01KPhysReduction.v1",
        "status": "KPHYS_EQUALS_ALPHA_PHYS_OR_EQUIVALENT_ACTION_UNIT_OPEN",
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
        "closed_internal_values": {
            "p_a_internal": 29.201650332199108,
            "p_Y_internal": 1.4217420994950278,
            "lambda_12_internal": 2.6179362173268497,
            "Delta_G12_internal": 0.08450302790361214,
        },
        "physical_anchor_reduction": {
            "best_structural_route": "m_theory_modal_gap_planck_anchor",
            "single_remaining_anchor": "alpha_phys or equivalent physical inverse-length/action unit",
            "Omega0_formula": alpha_phys["final_reduction"]["Omega0"],
            "Omega0_over_sqrt_alpha_phys": alpha_phys["final_reduction"]["Omega0_over_sqrt_alpha_phys"],
            "allowed_without_anchor": alpha_phys["theorem_result"]["allowed_outputs_without_new_anchor"],
            "forbidden_without_anchor": alpha_phys["theorem_result"]["forbidden_outputs_without_new_anchor"],
        },
        "open": {
            "K_phys": True,
            "alpha_phys": True,
            "Omega0_numeric": True,
            "ell_p_or_kappa11": True,
            "matching_scale": True,
            "RG_threshold_scheme": True,
            "alpha_zero_or_MZ": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTNextLabeledWorkorderAfterKPhysSourceHunt.v1",
        "status": "NEXT_WORKORDER_DIMENSIONAL_ANCHOR_PACKET_OR_RG_SCHEME",
        "primary": {
            "label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
            "task": "Attempt to fill the selected dimensional anchor packet: selected physical inverse-length/action unit, map to alpha_phys, and no-target proof.",
        },
        "secondary": {
            "label": "CONST-EM-01 / ALPHA1-RG-SCHEME / A6-MATCHING-RUNNING",
            "task": "Prepare the RG/matching scheme scaffold so a future K_phys can be propagated to alpha(M_Z) and alpha(0).",
        },
    }

    candidate = {
        "candidate": "MTTConstEM01Alpha1KPhysSourceHunt",
        "status": STATUS,
        "active_label": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS",
        "output_packets": {
            "physical_anchor_imports": rel(ANCHORS),
            "kphys_reduction": rel(REDUCTION),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "what_closes_now": {
            "physical_anchor_search_executed": True,
            "best_structural_route_identified": True,
            "K_phys_reduced_to_alpha_phys_or_action_unit": kphys_open,
            "target_backsolve_forbidden": True,
        },
        "what_remains_open": {
            "K_phys_value": True,
            "alpha_phys_value": True,
            "selected_dimensionful_modal_gap": True,
            "matching_scale": True,
            "RG_threshold_scheme": True,
            "alpha_zero_or_MZ_value": True,
        },
        "theorem": {
            "name": "CONSTEM01KPhysSourceHuntReductionTheorem",
            "proved": kphys_open,
            "statement": (
                "After internal weak-split closure, the physical electroweak normalization is reduced to the same single absolute "
                "action/unit anchor isolated by the GR/protospinor branch: alpha_phys, or an equivalent Omega0/ell_p/kappa11/modal-gap unit. "
                "The M-theory route supplies the correct structural slot, but no target-independent dimensionful value is selected by current sources."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EM_01_Alpha1_KPhysSourceHunt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "best_structural_route": "m_theory_modal_gap_planck_anchor",
        "K_phys_value_claimed": False,
        "alpha_phys_value_claimed": False,
        "physical_alpha_value_claimed": False,
        "next_primary": "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST EM 01 Alpha1 KPhys Source Hunt v1

Status: `{STATUS}`

Label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A5-KPHYS`

## Result

After internal weak-split closure, the physical electroweak normalization is
not blocked by the U1/Y determinant row anymore. It is blocked by the absolute
physical action/unit anchor.

Best structural route:

- M-theory/modal-gap Planck anchor,
- equivalently `alpha_phys`, `Omega0`, `ell_p`, or `kappa_11`.

Current reduction:

- `Omega0 = sqrt(alpha_phys) * sqrt(15/log(448))`,
- `Omega0/sqrt(alpha_phys) = 1.5675093859261626`.

## Boundary

No value is claimed for `K_phys`, `alpha_phys`, `Omega0`, `ell_p`, or
`kappa_11`. No Newton, Planck, cosmological, mass, TeV, or electroweak target
is used as a backsolve.

## Next

Next label: `CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A6-DIMENSIONAL-ANCHOR-PACKET`
"""

    for path, payload in [(ANCHORS, anchors), (REDUCTION, reduction), (NEXT_WORK, next_work), (OUTPUT, candidate), (CERT, cert)]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
