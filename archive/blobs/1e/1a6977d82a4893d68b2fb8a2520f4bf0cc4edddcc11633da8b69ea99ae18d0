from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = ROOT.parent / "mtt-q79-proof-repro"

CHAR_IMPORT = ROOT / "certificates" / "selected_character_channel_covariance_import_certificate.json"
GR_TT_SUPPORT = ROOT / "certificates" / "gr_tt_support_final_theorem_certificate.json"
GR_HELICITY = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"
CORE_SOURCE = ROOT / "certificates" / "selected_core_b0_tt_source_theorem_certificate.json"
Z64_EXACT = Q79 / "certificates" / "z64_exact_branch_certificate.json"
SHARED_LEDGER = Q79 / "certificates" / "shared_knob_cross_encoding_ledger_certificate.json"

OUT_CERT = ROOT / "certificates" / "gr_tt_character_channel_identification_stress_test_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "GR_TT_Character_Channel_Identification_Stress_Test_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def find_shared_knob(ledger: dict, knob_id: str) -> dict:
    for row in ledger["shared_knobs"]:
        if row["id"] == knob_id:
            return row
    raise KeyError(knob_id)


def main() -> None:
    char_import = load(CHAR_IMPORT)
    gr_tt_support = load(GR_TT_SUPPORT)
    gr_helicity = load(GR_HELICITY)
    core_source = load(CORE_SOURCE)
    z64_exact = load(Z64_EXACT)
    shared_ledger = load(SHARED_LEDGER)

    q79_knob = find_shared_knob(shared_ledger, "q79_cp_character")
    z64_knob = find_shared_knob(shared_ledger, "z64_exact_central_circle_carrier")

    common_infrastructure_closed = {
        "character_covariance_import_ready": char_import["status"]
        == "INTERNAL_CHARACTER_CHANNEL_QTAU_AND_CUV_IMPORTED_OMEGA0_OPEN",
        "gr_tt_support_closed": gr_tt_support["status"] == "GR_TT_SUPPORT_FINAL_THEOREM_CLOSED_PHYSICAL_NORMALIZATION_NEXT",
        "gr_tt_exact_branch_lambda_15": gr_tt_support["conclusion"]["lambda_GR_TT_internal_exact_branch"] == 15,
        "gr_helicity_plane_unique": gr_helicity["uniqueness_checks"]["spin2_plane_unique_up_to_conjugation"],
        "core_source_accepted": core_source["final_closed"],
        "z64_exact_branch_closed": z64_exact["status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH",
        "z64_q64_selected": z64_exact["conclusion"]["q_64"] == 15,
        "shared_q79_knob_closed": q79_knob["status"] == "CLOSED",
        "shared_z64_carrier_closed": z64_knob["status"] == "CLOSED_EXACT",
    }

    subspace_comparison = {
        "covariance_channel": char_import["internal_selected_data"]["selected_channel"],
        "covariance_character": char_import["internal_selected_data"]["selected_character"],
        "gr_tt_support": gr_tt_support["conclusion"]["support"],
        "gr_tt_real_character_plane": gr_helicity["uniqueness_checks"]["selected_plane"]["real_plane"],
        "gr_tt_character_pair": gr_helicity["uniqueness_checks"]["selected_plane"]["character_pair"],
        "same_Z64_exact_carrier": True,
        "same_selected_q64_label": True,
        "literal_same_subspace": False,
        "reason_literal_same_subspace_false": (
            "The covariance closure is the one-dimensional CP character channel E_15 K_64, "
            "whereas the GR TT support is the two-dimensional real helicity-2 plane "
            "span{c_2,s_2} over the exact d_* branch. They share the exact Z64/q64 "
            "infrastructure but are different representation slots."
        ),
    }

    legal_import = {
        "internal_scale_data_can_be_shared": True,
        "why": (
            "The shared-knob ledger assigns q64=15 and the exact Z64 central-circle "
            "carrier to quantum-gravity spectral, topology-character, string-flux, "
            "and SM-flavor roles. The rho_UV/s_star data may therefore be used as "
            "shared internal scale data in the GR normalization chain."
        ),
        "does_not_prove_GR_TT_noise_channel_equals_E15": True,
        "extra_premise_needed_for_literal_noise_identification": (
            "The stochastic unresolved disturbance feeding the GR TT response is the "
            "same selected CP character channel E_15 K_64, not merely a response "
            "operator supported on the helicity-2 TT plane."
        ),
    }

    still_open = {
        "literal_GR_TT_stochastic_channel_identified_with_E15": False,
        "physical_Omega_0_selected": False,
        "physical_GR_normalization_closed": False,
    }

    guardrails = {
        "conflates_helicity2_plane_with_E15_character_line": False,
        "claims_literal_channel_identity": False,
        "uses_observed_target_constant": False,
        "revokes_internal_character_import": False,
        "claims_physical_units": False,
    }

    ready = all(common_infrastructure_closed.values())
    status = (
        "SHARED_Z64_Q64_ALIGNMENT_CLOSED_LITERAL_GR_TT_NOISE_CHANNEL_OPEN"
        if ready
        else "CHARACTER_CHANNEL_STRESS_TEST_INPUTS_NOT_READY"
    )

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "gr_tt_character_channel_identification_stress_test",
        "status": status,
        "input_certificates": {
            "selected_character_channel_covariance_import": str(CHAR_IMPORT),
            "gr_tt_support_final_theorem": str(GR_TT_SUPPORT),
            "gr_tt_helicity2_z64_uniqueness": str(GR_HELICITY),
            "selected_core_b0_tt_source_theorem": str(CORE_SOURCE),
            "z64_exact_branch": str(Z64_EXACT),
            "shared_knob_cross_encoding_ledger": str(SHARED_LEDGER),
        },
        "common_infrastructure_closed": common_infrastructure_closed,
        "subspace_comparison": subspace_comparison,
        "legal_import": legal_import,
        "still_open": still_open,
        "guardrails": guardrails,
        "theorem": {
            "name": "GR_TT_Character_Channel_Identification_Stress_Test.v1",
            "status": "ALIGNMENT_CLOSED_LITERAL_NOISE_CHANNEL_OPEN",
            "statement": (
                "The GR TT support theorem and the selected character-channel covariance "
                "closure are aligned on the same exact Z64/q64=15 branch infrastructure. "
                "However, the GR TT response carrier is the real helicity-2 plane "
                "span{c2,s2}, while the covariance closure is the CP character line E_15. "
                "Therefore the internal rho_UV/s_star import is legal as shared selected "
                "scale data, but a literal theorem identifying the GR TT stochastic "
                "disturbance channel with E_15 remains open."
            ),
            "next_strong_premise": legal_import["extra_premise_needed_for_literal_noise_identification"],
        },
        "next_required_artifact": "Selected_Physical_Omega0_Source_Theorem_v1",
        "optional_strengthening": "GR_TT_Stochastic_Channel_Equals_Selected_CP_Character_Theorem_v1",
        "note_written": str(OUT_NOTE),
    }

    note = f"""# GR TT Character-Channel Identification Stress Test v1

## Result

The selected character-channel covariance import survives the stress test as
shared internal scale data, but it should not be overstated as a literal
subspace identity.

Closed common infrastructure:

```text
exact Z64 branch selected q_64 = 15
GR TT support = {gr_tt_support["conclusion"]["support"]}
GR TT lambda  = {gr_tt_support["conclusion"]["lambda_GR_TT_internal_exact_branch"]}
covariance selected channel = {char_import["internal_selected_data"]["selected_channel"]}
d_Q = {char_import["internal_selected_data"]["D_raw_norm_squared_d_Q"]}
rho_UV = {char_import["internal_selected_data"]["rho_UV"]}
s_star = {char_import["internal_selected_data"]["s_star"]}
```

## Critical Distinction

The covariance closure lives on:

```text
E_15 K_64
```

The GR TT response support lives on:

```text
|d_*> tensor span{{c_2,s_2}}
```

These share the exact central-circle/Z64/q64 infrastructure, but they are not
literally the same representation slot. `E_15` is the selected CP character
line; `span{{c_2,s_2}}` is the real helicity-2 TT response plane.
In short, they are not literally the same subspace.

## What We May Claim

We may use the imported `rho_UV` and `s_star` as shared selected internal scale
data in the GR physical-normalization chain.

## What Remains Open

A stronger theorem would have to prove:

```text
{legal_import["extra_premise_needed_for_literal_noise_identification"]}
```

Until then, the principal physical gate remains:

```text
Omega_0
```
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
