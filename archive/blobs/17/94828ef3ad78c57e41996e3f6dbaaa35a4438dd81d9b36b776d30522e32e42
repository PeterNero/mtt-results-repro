"""Audit local RG benchmark values and local-QFT observable functor interface."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_externalrgbenchmarkvalues_or_localqftobservablefunctor"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
BENCH = PACKET_DIR / "independent_local_rg_benchmark_values.packet.json"
FUNCTOR = PACKET_DIR / "local_qft_observable_functor_interface.packet.json"
UPDATED = PACKET_DIR / "updated_true_equivalence_blocker_matrix.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ExternalRGBenchmarkValues_or_LocalQFTObservableFunctor_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_EXTERNALRGBENCHMARKVALUES_OR_LOCALQFTOBSERVABLEFUNCTOR_BUILT_LOCAL_BENCHMARK_AND_FUNCTOR_INTERFACE"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bench = load(BENCH)
    functor = load(FUNCTOR)
    updated = load(UPDATED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")

    require(bench["passes_local_benchmark"] is True, "local benchmark failed")
    require(bench["max_delta_to_accepted"] <= bench["acceptance_tolerance"], "benchmark tolerance failure")
    require(math.isfinite(bench["max_delta_to_accepted"]), "nonfinite benchmark delta")
    require(bench["closes"]["independent_local_rg_benchmark_values"] is True, "local benchmark not closed")
    require(bench["closes"]["external_literature_rg_benchmark_values"] is False, "external benchmark overclaimed")
    require(bench["closes"]["precision_threshold_values"] is False, "threshold values overclaimed")
    require(bench["closes"]["pole_to_running_maps"] is False, "pole-running maps overclaimed")

    require(functor["acceptance_tests"]["functor_signature_declared"] is True, "functor signature missing")
    require(functor["acceptance_tests"]["source_vs_measured_boundary_preserved"] is True, "source boundary missing")
    require(functor["acceptance_tests"]["renormalization_metadata_required"] is True, "renormalization metadata missing")
    require(functor["acceptance_tests"]["benchmark_correlators_not_source_data"] is True, "correlator guard missing")
    require(functor["acceptance_tests"]["actual_correlator_values_filled"] is False, "correlator values overclaimed")
    require(functor["acceptance_tests"]["local_QFT_observable_functor_values_closed"] is False, "QFT values overclaimed")
    require(functor["functor"]["name"] == "Obs_SM^MTT", "functor name mismatch")
    require(len(functor["functor"]["arrows"]) >= 5, "functor arrows incomplete")

    require("independent local RG benchmark values" in updated["closed_now"], "updated matrix missing benchmark closure")
    require("local QFT observable functor interface" in updated["closed_now"], "updated matrix missing functor closure")
    for blocker in [
        "external literature RG benchmark values",
        "precision threshold and pole-to-running maps",
        "full covariance/profile likelihood values",
        "local QFT observable values/correlator replay",
        "QM/GR measurement and response interfaces",
        "actual selected Qa/SU3 operator packet replacing parity-interface replacement",
    ]:
        require(blocker in updated["remaining_true_equivalence_blockers"], f"missing blocker: {blocker}")
    require(updated["still_open_guardrails"]["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(updated["still_open_guardrails"]["no_knob_closed"] is False, "no-knob overclaimed")

    for key in [
        "independent_local_rg_benchmark_values_filled",
        "local_qft_observable_functor_interface_built",
        "true_equivalence_blocker_matrix_updated",
        "superset_strategy_preserved",
    ]:
        require(data["what_closes_now"][key] is True, f"missing close flag: {key}")
    require(data["closure_decision"]["SM_parity_closed"] is True, "SM parity flag mismatch")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclaimed")
    require(data["closure_decision"]["no_knob_closed"] is False, "candidate no-knob overclaimed")
    require(cert["local_rg_benchmark_passes"] is True, "cert local benchmark flag mismatch")
    require(cert["local_qft_functor_interface_built"] is True, "cert functor flag mismatch")

    for packet in [bench, functor, updated, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("superset move" in note, "note missing superset method")
    require("external literature RG benchmark values" in note, "note missing external benchmark guard")
    require(cert["next_required_artifact"] == "MTT_Selected_ThresholdCovarianceValues_or_QMGRInterface_v1", "next artifact mismatch")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
