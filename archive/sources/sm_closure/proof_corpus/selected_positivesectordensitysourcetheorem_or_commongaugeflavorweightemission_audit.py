from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_positivesectordensitysourcetheorem_or_commongaugeflavorweightemission"
STATUS = "MTT_SELECTED_CONDITIONAL_C1_POSITIVE_DENSITY_CONSTRUCTED_QL_SYMMETRIC_GAUGE_NOGO_PROVED_QL_RESOLVED_SOURCE_OPEN"
NEXT = "MTT_Selected_QuarkLeptonDoubletResolvedPositiveDensitySource_or_KineticWeightEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    density = load(ROOT / "candidate_data" / SLUG / "conditional_c1_positive_sector_density.packet.json")
    nogo = load(ROOT / "candidate_data" / SLUG / "quark_lepton_doublet_symmetry_gauge_nogo.packet.json")
    contract = load(ROOT / "candidate_data" / SLUG / "next_ql_resolved_density_source_contract.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_PositiveSectorDensitySourceTheorem_or_CommonGaugeFlavorWeightEmission_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == contract["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "source checks")
    check(density["positivity"]["all_blocks_positive_semidefinite"], "positivity")
    check(all(abs(value - expected) < 1e-12 for value, expected in zip(cert["right_block_spectrum"], [4, 1, 1])), "spectrum")
    check(all(abs(value - expected) < 1e-12 for value, expected in zip(cert["sector_trace_weights_Q_u_d_L_e_N"], [12, 6, 6, 12, 6, 6])), "traces")
    check(nogo["general_two_class_theorem"]["proved"], "no-go")
    check(cert["QL_symmetric_positive_density_no_go_proved"] and cert["Q_vs_L_source_asymmetry_required"], "frontier")
    check(not cert["strict_density_source_closed"], "strict overclaim")
    check(cert["nonuniversal_gauge_rows_accepted"] == 0, "row overclaim")
    check(not cert["no_knob_gauge_coupling_prediction_closed"], "prediction overclaim")
    check(cert["new_continuous_parameters"] == 0, "parameters")
    for phrase in ["Conditional density constructed", "Exact gauge test", "l > q + 2(u+d)", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("positive sector density theorem audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
