from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_nativegaugeactiontofinitebimodule_or_directgenerativesmbaseclosure"
STATUS = "MTT_SELECTED_NATIVE_GAUGE_ACTION_EXTENDED_TO_96D_REAL_EVEN_FINITE_BIMODULE_ORDER_ZERO_AND_ONE_CLOSED_PHYSICAL_DF_AND_DUALITY_OPEN"
NEXT = "MTT_Selected_PhysicalFiniteDiracOperatorAndIntersectionForm_or_FullFiniteTripleClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "native_gauge_action_finite_bimodule.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_NativeGaugeActionToFiniteBimodule_or_DirectGenerativeSMBaseClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require(cert["finite_algebra_representation_closed"] is True, "finite representation open")
    require(cert["particle_antiparticle_bimodule_dimension"] == 96, "bimodule dimension changed")
    require(cert["KO6_real_even_structure_closed"] is True, "KO6 structure open")
    require(cert["order_zero_closed"] is True, "order zero open")
    require(cert["structural_order_one_closed"] is True, "order one open")
    for key in ["physical_selected_DF_entries_closed", "orientability_closed", "Poincare_duality_closed", "full_finite_Connes_triple_closed"]:
        require(cert[key] is False, f"overclosed: {key}")
    require(packet["epistemic_policy"]["unit_incidence_coefficients_count_as_parameters"] is False, "incidence witnesses counted as parameters")
    require(packet["epistemic_policy"]["physical_Yukawa_magnitudes_claimed"] is False, "physical D_F overclaimed")
    require(max(packet["residuals"].values()) < 1e-12, "finite axiom residual failed")
    for phrase in ["96", "Exact Axiom Checks", "unit incidence witnesses", "add no parameters", "remaining full-finite-triple objects", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("native gauge action to finite bimodule audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
