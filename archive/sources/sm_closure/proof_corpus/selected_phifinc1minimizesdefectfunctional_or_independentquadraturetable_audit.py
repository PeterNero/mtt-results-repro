"""Audit PhiFinC1 minimization / independent quadrature table gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1minimizesdefectfunctional_or_independentquadraturetable"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
MINIMIZER_BINDING = PACKET_DIR / "phifinc1_minimizer_binding_reduction.packet.json"
QUADRATURE_TEMPLATE = PACKET_DIR / "independent_quadrature_table_template.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1MinimizesDefectFunctional_or_IndependentQuadratureTable_v1.md"
PAPER_DRAFT = ROOT / "proof_corpus" / "paper_appendix_drafts" / "selected_source" / "theta_execution_flavor__i10_phifinc1_minimizes_c1_defect_functional.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHIFINC1MINIMIZESDEFECTFUNCTIONAL_OR_INDEPENDENTQUADRATURETABLE_BUILT_BINDING_REDUCTION_OPEN"
NEXT = "MTT_Selected_MinimizerTraceC1PayloadTheorem_or_QuadratureTableValues_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    binding = load(MINIMIZER_BINDING)
    quadrature = load(QUADRATURE_TEMPLATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    draft = PAPER_DRAFT.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(NEXT in note, "note missing next artifact")

    require(binding["status"] == "REDUCED_TO_MINIMIZER_TRACE_AND_C1_RESPONSE_THEOREM_SLOTS", "binding status mismatch")
    slots = binding["existing_source_theorem_slots"]
    require(slots["I1_selected_strominger_minimizer_to_phifin_trace"]["status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN", "I1 status mismatch")
    require(slots["I5_dotD_alpha1_and_C1_response"]["status"] == "APPENDIX_DRAFT_PROOF_SLOT_OPEN", "I5 status mismatch")
    new_slot = binding["new_binding_theorem_slot"]
    require(new_slot["id"] == "I10_phifinc1_minimizes_c1_defect_functional", "I10 id mismatch")
    require(len(new_slot["dependencies"]) == 3, "I10 dependencies mismatch")
    require(new_slot["draft_path"].endswith("theta_execution_flavor__i10_phifinc1_minimizes_c1_defect_functional.md"), "I10 draft path mismatch")
    require(binding["would_close_if_proved"]["SM_parity_dynamic_packet_closes"] is True, "I10 sufficiency missing")
    require(binding["proved_now"] is False, "I10 overproved")
    require(len(binding["why_not_proved_now"]) == 3, "why-not-proved mismatch")

    require(quadrature["status"] == "TEMPLATE_READY_VALUES_EMPTY", "quadrature status mismatch")
    require(len(quadrature["required_values"]) == 6, "required values mismatch")
    require(quadrature["values_filled_now"] is False, "quadrature values overfilled")
    require(quadrature["would_close_if_filled"]["honest_independent_Galerkin_C1_closes"] is True, "quadrature sufficiency missing")
    require("copying b_selected from the patched replay" in quadrature["forbidden_shortcuts"], "forbidden shortcut missing")
    require("Theorem Slot I10" in draft, "draft missing theorem slot")
    require("target residuals" in draft, "draft missing guardrail")

    for key in [
        "physical_application_reduced_to_existing_minimizer_trace_stack",
        "new_I10_binding_theorem_slot_created",
        "independent_quadrature_table_template_created",
        "sufficiency_of_I10_or_quadrature_table_preserved",
        "observed_constants_excluded_as_selectors",
    ]:
        require(data["what_closes_now"][key] is True, f"close flag missing: {key}")
    for key in [
        "prove_I1_selected_minimizer_to_PhiFin_trace",
        "prove_I5_selected_dotD_C1_response",
        "prove_I10_PhiFinC1_minimizes_defect_functional",
        "fill_independent_quadrature_table_values",
        "unpatched_SM_parity_dynamic_packet_closure",
        "true_SM_equivalence_closure",
    ]:
        require(data["what_remains_open"][key] is True, f"remaining gate missing: {key}")
    decision = data["promotion_decision"]
    require(decision["PhiFinC1_minimizes_defect_functional_proved"] is False, "PhiFinC1 overproved")
    require(decision["independent_quadrature_table_values_filled"] is False, "quadrature overfilled")
    require(decision["unpatched_SM_parity_dynamic_packet_closed"] is False, "unpatched closure overclaimed")
    require(data["closure_claimed"] is False, "global closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched theorem overclaimed")
    require(data["observed_data_used"] is False and data["target_fitting_used"] is False, "data guardrail violated")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem missing")
    require("I10 theorem slot created" in note, "note missing summary")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
