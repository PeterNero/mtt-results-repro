from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonquarkorder_sharedcirclekineticoperator_or_exactresidualspectrum"
STATUS = "MTT_SELECTED_COMMON_TWO_COST_OPERATOR_CONSTRUCTED_CONDITIONALLY_ONELOOP_TRANSPORT_NOGO_PROVED_EXACT_RESIDUAL_SOURCE_OPEN"
NEXT = "MTT_Selected_ResidualCircleLensCostOperator_or_ExactGaugeKineticValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    operator = load(ROOT / "candidate_data" / SLUG / "conditional_common_projected_kinetic_operator.packet.json")
    rg_nogo = load(ROOT / "candidate_data" / SLUG / "one_loop_scale_transport_nogo.packet.json")
    correction = load(ROOT / "candidate_data" / SLUG / "exact_residual_cost_spectrum.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_CommonQuarkOrder_SharedCircleKineticOperator_or_ExactResidualSpectrum_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == correction["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(operator["finite_operator"]["strictly_positive"], "positivity")
    check(operator["finite_operator"]["gauge_commutant"], "gauge commutation")
    check(not operator["gauge_execution"]["exact_match"], "false exactness")
    check(rg_nogo["span_determinant_nonzero"], "transport no-go")
    check(rg_nogo["least_squares"]["residual_l2"] > 1e-5, "transport residual")
    check(not correction["epistemic_status"]["accepted_as_source"], "residual overclaim")
    check(not cert["strict_source_closed"], "source overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    check(cert["new_continuous_parameters"] == 0, "parameters")
    for phrase in ["Explicit common operator", "Scale-transport no-go", "Exact residual spectrum", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("common quark-order/shared-circle kinetic operator audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
