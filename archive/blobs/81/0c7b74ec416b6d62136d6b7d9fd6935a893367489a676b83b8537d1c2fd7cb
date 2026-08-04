"""Audit the electroweak no-knob bridge status after rho_UV closure."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
NOTE = REPO / "proof_corpus" / "Electroweak_No_Knob_Bridge_Audit_v1.md"
CERT = REPO / "certificates" / "electroweak_no_knob_bridge_audit_certificate.json"
RHO_CERT = REPO / "certificates" / "final_internal_rho_uv_selected_radius_theorem_certificate.json"
RHO_NOTE = REPO / "proof_corpus" / "Final_Internal_Rho_UV_Selected_Radius_Theorem_v1.md"
PRIMITIVE_NOTE = REPO / "proof_corpus" / "Primitive_Constant_Discipline_for_No_Knob_Program_v1.md"
THRESHOLD_NOTE = REPO / "proof_corpus" / "Execution_I_Threshold_Profile_Structural_Certificate_v1.md"

Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
THETA_V = Q79 / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md"
ROADMAP = Q79 / "A_Tiered_Roadmap_for_Calculations_in_Modal_Triplet_Theory__MTT__v2.md"
TOPOLOGY = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\13 Standard Model & Topology-Only Constraints\Topology__Only_Constraints_in_Modal_Triplet_Theory.md"
)
HETEROTIC = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings"
    r"\Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def check(name: str, ok: bool, detail: object = "") -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    rho_cert = json.loads(read(RHO_CERT))
    note = read(NOTE)
    rho_note = read(RHO_NOTE)
    primitive = read(PRIMITIVE_NOTE)
    threshold = read(THRESHOLD_NOTE)
    theta = read(THETA_V)
    roadmap = read(ROADMAP)
    topology = read(TOPOLOGY)
    heterotic = read(HETEROTIC)

    gates = cert["gates"]
    verdict = cert["verdict"]

    checks = [
        check(
            "certificate status",
            cert["status"] == "ELECTROWEAK_BRIDGE_FORMULATED_RHO_UV_LINK_OPEN",
            cert["status"],
        ),
        check(
            "rho internal theorem closed",
            rho_cert["status"] == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED"
            and abs(rho_cert["selected_values"]["rho_UV"] - cert["closed_internal_input"]["rho_UV"]) < 1e-15,
            rho_cert["selected_values"],
        ),
        check(
            "note imports rho values",
            contains_all(note, ["R_*     = 4.440528182269818", "rho_UV  = 0.164530397543639"]),
            "selected values",
        ),
        check(
            "rho theorem remains internal",
            contains_all(rho_note, ["electroweak prediction", "dimensionful SI constant"]),
            "no overclaim text",
        ),
        check(
            "Theta V ratio source",
            contains_all(theta, ["g_1", "g_2", "I_2(\\Theta)", "I_1(\\Theta)"]),
            "Theta overlap ratios",
        ),
        check(
            "Theta V conditional inputs",
            contains_all(theta, ["G_F", "m_W", "\\Delta r_{\\mathrm{eff}}", "0.23120"]),
            "weak-angle numerical path",
        ),
        check(
            "Theta V admits non-circular gate",
            contains_all(theta, ["requires computing", "internally", "\\sin^2\\theta_W(M_Z)"]),
            "internal g1/g2 requirement",
        ),
        check(
            "roadmap has structural electroweak identity",
            contains_all(roadmap, ["\\sin^2\\theta_W = 3/8", "Calibrate $K$ using one gauge coupling"]),
            "roadmap electroweak/gauge normalization",
        ),
        check(
            "topology-only SM support",
            contains_all(topology, ["exact Standard--Model hypercharges", "SU(2) Witten", "Anomaly cancellation"]),
            "topology support",
        ),
        check(
            "heterotic gauge kinetic route",
            contains_all(heterotic, ["g^{-2}=\\mathrm{Re}\\,S", "threshold corrections", "one-loop thresholds"]),
            "f=S and thresholds open",
        ),
        check(
            "threshold import forbidden",
            gates["old_threshold_import"]["classification"] == "FORBIDDEN_SYMBOL_COLLISION"
            and "without fitting the target threshold profile" in threshold
            and "rho_UV with Delta r_eff" in "identify rho_UV with Delta r_eff without a source-certified kernel",
            gates["old_threshold_import"],
        ),
        check(
            "primitive discipline applied",
            contains_all(primitive, ["Universality", "Prior selection", "Predictive surplus"])
            and gates["gauge_absolute_normalization"]["classification"] == "PRIMITIVE_OR_OPEN",
            "primitive-or-open normalization",
        ),
        check(
            "bridge remains open",
            verdict["electroweak_no_knob_closed"] is False
            and verdict["rho_uv_bridge_to_electroweak_closed"] is False
            and gates["rho_uv_to_electroweak_threshold"]["classification"] == "OPEN_NO_SOURCE_BRIDGE",
            verdict,
        ),
        check(
            "next theorem named",
            verdict["next_required_theorem"] == "Selected Electroweak Threshold Kernel Theorem"
            and "Selected Electroweak Threshold Kernel Theorem" in note,
            verdict["next_required_theorem"],
        ),
    ]

    print("\nElectroweak no-knob bridge audit")
    print("================================")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
