from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem"
STATUS = "MTT_SELECTED_TYPED_FAMILY_DIAGONAL_CHIRAL_SM_REPRESENTATION_AND_ANOMALY_TABLE_CLOSED_LOW_ENERGY_BRANCH_SELECTION_PREMISE_EXPOSED"
NEXT = "MTT_Selected_NativeFlagToE6SMChiralModuleCompatibilityAndUnimodularityTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "typed_family_gauge_carrier_and_anomaly_table.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_TypedFamilyGaugeCarrierAndDiagonalSMRepresentationTheorem_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(packet["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem failed")
    require((cert["one_family_dimension"], cert["three_family_dimension"]) == (16, 48), "carrier dimensions changed")
    require(cert["family_preserving_chiral_carrier_closed"] is True, "typed carrier open")
    require(cert["family_diagonal_gauge_action_closed"] is True, "family-diagonal action open")
    require(cert["local_anomaly_rows_cancel_exactly"] is True, "local anomaly failed")
    require(cert["Witten_SU2_anomaly_absent"] is True, "Witten anomaly failed")
    require(cert["selected_bundle_E6_and_three_27_source_closed"] is True, "bundle-derived E6 source hidden")
    require(cert["exact_branching_dictionary_closed"] is True, "exact branching dictionary reopened")
    require(cert["physical_low_energy_branch_selector_exposed"] is True, "physical branch selector hidden")
    require(cert["full_Connes_finite_triple_closed"] is False, "full finite triple overclosed")
    require(cert["native_unique_branching_and_unimodularity_closed"] is False, "native branching overclosed")
    require(packet["source_provenance"]["observed_SM_values_used"] is False, "observed values entered selection")
    require(len(packet["typed_carrier"]["left_Weyl_representation_rows"]) == 6, "representation rows missing")
    require(all(row["cancelled"] for row in packet["anomaly_table"].values()), "anomaly table not closed")
    for phrase in ["partly done before", "H_chiral", "48", "same family-preserving representation packet", "genuinely bundle-derived", "discrete physical selector", NEXT]:
        require(phrase in note, f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("typed family-gauge representation and anomaly audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
