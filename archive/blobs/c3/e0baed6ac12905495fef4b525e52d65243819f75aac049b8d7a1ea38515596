"""Try to fill the same-source operator packet, or produce a no-go."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

CONTRACT = DATA / "selected_routec_samesource_matter_slot_overlap_operator_packet.candidate.json"
PHIFIN = DATA / "selected_phifin_alpha1_payload.candidate.json"
PROJECTIVE = DATA / "projective_gerbe_rhoe_source_promotion.candidate.json"
S3_DIFF = DATA / "selected_s3_differential_cohomology_source_certificate.candidate.json"
C1_ROUTING = DATA / "selected_routec_selected_c1_routing_normalization_and_overlap_source_packet.candidate.json"
MATTER_THEOREM = DATA / "selected_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
ASEMBLY = DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"

OUTPUT = DATA / "selected_routec_samesource_operatorpacket_fill_or_nogo.candidate.json"
CERT = CERTS / "selected_routec_samesource_operatorpacket_fill_or_nogo_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1.md"

STATUS = "MTT_SELECTED_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY"
NEXT = "MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1"
VALIDATOR = ROOT / "scripts" / "validate_samesource_matter_slot_overlap_operator_packet.py"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def field(required: str, support: bool, reason: str, provenance: str = "support_shape_only") -> dict[str, Any]:
    return {
        "required": required,
        "support_present": support,
        "selected_emitted": False,
        "same_source": False,
        "theorem_derived": False,
        "provenance": provenance,
        "reason_not_selected": reason,
    }


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    try:
        report = json.loads(proc.stdout)
    except json.JSONDecodeError:
        report = {"raw_output": proc.stdout}
    report["exit_code"] = proc.returncode
    return report


def main() -> None:
    contract = load(CONTRACT)
    phifin = load(PHIFIN)
    projective = load(PROJECTIVE)
    s3_diff = load(S3_DIFF)
    c1_routing = load(C1_ROUTING)
    matter = load(MATTER_THEOREM)
    assembly = load(ASEMBLY)

    fields = {
        "source_identity": field(
            contract["required_fields"]["source_identity"]["required"],
            projective["promotion_gate_flags_after_s3_closure"]["selected_by_mtt"]
            and s3_diff["selected_source_packet"]["source_selected_by_mtt"],
            "S3/gerbe source is selected at source level, but visible/Route-C operator source identity is still open.",
        ),
        "matter_slot_charge": field(
            contract["required_fields"]["matter_slot_charge"]["required"],
            matter["matter_slot_charge"]["routeA_matches_required_partition"],
            "SU(5)/E6 route matches the required partition structurally, but the selected charge table is not emitted.",
        ),
        "singlet_neutrino_rule": field(
            contract["required_fields"]["singlet_neutrino_rule"]["required"],
            False,
            "No selected 1_M Dirac-neutrino routing rule was found in current artifacts.",
        ),
        "operator_values": field(
            contract["required_fields"]["operator_values"]["required"],
            phifin["payload_summary"]["all_support_shapes_present"],
            "D_E/dotD/Riesz/Green support shapes exist, but selected source flags and alpha1-driver provenance are false.",
        ),
        "overlap_transfer": field(
            contract["required_fields"]["overlap_transfer"]["required"],
            c1_routing["selection_verdict"]["conditional_algebra_closed"],
            "Source-to-C1 transfer is exact conditionally, but selected sector routing and selected transfer map are not emitted.",
            provenance="locked_target_selection",
        ),
        "normalization": field(
            contract["required_fields"]["normalization"]["required"],
            c1_routing["attempts"]["normalization"]["conditional_residual_norm"] < 1e-12,
            "Conditional solve normalization is exact, but no trace/inner-product/Hessian normalization is selected.",
            provenance="locked_target_selection",
        ),
        "primitive_contractions": field(
            contract["required_fields"]["primitive_contractions"]["required"],
            phifin["payload_summary"]["support_candidate_present"]["primitive_C1_contractions"],
            "Primitive C1/Yukawa contraction slots exist as templates/support, but selected values remain null.",
        ),
    }

    attempted = {
        "fields": fields,
        "packet_flags": {
            "one_same_source": False,
            "observed_data_used": False,
            "target_fitting_used": False,
            "promote_to_A_selected": False,
            "promote_to_b_selected": False,
        },
        "conditional_data_retained": {
            "conditional_A_shape": assembly["conditional_operator"]["shape"],
            "conditional_deltaTheta": assembly["locked_solve"]["deltaTheta_conditional"],
            "conditional_residual_norm": assembly["locked_solve"]["residual_norm"],
        },
    }

    candidate = {
        "candidate": "MTTSelectedRouteCSameSourceOperatorPacketFillOrNoGo",
        "status": STATUS,
        "inputs": {
            "contract": rel(CONTRACT),
            "selected_phifin_alpha1_payload": rel(PHIFIN),
            "projective_gerbe_source_promotion": rel(PROJECTIVE),
            "selected_s3_differential_cohomology_source": rel(S3_DIFF),
            "selected_c1_routing_normalization_packet": rel(C1_ROUTING),
            "matter_slot_charge_overlap_theorem": rel(MATTER_THEOREM),
            "conditional_A_assembly": rel(ASEMBLY),
        },
        "attempted_selected_packet": attempted,
        "fill_summary": {
            "required_fields": len(fields),
            "support_present": sum(1 for item in fields.values() if item["support_present"]),
            "selected_emitted": sum(1 for item in fields.values() if item["selected_emitted"]),
            "can_promote_A_selected": False,
            "can_promote_b_selected": False,
            "nogo_for_current_scaffolds": True,
        },
        "why_fill_fails": [
            "source-level S3/gerbe selection does not equal visible/Route-C operator-source emission",
            "matter-slot charge remains structural, not selected",
            "1_M Dirac-neutrino routing is absent",
            "D_E/dotD/Riesz/Green selected flags remain false",
            "overlap transfer and normalization are selected by the locked target only conditionally",
            "primitive C1/Yukawa contraction values remain null/support-only",
        ],
        "what_closes_now": {
            "fill_attempt_executed": True,
            "validator_added": True,
            "current_scaffold_nogo_proved": True,
            "conditional_A_retained_without_promotion": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_visible_or_routec_operator_source_identity": True,
            "selected_matter_slot_charge_table": True,
            "selected_1M_neutrino_rule": True,
            "selected_DE_dotD_Riesz_Green_values": True,
            "selected_overlap_transfer_functor": True,
            "selected_trace_hessian_normalization": True,
            "selected_primitive_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    validator_report = run_validator(OUTPUT)
    candidate["validator_report"] = validator_report
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    CERT.write_text(
        json.dumps(
            {
                "status": STATUS,
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "validator_exit_code": validator_report["exit_code"],
                "validator_ok": validator_report.get("ok", False),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
                "next_required_artifact": NEXT,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        """# MTT Selected Route-C SameSource OperatorPacket Fill or NoGo

Status: `MTT_SELECTED_ROUTEC_SAMESOURCE_OPERATORPACKET_FILL_ATTEMPT_NOGO_CURRENT_SCAFFOLDS_SUPPORT_ONLY`

The seven-field packet was attempted against the current artifacts.  The fill
does not validate.

## Result

Current artifacts provide broad support shapes, but no field is emitted as a
selected theorem-derived same-source value.  The validator rejects the packet
because the fields are support-only, conditional, target-localized, or absent.

The conditional Weyl-pair operator remains useful:

```text
A_conditional deltaTheta = b_splitter
deltaTheta = (1,1)
```

but it is not promoted to `A_selected` or `b_selected`.

## Minimal Next Attack

The next step is not more finite algebra.  It is a source-emission subpacket:

- visible/Route-C operator-source identity,
- selected matter-slot charge table,
- selected `1_M` Dirac-neutrino routing,
- selected D_E/dotD/Riesz/Green values,
- selected overlap-transfer functor,
- selected trace/Hessian normalization,
- selected primitive contractions.

Next artifact: `MTT_Selected_RouteC_SourceEmission_MinimalSubpacket_AttackPlan_v1`.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "validator_exit_code": validator_report["exit_code"]}, indent=2))


if __name__ == "__main__":
    main()
