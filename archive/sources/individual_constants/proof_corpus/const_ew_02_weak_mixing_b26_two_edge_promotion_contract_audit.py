"""Audit CONST-EW-02 B26 two-edge weak-mixing promotion contract."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b26_two_edge_promotion_contract"
SCRIPT = ROOT / "scripts" / f"build_{SLUG}.py"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
BASE = ROOT / "candidate_data" / SLUG
GAUGE = BASE / "gaugekinetic_rg_source_contract.packet.json"
C1 = BASE / "primitive_c1_sourcevalue_contract.packet.json"
SYNTHESIS = BASE / "superset_route_synthesis.packet.json"
BOUNDARY = BASE / "weak_mixing_b26_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_B26_TwoEdgePromotionContract_v1.md"

STATUS = "MTT_CONST_EW_02_B26_TWO_EDGE_PROMOTION_CONTRACT_BUILT_VALUES_OPEN"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def clean(packet: dict[str, object], name: str) -> None:
    require(packet["observed_data_used_as_selector"] is False, f"{name} uses observed selector")
    require(packet["target_fitting_used"] is False, f"{name} target fitting")
    require(packet["closure_claimed"] is False, f"{name} overclaims closure")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    require(computed["status"] == STATUS, "builder status mismatch")

    candidate = load(DATA)
    gauge = load(GAUGE)
    c1 = load(C1)
    synthesis = load(SYNTHESIS)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for name, packet in [
        ("candidate", candidate),
        ("gauge", gauge),
        ("c1", c1),
        ("synthesis", synthesis),
        ("boundary", boundary),
    ]:
        clean(packet, name)

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["two_edge_contract_built"] is True, "contract not built")
    require(candidate["theorem"]["proved"] is True, "exclusivity theorem not proved")
    require(candidate["internal_lambda_12_closed_preserved"] is True, "lambda12 not preserved")
    require(candidate["u_dyn_source_derived_preserved"] is True, "u_dyn not preserved")
    require(candidate["K_phys_or_f_ab_closed"] is False, "K_phys overclosed")
    require(candidate["mu_match_closed"] is False, "mu_match overclosed")
    require(candidate["RG_scheme_closed"] is False, "RG overclosed")
    require(candidate["primitive_C1_atoms_emitted"] is False, "primitive C1 overclosed")
    require(candidate["physical_weak_angle_closure"] is False, "physical weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "no-knob overclosed")

    required = gauge["required_source_packet"]
    require(set(required) == {"K_phys_or_gauge_kinetic_matrix", "mu_match", "RG_and_threshold_scheme", "full_threshold_vector"}, "gauge required packet changed")
    require(gauge["decision"]["K_phys_or_f_ab_closed"] is False, "gauge K_phys overclosed")
    require(gauge["decision"]["mu_match_closed"] is False, "gauge mu overclosed")
    require(gauge["decision"]["RG_scheme_closed"] is False, "gauge RG overclosed")
    require(len(gauge["external_refs"]) == 3, "external refs missing")
    require(len(gauge["corpus_refs"]) == 3, "corpus refs missing")
    require(all(ref["value_imported"] is False for ref in gauge["external_refs"]), "external value imported")

    c1_required = c1["required_source_packet"]
    require(c1_required["selected_bases"]["count"] == 12, "selected basis count")
    require(c1_required["primitive_atom_matrices"]["count"] == 24, "atom count")
    require(c1_required["b_and_homogeneous_zero_leaves"]["count"] == 4, "b/zero leaf count")
    require(c1["missing_leaf_count"] == 40, "missing leaf count")
    require(c1["decision"]["primitive_C1_atoms_emitted"] is False, "C1 atoms overclosed")
    require(c1["decision"]["A_selected_computable"] is False, "A overclosed")
    require(c1["decision"]["b_selected_computable"] is False, "b overclosed")

    strategy = synthesis["superset_strategy"]
    require(set(strategy) == {"straight_path", "cross_encoding_path", "universal_parameter_path"}, "superset paths changed")
    require(strategy["universal_parameter_path"]["allowed_by_B23"] is True, "B23 universal lane not imported")
    require("observed weak-angle" in synthesis["exclusivity_theorem"]["statement"], "selector guardrail missing")

    require(boundary["closed_now"]["two_edge_promotion_contract"] is True, "boundary contract not closed")
    require(boundary["still_open"]["K_phys_or_f_ab"] is True, "boundary K missing")
    require(boundary["still_open"]["primitive_C1_atom_values"] is True, "boundary C1 missing")
    require(boundary["guardrails"]["per_observable_retuning"] is False, "retuning guardrail failed")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B27-GAUGEKINETIC-ACTION-ANCHOR-EXECUTION", "next primary label")
    require(next_work["parallel"]["label"] == "CONST-EW-02 / WEAK-MIXING / B27-PRIMITIVE-C1-ATOM-VALUE-EXECUTION", "next parallel label")

    require(cert["status"] == STATUS, "cert status")
    require(cert["exclusivity_theorem_proved"] is True, "cert theorem")
    require(cert["closure_claimed"] is False, "cert closure")
    require("two source-admissible" in note, "note missing two-edge statement")

    print("CONST-EW-02 B26 two-edge promotion contract audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
