"""Audit selected sector zero-mode / End0 tensor-product construction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.py"
CANDIDATE = ROOT / "candidate_data" / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct.candidate.json"
CERT = ROOT / "certificates" / "selected_sector_zero_mode_realization_functor_or_end0_tensorproduct_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorZeroMode_Realization_Functor_or_End0TensorProduct_Construction_v1.md"

STATUS = "MTT_SELECTED_END0_TENSOR_PRODUCT_CARRIER_CONSTRUCTED_ZERO_MODE_REALIZATION_OPEN"
NEXT = "MTT_Selected_SectorZeroMode_AdjointTriplet_Realization_or_MatterSlotRouting_Theorem_v1"


def check(name: str, condition: bool, detail: object) -> bool:
    print(("PASS" if condition else "FAIL") + f": {name} -- {detail}")
    return condition


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    carrier = data["constructed_End0_tensor_product_carrier"]
    validation = data["validation"]
    decision = data["decision"]
    boundary = data["selected_realization_boundary"]

    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, data["status"]),
        check("certificate paths", cert["candidate_path"].endswith(CANDIDATE.name), cert),
        check(
            "sector order and dimensions",
            carrier["sector_order"] == ["Q", "u", "d", "L", "e", "N", "H"]
            and carrier["sector_dimensions"] == {"Q": 3, "u": 3, "d": 3, "L": 3, "e": 3, "N": 3, "H": 1}
            and carrier["total_dimension"] == 19,
            carrier["sector_dimensions"],
        ),
        check(
            "End0 domain basis",
            carrier["selected_domain_basis"] == ["T1", "T2", "T3"]
            and carrier["domain_ad_matrices"]["T3"] == [[0, -1, 0], [1, 0, 0], [0, 0, 0]],
            carrier["domain_ad_matrices"],
        ),
        check(
            "lie algebra and projectors",
            validation["all_lie_checks_pass"] is True
            and validation["projectors_sum_to_identity"] is True
            and validation["all_projectors_idempotent"] is True
            and validation["all_projectors_commute_with_End0_action"] is True
            and validation["all_distinct_projectors_orthogonal"] is True,
            validation,
        ),
        check(
            "sector T3 pattern",
            validation["matter_T3_norms_equal"] is True
            and validation["H_T3_response_zero"] is True
            and all(
                validation["sector_T3_response_norms"][sector]["rank"] == 3
                for sector in ["Q", "u", "d", "L", "e", "N"]
            )
            and validation["sector_T3_response_norms"]["H"]["rank"] == 1,
            validation["sector_T3_response_norms"],
        ),
        check(
            "rank match",
            data["rank_match"]["matches_expected_sector_kernel_rank_sum"] is True
            and data["rank_match"]["direct_sum_total_rank"] == 19,
            data["rank_match"],
        ),
        check(
            "normalization still open",
            data["normalization_boundary"]["physical_transfer_normalization_selected"] is False,
            data["normalization_boundary"],
        ),
        check(
            "routing still open",
            data["matter_slot_routing_boundary"]["selected_Z_to_u_e_X_to_d_nuD_routing"] is False
            and data["matter_slot_routing_boundary"]["selected_1M_singlet_rule"] is False,
            data["matter_slot_routing_boundary"],
        ),
        check(
            "selected realization still open",
            boundary["selected_sector_zero_mode_realization_proved"] is False
            and boundary["selected_family_triplets_equal_End0_adjoint_representation"] is False
            and boundary["selected_Higgs_singlet_under_End0"] is False,
            boundary,
        ),
        check(
            "decision honest",
            decision["End0_tensor_product_carrier_constructed"] is True
            and decision["sector_projectors_constructed"] is True
            and decision["commutator_and_projector_checks_pass"] is True
            and decision["selected_sector_zero_mode_realization_extracted"] is False
            and decision["selected_transfer_normalization_extracted"] is False
            and decision["selected_matter_slot_routing_extracted"] is False
            and decision["physical_dotD_alpha1_payload_extracted"] is False
            and decision["next_required_artifact"] == NEXT,
            decision,
        ),
        check(
            "no closure or target fitting",
            data["closure_claimed"] is False
            and data["target_fitting_used"] is False
            and cert["closure_claimed"] is False
            and cert["target_fitting_used"] is False,
            {"data": data["closure_claimed"], "cert": cert["closure_claimed"]},
        ),
        check(
            "note records boundary",
            "universal End0 tensor-product carrier is constructed" in note
            and "This is not yet physical sector closure" in note
            and f"Next artifact: `{NEXT}`" in note,
            NOTE,
        ),
    ]

    print("\nMTT selected sector zero-mode / End0 tensor-product construction audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
