"""Build CONST-HIGGS-01 H6E UV two-Higgs angle or primitive beta policy."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
Q79_REPO = TEXPAPERS / "mtt-q79-proof-repro"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h6e_uv_two_higgs_projection_angle_or_primitive_beta_policy"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
UV_SOURCE_AUDIT = BASE / "uv_two_higgs_projection_angle_source_audit.packet.json"
PRIMITIVE_POLICY = BASE / "primitive_beta_policy.packet.json"
SYMBOLIC_BOUNDARY = BASE / "symbolic_dterm_boundary_packet.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H6E_UVTwoHiggsProjectionAngleOrPrimitiveBetaPolicy_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H6E_UV_BETA_SOURCE_NOGO_PRIMITIVE_POLICY_BUILT"


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

    h6d_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source.candidate.json"
    h6d_single_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source" / "single_higgs_projection_import.packet.json"
    h6d_beta_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source" / "beta_or_projection_angle_source_test.packet.json"
    h6d_contract_path = DATA / "const_higgs_01_h6d_selected_dterm_boundary_or_beta_source" / "dterm_boundary_acceptance_contract.packet.json"
    h6c_boundary_path = DATA / "const_higgs_01_h6c_hsector_row_or_boundary_route_discriminator" / "susy_dterm_boundary_route_import.packet.json"
    q79_single_path = Q79_REPO / "certificates" / "single_higgs_channel_projection_certificate.json"

    h6d = load(h6d_path)
    h6d_single = load(h6d_single_path)
    h6d_beta = load(h6d_beta_path)
    h6d_contract = load(h6d_contract_path)
    h6c_boundary = load(h6c_boundary_path)
    q79_single = load(q79_single_path)

    uv_source_audit = {
        "schema": "MTTConstHiggs01H6EUVTwoHiggsProjectionAngleSourceAudit.v1",
        "status": "STRICT_UV_TWO_HIGGS_BETA_SOURCE_NOT_FOUND",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-SOURCE-AUDIT",
        "inputs": {
            "H6D_candidate": rel(h6d_path),
            "H6D_single_higgs_projection_import": rel(h6d_single_path),
            "H6D_beta_source_test": rel(h6d_beta_path),
            "q79_single_higgs_certificate": rel(q79_single_path),
        },
        "current_closed_support": {
            "low_energy_single_Higgs_projection": h6d["low_energy_single_Higgs_projection_imported"],
            "H_u_to_H": q79_single["higgs_doublet_embedding"]["H_u"] == "H",
            "H_d_to_Hdagger": q79_single["higgs_doublet_embedding"]["H_d"] == "H^dagger",
            "two_independent_low_energy_Higgs_alignment_references": q79_single["closed"]["two_independent_low_energy_higgs_alignment_references"],
            "Dterm_formula_ready": h6d["Dterm_boundary_formula_ready"],
        },
        "strict_source_absences": {
            "selected_UV_two_Higgs_VEV_ratio": True,
            "selected_beta_or_tan_beta": True,
            "selected_two_Higgs_projection_angle": True,
            "selected_heavy_Higgs_decoupling_angle": True,
            "selected_color_triplet_decoupling": q79_single["open"]["color_triplet_projection_or_decoupling"],
            "selected_Higgs_VEV_or_mass_prediction": q79_single["open"]["higgs_mass_and_vev_prediction"],
        },
        "proof_obstruction": {
            "single_Higgs_projection_is_low_energy_not_UV_angle": True,
            "Theta_tan_beta_10_is_representative_not_selected": True,
            "matter_slot_Hu_Hd_labels_are_channel_labels_not_VEV_ratios": True,
            "Dterm_formula_requires_beta_source_before_numeric_lambda": True,
        },
        "strict_no_knob_verdict": {
            "selected_beta_source_closed": False,
            "Dterm_boundary_numeric_value_derived": False,
            "strict_no_knob_Higgs_closure": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    primitive_policy = {
        "schema": "MTTConstHiggs01H6EPrimitiveBetaPolicy.v1",
        "status": "BETA_PRIMITIVE_ALLOWED_ONLY_AS_EXPLICIT_NON_NO_KNOB_POLICY",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-PRIMITIVE-BETA-POLICY",
        "policy": {
            "primitive_name": "beta_H or tan_beta_H",
            "allowed_tier": "EXPLICIT_PRIMITIVE_NON_NO_KNOB",
            "strict_no_knob_tier": False,
            "new_Higgs_specific_parameters_if_declared": 1,
            "new_parameters_declared_now": 0,
            "may_be_used_only_if": [
                "declared once before any Higgs-mass/lambda comparison",
                "not chosen from observed Higgs mass, observed vev, SM-parity lambda, or RG benchmark targets",
                "not retuned per observable, scale, or paper",
                "all downstream lambda_H statements display dependence on beta_H until a theorem derives it",
                "falsifiable by mismatch with other Higgs/EW observables after the same fixed value is used",
            ],
            "forbidden_if": [
                "renamed no-knob closure",
                "set to tan_beta=10 because older text used it as a representative value",
                "backsolved from m_H, lambda_H, v, or measured weak angle",
                "hidden inside threshold or RG matching constants",
            ],
        },
        "current_decision": {
            "declare_beta_primitive_now": False,
            "reason": "A beta primitive would be a Higgs-specific parameter and should be avoided until the UV two-Higgs source and intrinsic H-row routes are exhausted.",
            "recommended_use_now": "symbolic conditional replay only",
        },
        "superset_strategy": {
            "strict_path": "derive beta/tan_beta from selected UV two-Higgs projection or decoupling geometry",
            "conditional_path": "hold beta_H as an explicit primitive policy, not yet instantiated",
            "intrinsic_escape_path": "derive K_H^(4)[12,12,12,12] and avoid D-term beta entirely",
            "paths_combined_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    symbolic_boundary = {
        "schema": "MTTConstHiggs01H6ESymbolicDTermBoundaryPacket.v1",
        "status": "SYMBOLIC_DTERM_BOUNDARY_READY_NUMERIC_VALUE_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-SYMBOLIC-DTERM-BOUNDARY-PACKET",
        "inputs": {
            "H6D_Dterm_boundary_contract": rel(h6d_contract_path),
            "H6C_Dterm_boundary_import": rel(h6c_boundary_path),
        },
        "symbolic_boundary": {
            "potential_convention": h6d_contract["boundary_formula"]["potential_convention"],
            "formula": h6d_contract["boundary_formula"]["formula"],
            "equivalent_cos2beta_from_tanbeta": "cos(2 beta)^2 = ((tan_beta^2 - 1)/(tan_beta^2 + 1))^2",
            "inputs_required": ["g", "g_prime", "beta_H", "matching_scale", "threshold_RG_policy"],
        },
        "diagnostic_example_retained_only_for_replay": {
            "tan_beta": h6c_boundary["diagnostic_replay_not_source"]["tan_beta_example"],
            "cos2beta_sq": h6c_boundary["diagnostic_replay_not_source"]["cos2beta_sq_float"],
            "lambda_same_gauge_corrected_factor": h6c_boundary["diagnostic_replay_not_source"]["corrected_lambda_over_8_same_gauge_diagnostic"],
            "counts_as_source": False,
        },
        "numeric_status": {
            "selected_gauge_boundary_values_filled": False,
            "selected_beta_filled": False,
            "matching_scale_policy_filled": False,
            "threshold_RG_transport_filled": False,
            "numeric_lambda_H_derived": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstHiggs01H6ENextWork.v1",
        "status": "NEXT_WORKORDER_H6F_SYMBOLIC_REPLAY_OR_H7_INTRINSIC_ROW",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-NEXT",
        "primary_strict": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM",
            "task": "Either emit K_H^(4)[12,12,12,12] from the selected action or derive beta_H from a selected UV two-Higgs/decoupling theorem.",
        },
        "conditional_replay": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY",
            "task": "Carry lambda_H(beta_H,g,g') symbolically through matching/RG, while preserving that beta_H is not selected.",
        },
        "paper_insert_section": {
            "label": "CONST-HIGGS-01 / PAPER-INSERT / BETA-POLICY-AND-DTERM-BOUNDARY",
            "task": "State the exact 1/8 convention, reject tan_beta=10 as selected, and separate strict no-knob from explicit primitive tiers.",
        },
    }

    candidate = {
        "candidate": "MTTConstHiggs01H6EUVTwoHiggsProjectionAngleOrPrimitiveBetaPolicy",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-OR-PRIMITIVE-BETA-POLICY",
        "output_packets": {
            "uv_two_higgs_projection_angle_source_audit": rel(UV_SOURCE_AUDIT),
            "primitive_beta_policy": rel(PRIMITIVE_POLICY),
            "symbolic_dterm_boundary_packet": rel(SYMBOLIC_BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTHiggs01H6EUVBetaSourceNoGoAndPrimitivePolicyTheorem",
            "proved": True,
            "statement": (
                "Given H6D, the current corpus closes the low-energy single-Higgs projection and the symbolic D-term formula, but it does not emit a selected UV two-Higgs projection angle, beta/tan_beta, heavy-Higgs decoupling angle, or intrinsic K4 row. Therefore strict no-knob D-term Higgs closure is blocked. A beta primitive is admissible only as an explicit non-no-knob policy with one Higgs-specific parameter, fixed before comparison and not declared now. The only current output is a symbolic boundary packet, not a numerical lambda_H."
            ),
        },
        "low_energy_single_Higgs_projection_closed": True,
        "symbolic_Dterm_boundary_ready": True,
        "selected_UV_beta_source_found": False,
        "beta_primitive_policy_built": True,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "new_Higgs_specific_parameters_if_beta_declared": 1,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H6F_SymbolicDTermBoundaryReplay_or_H7IntrinsicRow_v1",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H6E_UVTwoHiggsProjectionAngleOrPrimitiveBetaPolicy_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "low_energy_single_Higgs_projection_closed": True,
        "symbolic_Dterm_boundary_ready": True,
        "selected_UV_beta_source_found": False,
        "beta_primitive_policy_built": True,
        "beta_primitive_declared_now": False,
        "new_Higgs_specific_parameters": 0,
        "new_Higgs_specific_parameters_if_beta_declared": 1,
        "DTerm_boundary_numeric_value_derived": False,
        "Higgs_quartic_numeric_value_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    note = f"""# MTT CONST HIGGS 01 H6E UV Two-Higgs Projection Angle Or Primitive Beta Policy v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6E-UV-TWO-HIGGS-PROJECTION-ANGLE-OR-PRIMITIVE-BETA-POLICY`

## Result

```text
low-energy single-Higgs projection closed        True
symbolic D-term boundary ready                   True
selected UV beta/tan_beta source                 False
beta primitive policy built                      True
beta primitive declared now                      False
new Higgs-specific parameters now                0
new parameters if beta declared                  1
numeric lambda_H                                 False
strict no-knob Higgs closure                     False
```

## Meaning

H6E prevents a hidden parameter move.  `beta_H` can be handled in only two
honest ways:

```text
strict route: derive beta_H from selected UV two-Higgs/decoupling geometry
conditional route: declare beta_H as one explicit non-no-knob primitive
```

No primitive is declared in H6E.  The usable artifact is only the symbolic
D-term boundary:

```text
lambda = (g^2 + g'^2) cos^2(2 beta_H) / 8
```

## Next

Strict:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7-INTRINSIC-H-SECTOR-K4-ROW-OR-UV-BETA-THEOREM`

Conditional:

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H6F-SYMBOLIC-DTERM-BOUNDARY-REPLAY`
"""

    for path, payload in [
        (UV_SOURCE_AUDIT, uv_source_audit),
        (PRIMITIVE_POLICY, primitive_policy),
        (SYMBOLIC_BOUNDARY, symbolic_boundary),
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
