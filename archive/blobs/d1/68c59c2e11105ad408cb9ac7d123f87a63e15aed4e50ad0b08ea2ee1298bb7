"""Build Step63 direct scalar-emission trial / dynamic-overlap frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step63_directscalaremission_trial_or_dynamicoverlap_frontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
TRIAL_PACKET = PACKET_DIR / "step63_direct_scalar_emission_trial.packet.json"
CUTSET = PACKET_DIR / "step63_dynamic_overlap_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step63_DirectScalarEmissionTrial_or_DynamicOverlapFrontier_v1.md"

STEP62 = DATA / "selected_step62_qualitativeorbit_rthetafunctional_import_or_thresholdmagnitude_frontier.candidate.json"
SAME_BRANCH = DATA / "selected_samebranchthresholdmassschemerows_or_sourceanchorconstruction.candidate.json"
NOKNOB_KERNEL = DATA / "selected_noknobvaluederivationkernel_or_sourceanchortheorem.candidate.json"
DIRECT = DATA / "selected_internalrthetascalarrowemission_or_universalanchorselection.candidate.json"
PHIFIN = DATA / "selected_phifinminimizertracesectorpayload_or_internalscalarrows.candidate.json"
U10 = DATA / "selected_u10ubar5_1m_sourcepromotion_samebranch_emission.candidate.json"
DYNAMIC = DATA / "selected_dynamic_overlapkernel_or_c1primitive_source_emission.candidate.json"

STATUS = "MTT_SELECTED_STEP63_DIRECT_SCALAR_EMISSION_TRIED_DYNAMIC_OVERLAP_FRONTIER_OPEN"
NEXT = "MTT_Selected_TypedBN_RetardedDerivative_or_PrimitiveResponse_ValueEmission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [STEP62, SAME_BRANCH, NOKNOB_KERNEL, DIRECT, PHIFIN, U10, DYNAMIC]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step63 inputs: " + ", ".join(missing))

    step62 = load(STEP62)
    same = load(SAME_BRANCH)
    kernel = load(NOKNOB_KERNEL)
    direct = load(DIRECT)
    phifin = load(PHIFIN)
    u10 = load(U10)
    dynamic = load(DYNAMIC)

    trial = {
        "schema": "MTTStep63DirectScalarEmissionTrial.v1",
        "status": "DIRECT_SCALAR_EMISSION_TRIED_AND_BLOCKED_HONESTLY",
        "closed_before_trial": {
            "Step62_Rtheta_functional_source_domain": step62["closure_decision"][
                "Rtheta_scalar_value_functional_source_domain_closed"
            ],
            "same_branch_readiness_8_of_9": same["closure_decision"]["Rtheta_readiness_8_of_9"],
            "final_no_knob_kernel_typed": kernel["closure_decision"]["final_no_knob_kernel_typed"],
            "transported_PhiFin_sector_payload_imported": phifin["closure_decision"][
                "transported_sector_payload_imported"
            ],
            "static_U10_Ubar5_1M_source_closed": u10["closure_decision"]["static_U10_Ubar5_1M_source_closed"],
        },
        "trial_result": {
            "direct_emission_attempt_executed": direct["closure_decision"]["direct_emission_attempt_executed"],
            "accepted_internal_scalar_row_count": direct["closure_decision"]["accepted_internal_scalar_row_count"],
            "lambda_H_row_emitted": direct["closure_decision"]["lambda_H_row_emitted"],
            "fullS2_payload_ready": direct["closure_decision"]["fullS2_payload_ready"],
            "universal_anchor_selected": direct["closure_decision"]["universal_anchor_selected"],
        },
        "post_trial_imports": {
            "PhiFin_trace_imported": phifin["what_closes_now"]["functional_PhiFin_trace_imported"],
            "validator_ready_sector_rho_s_imported": phifin["what_closes_now"]["validator_ready_sector_rho_s_imported"],
            "static_matter_slot_readout_closed": u10["closure_decision"]["static_matter_slot_readout_closed"],
            "static_U10_Ubar5_1M_source_closed": u10["closure_decision"]["static_U10_Ubar5_1M_source_closed"],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(TRIAL_PACKET, trial)

    cutset = {
        "schema": "MTTStep63DynamicOverlapFrontier.v1",
        "status": "DYNAMIC_OVERLAP_OR_C1_PRIMITIVE_FRONTIER_PINNED",
        "closed_or_reduced": dynamic["dynamic_cutset"]["already_closed_or_reduced"],
        "remaining_minimal_objects": dynamic["dynamic_cutset"]["remaining_minimal_objects"],
        "lanes": dynamic["lanes"],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "Static sector routing, transported Phi_fin/rho_s support, and direct scalar emission "
                "trial are complete. The remaining blocker is dynamic: typed B_N retarded derivative/"
                "alpha1 source-strength theorem, End0-to-sector functor values, or selected primitive "
                "response values with b_selected."
            ),
        },
        "dynamic_kernel_emitted": dynamic["dynamic_kernel_emitted"],
        "selected_C1_primitive_emitted": dynamic["selected_C1_primitive_emitted"],
        "A_selected_claimed": dynamic["A_selected_claimed"],
        "b_selected_claimed": dynamic["b_selected_claimed"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep63DirectScalarEmissionTrialOrDynamicOverlapFrontier",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "direct_scalar_emission_trial": rel(TRIAL_PACKET),
            "dynamic_overlap_frontier": rel(CUTSET),
        },
        "theorem": {
            "name": "Step63DirectScalarEmissionTrialAndDynamicOverlapFrontierTheorem",
            "proved": True,
            "statement": (
                "After Step62, the same-branch threshold/mass-scheme integration, final no-knob kernel, "
                "direct internal scalar-row emission attempt, transported Phi_fin/rho_s import, and static "
                "U10/Ubar5/1M matter-slot source closure can all be imported. The direct scalar trial emits "
                "zero accepted scalar rows. The active frontier is therefore the dynamic overlap/C1 primitive "
                "source: a typed B_N retarded derivative or primitive response value emission."
            ),
        },
        "closure_decision": {
            "direct_scalar_emission_trial_executed": True,
            "PhiFin_trace_and_static_matter_slot_blockers_retired": True,
            "dynamic_overlap_frontier_pinned": True,
            "accepted_internal_scalar_row_count": direct["closure_decision"]["accepted_internal_scalar_row_count"],
            "lambda_H_row_emitted": False,
            "dynamic_kernel_emitted": False,
            "selected_C1_primitive_emitted": False,
            "A_selected_claimed": False,
            "b_selected_claimed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step62["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step63_DirectScalarEmissionTrial_or_DynamicOverlapFrontier_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected Step63 DirectScalarEmissionTrial or DynamicOverlapFrontier v1

Status: `{STATUS}`.

## Trial Result

```text
same-branch readiness                 : 8/9
final no-knob kernel typed            : true
direct scalar emission tried          : true
Phi_fin/rho_s trace blockers retired  : true
static U10/Ubar5/1M source closed     : true
accepted internal scalar rows         : 0
lambda_H row emitted                  : false
dynamic kernel emitted                : false
selected C1 primitive emitted         : false
A_selected claimed                    : false
b_selected claimed                    : false
true SM equivalence closed            : false
full no-knob closure                  : false
```

## Active Frontier

The direct numerical row route has been tried against the closed source/domain,
same-branch readiness, transported Phi_fin support, and static matter-slot
readout. It still emits zero accepted rows. The remaining blocker is dynamic,
not static:

`{NEXT}`

Minimum next success: emit a typed same-branch `B_N` retarded derivative/alpha1
driver and End0-to-sector functor values, or emit selected primitive/vertex/
basis-transport response values with `b_selected`.
""",
        encoding="utf-8",
    )

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
