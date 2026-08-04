"""Audit finite projected HYM source principle / finite cutoff exactness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ALGEBRA = PACKET_DIR / "finite_projected_algebra_and_spectral_package.packet.json"
OPERATIONS = PACKET_DIR / "projected_hym_operations_exactness.packet.json"
EXACTNESS = PACKET_DIR / "finite_source_exactness_theorem.packet.json"
HSCALAR = PACKET_DIR / "h_scalar_functional_remaining_contract.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteProjectedHYMSourcePrinciple_or_BandlimitExactnessProof_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_FINITEPROJECTEDHYMSOURCEPRINCIPLE_OR_BANDLIMITEXACTNESSPROOF_"
    "FINITE_SOURCE_EXACTNESS_CLOSED_HSCALAR_FUNCTIONAL_OPEN"
)
NEXT = "MTT_Selected_HScalarFunctionalOnFiniteProjectedHYMAlgebra_or_HalfDensitySourceRule_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    algebra = load(ALGEBRA)
    operations = load(OPERATIONS)
    exactness = load(EXACTNESS)
    hscalar = load(HSCALAR)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("algebra", algebra),
        ("operations", operations),
        ("exactness", exactness),
        ("hscalar", hscalar),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    source = algebra["source_algebra"]
    require(source["algebra_vector_rank"] == 27, "algebra rank")
    require(source["hilbert_dimension"] == 27, "hilbert dimension")
    require(algebra["closed_here"]["A_N_source_algebra"] is True, "A_N not closed")
    require(algebra["closed_here"]["Tr_N_normalized_trace"] is True, "trace not closed")

    ops = operations["operations"]
    for name in ["P_N", "star_N", "exp_N", "Delta_N", "Green_N", "D_N_or_commutator"]:
        require(ops[name]["exact_in_finite_source"] is True, f"{name} exactness")
    require(
        operations["automatic_finite_cutoff_exactness"]["closed_for_selected_finite_source_object"] is True,
        "finite exactness",
    )
    require(
        operations["automatic_finite_cutoff_exactness"]["closed_for_unprojected_continuum_object"] is False,
        "continuum overclaim",
    )

    require(exactness["proved"] is True, "exactness theorem")
    require(exactness["exactness_scope"]["A_N_finite_source"] is True, "A_N exactness scope")
    require(exactness["exactness_scope"]["unprojected_continuum_HYM"] is False, "continuum exactness overclaim")
    require(exactness["accepted_value_source_rows"] == 0, "value row overclaim")

    require(hscalar["accepted_H_scalar_source_rows"] == 0, "H scalar overclaim")
    require("HScalarFunctionalOnFiniteProjectedHYMAlgebra" == hscalar["remaining_source_rule"]["name"], "H rule")
    require(data["closure_decision"]["finite_projected_HYM_source_principle_closed"] is True, "principle")
    require(data["closure_decision"]["automatic_finite_cutoff_exactness_for_A_N_closed"] is True, "A_N exactness")
    require(data["closure_decision"]["H_scalar_functional_on_A_N_closed"] is False, "H functional overclosed")
    require(data["closure_decision"]["accepted_H_scalar_source_rows"] == 0, "accepted rows")

    for phrase in [
        "FiniteProjectedHYMSourceExactnessTheorem",
        "A_N = C^3_class tensor M_3(C)_qutrit-left",
        "cutoff calculation is exact because it is an identity inside `A_N`",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: finite projected HYM source exactness is closed; "
        "H scalar half-density source rule remains open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
