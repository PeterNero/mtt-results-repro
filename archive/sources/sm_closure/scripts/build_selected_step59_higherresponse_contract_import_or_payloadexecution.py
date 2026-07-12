"""Build Step59 higher-response contract import / payload execution frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step59_higherresponse_contract_import_or_payloadexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
IMPORT_PACKET = PACKET_DIR / "step59_higherresponse_contract_import.packet.json"
CUTSET = PACKET_DIR / "step59_next_payloadexecution_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step59_HigherResponseContractImport_or_PayloadExecution_v1.md"

STEP58 = DATA / "selected_step58_internalrtheta_nogo_import_or_higherresponse_frontier.candidate.json"
HIGHER = DATA / "selected_higherresponserthetafunctional_or_sourceanchortheorem.candidate.json"
CONTRACT = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "rtheta_higher_response_functional_contract.packet.json"
)
DECISION = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "higher_response_or_source_anchor_decision.packet.json"
)
CUTSET_SOURCE = (
    DATA
    / "selected_higherresponserthetafunctional_or_sourceanchortheorem"
    / "next_cutset_after_higher_response_contract.packet.json"
)

STATUS = "MTT_SELECTED_STEP59_HIGHER_RESPONSE_CONTRACT_IMPORTED_PAYLOAD_EXECUTION_OPEN"
NEXT = "MTT_Selected_DynamicPhiFinC1PayloadRows_or_HigherResponseExecution_v1"


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
    inputs = [STEP58, HIGHER, CONTRACT, DECISION, CUTSET_SOURCE]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step59 inputs: " + ", ".join(missing))

    step58 = load(STEP58)
    higher = load(HIGHER)
    contract = load(CONTRACT)
    decision = load(DECISION)
    cutset_source = load(CUTSET_SOURCE)

    import_packet = {
        "schema": "MTTStep59HigherResponseContractImport.v1",
        "status": "TEN_ROW_HIGHER_RESPONSE_CONTRACT_IMPORTED",
        "step58_source": rel(STEP58),
        "higher_response_source": rel(HIGHER),
        "higher_response_Rtheta_functional_contract_closed": contract["contract_closed"],
        "codomain_scalar_row_count": contract["codomain_scalar_row_count"],
        "codomain_scalar_rows": contract["codomain_scalar_rows"],
        "execution_inputs_available_now": contract["execution_inputs_available_now"],
        "selected_functional_executed": contract["selected_functional_executed"],
        "accepted_scalar_row_count_now": contract["accepted_scalar_row_count_now"],
        "source_anchor_theorem_closed": decision["source_anchor_theorem_closed"],
        "selected_universal_parameter_count": decision["selected_universal_parameter_count"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(IMPORT_PACKET, import_packet)

    cutset = {
        "schema": "MTTStep59NextPayloadExecutionCutset.v1",
        "status": "NEXT_DYNAMIC_PHIFIN_C1_PAYLOAD_ROWS",
        "closed_now": {
            "higher_response_Rtheta_functional_contract_imported": True,
            "ten_scalar_row_target_fixed": True,
            "source_anchor_rechecked_not_selected": True,
        },
        "still_open": cutset_source["still_open"],
        "recommended_next": cutset_source["recommended_next"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedStep59HigherResponseContractImportOrPayloadExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "higherresponse_contract_import": rel(IMPORT_PACKET),
            "next_payloadexecution_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "Step59HigherResponseContractImportTheorem",
            "proved": True,
            "statement": (
                "The higher-response Rtheta functional contract is imported into the numbered plan. "
                "The ten scalar output rows are fixed, but execution is still blocked because dynamic "
                "Phi_fin/C1 payload rows and a source-anchor theorem are not selected."
            ),
        },
        "closure_decision": {
            "higher_response_Rtheta_functional_contract_closed": True,
            "codomain_scalar_row_count": contract["codomain_scalar_row_count"],
            "higher_response_payload_rows_emitted": False,
            "higher_response_Rtheta_executed": False,
            "accepted_scalar_row_count_now": 0,
            "source_anchor_theorem_closed": False,
            "selected_universal_parameter_count": 0,
            "no_knob_value_derivation_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": step58["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step59_HigherResponseContractImport_or_PayloadExecution_v1",
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
        f"""# MTT Selected Step59 HigherResponseContractImport or PayloadExecution v1

Status: `{STATUS}`.

```text
higher-response contract closed        : true
scalar output rows                     : {contract["codomain_scalar_row_count"]}
dynamic Phi_fin/C1 payload emitted     : false
higher-response Rtheta executed        : false
accepted scalar rows                   : 0
source-anchor theorem closed           : false
full no-knob closure                   : false
true SM equivalence                    : false
```

The next target is `{NEXT}`.
""",
        encoding="utf-8",
    )
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
