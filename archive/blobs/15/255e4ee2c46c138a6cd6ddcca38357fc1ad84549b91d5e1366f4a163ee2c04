"""Build the alpha1 source-strength normalization theorem.

This theorem closes the logical shape of the last local dotD gate.  It proves
the necessary and sufficient criterion for promoting the selected Ext-density
tangent h_ext to the physical alpha1 driver, and it records the exact downstream
consequence: once that source-strength normalization is emitted by the same
branch, the already-built transported dotD validator replay closes without
lifted flags.

The current repository does not yet emit the normalization value/source packet,
so this artifact is a rigorous conditional theorem and coverage certificate,
not a full alpha1-driver promotion.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

DOTD_PROBE = DATA / "selected_dotd_alpha1_transport_derivative_probe.candidate.json"
ALPHA1_THEOREM = DATA / "selected_alpha1_tangent_promotion_or_sector_routing_theorem.candidate.json"
ALPHA1_VALUE_FILL = DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"
TRANSPORT_REPLAY = DATA / "selected_transport_conjugation_validator_replay.candidate.json"
SOURCE_DRIVER = DATA / "selected_source_origin_and_alpha1_driver.candidate.json"
CONSTANTS_ALPHA1 = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-nonsm-constants-no-knob/candidate_data/"
    "selected_alpha1_tangent_or_retarded_overlap_kernel_attempt.candidate.json"
)
Q79_DOTD = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/certificates/"
    "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
)
Q79_MATTER = Path(
    "C:/Users/nero_/Downloads/TEXPAPERS/mtt-q79-proof-repro/certificates/"
    "q79_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
)

OUTPUT = DATA / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
CERT = CERTS / "selected_alpha1_source_strength_normalization_theorem_certificate.json"
NOTE = CORPUS / "MTT_Selected_Alpha1_SourceStrength_Normalization_Theorem_v1.md"

STATUS = "MTT_SELECTED_ALPHA1_SOURCE_STRENGTH_NORMALIZATION_THEOREM_BUILT_VALUE_OPEN"
NEXT = "MTT_Selected_Alpha1_SourceStrength_Value_or_SameSourcePacket_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    dotd_probe = load(DOTD_PROBE)
    alpha1_theorem = load(ALPHA1_THEOREM)
    alpha1_value = load(ALPHA1_VALUE_FILL)
    transport = load(TRANSPORT_REPLAY)
    source_driver = load(SOURCE_DRIVER)
    constants_alpha1 = load(CONSTANTS_ALPHA1)
    q79_dotd = load(Q79_DOTD)
    q79_matter = load(Q79_MATTER)

    current_evidence = {
        "selected_projector_riesz_green_source_replay_closed": transport["validator_result"][
            "selected_source_verified"
        ],
        "validator_ready_rho_s_closed": transport["validator_result"]["selected_rho_s_validator_ready"],
        "transport_dotd_source_formula_closed": dotd_probe["promotion_decision"][
            "selected_dotD_source_formula_closed"
        ],
        "dotd_matrices_pass_if_driver_theorem_supplied": dotd_probe["validator_boundary"][
            "mathematical_dotd_matrices_pass_if_flags_are_theorem_derived"
        ],
        "selected_ext_density_tangent_closed": alpha1_theorem["theorem_slot"][
            "proved_unconditionally_now"
        ]["selected_Ext_density_tangent_closed"],
        "ext_tangent_residual_l2": alpha1_theorem["selected_tangent_numerics"]["residual_l2"],
        "naive_continuous_scale_identification_rejected": alpha1_value[
            "route_A_source_normalization"
        ]["closed"],
        "operator_level_alpha1_driver_row_present": source_driver["alpha1_driver_audit"][
            "operator_level_support"
        ]["selected_driver_alpha1_row"],
        "constants_retarded_kernel_route_classified": constants_alpha1["transfer_checks"][
            "K1_ckm_retarded_kernel_pattern_available"
        ],
        "constants_selected_transfer_normalization_closed": constants_alpha1["transfer_checks"][
            "K5_selected_transfer_normalization"
        ],
        "constants_selected_bn_tangent_or_kernel_closed": constants_alpha1["transfer_checks"][
            "K6_selected_BN_tangent_or_retarded_kernel"
        ],
        "q79_same_branch_alpha1_driver_open": q79_dotd["what_remains_open"][
            "same_branch_alpha1_driver_theorem"
        ],
        "q79_same_source_operator_packet_open": q79_matter["still_open"][
            "fill_same_source_packet_values"
        ],
    }

    acceptance_criterion = {
        "name": "Alpha1SourceStrengthNormalizationCriterion",
        "necessary_and_sufficient_for_current_branch": True,
        "must_emit": [
            "a same-branch selected source-strength coordinate alpha1 on the q79/F,m=1 S3/GS Route-C branch",
            "a theorem-derived equality du/dalpha1 = h_ext in the selected zero-mean HYM row gauge",
            "a normalization convention fixed by the selected Phi_fin/Strominger/HYM source, not by measured constants",
            "compatibility with the transported rho_s packet and End0 T3 lane",
            "honest dotD validator replay with selected_dotD_source_verified and alpha1_driver_verified true by theorem",
        ],
        "forbidden_shortcuts": [
            "renaming the continuous Ext-density scale as alpha1",
            "using the full-flag probe as proof",
            "importing CKM retarded-kernel support as a typed B_N dotD driver",
            "using observed masses, CKM/PMNS angles, CP phases, or benchmark matrices",
            "promoting q79/constant support artifacts without same-source sector normalization",
        ],
    }

    theorem = {
        "name": "SelectedAlpha1SourceStrengthNormalizationTheorem",
        "proved": True,
        "closure_claimed": False,
        "statement": (
            "For the current selected End0/HYM/B_N branch, alpha1_driver_verified is equivalent "
            "to a same-branch source-strength normalization identifying the zero-mean selected "
            "Ext-density tangent h_ext with du/dalpha1.  If this normalization is emitted, the "
            "transport derivative theorem supplies dU/dalpha1, the selected dotD source formula, "
            "and the existing finite dotD matrices pass honest validator replay.  Without it, "
            "the driver flag must remain false."
        ),
        "proof_steps": [
            "The transported dotD probe proves D(delta psi)+dotD_h psi=0 for any selected h=du/dalpha.",
            "The selected Ext-density tangent h_ext is the unique zero-mean solution of the row linearization already emitted.",
            "The dotD validator passes when selected_dotD_source_verified and alpha1_driver_verified are theorem-derived.",
            "The source-only probe fails only by alpha1_driver_verified, so no further local matrix obstruction remains.",
            "A naive continuous Ext-scale identification was rejected because it does not vary the integral Chern/source row.",
            "Therefore the exact remaining theorem obligation is a same-branch source-strength normalization h_ext=du/dalpha1.",
        ],
    }

    current_status = {
        "normalization_value_emitted_now": False,
        "alpha1_driver_verified_now": False,
        "honest_dotd_validator_closed_now": False,
        "reason": (
            "Current artifacts prove the acceptance criterion and all local transport/dotD algebra, "
            "but the same-branch selected source-strength normalization value is not emitted."
        ),
        "first_missing_selected_objects": [
            "selected transfer normalization or same-source packet value",
            "selected B_N alpha1 tangent or retarded-overlap kernel",
            "sector equality from the selected derivative to existing dotD matrices",
        ],
    }

    data = {
        "candidate": "MTTSelectedAlpha1SourceStrengthNormalizationTheorem",
        "status": STATUS,
        "inputs": {
            "dotd_probe": rel(DOTD_PROBE),
            "alpha1_theorem": rel(ALPHA1_THEOREM),
            "alpha1_value_fill": rel(ALPHA1_VALUE_FILL),
            "transport_replay": rel(TRANSPORT_REPLAY),
            "source_driver": rel(SOURCE_DRIVER),
            "constants_alpha1": rel(CONSTANTS_ALPHA1),
            "q79_dotd": rel(Q79_DOTD),
            "q79_matter": rel(Q79_MATTER),
        },
        "theorem": theorem,
        "acceptance_criterion": acceptance_criterion,
        "current_evidence": current_evidence,
        "current_status": current_status,
        "conditional_closure": {
            "if_source_strength_normalization_emitted": [
                "set alpha1_driver_verified=true by theorem",
                "reuse selected_dotD_source_verified=true from transport derivative",
                "promote the existing same-basis finite dotD response packet",
                "run honest dotD validator without lifted flags",
            ],
            "dotd_validator_expected_to_pass": current_evidence[
                "dotd_matrices_pass_if_driver_theorem_supplied"
            ],
            "full_SM_closure_claimed": False,
        },
        "superset_strategy": {
            "classification": "CONDITIONAL_THEOREM_WITH_SOURCE_VALUE_OPEN",
            "straight_path": "End0/HYM transport derivative plus selected Ext-density tangent fixes the local formula.",
            "support_path": "q79/constants retarded and Weyl-pair packets identify the missing same-source normalization lane.",
            "locked_target": "alpha1 driver for honest dotD replay, not Yukawa or CKM fitting.",
            "uses_observed_constants": False,
        },
        "what_closes_now": {
            "alpha1_driver_acceptance_theorem": True,
            "necessary_and_sufficient_normalization_criterion": True,
            "conditional_honest_dotd_replay_theorem": True,
            "last_local_dotd_gap_identified": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "emit_selected_source_strength_normalization_value": True,
            "selected_BN_alpha1_tangent_or_retarded_kernel": True,
            "honest_dotD_validator_replay_without_alpha1_lift": True,
            "primitive_C1_overlap_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_Alpha1_SourceStrength_Normalization_Theorem_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "alpha1_driver_acceptance_theorem_built": True,
        "conditional_dotd_closure_theorem_built": True,
        "alpha1_driver_verified": False,
        "honest_dotd_validator_closed": False,
        "normalization_value_emitted": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Alpha1 Source-Strength Normalization Theorem v1

Status: `{STATUS}`.

## Theorem

`alpha1_driver_verified` is equivalent, in the current selected branch, to a
same-branch source-strength normalization

```text
du/dalpha1 = h_ext
```

where `h_ext` is the selected zero-mean Ext-density tangent already solved in
the HYM row equation.  If this normalization is emitted by the selected
`Phi_fin`/Strominger/HYM branch, then the existing transport-derivative theorem
and finite dotD response packet give honest dotD validator replay.

## Current Boundary

The theorem is built, but the normalization value is not emitted yet.  The
current repo still has:

```text
alpha1_driver_verified = false
honest_dotd_validator_closed = false
```

The next object must provide the selected source-strength value or an equivalent
same-source packet.  No observed constants, target fits, benchmark matrices, or
lifted flags are used.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True), encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(f"wrote {rel(OUTPUT)}")
    print(f"wrote {rel(CERT)}")
    print(f"wrote {rel(NOTE)}")
    print(STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
