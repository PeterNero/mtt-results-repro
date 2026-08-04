from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

PREV_IMPORT = ROOT / "certificates" / "routec_first_correction_search_galerkin_import_certificate.json"
SRC_CERT = SM / "certificates" / "selected_routec_correction_source_emission_or_selected_galerkin_values_certificate.json"
SRC_DATA = SM / "candidate_data" / "selected_routec_correction_source_emission_or_selected_galerkin_values.candidate.json"

OUT_CERT = ROOT / "certificates" / "routec_correction_source_emission_import_certificate.json"
OUT_PACKET = ROOT / "candidate_data" / "routec_correction_source_emission_import.packet.json"
OUT_NOTE = ROOT / "proof_corpus" / "RouteC_Correction_Source_Emission_Import_v1.md"

STATUS = "ROUTEC_CORRECTION_SOURCE_EMISSION_IMPORTED_SPLITTER_NOT_EMITTED_CONTRACT_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    prev = load(PREV_IMPORT)
    src_cert = load(SRC_CERT)
    src = load(SRC_DATA)

    emission = src["source_emission_attempt"]
    payload = src["selected_payload_audit"]
    source = src["source_origin_alpha1_audit"]
    galerkin = src["selected_galerkin_values_audit"]
    contract = src["source_emission_contract"]

    emitted_flags = [
        emitted
        for sector in emission["label_emission_search"].values()
        for emitted in sector["emitted_by_selected_inputs"].values()
    ]

    closed_now = {
        "previous_first_correction_search_imported": prev["theorem"]["proved"],
        "source_theorem_proved": src["theorem"]["proved"],
        "representative_splitter_nonemission_checked": src_cert["what_closes"][
            "representative_splitter_nonemission_checked"
        ],
        "selected_payload_slots_rechecked": src_cert["what_closes"]["selected_payload_slots_rechecked"],
        "honest_vs_formal_galerkin_promotion_rechecked": src_cert["what_closes"][
            "honest_vs_formal_galerkin_promotion_rechecked"
        ],
        "exact_source_emission_contract_built": src_cert["what_closes"][
            "exact_source_emission_contract_built"
        ],
        "target_fitting_excluded": src_cert["what_closes"]["target_fitting_excluded"],
    }

    emission_checks = {
        "source_emission_attempted": emission["attempted"] is True,
        "diagnostic_splitter_found": emission["diagnostic_splitter_found"] is True,
        "diagnostic_splitter_not_selected": emission["diagnostic_splitter_selected_by_mtt"] is False,
        "diagnostic_splitter_promotion_not_allowed": emission["diagnostic_splitter_promotion_allowed"] is False,
        "selected_source_does_not_emit_splitter": emission["selected_source_emits_splitter"] is False,
        "no_representative_label_emitted": emission["any_representative_label_emitted_by_selected_inputs"]
        is False
        and not any(emitted_flags),
    }

    payload_checks = {
        "support_shapes_present": payload["all_support_shapes_present"] is True,
        "selected_payload_flags_not_all_true": payload["all_selected_payload_flags_true"] is False,
        "selected_deltaTheta_C1_missing": payload["selected_deltaTheta_C1_solution_present"] is False,
        "sector_response_matrices_missing": payload["sector_response_matrices_present"] is False,
        "primitive_contractions_missing": payload["primitive_contractions_present"] is False,
        "selected_values_not_emitted": payload["selected_values_emitted"] is False,
    }

    source_galerkin_checks = {
        "source_support_converges": source["support_converges"] is True,
        "source_flags_not_all_true": source["all_source_flags_true"] is False,
        "alpha1_values_absent": source["all_alpha1_values_present"] is False,
        "galerkin_manifest_filled": galerkin["manifest_filled"] is True,
        "galerkin_honest_root_not_all_pass": galerkin["honest_root_all_pass"] is False,
        "galerkin_selected_corrections_not_emitted": galerkin["selected_correction_matrices_emitted"] is False,
        "formal_lift_diagnostic_only": galerkin["formal_lift_is_diagnostic_only"] is True,
        "formal_lift_not_promotable_as_proof": galerkin["formal_lift_promotable_as_proof"] is False,
    }

    contract_checks = {
        "contract_name_locked": contract["name"] == "RouteCSelectedSplitterSourceEmissionContract",
        "contract_requires_selected_deltaTheta_or_equivalent": contract["minimum_acceptance_tests"][
            "selected_deltaTheta_C1_or_equivalent_present"
        ]
        is True,
        "contract_requires_sector_response_matrices": contract["minimum_acceptance_tests"][
            "sector_response_matrices_M_u_M_d_M_e_M_nuD_present"
        ]
        is True,
        "contract_requires_unlifted_source_flags": contract["minimum_acceptance_tests"][
            "selected_source_flags_not_lifted"
        ]
        is True,
        "contract_forbids_target_fitting": contract["minimum_acceptance_tests"]["target_fitting_used"] is False,
    }

    open_gate_checks = {
        "closure_not_claimed": src["closure_claimed"] is False,
        "target_fitting_not_used": src["target_fitting_used"] is False,
        "next_artifact_is_deltaTheta_solve": src["next_required_artifact"] == NEXT_ARTIFACT,
    }

    still_open_checks = {key: value is True for key, value in src["what_remains_open"].items()}

    theorem = {
        "name": "RouteCCorrectionSourceEmissionImportTheorem",
        "proved": all(closed_now.values())
        and all(emission_checks.values())
        and all(payload_checks.values())
        and all(source_galerkin_checks.values())
        and all(contract_checks.values())
        and all(open_gate_checks.values())
        and all(still_open_checks.values()),
        "statement": (
            "The imported source-emission audit proves that the diagnostic "
            "qutrit/Weyl splitter is not emitted by current selected Route-C, "
            "Phi_fin, source-origin, alpha1, or honest Galerkin payloads. It "
            "therefore closes the non-emission audit and reduces the next proof "
            "to a selected source-emission contract: provide selected deltaTheta_C1 "
            "or equivalent correction source, selected dotD/alpha1/Hessian/primitive "
            "data, and sector response matrices, then rerun locked mass, mixing, "
            "and CP tests without target fitting."
        ),
    }

    verdict = {
        "diagnostic_splitter_source_emitted": False,
        "selected_values_emitted": False,
        "honest_galerkin_values_promoted": False,
        "source_emission_contract_built": True,
        "observed_flavor_data_used": False,
        "next_required_artifact": NEXT_ARTIFACT,
    }

    packet = {
        "theorem": theorem,
        "source_status": src["status"],
        "closed_now": closed_now,
        "emission_checks": emission_checks,
        "payload_checks": payload_checks,
        "source_galerkin_checks": source_galerkin_checks,
        "contract_checks": contract_checks,
        "open_gate_checks": open_gate_checks,
        "still_open_checks": still_open_checks,
        "source_emission_attempt": emission,
        "selected_payload_audit": payload,
        "source_origin_alpha1_audit": source,
        "selected_galerkin_values_audit": galerkin,
        "source_emission_contract": contract,
        "what_remains_open": src["what_remains_open"],
        "verdict": verdict,
    }

    note = """# Route-C Correction Source Emission Import v1

## Result

The diagnostic qutrit/Weyl splitter is not source-emitted by the current
selected artifacts.

The selected Phi_fin alpha1 payload, selected source-origin/alpha1 driver, and
honest Route-C Galerkin first-run stack do not emit selected correction
matrices, selected `deltaTheta_C1`, selected sector response matrices, or
selected Galerkin values.

## Contract

The next proof must provide one same-branch selected emission route:

```text
selected deltaTheta_C1 or equivalent selected correction source
selected dotD_alpha1
selected lower Hessian/source blocks
selected zero-mode bases
selected primitive C1 contractions
sector response matrices M_u, M_d, M_e, M_nuD
```

After those exist, the locked finite tests remain:

```text
nonzero traceless Hermitian mass splitting
nonzero CKM and PMNS commutator norms
nonzero complex CP-odd invariant
no observed flavor targets or lifted flags as proof data
```

## Status

```text
ROUTEC_CORRECTION_SOURCE_EMISSION_IMPORTED_SPLITTER_NOT_EMITTED_CONTRACT_OPEN
```

The next required artifact is:

```text
MTT_Selected_RouteC_Splitter_Source_Emission_Contract_or_Selected_DeltaTheta_C1_Solve_v1
```
"""

    OUT_PACKET.write_text(json.dumps(packet, indent=2), encoding="utf-8")
    OUT_CERT.write_text(
        json.dumps(
            {
                "program": "MTT protospinor GR response proof",
                "certificate": "routec_correction_source_emission_import",
                "status": STATUS,
                "input_certificates": {
                    "routec_first_correction_search_galerkin_import": str(PREV_IMPORT),
                    "selected_routec_correction_source_emission_or_selected_galerkin_values": str(SRC_CERT),
                },
                "theorem": theorem,
                "closed_now": closed_now,
                "emission_checks": emission_checks,
                "payload_checks": payload_checks,
                "source_galerkin_checks": source_galerkin_checks,
                "contract_checks": contract_checks,
                "open_gate_checks": open_gate_checks,
                "still_open_checks": still_open_checks,
                "verdict": verdict,
                "packet_written": str(OUT_PACKET),
                "note_written": str(OUT_NOTE),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_PACKET}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
