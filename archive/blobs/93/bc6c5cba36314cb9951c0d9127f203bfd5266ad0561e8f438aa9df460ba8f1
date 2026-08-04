from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_THEOREM = ROOT / "certificates" / "gr_tt_projector_window_helicity2_z64_source_theorem_certificate.json"
HELICITY_FUNCTOR = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"

OUT_CERT = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "GR_TT_Helicity2_Z64_Uniqueness_Theorem_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def char_order(n: int, k: int) -> int:
    return 1 if k % n == 0 else n // math.gcd(n, k)


def real_character_planes(n: int) -> list[dict]:
    planes = []
    for k in range(1, n // 2):
        planes.append(
            {
                "real_plane": f"span{{cos({k} theta_j), sin({k} theta_j)}}",
                "character_pair": [k, (-k) % n],
                "order": char_order(n, k),
                "dimension_real": 2,
            }
        )
    return planes


def main() -> None:
    source = load(SOURCE_THEOREM)
    helicity = load(HELICITY_FUNCTOR)

    n = helicity["numerical_checks"]["N"]
    spin = 2
    planes = real_character_planes(n)
    selected = [p for p in planes if spin in p["character_pair"] or (-spin) % n in p["character_pair"]]
    competitors = [p for p in planes if p not in selected]

    uniqueness_checks = {
        "finite_carrier_is_Z64": n == 64,
        "real_two_dimensional_character_planes_count": len(planes),
        "spin2_character_label": spin,
        "spin2_plane_unique_up_to_conjugation": len(selected) == 1,
        "selected_plane": selected[0] if selected else None,
        "selected_plane_order": selected[0]["order"] if selected else None,
        "competitor_count": len(competitors),
        "all_other_real_planes_have_wrong_rotation_weight": all(
            spin not in p["character_pair"] and (-spin) % n not in p["character_pair"] for p in competitors
        ),
        "compression_to_15_I2_already_verified": helicity["verdict"]["algebraic_compression_to_15_I2_closed"],
        "retarded_kernel_invariance_already_verified": helicity["verdict"][
            "retarded_kernel_preserves_functor_image"
        ],
    }

    theorem = {
        "name": "GR_TT_Helicity2_Z64_Uniqueness_Theorem",
        "statement": (
            "Inside the retained real two-dimensional character planes of C[Z64], "
            "the only plane with spin-2 rotation weight under the same central-circle "
            "angular coordinate is the k=2 conjugate pair span{c_2,s_2}."
        ),
        "closed": (
            uniqueness_checks["finite_carrier_is_Z64"]
            and uniqueness_checks["spin2_plane_unique_up_to_conjugation"]
            and uniqueness_checks["all_other_real_planes_have_wrong_rotation_weight"]
            and uniqueness_checks["compression_to_15_I2_already_verified"]
            and uniqueness_checks["retarded_kernel_invariance_already_verified"]
        ),
        "proof_dependencies": [
            "TT plus/cross has spin-2 rotation weight",
            "central-circle carrier is C[Z64]",
            "use the same central-circle angular coordinate for the TT response character",
            "exact branch tower is d_* with L64 eigenvalue 15",
        ],
    }

    remaining_premises = {
        "same_central_circle_angle_for_GR_TT_response": {
            "status": "SOURCE_COMPATIBLE_BUT_NOT_EXPLICITLY_CERTIFIED",
            "meaning": (
                "The TT spin-2 transverse rotation angle is represented by the same "
                "central-circle coordinate used by the retained exact Z64 carrier."
            ),
        },
        "selected_GR_TT_Aint_projector_window_is_a_central_circle_character_subfiber": {
            "status": "SOURCE_COMPATIBLE_BUT_NOT_EXPLICITLY_CERTIFIED",
            "meaning": (
                "The GR TT SPT internal projector/window selects a finite central-circle "
                "character plane over d_*, not a different internal complement."
            ),
        },
    }

    closure_if_premises = {
        "if_both_remaining_premises_are_accepted": {
            "selected_projector_window": "|d_*> tensor span{c_2,s_2}",
            "lambda_GR_TT": 15.0,
            "status": "FULL_EXACT_BRANCH_GR_TT_GAP_15",
        },
        "without_those_premises": {
            "status": "UNIQUE_HELICITY2_Z64_WINDOW_PROVED_CHARACTER_WINDOW_PREMISE_OPEN",
        },
    }

    note = """# GR TT Helicity-2 Z64 Uniqueness Theorem v1

## Result

The representation-theoretic part is now closed.

Inside the real two-dimensional character planes of the retained `C[Z64]`
carrier, the only plane with spin-2 rotation weight is:

```text
span{c_2, s_2}
```

equivalently the conjugate character pair:

```text
k = 2 and k = 62 mod 64.
```

This plane has order `32`, which is expected for spin-2 periodicity.

## Consequence

If the selected GR TT `A_int` projector/window is a central-circle character
subfiber over the exact branch and uses the same central-circle angular
coordinate, then the previous source-compatible candidate is no longer merely a
candidate. It is unique:

```text
selected GR TT A_int projector/window
  =
|d_*> tensor span{c_2,s_2}
```

The already verified compression then gives:

```text
lambda_GR,TT = 15
```

in canonical exact-branch internal units.

## Remaining Premises

The proof no longer needs a numerical choice. It needs only these structural
premises to be source-certified:

```text
1. GR TT response is represented on a central-circle character subfiber.
2. The TT response uses the same central-circle angular coordinate.
```

Given those, the `k=2` helicity plane and the value `15` are forced.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_helicity2_z64_uniqueness_theorem",
        "status": "UNIQUE_HELICITY2_Z64_WINDOW_PROVED_CHARACTER_WINDOW_PREMISE_OPEN",
        "input_certificates": {
            "gr_tt_projector_window_helicity2_z64_source_theorem": str(SOURCE_THEOREM),
            "tt_helicity2_z64_carrier_functor": str(HELICITY_FUNCTOR),
        },
        "source_status_inherited": {
            "source_identity_closed": source["theorem_decision"]["source_identity_closed"],
            "previous_status": source["status"],
        },
        "uniqueness_checks": uniqueness_checks,
        "theorem": theorem,
        "remaining_premises": remaining_premises,
        "closure_if_premises": closure_if_premises,
        "guardrails": {
            "claims_remaining_premises_sourced": False,
            "claims_unconditional_full_GR_TT_gap_15": False,
            "claims_order32_is_primitive_order64": False,
            "claims_physical_dimensionful_gap": False,
            "claims_Newton_or_Planck_prediction": False,
        },
        "next_gate": {
            "name": "Central_Character_Window_Premise_for_GR_TT",
            "minimal_statement": (
                "The selected GR TT SPT internal projector/window is a central-circle "
                "character subfiber over the exact d_* branch, using the same central-circle "
                "angle as the spin-2 TT response."
            ),
            "then_forced": [
                "the subfiber is the unique k=2 real helicity plane",
                "U_TT^* L64 U_TT = 15 I2",
                "lambda_GR,TT = 15 in canonical exact-branch internal units",
            ],
        },
        "note_written": str(OUT_NOTE),
    }

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
