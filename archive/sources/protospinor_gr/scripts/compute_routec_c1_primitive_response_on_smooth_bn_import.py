from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DOTD_IMPORT = ROOT / "certificates" / "routec_sector_projectors_dotd_on_smooth_bn_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_c1_primitive_response_on_smooth_bn_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_c1_primitive_response_on_smooth_bn_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_C1_Primitive_Response_on_Smooth_BN_Import_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def max_abs_entry(matrix: list[list[object]]) -> float:
    def value_abs(value: object) -> float:
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return abs(float(value))
        if isinstance(value, list) and len(value) == 2:
            return (float(value[0]) ** 2 + float(value[1]) ** 2) ** 0.5
        raise TypeError(value)

    return max((value_abs(value) for row in matrix for value in row), default=0.0)


def main() -> None:
    dotd_import = load(DOTD_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)
    matrices = src["c1_response_matrices"]
    matrix_norms = {sector: max_abs_entry(item["matrix"]) for sector, item in matrices.items()}

    closed_now = {
        "previous_projectors_dotD_imported": dotd_import["theorem"]["proved"],
        "primitive_C1_contraction_engine_built": src_cert["what_closes"]["primitive_C1_contraction_engine_built"],
        "canonical_mode_conserving_tensor_tested": src_cert["what_closes"]["canonical_mode_conserving_tensor_tested"],
        "canonical_tensor_zero_response_result_proved_finitely": src_cert["what_closes"]["canonical_tensor_zero_response_result_proved_finitely"],
        "missing_C1_object_sharpened": src_cert["what_closes"]["missing_C1_object_sharpened"],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    no_go_checks = {
        "canonical_tensor_has_nonzero_slots": src["primitive_tensor"]["nonzero_tensor_slots"] == 729,
        "canonical_tensor_not_selected_by_theorem": src["primitive_tensor"]["selected_by_theorem"] is False,
        "four_C1_sectors_emitted": set(matrices) == {"u", "d", "e", "nuD"},
        "all_c1_matrices_zero": (
            src["diagnostics"]["all_c1_matrices_zero_for_canonical_tensor"] is True
            and all(value == 0.0 for value in matrix_norms.values())
        ),
        "response_support_recorded": all(src["diagnostics"]["response_support"][sector] for sector in ("Q", "u", "d", "L", "e", "N", "H")),
        "zero_reason_records_active_mode_selection_rule": "active-mode conservation" in src["diagnostics"]["why_zero"],
    }

    still_open_checks = {
        "selected_noninvariant_C1_primitive_or_vertex_open": src["what_remains_open"]["selected_noninvariant_C1_primitive_or_vertex"] is True,
        "selected_basis_transport_between_zero_and_response_modes_open": src["what_remains_open"]["selected_basis_transport_between_zero_and_response_modes"] is True,
        "nonzero_C1_response_matrices_open": src["what_remains_open"]["nonzero_C1_response_matrices"] is True,
        "selected_dotD_source_verified_open": src["what_remains_open"]["selected_dotD_source_verified"] is True,
        "alpha1_driver_verified_open": src["what_remains_open"]["alpha1_driver_verified"] is True,
        "honest_replay_open": src["what_remains_open"]["honest_replay_without_lifted_flags"] is True,
        "yukawa_CKM_PMNS_magnitudes_open": src["what_remains_open"]["yukawa_CKM_PMNS_magnitudes"] is True,
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
    }

    theorem = {
        "name": "RouteCC1PrimitiveResponseOnSmoothBNImportTheorem",
        "proved": all(closed_now.values()) and all(no_go_checks.values()) and all(still_open_checks.values()),
        "statement": (
            "For the emitted 27-mode B_N dotD response packet, the canonical "
            "finite translation-invariant F3^2 x qutrit trilinear tensor gives "
            "zero one-response C1 matrices in the u,d,e,nuD sectors. Nonzero C1 "
            "data therefore require a selected non-invariant primitive, vertex "
            "correction, basis transport, or source theorem deriving a different "
            "selected trilinear tensor."
        ),
    }

    verdict = {
        "canonical_C1_contraction_engine_built": True,
        "canonical_translation_invariant_C1_response_nonzero": False,
        "nonzero_selected_C1_response_found": False,
        "selected_noninvariant_primitive_required": True,
        "basis_transport_or_vertex_required": True,
        "yukawa_CKM_PMNS_claim_allowed": False,
        "next_required_artifact": src["next_required_artifact"],
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "primitive_tensor": src["primitive_tensor"],
        "matrix_norms": matrix_norms,
        "diagnostics": src["diagnostics"],
        "closed_now": closed_now,
        "no_go_checks": no_go_checks,
        "still_open_checks": still_open_checks,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C C1 Primitive Response on Smooth B_N Import v1

## Result

The first natural C1 primitive-response contraction has been imported on the
same 27-mode `B_N` basis.

The tested primitive is the canonical finite translation-invariant trilinear
tensor with active `F3^2` mode conservation and qutrit fiber conservation.

```text
nonzero primitive tensor slots = 729
u,d,e,nuD one-response C1 matrices = 0
```

This zero result is a finite selection-rule theorem, not numerical noise. The
emitted horizontal responses live in active mode `(-1,-1)`, while zero modes
and the Higgs zero mode live in `(0,0)`. A one-response trilinear term therefore
violates canonical active-mode conservation.

## Boundary

No Yukawa, CKM, PMNS, mass, or full SM closure claim is made here.

Nonzero C1 response now requires one of:

```text
selected non-invariant C1 primitive or vertex tensor
selected basis transport mixing zero and response modes
same-source theorem deriving a different selected trilinear tensor
full Iwasawa/Strominger data whose response support changes the rule
```

## Status

```text
ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_IMPORTED_SELECTED_PRIMITIVE_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_NonInvariant_C1_Primitive_or_BasisTransport_Search_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_c1_primitive_response_on_smooth_bn_import",
                "status": "ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_IMPORTED_SELECTED_PRIMITIVE_OPEN",
                "input_certificates": {
                    "routec_sector_projectors_dotd_on_smooth_bn_import": str(DOTD_IMPORT),
                    "selected_routec_c1_primitive_response_on_smooth_bn": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "no_go_checks": no_go_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print("STATUS: ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_IMPORTED_SELECTED_PRIMITIVE_OPEN")


if __name__ == "__main__":
    main()
