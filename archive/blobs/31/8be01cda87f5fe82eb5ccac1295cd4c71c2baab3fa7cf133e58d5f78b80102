"""Build bottom/charm/tau formula import or R_theta mass-scheme derivation artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bottomcharmtauformulaimport_or_rthetamassschemederivation"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SOURCE_FAMILIES = PACKET_DIR / "external_bct_formula_source_families.packet.json"
ROW_ATTEMPT = PACKET_DIR / "bottom_charm_tau_formula_row_acceptance_attempt.packet.json"
RTHETA_GAP = PACKET_DIR / "rtheta_bct_mass_scheme_derivation_gap.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_bct_formula_source_import.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BottomCharmTauFormulaImport_or_RThetaMassSchemeDerivation_v1.md"

PREVIOUS = DATA / "selected_bottomcharmtaumaps_or_rthetathresholdderivation.candidate.json"
INVENTORY = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_native_residual_inventory.packet.json"
)
FILL_ATTEMPT = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_map_row_fill_attempt.packet.json"
)
RTHETA_RECHECK = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "rtheta_bottom_charm_tau_projection_recheck.packet.json"
)
IMPORT_CONTRACT = (
    DATA
    / "selected_bottomcharmtaumaps_or_rthetathresholdderivation"
    / "bottom_charm_tau_external_map_import_contract.packet.json"
)

STATUS = (
    "MTT_SELECTED_BOTTOMCHARMTAUFORMULAIMPORT_OR_RTHETAMASSSCHEMEDERIVATION_"
    "BUILT_FORMULA_FAMILIES_IMPORTED_ROWS_OPEN"
)
NEXT = "MTT_Selected_BottomCharmTauRunDecReplay_or_RThetaMassSchemeRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing b/c/tau formula import sources: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, INVENTORY, FILL_ATTEMPT, RTHETA_RECHECK, IMPORT_CONTRACT]
    require_sources(sources)

    previous = load(PREVIOUS)
    inventory = load(INVENTORY)
    fill_attempt = load(FILL_ATTEMPT)
    rtheta_recheck = load(RTHETA_RECHECK)
    import_contract = load(IMPORT_CONTRACT)

    formula_sources = [
        {
            "id": "RunDec-original",
            "role": "QCD running and decoupling formula implementation source for quark masses",
            "accepted_for": ["bottom_MSbar_native_scale_transport", "charm_MSbar_native_scale_transport"],
            "citation": "Chetyrkin, Kuehn, Steinhauser, RunDec: a Mathematica package for running and decoupling of the strong coupling and quark masses",
            "url": "https://arxiv.org/abs/hep-ph/0004189",
            "accepted_as_formula_family": True,
        },
        {
            "id": "CRunDec",
            "role": "C++ implementation of RunDec formulae for running/decoupling and mass scheme transformations",
            "accepted_for": ["bottom_MSbar_native_scale_transport", "charm_MSbar_native_scale_transport"],
            "citation": "Schmidt and Steinhauser, CRunDec: a C++ package for running and decoupling of the strong coupling and quark masses",
            "url": "https://arxiv.org/abs/1201.6149",
            "accepted_as_formula_family": True,
        },
        {
            "id": "RunDec-v3",
            "role": "updated RunDec/CRunDec formula implementation source including higher-loop running/decoupling support",
            "accepted_for": ["bottom_MSbar_native_scale_transport", "charm_MSbar_native_scale_transport"],
            "citation": "Herren and Steinhauser, Version 3 of RunDec and CRunDec",
            "url": "https://arxiv.org/abs/1703.03751",
            "accepted_as_formula_family": True,
        },
        {
            "id": "PDG-quark-masses",
            "role": "MSbar quark-mass scheme and native-scale convention source",
            "accepted_for": ["bottom_MSbar_native_scale_transport", "charm_MSbar_native_scale_transport"],
            "citation": "Particle Data Group review of quark masses",
            "url": "https://pdg.lbl.gov/2023/reviews/rpp2023-rev-quark-masses.pdf",
            "accepted_as_formula_family": True,
        },
        {
            "id": "Huang-Zhou-running-fermion-masses",
            "role": "external running quark/lepton mass table/formula provenance family for b/c/tau values at representative scales",
            "accepted_for": [
                "bottom_MSbar_native_scale_transport",
                "charm_MSbar_native_scale_transport",
                "tau_pole_rest_to_running_lepton",
            ],
            "citation": "Huang and Zhou, Precise Values of Running Quark and Lepton Masses in the Standard Model",
            "url": "https://arxiv.org/abs/2009.04851",
            "accepted_as_formula_family": True,
        },
        {
            "id": "Xing-Zhang-Zhou-running-masses",
            "role": "external running quark and charged-lepton mass table provenance family",
            "accepted_for": [
                "bottom_MSbar_native_scale_transport",
                "charm_MSbar_native_scale_transport",
                "tau_pole_rest_to_running_lepton",
            ],
            "citation": "Xing, Zhang, Zhou, Updated Values of Running Quark and Lepton Masses",
            "url": "https://arxiv.org/abs/0712.1419",
            "accepted_as_formula_family": True,
        },
    ]
    source_families = {
        "schema": "MTTExternalBCTFormulaSourceFamilies.v1",
        "status": "BOTTOM_CHARM_TAU_EXTERNAL_FORMULA_SOURCE_FAMILIES_IMPORTED",
        "import_contract_source": rel(IMPORT_CONTRACT),
        "formula_sources": formula_sources,
        "accepted_formula_family_count": sum(1 for source in formula_sources if source["accepted_as_formula_family"]),
        "bottom_charm_quark_running_formula_family_closed": True,
        "tau_running_table_formula_family_closed": True,
        "machine_replay_or_table_values_imported": False,
        "accepted_map_rows_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SOURCE_FAMILIES, source_families)

    row_requirements = []
    for row in fill_attempt["required_maps"]:
        row_requirements.append(
            {
                "id": row["id"],
                "policy_requirement": row["policy_requirement"],
                "formula_family_available": True,
                "native_residual_inventory_available": inventory["inventory_closed"],
                "versioned_replay_values_imported": False,
                "accepted_as_external_map_row": False,
                "accepted_as_Rtheta_source_row": False,
                "blocking_reason": (
                    "Formula provenance family is imported, but no versioned RunDec/table replay "
                    "has emitted this row with uncertainty sidecars."
                ),
            }
        )
    row_attempt = {
        "schema": "MTTBottomCharmTauFormulaRowAcceptanceAttempt.v1",
        "status": "FORMULA_FAMILIES_AVAILABLE_NO_BCT_ROWS_ACCEPTED",
        "source_families_source": rel(SOURCE_FAMILIES),
        "inventory_source": rel(INVENTORY),
        "row_requirements": row_requirements,
        "accepted_bottom_charm_tau_map_rows": [],
        "accepted_bottom_charm_tau_map_row_count": 0,
        "formula_family_import_closes_rows": False,
        "residual_rows_are_source_rows": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(ROW_ATTEMPT, row_attempt)

    rtheta_gap = {
        "schema": "MTTRThetaBCTMassSchemeDerivationGap.v1",
        "status": "FORMULA_FAMILIES_IMPORTED_SELECTED_RTHETA_DERIVATION_OPEN",
        "rtheta_recheck_source": rel(RTHETA_RECHECK),
        "precoefficient_skeletons_present": rtheta_recheck["precoefficient_skeletons_present"],
        "selected_Rtheta_mass_scheme_derivation_closed": rtheta_recheck[
            "selected_Rtheta_mass_scheme_derivation_closed"
        ],
        "minimal_internal_missing_object": rtheta_recheck["minimal_internal_missing_object"],
        "formula_families_may_validate_Rtheta": True,
        "formula_families_select_Rtheta": False,
        "what_Rtheta_must_still_derive": [
            "selected Route-C/Strominger Galerkin residual solve",
            "coherent spectral zero-mode projector retention",
            "bottom/charm/tau mass-scheme map rows from selected projection data",
            "basis map from selected rows to external running-mass formula coordinates",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(RTHETA_GAP, rtheta_gap)

    cutset = {
        "schema": "MTTNextCutsetAfterBCTFormulaSourceImport.v1",
        "status": "NEXT_ATTACK_RUNDEC_REPLAY_OR_RTHETA_MASS_SCHEME_ROWS",
        "closed_now": {
            "external_formula_source_families_imported": True,
            "bottom_charm_quark_running_formula_family": True,
            "tau_running_table_formula_family": True,
            "formula_import_nonselector_gap": True,
        },
        "still_open": {
            "versioned_RunDec_or_table_replay_values": True,
            "accepted_bottom_charm_tau_map_rows": True,
            "selected_Rtheta_mass_scheme_derivation": True,
            "W_Z_H_electroweak_matching_rows": True,
            "full_covariance_profile_likelihood": True,
            "true_SM_equivalence": True,
            "full_no_knob": True,
        },
        "recommended_next": {
            "artifact": NEXT,
            "route_A": "implement or import a versioned RunDec/CRunDec replay for b and c masses plus a tau running table/formula replay",
            "route_B": "derive the b/c/tau rows from selected Rtheta projection data",
            "route_C": "import published running fermion mass tables as external validation rows with sidecars",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedBottomCharmTauFormulaImportOrRThetaMassSchemeDerivation",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "external_bct_formula_source_families": rel(SOURCE_FAMILIES),
            "bottom_charm_tau_formula_row_acceptance_attempt": rel(ROW_ATTEMPT),
            "rtheta_bct_mass_scheme_derivation_gap": rel(RTHETA_GAP),
            "next_cutset_after_bct_formula_source_import": rel(CUTSET),
        },
        "theorem": {
            "name": "BottomCharmTauFormulaSourceFamilyImportTheorem",
            "proved": True,
            "statement": (
                "External formula/provenance families sufficient to define the b/c quark running problem "
                "and tau running-table problem can be imported without selecting the MTT branch. This closes "
                "the source-family layer but not the map rows: no versioned RunDec/table replay has emitted "
                "b/c/tau values with sidecars, and the selected Rtheta mass-scheme derivation remains open."
            ),
        },
        "what_closes_now": cutset["closed_now"],
        "what_remains_open": cutset["still_open"],
        "closure_decision": {
            "external_formula_source_families_imported": True,
            "bottom_charm_quark_running_formula_family_closed": True,
            "tau_running_table_formula_family_closed": True,
            "accepted_bottom_charm_tau_map_row_count": 0,
            "accepted_bottom_charm_tau_map_rows_closed": False,
            "versioned_RunDec_or_table_replay_values_closed": False,
            "selected_Rtheta_mass_scheme_derivation_closed": False,
            "W_Z_H_electroweak_matching_rows_closed": False,
            "full_covariance_profile_likelihood_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_BottomCharmTauFormulaImport_or_RThetaMassSchemeDerivation_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "external_formula_source_families_imported": True,
        "accepted_bottom_charm_tau_map_row_count": 0,
        "next_required_artifact": NEXT,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected BottomCharmTauFormulaImport or RThetaMassSchemeDerivation v1

Status: `{STATUS}`.

This artifact imports the external formula/provenance families for b/c/tau map
rows.

```text
external formula source families imported : true
b/c quark running family closed           : true
tau running table/formula family closed   : true
accepted b/c/tau map rows                 : 0
selected Rtheta derivation closed         : false
```

The useful gain is provenance.  RunDec/CRunDec and running fermion-mass table
families are now accepted as formula sources for future replay, but they do not
emit rows by themselves and do not select the MTT branch.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
