"""Build CONST-EW-02 B14 scale-law and covariance import.

B14 imports two source promotions discovered in the neighboring non-SM/GR
normalization chain:

1. the selected H2 horizontal scale law;
2. the selected q64=15 character-channel covariance data, G_11=d_Q=1.

This closes two B13 source blockers, but it deliberately does not identify the
internal H2 scale or rho_UV response with the electroweak profile product xL.
The remaining object is the actual electroweak projection/product map.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
GR = TEXPAPERS / "mtt-protospinor-gr-response-proof"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b14_scalelaw_projection_or_phi_ew_import"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
H2_IMPORT = BASE / "selected_h2_scalelaw_import.packet.json"
COV_IMPORT = BASE / "selected_covariance_phi_ew_import.packet.json"
GAP = BASE / "projection_gap_after_import.packet.json"
BOUNDARY = BASE / "weak_mixing_b14_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B14_ScaleLawProjectionOrPhiEWImport_v1.md"

STATUS = "MTT_CONST_EW_02_B14_H2_AND_COVARIANCE_IMPORTED_EW_PROJECTION_OPEN"


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

    b13_path = DATA / "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt.candidate.json"
    b13_synthesis_path = DATA / "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt" / "dual_route_synthesis.packet.json"
    b13_heterotic_path = DATA / "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt" / "heterotic_strominger_scale_route.packet.json"
    b13_rho_path = DATA / "const_ew_02_weak_mixing_b13_dual_route_xl_emission_attempt" / "rho_uv_phi_ew_route.packet.json"
    scale_gate_note = GR / "proof_corpus" / "Physical_Scale_Lifting_Anchor_Gate_v1.md"
    scale_gate_cert = GR / "certificates" / "physical_scale_lifting_anchor_gate_certificate.json"
    cov_note = GR / "proof_corpus" / "Selected_Character_Channel_Covariance_Import_v1.md"
    cov_cert_path = GR / "certificates" / "selected_character_channel_covariance_import_certificate.json"

    b13 = load(b13_path)
    b13_synthesis = load(b13_synthesis_path)
    b13_heterotic = load(b13_heterotic_path)
    b13_rho = load(b13_rho_path)
    scale_cert = load(scale_gate_cert)
    cov_cert = load(cov_cert_path)

    xL_required = float(b13_synthesis["target"]["xL_required"])
    sin2_if_emitted = float(b13_synthesis["target"]["sin2_if_emitted"])
    scale_data = scale_cert["imported_internal_scale_lift"]
    cov_data = cov_cert["internal_selected_data"]

    R_star = float(scale_data["R_star"])
    L_logR = math.log(R_star)
    x_required_if_L_logR = xL_required / L_logR
    rho_from_formula = (64.0 * (2.0 * math.pi) ** 2 / (16.0 * R_star**4 + 8.0)) ** 2

    h2_import = {
        "schema": "MTTConstEW02B14SelectedH2ScaleLawImport.v1",
        "status": "SELECTED_H2_SCALELAW_IMPORTED_EW_PROJECTION_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-H2-SCALELAW-IMPORT",
        "inputs": {
            "B13_heterotic_route": rel(b13_heterotic_path),
            "physical_scale_lifting_anchor_gate_note": rel(scale_gate_note),
            "physical_scale_lifting_anchor_gate_certificate": rel(scale_gate_cert),
        },
        "imported_selection": {
            "scale_law": scale_data["scale_law"],
            "selected_horizontal_scale_law_closed": scale_cert["closed_tests"]["selected_horizontal_scale_law_closed"],
            "R_star": R_star,
            "r3": scale_data["r3"],
            "v1_tilde": scale_data["v1_tilde"],
            "rho_UV": scale_data["rho_UV"],
            "s_star_from_rho": scale_data["s_star_from_rho"],
        },
        "diagnostic_if_identified_with_electroweak_log": {
            "L_logR": L_logR,
            "x_required_for_xL": x_required_if_L_logR,
            "why_diagnostic_only": "No source theorem identifies this internal scale ratio with mu_match/MZ or the electroweak profile log.",
        },
        "import_scope": "shared selected internal H2 horizontal scale law only",
        "electroweak_projection_selected": False,
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cov_import = {
        "schema": "MTTConstEW02B14SelectedCovariancePhiEWImport.v1",
        "status": "SELECTED_CHARACTER_COVARIANCE_IMPORTED_PHI_EW_PRODUCT_MAP_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-PHI-EW-COVARIANCE-IMPORT",
        "inputs": {
            "B13_rhoUV_route": rel(b13_rho_path),
            "selected_character_channel_covariance_note": rel(cov_note),
            "selected_character_channel_covariance_certificate": rel(cov_cert_path),
        },
        "imported_covariance": {
            "selected_character": cov_data["selected_character"],
            "selected_channel": cov_data["selected_channel"],
            "covariance": cov_data["covariance"],
            "retarded_kernel_action": cov_data["retarded_kernel_action"],
            "D_raw_norm_squared_d_Q": cov_data["D_raw_norm_squared_d_Q"],
            "G_11": cov_data["G_11"],
            "R_star": cov_data["R_star"],
            "C_UV_norm_internal": cov_data["C_UV_norm_internal"],
            "rho_UV": cov_data["rho_UV"],
            "rho_from_formula_with_G11_eq_dQ_eq_1": rho_from_formula,
        },
        "identification_premise": cov_cert["identification_premise"],
        "what_this_removes_from_B13": [
            "selected response-row inner product G_11",
            "selected finite-memory disturbance covariance ||D_raw||^2",
        ],
        "what_it_does_not_remove": [
            "projection map Phi_EW(rho_UV, branch data)->xL",
            "proof that the selected character covariance is the electroweak threshold covariance rather than only the shared internal rho_UV covariance",
            "scheme/threshold policy for mapping the internal response to low-scale weak mixing",
        ],
        "phi_ew_product_map_selected": False,
        "emits_xL": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    projection_gap = {
        "schema": "MTTConstEW02B14ProjectionGapAfterImport.v1",
        "status": "SOURCE_DATA_IMPORTED_PRODUCT_MAP_STILL_MISSING",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-PROJECTION-GAP",
        "target_product": {
            "xL_required": xL_required,
            "sin2_if_emitted": sin2_if_emitted,
        },
        "now_source_verified": {
            "selected_horizontal_scale_law_H2": True,
            "selected_G_11": True,
            "selected_D_raw_norm_squared_d_Q": True,
            "selected_q64_15_character_channel": True,
        },
        "not_source_verified": {
            "H2_to_electroweak_log_projection": True,
            "Phi_EW_to_xL_product_map": True,
            "same_branch_electroweak_threshold_operator": True,
            "strict_no_knob_weak_angle_value": True,
        },
        "forbidden_promotions": [
            "use closeness of H2 diagnostics to select electroweak x",
            "identify R_star with mu_match/MZ by notation alone",
            "use observed weak mixing angle to define Phi_EW",
            "treat G_11=d_Q=1 as sufficient for xL without the product map",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B14Boundary.v1",
        "status": "B13_SOURCE_BLOCKERS_PARTLY_CLOSED_EW_PROJECTION_REMAINS",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-BOUNDARY",
        "closed_now": {
            "selected_horizontal_scale_law": True,
            "selected_H2_scale_law": True,
            "selected_G11_and_Draw_covariance": True,
            "selected_character_channel_q64_15": True,
            "rhoUV_internal_source_data_imported": True,
        },
        "still_open": {
            "actual_xL_source_emission": True,
            "electroweak_projection_from_H2_scale_law": True,
            "Phi_EW_rhoUV_to_xL": True,
            "same_branch_threshold_determinant": True,
            "physical_weak_angle_closure": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B14NextWork.v1",
        "status": "NEXT_WORKORDER_EW_PRODUCT_MAP",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B15-H2-EW-PROJECTION-OR-PHI-EW-PRODUCT",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B15-H2-EW-PROJECTION",
            "task": "Prove a typed projection from selected H2 internal scale data to the electroweak profile product xL without using measured weak-angle data.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B15-PHI-EW-PRODUCT-MAP",
            "task": "Construct Phi_EW from the selected q64=15 rho_UV response/covariance data and show whether it emits xL.",
        },
        "candidate_theorem_name": "Selected_H2_ElectroweakProjection_or_PhiEW_ProductMap_v1",
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB14ScaleLawProjectionOrPhiEWImport",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B14-SCALELAW-EW-PROJECTION-OR-PHI-EW",
        "output_packets": {
            "selected_h2_scalelaw_import": rel(H2_IMPORT),
            "selected_covariance_phi_ew_import": rel(COV_IMPORT),
            "projection_gap_after_import": rel(GAP),
            "weak_mixing_b14_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B14ScaleLawAndCovarianceImportTheorem",
            "proved": True,
            "statement": (
                "Given the imported physical scale-lifting anchor gate and selected "
                "character-channel covariance certificate, B14 promotes the H2 "
                "horizontal scale law and the selected covariance data G_11=d_Q=1 "
                "as source-verified internal inputs for the weak-mixing frontier. "
                "This does not emit xL until a selected electroweak projection or "
                "Phi_EW product map is proved."
            ),
        },
        "strict_xL_emitted_now": False,
        "what_closes_now": boundary["closed_now"],
        "what_remains_open": boundary["still_open"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B14_ScaleLawProjectionOrPhiEWImport_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "input_candidate": rel(b13_path),
        "input_external_certificates": {
            "physical_scale_lifting_anchor_gate": rel(scale_gate_cert),
            "selected_character_channel_covariance_import": rel(cov_cert_path),
        },
        "selected_H2_imported": True,
        "selected_covariance_imported": True,
        "G_11": cov_data["G_11"],
        "D_raw_norm_squared_d_Q": cov_data["D_raw_norm_squared_d_Q"],
        "R_star": R_star,
        "rho_UV": cov_data["rho_UV"],
        "strict_xL_emitted_now": False,
        "electroweak_projection_selected": False,
        "Phi_EW_product_map_selected": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B14 Scale Law Projection Or Phi EW Import v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B14-SCALELAW-EW-PROJECTION-OR-PHI-EW`

## Result

B14 imports two source promotions from the shared non-SM/GR normalization chain.

Closed on the shared selected internal branch:

```text
scale law = H2
R_star    = {R_star}
rho_UV    = {cov_data["rho_UV"]}
G_11      = {cov_data["G_11"]}
d_Q       = ||D_raw||^2 = {cov_data["D_raw_norm_squared_d_Q"]}
channel   = {cov_data["selected_channel"]}
```

This removes the B13 blockers `selected_horizontal_scale_law`,
`selected_G11`, and `selected_D_raw_covariance`.

## Still Open

This does not yet prove the weak mixing angle.  The missing object is:

```text
Selected_H2_ElectroweakProjection_or_PhiEW_ProductMap_v1
```

It must prove one of:

```text
H2 selected scale data -> xL
Phi_EW(rho_UV, q64=15 covariance data) -> xL
```

without using observed weak-angle or alpha values as selectors.

## Diagnostic Only

If one incorrectly treated `L=log(R_star)` as the electroweak log, then:

```text
L = {L_logR}
x required for xL = {x_required_if_L_logR}
```

This is not promoted because the electroweak projection is still absent.

## Next

`CONST-EW-02 / WEAK-MIXING / B15-H2-EW-PROJECTION-OR-PHI-EW-PRODUCT`
"""

    for path, payload in [
        (H2_IMPORT, h2_import),
        (COV_IMPORT, cov_import),
        (GAP, projection_gap),
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
