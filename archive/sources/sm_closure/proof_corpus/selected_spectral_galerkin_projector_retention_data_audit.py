"""Audit the selected spectral Galerkin/projector-retention data artifact."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "candidate_data" / "selected_spectral_galerkin_projector_retention_data.candidate.json"
CERT = REPO / "certificates" / "selected_spectral_galerkin_projector_retention_data_certificate.json"
NOTE = REPO / "proof_corpus" / "MTT_Selected_Spectral_Galerkin_Projector_Retention_Data_v1.md"


def check(name: str, condition: bool, detail: object) -> tuple[str, bool, object]:
    return name, condition, detail


def main() -> int:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    audit = data["two_layer_projector_audit"]
    block = audit["block_projector_layer"]
    spectral = audit["spectral_projector_layer"]
    contract = data["selected_solve_contract"]
    open_items = data["what_remains_open"]

    checks = [
        check(
            "status",
            data["status"] == "MTT_SELECTED_SPECTRAL_GALERKIN_PROJECTOR_RETENTION_DATA_REDUCED_TO_SELECTED_ROUTEC_GALERKIN_SOLVE",
            data["status"],
        ),
        check("certificate agreement", cert["status"] == data["status"], cert),
        check(
            "superset contract reduction",
            data["superset_mode"]["classification"] == "SUPERSET_REPAIR_CONTRACT_REDUCTION"
            and data["superset_mode"]["superset_repair"]["repair_object"] == "SelectedRouteCStromingerGalerkinResidualSolve",
            data["superset_mode"],
        ),
        check(
            "no target fitting",
            data["target_fitting_used"] is False
            and cert["target_fitting_used"] is False
            and data["superset_mode"]["diagnostic_backfit_only"]["used"] is False,
            data["superset_mode"]["diagnostic_backfit_only"],
        ),
        check(
            "block projectors closed",
            block["selected_S3_flat_Deligne_class"] is True
            and block["smooth_Freed_Witten_cancellation"] is True
            and block["block_family_Higgs_projector_retention"] is True,
            block,
        ),
        check(
            "spectral projectors still open",
            audit["layer_separation_honest"] is True
            and spectral["coherent_spectral_zero_mode_projector_retention"] is False
            and open_items["coherent_spectral_projector_retention"] is True,
            spectral,
        ),
        check("corpus support imported", all(data["corpus_support"].values()), data["corpus_support"]),
        check(
            "routec support but selected flags open",
            data["routec_operator_support"]["DE_boundary_shapes_present"] is True
            and data["routec_operator_support"]["Green_operator_and_gap_shapes_present"] is True
            and data["routec_operator_support"]["dotD_horizontal_shapes_present"] is True
            and data["routec_operator_support"]["selected_flags_all_false"] is True,
            data["routec_operator_support"],
        ),
        check(
            "monad role disciplined",
            data["monad_role_discipline"]["monad_can_seed_matter_zero_modes"] is True
            and data["monad_role_discipline"]["monad_cannot_be_visible_alpha1_source"] is True,
            data["monad_role_discipline"],
        ),
        check(
            "selected solve contract complete",
            contract["name"] == "SelectedRouteCStromingerGalerkinResidualSolve"
            and "spectral gap separation for each sector operator" in contract["equations"]
            and "selected_source_verified true for route residual, D_E, Riesz/Green, and dotD slots" in contract["acceptance"],
            contract,
        ),
        check(
            "closure not claimed",
            cert["closure_claimed"] is False and cert["what_remains_open"]["full_SM_or_no_knob_closure"] is True,
            cert,
        ),
        check(
            "next artifact",
            data["next_required_artifact"] == "MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1"
            and cert["primary_next_artifact"] == data["next_required_artifact"],
            cert,
        ),
        check(
            "note records two layers",
            "Block-sector projector retention is closed" in note
            and "Coherent spectral zero-mode projector retention remains open" in note
            and "Next artifact: `MTT_Selected_RouteC_Strominger_Galerkin_Solve_Spec_v1`" in note,
            NOTE,
        ),
    ]

    failed = False
    for name, condition, detail in checks:
        status = "PASS" if condition else "FAIL"
        print(f"{status}: {name} -- {detail}")
        if not condition:
            failed = True
    print("\nMTT selected spectral Galerkin/projector-retention data audit")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
