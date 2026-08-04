"""Import the S2 Phi_fin finite operator scaffold without selected values."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")

S1_PACKET = DATA / "selected_phifin_s1s2_value_emission.partial_filled.json"
GR_CERT = GR / "certificates" / "phifin_operator_payload_scaffold_import_certificate.json"
GR_PACKET = GR / "candidate_data" / "phifin_operator_payload_scaffold_import.packet.json"

OUTPUT_PACKET = DATA / "selected_phifin_s1s2_value_emission.s2_scaffold.json"
OUTPUT_CERT = CERTS / "selected_phifin_s2_operator_scaffold_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Selected_PhiFin_S2_Operator_Scaffold_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sector_shapes(summary: dict[str, Any], matrix_key: str) -> dict[str, Any]:
    return {
        sector: {
            "dimension": values.get("domain_dimension", values.get("dimension")),
            "expected_kernel_dimension": values["expected_kernel_dimension"],
            "zero_mode_count": values["zero_mode_count"],
            "matrix_shape": values[matrix_key],
        }
        for sector, values in summary.items()
    }


def build_packet() -> dict[str, Any]:
    base = load_json(S1_PACKET)
    gr_cert = load_json(GR_CERT)
    gr_packet = load_json(GR_PACKET)
    packet = json.loads(json.dumps(base))

    basis_id = gr_cert["basis_ids"]["D_E"]
    dotd_basis_id = gr_cert["basis_ids"]["dotD"]
    if basis_id != dotd_basis_id:
        raise ValueError(f"basis mismatch: {basis_id} != {dotd_basis_id}")

    packet["status"] = "PARTIAL_FILLED_S1_RHOE_AND_S2_OPERATOR_SCAFFOLD_VALUES_OPEN"
    packet["S2_galerkin_basis_and_operator_blocks"] = {
        "basis_BN_or_Cech_basis_entries": {
            "status": "SCAFFOLD_IMPORTED_NOT_SELECTED_BASIS",
            "basis_id": basis_id,
            "source_certificate": str(GR_CERT),
            "source_packet": str(GR_PACKET),
            "domain_dimension": 27,
            "family_zero_mode_dimension": 3,
            "higgs_zero_mode_dimension": 1,
            "same_basis_as_S1_rhoE_deck_shadow": True,
        },
        "quadrature_or_inner_product_rule": {
            "status": "MODEL_ACTIVE_SCAFFOLD_IMPORTED_NOT_SELECTED_RULE",
            "rule": "finite 27-mode B_N scaffold inner product from imported Route-C smooth B_N payload",
            "selected_rule_emitted": False,
        },
        "D_E_matrix_entries": {
            "status": "SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES",
            "basis_id": basis_id,
            "sector_shapes": sector_shapes(gr_cert["D_E_summary"], "D_E_matrix_shape"),
            "shape_checks_pass": all(
                values["matrix_shape_matches_complement_to_domain"]
                and values["zero_mode_count_matches_expected_kernel"]
                for values in gr_cert["D_E_summary"].values()
            ),
            "selected_source_verified": gr_cert["source_flags"]["D_E_selected_source_verified"],
        },
        "Riesz_projector_entries": {
            "status": "MODEL_ACTIVE_SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES",
            "basis_id": basis_id,
            "green_operator_verified_in_scaffold": all(
                values["green_operator_verified"]
                for values in gr_cert["dotD_projector_summary"].values()
            ),
            "selected_gap_error_certificate_emitted": False,
        },
        "reduced_Green_entries": {
            "status": "MODEL_ACTIVE_SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES",
            "basis_id": basis_id,
            "green_operator_verified_in_scaffold": all(
                values["green_operator_verified"]
                for values in gr_cert["dotD_projector_summary"].values()
            ),
            "selected_reduced_green_emitted": False,
        },
        "dotD_alpha1_matrix_entries": {
            "status": "SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES",
            "basis_id": basis_id,
            "sector_shapes": sector_shapes(
                gr_cert["dotD_projector_summary"], "dotD_alpha1_matrix_shape"
            ),
            "selected_dotD_source_verified": gr_cert["source_flags"][
                "dotD_selected_source_verified"
            ],
            "alpha1_driver_verified": gr_cert["source_flags"]["dotD_alpha1_driver_verified"],
        },
        "sector_projectors": {
            "status": "SCAFFOLD_IMPORTED_NOT_SELECTED_VALUES",
            "basis_id": basis_id,
            "sector_shapes": sector_shapes(
                gr_cert["dotD_projector_summary"], "sector_projector_shape"
            ),
            "horizontal_gauge_verified_in_scaffold": all(
                values["horizontal_gauge_verified"]
                for values in gr_cert["dotD_projector_summary"].values()
            ),
        },
        "gap_gamma_N": "OPEN_SELECTED_GAP_CERTIFICATE_REQUIRED",
        "residual_epsilon_N": "OPEN_SELECTED_TRUNCATION_ERROR_CERTIFICATE_REQUIRED",
        "gap_condition_epsilon_lt_gamma_margin": False,
    }

    packet["S2_operator_scaffold_import"] = {
        "status": "SCAFFOLD_IMPORTED_SELECTED_VALUES_OPEN",
        "source_certificate": str(GR_CERT),
        "source_packet": str(GR_PACKET),
        "theorem": gr_packet["theorem"],
        "closed_now": gr_cert["closed_now"],
        "source_flags": gr_cert["source_flags"],
        "C1_summary": gr_cert["C1_summary"],
        "still_open": gr_cert["still_open"],
        "verdict": gr_cert["verdict"],
    }
    packet["validator_replay"].update(
        {
            "D_E_validator_passes": False,
            "Riesz_gap_validator_passes": False,
            "reduced_Green_validator_passes": False,
            "dotD_response_validator_passes": False,
            "selected_source_promotion_passes_without_lifted_flags": False,
            "scaffold_shape_validator_passes": True,
        }
    )
    packet["partial_fill_guardrail"].update(
        {
            "full_selected_payload_emitted": False,
            "selected_source_flags_may_be_set_true": False,
            "S2_scaffold_imported_but_selected_values_open": True,
            "reason": "S2 operator scaffold imported from same-basis Route-C B_N payload; selected source promotion, selected gap/error, and honest replay remain open.",
        }
    )
    return packet


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    s2 = packet["S2_galerkin_basis_and_operator_blocks"]
    scaffold = packet["S2_operator_scaffold_import"]
    return {
        "certificate": "SelectedPhiFinS2OperatorScaffoldImport",
        "status": "SELECTED_PHIFIN_S2_OPERATOR_SCAFFOLD_IMPORTED_SELECTED_VALUES_OPEN",
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "input_packet": str(S1_PACKET.relative_to(ROOT)),
        "input_scaffold_certificate": str(GR_CERT),
        "input_scaffold_packet": str(GR_PACKET),
        "what_closes_now": {
            "same_basis_id_for_DE_dotD_and_S1_rhoE_shadow": s2[
                "basis_BN_or_Cech_basis_entries"
            ]["same_basis_as_S1_rhoE_deck_shadow"],
            "S2_27_mode_operator_scaffold_imported": True,
            "D_E_sector_shapes_imported": s2["D_E_matrix_entries"]["shape_checks_pass"],
            "sector_projectors_dotD_shapes_imported": True,
            "family_zero_mode_dimension_three_retained": scaffold["closed_now"][
                "family_zero_mode_dimension_three_retained"
            ],
            "higgs_zero_mode_dimension_one_retained": scaffold["closed_now"][
                "Higgs_zero_mode_dimension_one_retained"
            ],
            "canonical_C1_zero_response_no_go_carried_forward": scaffold["closed_now"][
                "canonical_C1_zero_response_no_go_preserved"
            ],
            "target_fitting_excluded": scaffold["closed_now"]["target_fitting_excluded"],
        },
        "what_remains_open": {
            "full_S1_source_promotion_for_rhoE": True,
            "selected_D_E_source_promotion": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "selected_gap_error_certificate": True,
            "honest_routec_validator_replay": True,
            "selected_S2_value_emission": True,
            "A_selected": True,
            "b_selected": True,
        },
        "guardrails": {
            "claims_full_selected_payload_emitted": False,
            "claims_selected_source_flags_may_be_set_true": False,
            "claims_selected_D_E_values_emitted": False,
            "claims_selected_Riesz_Green_values_emitted": False,
            "claims_selected_dotD_values_emitted": False,
            "claims_A_selected_emitted": False,
            "claims_b_selected_emitted": False,
            "uses_observed_or_benchmark_inputs": False,
            "uses_formal_lift_flags_as_proof": False,
        },
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    s2 = packet["S2_galerkin_basis_and_operator_blocks"]
    de = s2["D_E_matrix_entries"]["sector_shapes"]
    dotd = s2["dotD_alpha1_matrix_entries"]["sector_shapes"]
    sectors = ", ".join(sorted(de))
    return f"""# Selected PhiFin S2 Operator Scaffold Import v1

## Result

The S2 finite operator scaffold is imported into the local Phi_fin packet.

Status: `{cert["status"]}`

This is a scaffold import, not selected value emission. It records the same
`F3xF3_gerbe_twisted_fourier_N1_rank3` basis, the 27-mode B_N operator shapes,
sector projectors, `D_E` shapes, and `dotD_alpha1` shapes. It also carries
forward the canonical C1 zero-response no-go.

## Imported Scaffold

```text
basis id: {s2["basis_BN_or_Cech_basis_entries"]["basis_id"]}
domain dimension: {s2["basis_BN_or_Cech_basis_entries"]["domain_dimension"]}
sectors: {sectors}
family zero-mode dimension: {s2["basis_BN_or_Cech_basis_entries"]["family_zero_mode_dimension"]}
Higgs zero-mode dimension: {s2["basis_BN_or_Cech_basis_entries"]["higgs_zero_mode_dimension"]}
D_E selected source verified: {s2["D_E_matrix_entries"]["selected_source_verified"]}
dotD selected source verified: {s2["dotD_alpha1_matrix_entries"]["selected_dotD_source_verified"]}
alpha1 driver verified: {s2["dotD_alpha1_matrix_entries"]["alpha1_driver_verified"]}
```

Representative shapes:

```text
Q D_E shape: {de["Q"]["matrix_shape"]}
Q dotD_alpha1 shape: {dotd["Q"]["matrix_shape"]}
H D_E shape: {de["H"]["matrix_shape"]}
H dotD_alpha1 shape: {dotd["H"]["matrix_shape"]}
```

## Boundary

The following are deliberately still open:

- selected source promotion for `rho_E`
- selected `D_E` source promotion
- selected `dotD` source and alpha1 driver
- selected positive gap and truncation-error certificate
- honest Route-C replay without lifted flags
- selected S2 numerical value emission
- `A_selected` and `b_selected`

This is the useful middle layer: it proves the S2 operator carrier is no longer
vague, while keeping the proof honest about the missing selected source data.
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
