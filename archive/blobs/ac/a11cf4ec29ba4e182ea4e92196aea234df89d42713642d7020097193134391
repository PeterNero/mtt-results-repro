"""Audit primitive-class C1 observable / higher-order response import."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_import.candidate.json"
CERT = ROOT / "certificates" / "primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission_import_certificate.json"
NOTE = ROOT / "proof_corpus" / "PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_Import_v1.md"
BUILDER = ROOT / "scripts" / "import_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.py"

STATUS = "PRIMITIVECLASS_C1OBSERVABLE_IMPORTED_HIGHERORDER_FULLRESPONSE_VALUES_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveC1Contractions_or_WeylPairSectorRouting_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER), "--write"], cwd=ROOT, check=True)
    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["theorem"]["closure_claimed"] is False, "closure overclaimed")

    for name, value in data["checks"].items():
        require(value is True, f"failed check: {name}")

    obs = data["primitive_class_C1_observable_packet"]
    require(obs["active_shift"] == [1, 1], "active shift mismatch")
    require(obs["fixed_fiber_quotient_class"] == [0, 1, 2], "fiber class mismatch")
    require(obs["all_representatives_scalar_identity"] is True, "scalar identity missing")
    require(obs["flavor_splitting_possible_at_current_layer"] is False, "flavor overclaimed")

    emission = data["higherorder_or_fullresponse_source_emission_packet"]
    require(emission["alpha1_dotD_status"]["active_blocker"] is False, "alpha1 still active")
    require(emission["current_layer_status"]["no_go_proved"] is True, "current no-go missing")
    require(emission["current_layer_status"]["current_values_available"] is False, "values overclaimed")
    require(emission["source_emission_status"]["source_emission_contract_built"] is True, "contract missing")
    require(
        emission["source_emission_status"]["selected_source_emits_splitter"] is False,
        "splitter overpromoted",
    )

    remains = data["what_remains_open"]
    for key in [
        "selected_higher_order_or_full_response_matrices",
        "selected_A_selected",
        "selected_b_selected",
        "selected_deltaTheta_C1_solution",
        "sector_response_matrices_M_u_M_d_M_e_M_nuD",
        "nondegenerate_yukawa_hierarchy",
        "CKM_PMNS_CP_from_selected_matrices",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    guardrails = data["guardrails"]
    require(guardrails["primitive_class_C1_observable_emitted"] is True, "observable not emitted")
    require(guardrails["current_C1_layer_flavor_closure_claimed"] is False, "flavor overclaim")
    require(guardrails["selected_values_available"] is False, "values overclaim")
    require(guardrails["A_selected_claimed"] is False, "A_selected overclaim")
    require(guardrails["b_selected_claimed"] is False, "b_selected overclaim")
    require(guardrails["observed_data_used"] is False, "observed data used")
    require(guardrails["target_fitting_used"] is False, "target fitting used")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
