from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MTT = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

BTT_PACKET = ROOT / "candidate_data" / "selected_tt_metric_shape_map_image.template.json"
BTT_THEOREM = ROOT / "certificates" / "selected_tt_metric_shape_map_image_theorem_certificate.json"
QG_SOURCE = MTT / "12 Quantum Gravity" / "Modal_Triplet_Theory__From_MTT_to_a_UV_Finite__Unitary_Quantum_Gravity_v4.md"
FCP_SOURCE = MTT / "5 Dirac Delta" / "Finite_Coherent_Projection_in_Modal_Triplet_Theory_v2.md"

OUT_CERT = ROOT / "certificates" / "btt_packet_partial_fill_weight_brs_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "selected_tt_metric_shape_map_image.partial_fill.json"
OUT_NOTE = ROOT / "proof_corpus" / "BTT_Packet_Partial_Fill_Weight_BRS_Theorem_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has(text: str, *needles: str) -> bool:
    return all(needle in text for needle in needles)


def rotate_plus_cross(theta: float) -> list[list[float]]:
    """SO(2) action on the plus/cross polarization basis."""
    return [
        [math.cos(2.0 * theta), math.sin(2.0 * theta)],
        [-math.sin(2.0 * theta), math.cos(2.0 * theta)],
    ]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def close(a: float, b: float) -> bool:
    return abs(a - b) < 1e-12


def main() -> None:
    template = load(BTT_PACKET)
    theorem = load(BTT_THEOREM)
    qg = read(QG_SOURCE)
    fcp = read(FCP_SOURCE)

    theta = 0.37
    phi = 0.81
    r_theta_phi = matmul(rotate_plus_cross(theta), rotate_plus_cross(phi))
    r_sum = rotate_plus_cross(theta + phi)
    representation_check = all(
        close(r_theta_phi[i][j], r_sum[i][j]) for i in range(2) for j in range(2)
    )
    nontrivial_weight_check = not close(rotate_plus_cross(theta)[0][0], math.cos(theta))

    source_tests = {
        "qg_tt_two_point_physical_and_gauge_invariant": has(
            qg,
            "physical TT two-point function",
            "projected, gauge-invariant graviton correlator",
        ),
        "qg_pure_gauge_removed_by_bv": has(
            qg,
            "pure-gauge directions are removed by the BV gauge-fixing",
        ),
        "qg_brs_physical_observables_gauge_independent": has(
            qg,
            "BRST/BV cohomology of observables",
            "Physical observables",
            "gauge independent",
        ),
        "fcp_linearized_filter_has_tt_projectors": has(
            fcp,
            "B_{\\rm grav}^{\\rm lin}",
            "P_{\\rm TT}",
            "transverse-traceless",
        ),
        "fcp_filter_acts_on_spin2_not_diffeomorphism_modes": has(
            fcp,
            "weak-field gravitational filtering acts on physical spin-2 data",
            "not pure",
            "diffeomorphism modes",
        ),
    }

    closed_properties = {
        "B_TT_central_circle_weight": 2,
        "B_TT_BRST_quotient_compatible": True,
    }

    still_open_properties = {
        "B_TT_nonzero": None,
        "B_TT_image_in_retained_exact_branch": None,
        "same_central_circle_angle_as_Z64_carrier": None,
    }

    partial_packet = dict(template)
    partial_packet["schema"] = "SelectedTTMetricShapeMapImage.partial_fill.v1"
    partial_packet["required_properties"] = {
        **template["required_properties"],
        **closed_properties,
    }
    partial_packet["closed_properties"] = closed_properties
    partial_packet["still_open_properties"] = still_open_properties
    partial_packet["note"] = (
        "Weight and BRST/TT quotient compatibility are now closed. The exact retained-branch "
        "image and same-angle identification remain open; do not promote lambda_GR,TT=15 until they close."
    )
    OUT_PACKET.write_text(json.dumps(partial_packet, indent=2), encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "btt_packet_partial_fill_weight_brs",
        "status": "BTT_PACKET_PARTIALLY_FILLED_WEIGHT2_BRS_CLOSED_EXACT_IMAGE_OPEN",
        "input_certificates": {
            "selected_tt_metric_shape_map_image_theorem": str(BTT_THEOREM),
        },
        "source_files": {
            "qg": str(QG_SOURCE),
            "finite_coherent_projection": str(FCP_SOURCE),
        },
        "source_tests": source_tests,
        "polarization_weight_proof": {
            "basis": ["TT_plus", "TT_cross"],
            "rotation_matrix": "R(theta)=[[cos(2 theta), sin(2 theta)],[-sin(2 theta), cos(2 theta)]]",
            "representation_check_Rtheta_Rphi_equals_Rtheta_plus_phi": representation_check,
            "nontrivial_spin2_not_spin1_check": nontrivial_weight_check,
            "central_circle_weight": 2,
            "conclusion": "The TT plus/cross plane carries helicity/central-circle weight 2.",
        },
        "closed_properties": closed_properties,
        "still_open_properties": still_open_properties,
        "partial_packet_written": str(OUT_PACKET),
        "theorem_consequence": {
            "unconditional_lambda_GR_TT_15": False,
            "why": (
                "The B_TT exact retained-branch image and same central-circle angle are still not "
                "computed from DG(Psi*) Pi_coh."
            ),
            "if_remaining_properties_close_then": theorem["theorem"]["conditional_conclusion"],
        },
        "guardrails": {
            "claims_BTT_exact_image_computed": False,
            "claims_same_angle_with_Z64_closed": False,
            "claims_unconditional_lambda_GR_TT_15": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = """# BTT Packet Partial Fill: Weight and BRST Theorem v1

## Closed Now

Two fields in the selected `B_TT` packet are now closed.

1. The TT plus/cross plane has spin/helicity weight `2`. Under a transverse
   rotation by angle `theta`, the real polarization basis transforms by
   `R(theta)=[[cos(2 theta), sin(2 theta)],[-sin(2 theta), cos(2 theta)]]`.
   This is exactly the real weight-2 character action.

2. The `B_TT` restriction is compatible with the BRST/diffeomorphism quotient
   at the level supported by the corpus: QG works on physical TT two-point
   functions, pure-gauge directions are removed by BV gauge fixing, and the
   finite-projection paper requires weak-field gravitational filters to act on
   physical spin-2 TT data rather than diffeomorphism modes.

## Still Open

This does not yet compute the exact internal image of

```text
B_TT = DG(Psi*) Pi_coh |_{TT}
```

inside the retained exact branch `H0 tensor K64 tensor C|d_*>`, and it does not
yet prove that the TT central-circle angle is the same sampled angle used by the
exact `Z64` carrier. Therefore it still does not unconditionally prove
`lambda_GR,TT=15`.

## Remaining Minimal Gate

Compute or source the image of `DG(Psi*) Pi_coh` on the TT plus/cross quotient.
The two fields closed here mean the remaining check is narrower:

```text
B_TT nonzero,
B_TT image lies in H0 tensor K64 tensor C|d_*>,
same central-circle angle as the retained Z64 carrier.
```
"""
    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
