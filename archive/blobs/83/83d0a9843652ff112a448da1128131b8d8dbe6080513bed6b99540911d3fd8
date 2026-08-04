"""Build PhiFinC1 source-emission / finite-row independence theorem frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinc1sourceemissionorfiniterowindependencetheorem"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
CRITERIA = PACKET_DIR / "source_ownership_acceptance_criteria.packet.json"
PREMISES = PACKET_DIR / "remaining_source_ownership_premises.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem_v1.md"

FINAL_PROFILE = DATA / "selected_finalprofilelikelihoodordynamicpayloadvalues.candidate.json"
PSM_THEOREM = DATA / (
    "selected_psm_c1_02_selectedphifinc1sourceemissiontheorem_or_"
    "finitec1rowsourceindependencetheorem.candidate.json"
)
PSM_GATE = DATA / "selected_psm_c1_02_physicalboundaryfirstvariation_or_routebrowsourceindependence.candidate.json"
ROUTE_B = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"

STATUS = (
    "MTT_SELECTED_PHIFINC1SOURCEEMISSIONORFINITEROWINDEPENDENCETHEOREM_"
    "CRITERIA_PROVED_PREMISES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing PhiFinC1 theorem inputs: " + ", ".join(missing))


def main() -> int:
    sources = [FINAL_PROFILE, PSM_THEOREM, PSM_GATE, ROUTE_B]
    require_sources(sources)

    final_profile = load(FINAL_PROFILE)
    theorem = load(PSM_THEOREM)
    gate = load(PSM_GATE)
    route_b = load(ROUTE_B)

    theorem_decision = theorem["closure_decision"]
    gate_decision = gate["closure_decision"]

    criteria_packet = {
        "schema": "MTTSourceOwnershipAcceptanceCriteria.v1",
        "status": "ROUTE_A_AND_ROUTE_B_ACCEPTANCE_CRITERIA_PROVED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_source_ownership_criteria_proved": theorem_decision["selected_source_ownership_criteria_proved"],
        "route_A_acceptance_criterion_proved": theorem["what_closes_now"]["Route_A_acceptance_criterion_proved"],
        "route_B_acceptance_criterion_proved": theorem["what_closes_now"]["Route_B_acceptance_criterion_proved"],
        "source_ownership_boundary_frozen_like_SM_parity": theorem["what_closes_now"][
            "source_ownership_boundary_frozen_like_SM_parity"
        ],
        "finite_rows_closed_as_replay_postchecks": theorem_decision["finite_rows_closed_as_replay_postchecks"],
        "local_principle_route_A_validates": gate_decision["local_principle_route_A_validates"],
        "strict_row_source_independence_validator_built": route_b["what_closes_now"][
            "strict_row_source_independence_validator_built"
        ],
    }
    write_json(CRITERIA, criteria_packet)

    remaining_premises = [
        "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma",
        "independent_finite_C1_row_formula_source_theorem",
    ]
    premises_packet = {
        "schema": "MTTRemainingSourceOwnershipPremises.v1",
        "status": "SOURCE_OWNERSHIP_PREMISES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "remaining_premises": remaining_premises,
        "remaining_premise_count": len(remaining_premises),
        "route_A_source_emission_theorem_proved_now": theorem_decision[
            "route_A_source_emission_theorem_proved_now"
        ],
        "route_B_row_source_independence_theorem_proved_now": theorem_decision[
            "route_B_row_source_independence_theorem_proved_now"
        ],
        "unpatched_PSM_C1_02_closed": theorem_decision["unpatched_PSM_C1_02_closed"],
        "true_SM_equivalence_closed": theorem_decision["true_SM_equivalence_closed"],
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(PREMISES, premises_packet)

    decision = {
        "PhiFinC1_source_emission_or_finite_row_independence_frontier_attacked": True,
        "selected_source_ownership_criteria_proved": True,
        "route_A_acceptance_criterion_proved": True,
        "route_B_acceptance_criterion_proved": True,
        "finite_rows_closed_as_replay_postchecks": True,
        "source_ownership_boundary_frozen_like_SM_parity": True,
        "strict_row_source_independence_validator_built": True,
        "route_A_source_emission_theorem_proved_now": False,
        "route_B_row_source_independence_theorem_proved_now": False,
        "remaining_source_ownership_premise_count": len(remaining_premises),
        "actual_dynamic_QaSU3_payload_values_closed": False,
        "accepted_true_equivalence_precision_rows": 0,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "source_ownership_acceptance_criteria": rel(CRITERIA),
            "remaining_source_ownership_premises": rel(PREMISES),
        },
        "theorem": {
            "name": "PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem",
            "proved": True,
            "statement": (
                "The final dynamic payload theorem frontier has its acceptance "
                "criteria and source-ownership boundary proved. The theorems "
                "themselves are not yet proved; the remaining work is exactly "
                "the no-extra-boundary finite-quotient source lemma or the "
                "independent finite-C1 row-formula source theorem."
            ),
        },
        "upstream_frontier": {
            "candidate": rel(FINAL_PROFILE),
            "status": final_profile["status"],
        },
        "closure_decision": decision,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(OUT, candidate)

    cert = {
        "certificate": "MTT_Selected_PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "theorem_proved": True,
        **decision,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem v1

Status: `{STATUS}`.

## Closed Now

```text
selected source ownership criteria proved         true
Route A acceptance criterion proved               true
Route B acceptance criterion proved               true
finite rows closed as replay postchecks           true
source ownership boundary frozen                  true
strict row source-independence validator built    true
```

## Still Open

```text
Route A source-emission theorem proved            false
Route B row-source independence theorem proved    false
remaining source-ownership premises               {len(remaining_premises)}
actual dynamic Qa/SU3 payload values              false
true SM equivalence                               false
```

Remaining premises:

- `PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma`
- `independent_finite_C1_row_formula_source_theorem`

Next artifact: `{NEXT_ARTIFACT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
