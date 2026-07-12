"""Import primitive fiber-shift or typed-retarded-selector source theorem."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
SM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure")

PREVIOUS = CERTS / "typedbn_retarded_derivative_or_primitive_response_valueemission_import_certificate.json"
SM_PACKET = SM / "candidate_data" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem.candidate.json"
SM_CERT = SM / "certificates" / "selected_primitivefibershift_or_typedretardedselector_sourcetheorem_certificate.json"

OUTPUT_PACKET = DATA / "primitive_fibershift_or_typed_retarded_selector_sourcetheorem_import.candidate.json"
OUTPUT_CERT = CERTS / "primitive_fibershift_or_typed_retarded_selector_sourcetheorem_import_certificate.json"
OUTPUT_NOTE = CORPUS / "PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_Import_v1.md"

STATUS = "PRIMITIVE_FIBERCLASS_QUOTIENT_IMPORTED_HIGHERORDER_FULLRESPONSE_OPEN"
PREVIOUS_STATUS = "TYPEDBN_OR_PRIMITIVE_RESPONSE_VALUEEMISSION_IMPORTED_SELECTOR_PROVENANCE_OPEN"
SM_STATUS = (
    "MTT_SELECTED_PRIMITIVEFIBERSHIFT_OR_TYPEDRETARDEDSELECTOR_"
    "SOURCETHEOREM_BUILT_FIBERCLASS_QUOTIENT_SELECTED_ABSOLUTE_SELECTOR_OPEN"
)
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    sm_packet = load(SM_PACKET)
    sm_cert = load(SM_CERT)
    primitive = sm_packet["primitive_selector"]
    typed = sm_packet["typed_retarded_selector"]
    payload = sm_packet["observable_class_payload"]
    remains = sm_packet["what_remains_open"]

    checks = {
        "G0_previous_frontier_matches": previous["status"] == PREVIOUS_STATUS,
        "G1_upstream_selector_theorem_proved": sm_cert["status"] == SM_STATUS
        and sm_cert["theorem_proved"] is True
        and sm_cert["active_shift_selected_claimed"] is True
        and sm_cert["fiber_class_quotient_selected_claimed"] is True,
        "G2_active_shift_selected": primitive["active_shift_selected"] is True
        and primitive["selected_active_shift"] == [1, 1],
        "G3_absolute_fiber_origin_not_selected": primitive["absolute_fiber_shift_selected"] is False
        and sm_cert["absolute_fiber_shift_selected_claimed"] is False,
        "G4_fiber_quotient_selected_for_current_C1": primitive[
            "fiber_class_quotient_selected_for_current_observables"
        ]
        is True
        and primitive["fixed_fiber_class"] == [0, 1, 2]
        and primitive["canonical_computation_representative"] == "fiber_shift_0"
        and primitive["canonical_representative_is_physical_selector"] is False,
        "G5_current_observables_invariant": all(
            sectors[sector]["rank"] == 3 and sectors[sector]["YYstar_is_scalar_identity"] is True
            for sectors in primitive["invariant_spectral_observables"].values()
            for sector in ["u", "d", "e", "nuD"]
        ),
        "G6_current_layer_flavor_split_not_claimed": payload[
            "selected_current_C1_observable_class"
        ]
        is True
        and payload["selected_matrix_representative"] is False
        and payload["current_layer_flavor_splitting_possible"] is False,
        "G7_typed_retarded_still_support_only": typed["attempted"] is True
        and typed["selected"] is False
        and sm_cert["typed_retarded_selector_claimed"] is False,
        "G8_no_full_closure_or_target_overclaim": sm_packet["closure_claimed"] is False
        and sm_packet["A_selected_claimed"] is False
        and sm_packet["b_selected_claimed"] is False
        and sm_packet["observed_data_used"] is False
        and sm_packet["target_fitting_used"] is False,
    }

    return {
        "packet": "PrimitiveFiberShift_or_TypedRetardedSelector_SourceTheorem_Import_v1",
        "status": STATUS,
        "inputs": {
            "previous_local_import": str(PREVIOUS.relative_to(ROOT)),
            "sm_selector_packet": str(SM_PACKET),
            "sm_selector_certificate": str(SM_CERT),
        },
        "theorem": {
            "name": "PrimitiveFiberClassQuotientImportTheorem",
            "proved": all(checks.values()),
            "closure_claimed": False,
            "statement": (
                "The selected primitive active shift is (1,1). No absolute qutrit "
                "fiber origin is selected; instead, shifts 0, 1, and 2 form the "
                "selected quotient class for current finite C1 spectral observables. "
                "Shift 0 is legal only as a computation representative. The current "
                "observable class is scalar-permutation degenerate, so flavor "
                "hierarchy, CKM/PMNS, CP, A_selected, and b_selected require selected "
                "higher-order or full-response matrices."
            ),
        },
        "checks": checks,
        "selected_primitive_class": {
            "selected_active_shift": primitive["selected_active_shift"],
            "fixed_fiber_class": primitive["fixed_fiber_class"],
            "representative_for_computation": payload["representative_for_computation"],
            "absolute_fiber_shift_selected": primitive["absolute_fiber_shift_selected"],
            "selected_current_C1_observable_class": payload["selected_current_C1_observable_class"],
            "selected_matrix_representative": payload["selected_matrix_representative"],
            "current_layer_flavor_splitting_possible": payload[
                "current_layer_flavor_splitting_possible"
            ],
        },
        "invariant_spectral_observables": primitive["invariant_spectral_observables"],
        "what_closes_now": sm_packet["what_closes_now"],
        "what_remains_open": remains,
        "frontier_update": {
            "old_next": previous["next_required_artifact"],
            "current_next": NEXT,
            "why": (
                "The hidden fiber-origin knob is removed for current spectral C1 "
                "observables. The next obstacle is no longer a fiber-shift choice, "
                "but higher-order/full-response source emission that breaks the "
                "current scalar-permutation degeneracy."
            ),
        },
        "guardrails": {
            "active_shift_selected_claimed": True,
            "fiber_class_quotient_selected_claimed": True,
            "absolute_fiber_shift_selected_claimed": False,
            "selected_matrix_representative_claimed": False,
            "typed_retarded_selector_claimed": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "observed_data_used": False,
            "target_fitting_used": False,
        },
        "next_required_artifact": NEXT,
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "PrimitiveFiberShiftOrTypedRetardedSelectorSourceTheoremImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "selected_primitive_class": packet["selected_primitive_class"],
        "frontier_update": packet["frontier_update"],
        "what_remains_open": packet["what_remains_open"],
        "guardrails": packet["guardrails"],
        "next_required_artifact": packet["next_required_artifact"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# PrimitiveFiberShift or TypedRetardedSelector SourceTheorem Import v1

Status: `{cert["status"]}`.

## Result

The primitive active shift is selected as `(1,1)`.  The absolute qutrit fiber
origin is not selected; instead, fixed fiber shifts `0,1,2` form the selected
quotient class for current finite C1 spectral observables.  Shift `0` is only a
computation representative.

```json
{json.dumps(packet["selected_primitive_class"], indent=2, sort_keys=True)}
```

## Boundary

The current class is scalar-permutation degenerate.  It does not produce
nondegenerate Yukawa hierarchy, CKM/PMNS, CP, `A_selected`, or `b_selected`.

Next artifact: `{packet["next_required_artifact"]}`.
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
