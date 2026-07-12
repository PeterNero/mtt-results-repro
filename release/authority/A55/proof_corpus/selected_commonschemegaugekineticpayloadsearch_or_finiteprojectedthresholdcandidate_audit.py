from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_commonschemegaugekineticpayloadsearch_or_finiteprojectedthresholdcandidate"
STATUS = "MTT_SELECTED_TREE_GAUGE_KINETIC_PAYLOAD_CLOSED_FINITE_THRESHOLD_COMPONENTS_FOUND_COMMON_SCHEME_SUPERTRACE_OPEN"
NEXT = "MTT_Selected_GaugeInsertedHeatSupertraceSecondVariation_or_CommonSchemeThresholdPayload_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    packet = load(ROOT / "candidate_data" / SLUG / "common_scheme_payload_search_and_finite_candidate.packet.json")
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    template = load(ROOT / "candidate_data" / SLUG / "gauge_inserted_heat_supertrace_payload.template.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_CommonSchemeGaugeKineticPayloadSearch_or_FiniteProjectedThresholdCandidate_v1.md").read_text(encoding="utf-8")

    require(packet == candidate, "packet/candidate mismatch")
    require(packet["status"] == cert["status"] == STATUS, "status changed")
    require(packet["next_required_artifact"] == cert["next_required_artifact"] == NEXT, "next changed")
    require(all(packet["checks"].values()), "payload search checks failed")
    require(cert["tree_level_common_scheme_rows_closed"] == 3, "tree payload lost")
    require(cert["threshold_common_scheme_rows_closed"] == 0, "mixed threshold rows promoted")
    require(packet["accepted_tree_level_payload"]["trace_coefficients"] == [6.0, 6.0, 6.0], "tree traces changed")
    require(abs(packet["finite_projected_candidate"]["conditional_logdet_vector"][0] - 29.201650332199108) < 1e-12, "U1 quotient mismatch")
    require(packet["finite_projected_candidate"]["source_factorization_selected"] is False, "conditional factorization promoted")
    require(cert["canonical_response_candidates_rejected"] is True, "failed candidate promoted")
    require(all(not row["accepted"] for row in template["sector_rows"].values()), "empty supertrace row accepted")
    require(cert["strict_spectral_action_closed"] is False, "strict closure overclaimed")
    for phrase in ["(6,6,6)", "(2,2,3)", "not by itself", "different domains", "second variation", NEXT]:
        require(phrase.lower() in note.lower(), f"note missing: {phrase}")
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("common-scheme gauge payload search audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
