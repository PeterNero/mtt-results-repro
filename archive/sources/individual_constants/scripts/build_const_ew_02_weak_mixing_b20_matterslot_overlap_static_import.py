"""Build CONST-EW-02 B20 matter-slot overlap static import.

B20 imports the later SM-slot functor/static readout results from the SM-parity
repo. This discharges the static sector-routing and trace-normalization parts
of the B19 Route-C matter-slot blocker, while preserving the dynamic C1 and
weak-angle gates as open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b20_matterslot_overlap_static_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = BASE / "smslot_static_matterslot_overlap_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b20_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B20_MatterSlotOverlapStaticImport_v1.md"

STATUS = "MTT_CONST_EW_02_B20_STATIC_MATTERSLOT_OVERLAP_IMPORTED_DYNAMIC_C1_OPEN"


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

    b19_path = DATA / "const_ew_02_weak_mixing_b19_visible_source_solve_or_ende_values.candidate.json"
    b19_boundary_path = DATA / "const_ew_02_weak_mixing_b19_visible_source_solve_or_ende_values" / "weak_mixing_b19_boundary.packet.json"
    readout_path = SM / "candidate_data" / "selected_matterslot_readout_backimport_from_smslotfunctor.candidate.json"
    readout_cert_path = SM / "certificates" / "selected_matterslot_readout_backimport_from_smslotfunctor_certificate.json"
    overlap_path = SM / "candidate_data" / "selected_smslotfunctor_overlapkernel_source_emission.candidate.json"
    overlap_cert_path = SM / "certificates" / "selected_smslotfunctor_overlapkernel_source_emission_certificate.json"
    downstream_path = SM / "candidate_data" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger.candidate.json"
    downstream_cert_path = SM / "certificates" / "selected_smslotfunctor_downstream_operator_payloads_or_smparity_ledger_certificate.json"

    b19 = load(b19_path)
    b19_boundary = load(b19_boundary_path)
    readout = load(readout_path)
    readout_cert = load(readout_cert_path)
    overlap = load(overlap_path)
    overlap_cert = load(overlap_cert_path)
    downstream = load(downstream_path)
    downstream_cert = load(downstream_cert_path)

    import_packet = {
        "schema": "MTTConstEW02B20SMSlotStaticMatterSlotOverlapImport.v1",
        "status": "STATIC_MATTERSLOT_ROUTE_AND_TRACE_NORMALIZATION_IMPORTED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B20-ROUTEC-MATTERSLOT-OVERLAP-NORMALIZATION",
        "inputs": {
            "B19_candidate": rel(b19_path),
            "B19_boundary": rel(b19_boundary_path),
            "SM_readout_candidate": rel(readout_path),
            "SM_readout_certificate": rel(readout_cert_path),
            "SM_overlap_candidate": rel(overlap_path),
            "SM_overlap_certificate": rel(overlap_cert_path),
            "SM_downstream_ledger_candidate": rel(downstream_path),
            "SM_downstream_ledger_certificate": rel(downstream_cert_path),
        },
        "superset_strategy": {
            "mode": "BACKIMPORT_STATIC_SMSLOTFUNCTOR_TO_WEAK_MIXING_ROUTEC_BLOCKER",
            "using_one_straight_path": False,
            "straight_path": "selected terminal section-ring/SM-slot functor source arrows",
            "support_paths": [
                "q79 SU5/E6 polarization and 1_M Dirac-neutrino dictionary",
                "transported-projector trace Gram normalization",
                "same-source SM-slot functor consistency map",
            ],
            "locked_target_role": "conditional C1 columns remain consistency checks, not selectors",
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "static_import_closes": {
            "selected_sector_route_Z_to_u_e_X_to_d_nuD": downstream_cert["what_closes"]["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"],
            "selected_1M_Dirac_neutrino_shift_rule": downstream_cert["what_closes"]["selected_static_1M_Dirac_neutrino_shift_rule"],
            "selected_overlap_transfer_normalization": overlap_cert["what_closes"]["selected_overlap_transfer_normalization"],
            "selected_SMSlotFunctor_all_six_arrows": overlap_cert["what_closes"]["selected_SMSlotFunctor_all_six_arrows"],
            "static_readout_closed": readout_cert["static_readout_closed"],
            "target_fitting_excluded": downstream_cert["what_closes"]["target_fitting_excluded"],
        },
        "static_values": {
            "phase_route": downstream["weylpair_consequence"]["phase_route"],
            "shift_route": downstream["weylpair_consequence"]["shift_route"],
            "unit_trace_transfer": downstream["old_contract_reclassification"]["normalization"]["unit_trace_transfer"],
            "kernel_definition": overlap["selected_overlap_kernel"]["kernel_definition"],
            "raw_Ti_frobenius_norm": overlap["selected_overlap_kernel"]["normalization_values"]["raw_Ti_frobenius_norm"],
            "matter_triplet_rank": overlap["selected_overlap_kernel"]["normalization_values"]["matter_triplet_rank"],
        },
        "dynamic_tier_not_promoted": {
            "dynamic_visible_routec_operator_source_identity": downstream_cert["what_remains_open"]["dynamic_visible_routec_operator_source_identity"],
            "selected_D_E_Riesz_Green_dotD": downstream_cert["what_remains_open"]["selected_D_E_Riesz_Green_dotD"],
            "selected_dynamic_overlap_tensor_or_transfer_functor": downstream_cert["what_remains_open"]["selected_dynamic_overlap_tensor_or_transfer_functor"],
            "selected_primitive_C1_contractions": downstream_cert["what_remains_open"]["selected_primitive_C1_contractions"],
            "selected_b_selected_and_Hessian_normalization": downstream_cert["what_remains_open"]["selected_b_selected_and_Hessian_normalization"],
            "promote_conditional_A_to_A_selected": downstream_cert["what_remains_open"]["promote_conditional_A_to_A_selected"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B20Boundary.v1",
        "status": "STATIC_B19_MATTERSLOT_BLOCKERS_DISCHARGED_DYNAMIC_WEAKANGLE_BLOCKERS_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B20-BOUNDARY",
        "closed_now": {
            "b19_matter_slot_overlap_static_blocker_retired": True,
            "selected_static_sector_route_Z_to_u_e_X_to_d_nuD": True,
            "selected_static_1M_Dirac_neutrino_shift_rule": True,
            "selected_static_trace_transfer_normalization": True,
            "selected_SMSlotFunctor_all_six_arrows": True,
        },
        "preserved_from_B19": {
            "finite_RouteC_construct_executed": b19_boundary["closed_now"]["finite_RouteC_construct_executed"],
            "routec_operator_algebra_closed_conditionally": b19_boundary["closed_now"]["routec_operator_algebra_closed_conditionally"],
            "source_level_weyl_carrier_closed": b19_boundary["closed_now"]["source_level_weyl_carrier_closed"],
        },
        "still_open": {
            "source_solve_closed": b19["source_solve_closed"] is False,
            "dynamic_visible_routec_operator_source_identity": True,
            "selected_D_E_Riesz_Green_dotD": True,
            "selected_dynamic_overlap_tensor_or_transfer_functor": True,
            "selected_primitive_C1_contractions": True,
            "selected_b_selected_and_Hessian_normalization": True,
            "EndE_rhoE_values_or_threshold_operator": True,
            "heat_spectrum_torsion_or_determinant_finite_part": True,
            "actual_xL_source_emission": True,
            "physical_weak_angle_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B20NextWork.v1",
        "status": "NEXT_WORKORDER_DYNAMIC_OVERLAP_OR_PRIMITIVE_C1",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-C1-OR-ENDE-FINITE-RESPONSE",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-OVERLAP-KERNEL-OR-PRIMITIVE-C1-SOURCE-EMISSION",
            "task": "Emit the same-branch dynamic source-to-C1 overlap tensor or primitive C1 contractions and b_selected/Hessian normalization.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B21-ROUTEC-OPERATOR-SOURCE-IDENTITY-AND-DE-GREEN-DOTD",
            "task": "Promote visible/Route-C operator source identity and selected D_E/Riesz/Green/dotD values from the same branch.",
        },
        "fallback": {
            "label": "CONST-EW-02 / WEAK-MIXING / B21-ENDE-RHOE-FINITE-RESPONSE",
            "task": "Emit selected EndE/rhoE values or a direct heat/torsion/determinant finite response.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB20MatterSlotOverlapStaticImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B20-MATTERSLOT-OVERLAP-OR-SOURCE-AUGMENTATION",
        "output_packets": {
            "smslot_static_matterslot_overlap_import": rel(IMPORT_PACKET),
            "weak_mixing_b20_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B20StaticMatterSlotOverlapImportTheorem",
            "proved": True,
            "statement": (
                "The later selected SM-slot functor/backimport results discharge the "
                "B19 static matter-slot and overlap-normalization blockers: Z/clock "
                "routes to u,e; X/shift routes to d,nuD; 1_M=N^c is on the Dirac "
                "shift side; and finite trace transfer normalization is selected. "
                "This is a static-tier import only and does not promote dynamic C1 "
                "operator values, primitive contractions, b_selected, xL, or the "
                "physical weak angle."
            ),
        },
        "static_matterslot_overlap_blocker_retired": True,
        "dynamic_C1_promoted": False,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B20_MatterSlotOverlapStaticImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "static_matterslot_overlap_blocker_retired": True,
        "dynamic_C1_promoted": False,
        "strict_xL_emitted_now": False,
        "physical_weak_angle_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B20 MatterSlot Overlap Static Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B20-MATTERSLOT-OVERLAP-OR-SOURCE-AUGMENTATION`

## Result

B20 imports the later SM-slot functor/static readout closure into the weak-mixing
Route-C branch.

Closed now:

```text
Z/clock -> u,e
X/shift -> d,nuD
1_M=N^c Dirac-neutrino shift rule
selected finite trace transfer normalization
selected SM-slot functor all six arrows
```

Still open:

```text
dynamic visible/Route-C operator source identity
selected D_E/Riesz/Green/dotD
dynamic C1 overlap tensor or primitive C1 contractions
b_selected/Hessian normalization
EndE/rhoE finite response or heat/torsion/determinant finite part
xL and physical weak angle
```

## Superset Use

This combines multiple source-compatible paths: terminal section-ring arrows,
q79 SU5/E6 matter-slot polarization, and transported-projector trace Gram
normalization. The locked C1 columns remain diagnostics only, not selectors.
"""

    for path, payload in [
        (IMPORT_PACKET, import_packet),
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
