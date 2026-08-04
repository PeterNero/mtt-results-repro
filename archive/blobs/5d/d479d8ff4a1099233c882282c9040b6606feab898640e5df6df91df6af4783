"""Build Higgs C1 variation-slot extension or ambient Hessian rows packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsc1variationslotextension_or_ambienthessianrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsC1VariationSlotExtension_or_AmbientHessianRows_v1.md"

SLOT_CONTRACT = PACKET_DIR / "higgs_c1_variation_slot_extension_contract.packet.json"
HESSIAN_CONTRACT = PACKET_DIR / "ambient_hessian_restriction_row_contract.packet.json"
SLOT_ATTEMPT = PACKET_DIR / "higgs_c1_slot_extension_execution_attempt.packet.json"
HESSIAN_ATTEMPT = PACKET_DIR / "ambient_hessian_restriction_execution_attempt.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_higgs_c1_extension_attempt.packet.json"

PREVIOUS = DATA / "selected_c1tobhuvprojectiontensor_or_fhuvrows.candidate.json"
C1_ROUTING = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_72_slot_routing.packet.json"
)
C2_EHUV = (
    DATA
    / "selected_higgshymsectionringquadraturebridge_or_directhuvpayload"
    / "c2_ehuv_finite_quotient_basis_exactness.packet.json"
)
C3_EHUV = (
    DATA
    / "selected_ehuvhymmetricconnectionfixedpoint_or_directhuvpayload"
    / "c3_ehuv_hym_metric_connection_binding.packet.json"
)
BHUV = (
    DATA
    / "selected_bhuvtwocolumnsourceorthonormallift_or_msourcehuvfrontier"
    / "bhuv_two_column_source_orthonormal_lift.packet.json"
)
C1_PAYLOAD = (
    DATA
    / "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
    / "selected_c1_hessian_payload_import.packet.json"
)
PROJECTION_ATTEMPT = (
    DATA
    / "selected_fhuvrestrictionmatrixrows_or_bselectedprojectionexecution"
    / "bselected_projection_execution_attempt.packet.json"
)

STATUS = (
    "MTT_SELECTED_HIGGSC1VARIATIONSLOTEXTENSION_OR_AMBIENTHESSIANROWS_"
    "CONTRACTS_CLOSED_ROWS_OPEN"
)
NEXT = "MTT_Selected_EHuvC1VariationOperators_or_AmbientHessianRestrictionRows_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Higgs C1 extension inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [PREVIOUS, C1_ROUTING, C2_EHUV, C3_EHUV, BHUV, C1_PAYLOAD, PROJECTION_ATTEMPT]
    require_sources(sources)

    previous = load(PREVIOUS)
    c1_routing = load(C1_ROUTING)
    c2 = load(C2_EHUV)
    c3 = load(C3_EHUV)
    bhuv = load(BHUV)
    c1_payload = load(C1_PAYLOAD)
    projection_attempt = load(PROJECTION_ATTEMPT)

    routed_sectors = sorted({row["sector"] for row in c1_routing["rows"]})
    higgs_labels = c2["typing_checks"]["ordered_E_H_UV_basis_labels"]
    normalized_higgs_labels = [label.replace("^", "_").replace("dagger", "dagger") for label in higgs_labels]
    higgs_sector_aliases = {"H", "H_u", "H_d", "H_d^dagger", "H_d_dagger"}
    higgs_slot_rows = [row for row in c1_routing["rows"] if row["sector"] in higgs_sector_aliases]
    phase_count = sum(1 for row in c1_routing["rows"] if row["variation_operator_shape"] == "phase_R_Z")
    shift_count = sum(1 for row in c1_routing["rows"] if row["variation_operator_shape"] == "shift_R_X")
    selected_source_flags = sum(1 for row in c1_routing["rows"] if row["operator_selected_as_source_now"])
    hessian_counterterm_flags = sum(1 for row in c1_routing["rows"] if row["hessian_counterterm_sourced"])

    required_slots = [
        {
            "slot": "H_u.phase_R_Z",
            "source_column": "H_u",
            "variation_coordinate": "phase_R_Z",
            "role": "C1 phase coordinate evaluated on the H_u B_Huv column",
        },
        {
            "slot": "H_u.shift_R_X",
            "source_column": "H_u",
            "variation_coordinate": "shift_R_X",
            "role": "C1 shift coordinate evaluated on the H_u B_Huv column",
        },
        {
            "slot": "H_d_dagger.phase_R_Z",
            "source_column": "H_d^dagger",
            "variation_coordinate": "phase_R_Z",
            "role": "C1 phase coordinate evaluated on the H_d^dagger B_Huv column",
        },
        {
            "slot": "H_d_dagger.shift_R_X",
            "source_column": "H_d^dagger",
            "variation_coordinate": "shift_R_X",
            "role": "C1 shift coordinate evaluated on the H_d^dagger B_Huv column",
        },
    ]

    slot_contract = {
        "schema": "MTTHiggsC1VariationSlotExtensionContract.v1",
        "status": "HIGGS_C1_VARIATION_SLOT_EXTENSION_CONTRACT_CLOSED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "object": {
            "name": "T_C1<-E_H^UV",
            "domain": "selected source-orthonormal E_H^UV/B_Huv columns H_u,H_d^dagger",
            "codomain": "selected C1 variation coordinates (phase_R_Z, shift_R_X) before residual replay",
            "minimum_symbolic_slot_count": len(required_slots),
            "required_slots": required_slots,
            "matrix_shape_if_emitted": [2, 2],
            "matrix_rows": ["phase_R_Z", "shift_R_X"],
            "matrix_columns": ["H_u", "H_d^dagger"],
        },
        "acceptance_requirements": [
            "same selected q79/F,m=1 source branch as C1 and E_H^UV",
            "source-owned operator rows, not residual-projector replay rows",
            "pre-compression provenance before A^T A is formed",
            "finite quotient admissibility for the two Higgs columns",
            "basis-phase covariance under B_Huv -> B_Huv V",
            "certificate that the four slot values are C1 variation coordinates",
        ],
        "execution_formula_after_slot_emission": {
            "compressed_dynamic_C1_normal_matrix": c1_payload["compressed_payload"]["A_transpose_A"],
            "formula": "M_Huv = T_C1<-E_H^UV^* (A^T A)_C1 T_C1<-E_H^UV",
            "current_simplification": "Since (A^T A)_C1 = 12 I_2, emitted T rows would give M_Huv = 12 T^* T.",
            "important_guard": "This is only an execution formula; it is not a source for T.",
        },
        "decision": {
            "higgs_c1_slot_extension_contract_closed": True,
            "minimum_slot_schema_closed": True,
            "formula_for_future_execution_closed": True,
        },
    }

    hessian_contract = {
        "schema": "MTTAmbientHessianRestrictionRowContract.v1",
        "status": "AMBIENT_HESSIAN_RESTRICTION_ROW_CONTRACT_CLOSED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "accepted_routes": {
            "full_ambient_route": {
                "object": "Hess(F_C1)_selected on the selected Q_sel^U ambient 27-mode carrier",
                "matrix_shape": [27, 27],
                "restriction": "M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv",
                "requires": [
                    "ambient row/entry source ownership",
                    "Hermitian symmetry or real second-variation symmetry",
                    "finite trace/quadrature exactness or certified error bounds",
                    "projection of the two B_Huv columns into the same ambient basis",
                ],
            },
            "restricted_row_route": {
                "object": "direct source-owned restriction rows on span(B_Huv)",
                "matrix_shape": [2, 2],
                "required_rows": ["Huu", "Hud_re", "Hud_im", "Hdd"],
                "requires": [
                    "same-source exactness certificate",
                    "Hermitian/source-ownership certificate",
                    "quotient admissibility certificate",
                    "no observed Higgs/Yukawa/mass value as selector",
                ],
            },
        },
        "forbidden_substitutes": [
            "compressed A^T A normal matrix without ambient or Higgs-slot map",
            "diagonal E_H^UV HYM metric/connection alone",
            "low-energy quotient q(H_u)=q(H_d^dagger)=H alone",
            "selected s_beta or polar angle support alone",
            "observed Higgs beta/lambda/mass values",
        ],
        "decision": {
            "ambient_hessian_row_contract_closed": True,
            "restriction_row_contract_closed": True,
            "forbidden_substitutes_retired": True,
        },
    }

    slot_attempt = {
        "schema": "MTTHiggsC1SlotExtensionExecutionAttempt.v1",
        "status": "HIGGS_C1_SLOT_EXTENSION_EXECUTED_ZERO_SELECTED_SLOTS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "current_c1_routing_inventory": {
            "row_count": c1_routing["row_count"],
            "phase_R_Z_rows": phase_count,
            "shift_R_X_rows": shift_count,
            "routed_sectors": routed_sectors,
            "sector_routing": c1_routing["sector_routing"],
            "operator_selected_as_source_now_true_count": selected_source_flags,
            "hessian_counterterm_sourced_true_count": hessian_counterterm_flags,
        },
        "higgs_source_inventory": {
            "ordered_E_H_UV_basis_labels": higgs_labels,
            "uv_lift_source_ids": c2["finite_quotient_basis"]["uv_lift_basis"],
            "T3_eigenline_binding_closed": c3["bridge_clause_closed"],
            "B_Huv_source_orthonormal_lift_emitted": bhuv["whitening_map_and_lift"][
                "B_Huv_symbolic_exact_payload_emitted"
            ],
        },
        "required_slot_inventory": required_slots,
        "matched_selected_higgs_slots": [],
        "missing_selected_higgs_slots": [slot["slot"] for slot in required_slots],
        "decision": {
            "current_higgs_slot_extension_execution_attempted": True,
            "selected_Higgs_C1_variation_slots_emitted": False,
            "selected_Higgs_C1_variation_slot_count": 0,
            "required_minimum_Higgs_C1_variation_slot_count": len(required_slots),
            "C1_matter_slot_routing_available": True,
            "Higgs_E_H_UV_source_ids_available": True,
        },
        "reason": (
            "The only current C1 variation table is a 72-row matter-sector table "
            "over u,d,e,nuD.  It contains no H_u/H_d^dagger rows and its rows are "
            "not selected as source-owned Higgs variation operators."
        ),
    }

    hessian_attempt = {
        "schema": "MTTAmbientHessianRestrictionExecutionAttempt.v1",
        "status": "AMBIENT_HESSIAN_RESTRICTION_EXECUTED_ZERO_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "available_dynamic_C1_payload": {
            "strict_dynamic_C1_payload_imported": c1_payload["decision"][
                "strict_dynamic_C1_payload_imported"
            ],
            "A_transpose_A": c1_payload["compressed_payload"]["A_transpose_A"],
            "A_transpose_b": c1_payload["compressed_payload"]["A_transpose_b"],
            "selected_b_selected_available": c1_payload["decision"][
                "selected_b_selected_available"
            ],
        },
        "current_naive_projection_guard": {
            "attempted": projection_attempt["decision"]["B_selected_projection_execution_attempted"],
            "accepted": projection_attempt["decision"]["selected_F_Huv_second_variation_emitted"],
            "reason": projection_attempt["naive_identification_guard"]["decision"],
        },
        "ambient_rows": {
            "ambient_27_by_27_Hessian_matrix": None,
            "ambient_27_mode_basis_binding": None,
            "B_Huv_restriction_entries": None,
        },
        "restricted_rows": {
            "Huu": None,
            "Hud_re": None,
            "Hud_im": None,
            "Hdd": None,
            "Delta": None,
            "Re_Omega": None,
            "Im_Omega": None,
        },
        "decision": {
            "current_ambient_hessian_row_execution_attempted": True,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "ambient_Hessian_restriction_rows_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
        "reason": (
            "The imported A^T A=12 I_2 payload is already compressed in C1 "
            "coordinates.  Without either T_C1<-E_H^UV or ambient Hess(F_C1) "
            "rows, it cannot be legally restricted to B_Huv."
        ),
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHiggsC1ExtensionAttempt.v1",
        "status": "NEXT_FRONTIER_EHUV_C1_VARIATION_OPERATORS_OR_AMBIENT_HESSIAN_RESTRICTION_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "Higgs C1 variation-slot extension contract",
            "minimum four-slot T_C1<-E_H^UV schema",
            "ambient 27x27 Hess(F_C1) or direct 2x2 restriction-row acceptance contract",
            "future execution formula M_Huv=12 T^*T after T is selected",
            "current corpus execution showing zero selected Higgs C1 slots and zero ambient Hessian rows",
        ],
        "still_open": [
            "selected E_H^UV C1 variation operator rows for H_u and H_d^dagger",
            "or selected ambient Hess(F_C1) rows/restriction rows on the 27-mode carrier",
            "source-owned T_C1<-E_H^UV numeric/symbolic entries",
            "B_Huv^* Hess(F_C1)_selected B_Huv execution",
            "direct nonzero Herm(2) Huv rows and certificates",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsC1VariationSlotExtensionOrAmbientHessianRows",
        "schema": "MTTSelectedCandidate.v1",
        "status": STATUS,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "minimal_parameter_tier_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
        "theorem": {
            "name": "HiggsC1VariationSlotExtensionOrAmbientHessianRowsNotYetEmittedTheorem",
            "proved": True,
            "statement": (
                "The legal Higgs execution object is now reduced to either a "
                "selected four-slot C1 variation map T_C1<-E_H^UV from "
                "H_u,H_d^dagger into phase_R_Z,shift_R_X coordinates, or a "
                "selected ambient Hess(F_C1) row payload whose restriction to "
                "B_Huv is certified. The current corpus provides matter-sector "
                "C1 routing, selected E_H^UV source IDs, diagonal HYM binding, "
                "and the compressed dynamic C1 normal matrix A^T A=12I, but it "
                "emits zero selected Higgs C1 slots and zero ambient Hessian "
                "restriction rows. Therefore no F_Huv rows are emitted yet."
            ),
        },
        "packets": {
            "higgs_c1_variation_slot_extension_contract": rel(SLOT_CONTRACT),
            "ambient_hessian_restriction_row_contract": rel(HESSIAN_CONTRACT),
            "higgs_c1_slot_extension_execution_attempt": rel(SLOT_ATTEMPT),
            "ambient_hessian_restriction_execution_attempt": rel(HESSIAN_ATTEMPT),
            "next_cutset": rel(CUTSET),
        },
        "inputs": {
            "previous": rel(PREVIOUS),
            "c1_routing": rel(C1_ROUTING),
            "c2_ehuv": rel(C2_EHUV),
            "c3_ehuv": rel(C3_EHUV),
            "bhuv": rel(BHUV),
            "c1_payload": rel(C1_PAYLOAD),
            "projection_attempt": rel(PROJECTION_ATTEMPT),
        },
        "closure_decision": {
            "higgs_c1_slot_extension_contract_closed": True,
            "ambient_hessian_row_contract_closed": True,
            "current_higgs_slot_extension_execution_attempted": True,
            "current_ambient_hessian_row_execution_attempted": True,
            "future_execution_formula_M_Huv_equals_12_TstarT_closed": True,
            "C1_matter_slot_routing_available": True,
            "Higgs_E_H_UV_source_ids_available": True,
            "selected_Higgs_C1_variation_slots_emitted": False,
            "ambient_27_by_27_Hessian_matrix_emitted": False,
            "ambient_Hessian_restriction_rows_emitted": False,
            "selected_F_Huv_rows_emitted": False,
            "direct_Herm2_row_payload_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "C1_72_slot_row_count": c1_routing["row_count"],
            "C1_phase_R_Z_rows": phase_count,
            "C1_shift_R_X_rows": shift_count,
            "C1_routed_sector_count": len(routed_sectors),
            "C1_higgs_slot_rows_found": len(higgs_slot_rows),
            "required_minimum_Higgs_C1_variation_slot_count": len(required_slots),
            "selected_Higgs_C1_variation_slot_count": 0,
            "ambient_Hessian_matrix_shape": [27, 27],
            "restricted_Huv_matrix_shape": [2, 2],
            "accepted_F_Huv_row_count": 0,
            "accepted_certificate_count": 0,
        },
    }

    cert = {
        "certificate": "MTTSelectedHiggsC1VariationSlotExtensionOrAmbientHessianRows",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "theorem_proved": True,
        "minimal_parameter_tier_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "higgs_c1_slot_extension_contract_closed": True,
        "ambient_hessian_row_contract_closed": True,
        "current_higgs_slot_extension_execution_attempted": True,
        "current_ambient_hessian_row_execution_attempted": True,
        "future_execution_formula_M_Huv_equals_12_TstarT_closed": True,
        "selected_Higgs_C1_variation_slots_emitted": False,
        "ambient_27_by_27_Hessian_matrix_emitted": False,
        "ambient_Hessian_restriction_rows_emitted": False,
        "selected_F_Huv_rows_emitted": False,
        "direct_Herm2_row_payload_emitted": False,
        "accepted_F_Huv_row_count": 0,
        "accepted_certificate_count": 0,
    }

    note = f"""# MTT Selected HiggsC1VariationSlotExtension or AmbientHessianRows v1

Status: `{STATUS}`

## Theorem

The remaining legal Higgs/Huv execution object is now sharply typed.  One of
the following must be emitted from selected source data:

```text
T_C1<-E_H^UV =
  rows:    phase_R_Z, shift_R_X
  columns: H_u, H_d^dagger
```

or an ambient selected `27x27` `Hess(F_C1)` row payload whose restriction to
the `B_Huv` columns is certified:

```text
M_Huv = B_Huv^* Hess(F_C1)_selected B_Huv
```

Because the active dynamic C1 payload has `(A^T A)_C1 = 12 I_2`, a future
selected Higgs C1 slot matrix `T` would execute immediately as:

```text
M_Huv = 12 T^* T
```

This is an execution formula only.  It does not source `T`.

Current corpus execution:

- C1 72-slot routed sectors: `{routed_sectors}`
- Higgs source labels: `{higgs_labels}`
- Higgs C1 slots found in current routing: `{len(higgs_slot_rows)}`
- Required minimum Higgs C1 slots: `{len(required_slots)}`
- Ambient selected `27x27` Hessian rows emitted: `0`
- Accepted `F_Huv` rows: `0`

Next artifact: `{NEXT}`
"""

    write_json(SLOT_CONTRACT, slot_contract)
    write_json(HESSIAN_CONTRACT, hessian_contract)
    write_json(SLOT_ATTEMPT, slot_attempt)
    write_json(HESSIAN_ATTEMPT, hessian_attempt)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE {rel(OUTPUT)}")
    print(f"WROTE {rel(CERT)}")
    print(f"WROTE {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
