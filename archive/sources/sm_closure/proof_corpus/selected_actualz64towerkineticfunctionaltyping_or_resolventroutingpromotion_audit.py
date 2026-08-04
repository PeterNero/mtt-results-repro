from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion"
STATUS = "MTT_SELECTED_ACTUAL_Z64_SPECTRUM_COMPUTED_A70_LABEL_SUM_TYPING_REJECTED_NORMALIZED_TRACE_IDENTITY_CONDITIONAL"
NEXT = "MTT_Selected_GaugeKineticFunctionalOfL64AndQ79Chord_or_StrictResidualValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / f"build_{SLUG}.py")], cwd=ROOT, check=True)
    candidate = load(ROOT / "candidate_data" / f"{SLUG}.candidate.json")
    spectrum = load(ROOT / "candidate_data" / SLUG / "actual_z64_tower_spectrum.packet.json")
    typing = load(ROOT / "candidate_data" / SLUG / "a70_resolvent_typing_audit.packet.json")
    trace = load(ROOT / "candidate_data" / SLUG / "normalized_trace_routing_theorem.packet.json")
    functionals = load(ROOT / "candidate_data" / SLUG / "typed_spectral_functional_trials.packet.json")
    cert = load(ROOT / "certificates" / f"{SLUG}_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_ActualZ64TowerKineticFunctionalTyping_or_ResolventRoutingPromotion_v1.md").read_text(encoding="utf-8")

    check(candidate["status"] == cert["status"] == STATUS, "status")
    check(candidate["next_required_artifact"] == cert["next_required_artifact"] == functionals["next_required_artifact"] == NEXT, "next")
    check(all(candidate["checks"].values()), "builder checks")
    check(spectrum["composition_count"] == 16, "tower count")
    check(cert["actual_spectrum"] == [[15, 1], [24, 4], [33, 3], [69, 3], [78, 2], [258, 2], [1023, 1]], "spectrum")
    check(not typing["verdict"]["strict_promotion_allowed"], "typing overclaim")
    check(typing["verdict"]["A70_numerical_candidate_retained"], "candidate lost")
    check(trace["basis_independent"], "trace theorem")
    check(not trace["strict_routing_promoted"], "routing overclaim")
    check(functionals["exact_match_count"] == functionals["accepted_count"] == 0, "functional overclaim")
    check(cert["strict_gauge_values_accepted"] == 0, "strict rows")
    for phrase in ["Actual selected spectrum", "A70 typing result", "What is proved for 31/42", "Typed search", NEXT]:
        check(phrase.lower() in note.lower(), phrase)
    print(json.dumps(cert, indent=2, sort_keys=True))
    print("actual Z64 tower typing audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
