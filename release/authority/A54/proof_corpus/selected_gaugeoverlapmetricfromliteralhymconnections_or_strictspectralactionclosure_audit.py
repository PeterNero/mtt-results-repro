from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_gaugeoverlapmetricfromliteralhymconnections_or_strictspectralactionclosure"
STATUS = "MTT_SELECTED_LITERAL_HYM_SU2_CONNECTION_CLOSED_GAUGE_KINETIC_FUNCTIONALS_OPEN_TWO_RATIO_IDENTIFIABILITY_NOT_CLOSED"
NEXT = "MTT_Selected_CircleNilConnectionsAndCommonSchemeGaugeKineticFunctionalPayload_or_StrictSpectralActionClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "gauge_overlap_identifiability_and_source_contract.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    template = load(ROOT / "candidate_data" / SLUG / "literal_hym_sector_norm_payload.template.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_GaugeOverlapMetricFromLiteralHYMConnections_or_StrictSpectralActionClosure_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(all(packet["checks"].values()), "source-rank checks failed")
    require(cert["normalized_sector_functionals_emitted"] == 0, "unsupported kinetic norm promoted")
    require(cert["selected_SU2_literal_HYM_connection_closed"] is True, "SU2 connection lost")
    require(cert["selected_SU2_literal_gauge_kinetic_norm_closed"] is False, "connection promoted to kinetic norm")
    require(cert["independent_overlap_ratios_emitted"] == 0, "unsupported ratio promoted")
    require(cert["single_response_insufficient_for_two_ratios"] is True, "rank no-go failed")
    require(cert["canonical_completions_rejected"] is True, "canonical completion promoted")
    require(cert["strict_spectral_action_closed"] is False, "strict closure overclaimed")
    require(cert["new_continuous_parameters"] == 0, "new parameter introduced")
    require(set(packet["identifiability"]["missing_independent_sector_rows"]) == {"U1_circle", "SU3_nil"}, "missing rows changed")
    require(all(not row["accepted"] for row in template["rows"].values()), "empty source row accepted")
    for phrase in ["1/3", "0/3", "0/2", "rank", "U1_circle", "SU3_nil", "does not", NEXT]:
        require(phrase.lower() in note.lower(), f"note missing: {phrase}")

    print(json.dumps(cert, indent=2, sort_keys=True))
    print("literal HYM gauge-overlap source-rank audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
