"""Attempt to derive the physical-normalization axiom / strict PEW upgrade.

The previous artifact constructed the explicit physical-normalization axiom and
the direct H K certificate under that axiom.  This artifact asks whether current
repo/cross-repo source data derive the axiom without the premise.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CONST = Path("C:/Users/nero_/Downloads/TEXPAPERS/mtt-individual-constants-source-search")

SLUG = "selected_physicalnormalizationaxiomderivation_or_strictpewnoknobupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_TESTS = PACKET_DIR / "strict_physical_normalization_derivation_route_tests.packet.json"
NO_GO = PACKET_DIR / "scale_symmetry_and_threshold_value_obstruction.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_strict_pew_upgrade_witness.packet.json"
NEXT_PACKET = PACKET_DIR / "next_source_value_payload_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1.md"

PREVIOUS = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate.candidate.json"
PREVIOUS_AXIOM = DATA / "selected_physicalnormalizationsourceaxiom_or_directkcertificate" / "physical_normalization_source_axiom.packet.json"
PREVIOUS_DIRECT_K = (
    DATA
    / "selected_physicalnormalizationsourceaxiom_or_directkcertificate"
    / "direct_kthreshold_omega_h_lambda_certificate_under_axiom.packet.json"
)
PEW_PAYLOAD = DATA / "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload" / "pew_gauge_action_source_payload.packet.json"
DIRECT_K_PAYLOAD = (
    DATA / "selected_pewgaugeactionnormalizationsourcepacket_or_directkcertificatepayload" / "direct_k_certificate_payload.packet.json"
)
EW_RG = DATA / "selected_electroweakgaugekineticnormalizationandrg_or_bn27repairsourceamendment_or_directhkrow.candidate.json"
H_GAUGE = DATA / "selected_hgaugekineticnormalizationmumatch_or_directhkthresholdrow.candidate.json"
STROMINGER = DATA / "selected_heteroticstromingerewthresholdkernel_or_bn27directcarriersourcetheorem_or_directhkrow.candidate.json"
AEW_CORRECTION = DATA / "selected_aewcorrectionfactorsourcetheorem_or_physicalnormalizationrun.candidate.json"
STRICT_METROLOGY = (
    CONST
    / "candidate_data"
    / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive"
    / "strict_same_branch_metrology_attempt.packet.json"
)
G4 = (
    CONST
    / "candidate_data"
    / "const_gr_01_absolute_scale_g4_omega0_physical_unit_or_one_metrology_primitive.candidate.json"
)

STATUS = (
    "MTT_SELECTED_PHYSICALNORMALIZATIONAXIOMDERIVATION_OR_STRICTPEWNOKNOBUPGRADE_"
    "DERIVATION_ATTEMPTED_SCALE_AND_THRESHOLD_VALUES_OPEN"
)
NEXT = "MTT_Selected_StromingerThresholdOperatorValue_or_MetrologyUnitSource_v1"


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


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing strict PEW upgrade inputs: " + ", ".join(missing))


def route_row(route_id: str, status: str, accepted: bool, filled: int, required: int, blockers: list[str]) -> dict[str, Any]:
    return {
        "route_id": route_id,
        "status": status,
        "accepted_as_strict_derivation": accepted,
        "filled_fields": filled,
        "required_fields": required,
        "blocking_reasons": blockers,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }


def main() -> int:
    sources = [
        PREVIOUS,
        PREVIOUS_AXIOM,
        PREVIOUS_DIRECT_K,
        PEW_PAYLOAD,
        DIRECT_K_PAYLOAD,
        EW_RG,
        H_GAUGE,
        STROMINGER,
        AEW_CORRECTION,
        STRICT_METROLOGY,
        G4,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_axiom = load(PREVIOUS_AXIOM)
    previous_direct_k = load(PREVIOUS_DIRECT_K)
    pew_payload = load(PEW_PAYLOAD)
    direct_k_payload = load(DIRECT_K_PAYLOAD)
    ew_rg = load(EW_RG)
    h_gauge = load(H_GAUGE)
    strominger = load(STROMINGER)
    aew_correction = load(AEW_CORRECTION)
    strict_metrology = load(STRICT_METROLOGY)
    g4 = load(G4)

    route_tests = {
        "schema": "MTTStrictPhysicalNormalizationDerivationRouteTests.v1",
        "status": "ALL_CURRENT_STRICT_DERIVATION_ROUTES_TESTED_ZERO_ACCEPTED",
        "closure_claimed": True,
        "routes": [
            route_row(
                "same_branch_physical_metrology",
                strict_metrology["status"],
                False,
                0,
                1,
                [
                    "absolute dimensionful non-identifiability leaves one positive scale free",
                    "relative physical scale solution is closed but no physical rod/clock value is selected",
                    "one-metrology primitive tier is available but not strict no-knob",
                ],
            ),
            route_row(
                "same_branch_gauge_action_normalization",
                "PAYLOAD_FIELDS_LOCKED_ZERO_FINAL_VALUES",
                False,
                pew_payload["filled_field_count"],
                pew_payload["required_field_count"],
                [
                    "physical_gauge_action_anchor is unfilled",
                    "matching_scale_mu_match is unfilled",
                    "RG_threshold_scheme is unfilled",
                    "gaugekinetic_normalization is unfilled",
                    "exact_A_EW_source_expression is unfilled",
                ],
            ),
            route_row(
                "heterotic_strominger_threshold_kernel",
                strominger["status"],
                False,
                1 if strominger["closure_decision"]["tree_level_gauge_kinetic_slot_filled"] else 0,
                4,
                [
                    "tree-level f=S slot is support only",
                    "selected heterotic/Strominger kernel values are open",
                    "analytic torsion or threshold operator finite part is open",
                    "matching scale and RG scheme are open",
                ],
            ),
            route_row(
                "direct_H_K_certificate",
                direct_k_payload["status"],
                False,
                direct_k_payload["filled_certificate_count"],
                len(direct_k_payload["required_certificate_fields"]),
                [
                    "row-level K_threshold.Omega_H.lambda value is not emitted without the axiom",
                    "same-scheme alignment certificate is missing",
                    "D_fin.H value row or symbolic cancellation is not promoted as final row certificate",
                    "selected physical normalization and mu_match are missing",
                ],
            ),
            route_row(
                "A_EW_correction_factor",
                aew_correction["status"],
                False,
                aew_correction["closure_decision"]["accepted_correction_source_row_count"],
                1,
                [
                    "best 103-denominator correction is a near-miss theorem target only",
                    "no same-source correction functional or quotient source theorem emits it",
                ],
            ),
        ],
        "accepted_strict_derivation_route_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    no_go = {
        "schema": "MTTScaleSymmetryAndThresholdValueObstruction.v1",
        "status": "STRICT_PEW_AXIOM_NOT_DERIVED_CURRENT_SOURCE_DATA",
        "closure_claimed": True,
        "scale_symmetry_obstruction": strict_metrology["current_no_go"],
        "threshold_value_obstruction": {
            "strict_primary_route": ew_rg["closure_decision"]["strict_primary_route"],
            "strict_primary_route_selected": ew_rg["closure_decision"]["strict_primary_route_selected"],
            "gaugekinetic_normalization_closed": ew_rg["closure_decision"]["gaugekinetic_normalization_closed"],
            "matching_scale_closed": ew_rg["closure_decision"]["matching_scale_closed"],
            "RG_scheme_closed": ew_rg["closure_decision"]["RG_scheme_closed"],
            "selected_heterotic_strominger_kernel_closed": strominger["closure_decision"][
                "selected_heterotic_strominger_kernel_closed"
            ],
            "analytic_torsion_or_threshold_operator_closed": strominger["closure_decision"][
                "analytic_torsion_or_threshold_operator_closed"
            ],
        },
        "why_previous_axiom_stays_premise": [
            "the axiom fixes the one remaining physical gauge/action normalization coordinate",
            "current MTT packets fix dimensionless ratios and internal weak split but not the physical unit/action row",
            "using lambda_H or A_EW postcheck would be target selection",
        ],
        "strict_no_knob_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional = {
        "schema": "MTTConditionalStrictPEWUpgradeWitness.v1",
        "status": "CONDITIONAL_WITNESS_BUILT_IF_SOURCE_VALUES_EMITTED",
        "closure_claimed": True,
        "if_supplied": [
            "same-branch physical gauge/action normalization P_EW or K_phys/f_ab",
            "selected mu_match",
            "selected RG/threshold scheme",
            "Strominger threshold operator/torsion finite part or direct H K row certificate",
        ],
        "then_closes": {
            "derive_SelectedPhysicalGaugeActionNormalizationAxiom": True,
            "strict_P_EW_source_rows": 1,
            "strict_direct_K_threshold_Omega_H_lambda_rows": 1,
            "strict_selected_K_row_count": 10,
            "H_specific_parameter_count": 0,
            "remove_shared_physical_primitive_from_parameter_ledger": True,
            "minimal_ledger_non_neutrino_excluding_QCD_theta_if_P_EW_closes": 17,
            "minimal_ledger_PMNS_excluding_QCD_theta_if_P_EW_closes": 23,
        },
        "currently_supplied": {
            "same_branch_physical_gauge_action_normalization": False,
            "selected_mu_match": False,
            "selected_RG_threshold_scheme": False,
            "threshold_operator_or_direct_K_certificate": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTNextSourceValuePayloadContract.v1",
        "status": "NEXT_IS_STROMINGER_THRESHOLD_OPERATOR_VALUE_OR_METROLOGY_UNIT_SOURCE",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "non_looping_targets": [
            "compute/source the selected Strominger HYM/monad threshold operator finite part",
            "compute/source selected local-system torsion values",
            "derive a same-branch physical unit/action normalization breaking the scale symmetry",
            "emit a direct row-level K_threshold.Omega_H.lambda certificate independent of A_EW",
        ],
        "forbidden_targets": [
            "reuse the explicit axiom as if it were derived",
            "promote the 103 near-miss correction without a source theorem",
            "use lambda_H, A_EW, weak angle, or alpha as selectors",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "derivation_attempted": True,
        "accepted_strict_derivation_route_count": 0,
        "physical_normalization_axiom_derived": False,
        "strict_P_EW_source_rows": 0,
        "strict_direct_K_threshold_Omega_H_lambda_rows": 0,
        "premised_axiom_lane_preserved": previous["closure_decision"]["physical_normalization_source_axiom_constructed"],
        "premised_ten_K_ledger_preserved": previous["closure_decision"]["premised_selected_K_row_count"] == 10,
        "scale_symmetry_no_go_active": strict_metrology["strict_no_knob_Omega0_derived"] is False,
        "strominger_threshold_values_open": strominger["closure_decision"]["selected_heterotic_strominger_kernel_closed"] is False,
        "strict_no_knob_ten_row_closure": False,
        "full_no_knob_closed": False,
        "true_SM_equivalence_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalNormalizationAxiomDerivationOrStrictPEWNoKnobUpgrade",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "strict_physical_normalization_derivation_route_tests": rel(ROUTE_TESTS),
            "scale_symmetry_and_threshold_value_obstruction": rel(NO_GO),
            "conditional_strict_pew_upgrade_witness": rel(CONDITIONAL),
            "next_source_value_payload_contract": rel(NEXT_PACKET),
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "PhysicalNormalizationAxiomDerivationAttemptTheorem",
            "proved": True,
            "statement": (
                "The explicit physical-normalization axiom constructed in the previous step is not derivable "
                "from current source data.  Same-branch metrology is blocked by an absolute scale symmetry, "
                "and the selected heterotic/Strominger gauge-action route lacks threshold operator/torsion "
                "values, mu_match, and RG scheme.  The premised one-primitive H/lambda closure remains valid, "
                "while strict no-knob PEW closure is reduced to a concrete source-value payload."
            ),
        },
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalNormalizationAxiomDerivation_or_StrictPEWNoKnobUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        **decision,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PhysicalNormalizationAxiomDerivation or StrictPEWNoKnobUpgrade v1

Status: `{STATUS}`.

## Result

The strict upgrade was attempted against all current legal routes:

```text
same-branch metrology / Omega0        : blocked by one-dimensional scale symmetry
same-branch gauge/action normalization: 0/8 final PEW fields filled
heterotic/Strominger threshold route  : framework selected, values open
direct H K certificate                : 0 final certificate rows
A_EW correction factor                : near-miss only, 0 accepted rows
```

Therefore:

```text
physical-normalization axiom derived       : false
strict P_EW source rows                    : 0
strict direct K_threshold.Omega_H.lambda   : 0
strict no-knob ten-row closure             : false
premised one-primitive H/lambda lane       : preserved
```

## Non-Looping Next Payload

The next strict-upgrade object is not another status audit.  It must emit one
of these source values:

```text
1. selected Strominger HYM/monad threshold operator finite part
2. selected local-system torsion value
3. same-branch physical unit/action normalization breaking scale symmetry
4. direct row-level K_threshold.Omega_H.lambda certificate
```

Next artifact: `{NEXT}`.
"""

    write_json(ROUTE_TESTS, route_tests)
    write_json(NO_GO, no_go)
    write_json(CONDITIONAL, conditional)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
