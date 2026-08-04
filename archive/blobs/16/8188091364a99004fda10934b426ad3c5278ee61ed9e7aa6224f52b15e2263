"""Audit seven exact q79 symbolic-u2 lines at u1=2 across both spaces."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S5 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space5_symbolic_u2_prefix"
S6 = ROOT / "candidate_data" / "q79_Ronly_u1_002_space6_symbolic_u2_prefix"
EXCEPTION = ROOT / "candidate_data" / "q79_Ronly_u1_002_symbolic_exception_D_closure"
PARENTS = ROOT / "candidate_data" / "q79_Ronly_classfree_representative_lines"
BUILDER = ROOT / "scripts" / "build_q79_Ronly_fixed_u1_u2_symbolic_family.py"
EMITTER = ROOT / "scripts" / "emit_q79_Ronly_symbolic_v_line.py"
TRANSPORT = ROOT / "scripts" / "transport_q79_Ronly_symbolic_u3_basis_to_v.py"
D_VERIFIER = ROOT / "scripts" / "verify_q79_Ronly_symbolic_affine_quadratic_exception_D_unit_general.py"
CERTIFIER = ROOT / "scripts" / "certify_q79_Ronly_u1_002_cross_space_symbolic_prefix_v2.py"
CERTIFICATE = ROOT / "certificates" / "Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v2.json"
THEOREM = Path(__file__).with_name("Q79_Ronly_U1_002_CrossSpace_Symbolic_Prefix_v2.md")
V1_AUDIT = Path(__file__).with_name("q79_Ronly_u1_002_space5_symbolic_u2_prefix_audit.py")
STEM = "space5_class1_u1_002_a_050_symbolic_v"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def packet_without_paths(packet: dict[str, object]) -> dict[str, object]:
    cleaned = json.loads(json.dumps(packet))
    cleaned["parent_input"].pop("path", None)
    for row in cleaned["records"]:
        row["input"].pop("path", None)
    return cleaned


def line_packet_without_paths(packet: dict[str, object]) -> dict[str, object]:
    cleaned = json.loads(json.dumps(packet))
    cleaned["parent_input"].pop("path", None)
    cleaned["output"].pop("path", None)
    return cleaned


def transport_semantics(packet: dict[str, object]) -> dict[str, object]:
    artifacts = packet.get("artifacts", {})
    hashes = {
        key: value.get("sha256")
        for key, value in artifacts.items()
        if key != "target_input_packet"
    }
    return {
        "schema": packet.get("schema"),
        "status": packet.get("status"),
        "field": packet.get("field"),
        "canonical_a": packet.get("canonical_a"),
        "coordinate_isomorphism": packet.get("coordinate_isomorphism"),
        "artifact_hashes": hashes,
        "quotient": packet.get("quotient"),
        "checks": packet.get("checks"),
        "theorem": packet.get("theorem"),
        "claim_boundary": packet.get("claim_boundary"),
        "new_continuous_fit_parameters": packet.get("new_continuous_fit_parameters"),
    }


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def main() -> None:
    required = [
        BUILDER, EMITTER, TRANSPORT, D_VERIFIER, CERTIFIER, CERTIFICATE,
        THEOREM, V1_AUDIT, S5 / "family.packet.json", S6 / "family.packet.json",
    ]
    required.extend(
        S6 / "inputs" / f"space6_u1_002_u2_{u2:03d}.msolve.in"
        for u2 in range(1, 101)
    )
    required.extend(
        [
            S6 / "inputs" / "space6_u1_002_u2_001.msolve.out",
            S6 / "inputs" / "space6_u1_002_u2_001.msolve.log",
            S6 / "inputs" / "space6_u1_002_u2_002.msolve.out",
            S6 / "inputs" / "space6_u1_002_u2_002.msolve.log",
            S5 / "inputs" / "space5_u1_002_u2_004.msolve.out",
            S5 / "inputs" / "space5_u1_002_u2_004.msolve.log",
            S5 / "inputs" / "space5_u1_002_u2_005.msolve.out",
            S5 / "inputs" / "space5_u1_002_u2_005.msolve.log",
            EXCEPTION / f"{STEM}.msolve.in",
            EXCEPTION / f"{STEM}.input.packet.json",
            EXCEPTION / f"{STEM}.transported.msolve.out",
            EXCEPTION / f"{STEM}.transport.certificate.json",
            EXCEPTION / f"{STEM}.D_unit.certificate.json",
        ]
    )
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        print("Missing files:\n" + "\n".join(missing))
        raise SystemExit(1)

    v1_run = run([sys.executable, str(V1_AUDIT)])
    with tempfile.TemporaryDirectory(prefix="q79-u1-002-crossspace-") as directory:
        temporary = Path(directory)
        rebuilt_s6 = temporary / "space6_inputs"
        rebuilt_s6_packet_path = temporary / "space6_family.packet.json"
        build_run = run(
            [
                sys.executable, str(BUILDER),
                "--input", relative(PARENTS / "space6_classfree_saturated_hR_core.msolve.in"),
                "--space", "6", "--u1", "2",
                "--output-dir", str(rebuilt_s6),
                "--packet", str(rebuilt_s6_packet_path),
            ]
        )
        s6_inputs_equal = build_run.returncode == 0 and all(
            (rebuilt_s6 / f"space6_u1_002_u2_{u2:03d}.msolve.in").read_bytes()
            == (S6 / "inputs" / f"space6_u1_002_u2_{u2:03d}.msolve.in").read_bytes()
            for u2 in range(1, 101)
        )
        rebuilt_s6_packet = json.loads(rebuilt_s6_packet_path.read_text(encoding="utf-8")) if rebuilt_s6_packet_path.is_file() else {}
        committed_s6_packet = json.loads((S6 / "family.packet.json").read_text(encoding="utf-8"))
        s6_packet_equal = packet_without_paths(rebuilt_s6_packet) == packet_without_paths(committed_s6_packet)

        target_input = temporary / f"{STEM}.msolve.in"
        target_packet_path = temporary / f"{STEM}.input.packet.json"
        emitter_run = run(
            [
                sys.executable, str(EMITTER),
                "--input", relative(PARENTS / "space_5_h0_g0_class1_inverse_root.msolve.in"),
                "--scalar-class", "1", "--u1", "2", "--a", "50",
                "--output", str(target_input), "--packet", str(target_packet_path),
            ]
        )
        committed_target_input = EXCEPTION / f"{STEM}.msolve.in"
        committed_target_packet_path = EXCEPTION / f"{STEM}.input.packet.json"
        target_input_equal = target_input.is_file() and target_input.read_bytes() == committed_target_input.read_bytes()
        rebuilt_target_packet = json.loads(target_packet_path.read_text(encoding="utf-8")) if target_packet_path.is_file() else {}
        committed_target_packet = json.loads(committed_target_packet_path.read_text(encoding="utf-8"))
        target_packet_equal = line_packet_without_paths(rebuilt_target_packet) == line_packet_without_paths(committed_target_packet)

        transported_basis = temporary / f"{STEM}.transported.msolve.out"
        transport_certificate = temporary / f"{STEM}.transport.certificate.json"
        transport_run = run(
            [
                sys.executable, str(TRANSPORT),
                "--source-input", relative(S5 / "inputs" / "space5_u1_002_u2_004.msolve.in"),
                "--source-basis", relative(S5 / "inputs" / "space5_u1_002_u2_004.msolve.out"),
                "--target-input", str(target_input),
                "--target-packet", str(target_packet_path),
                "--a", "50",
                "--output-basis", str(transported_basis),
                "--output-certificate", str(transport_certificate),
            ]
        )
        committed_transport_path = EXCEPTION / f"{STEM}.transport.certificate.json"
        committed_transport = json.loads(committed_transport_path.read_text(encoding="utf-8"))
        rebuilt_transport = json.loads(transport_certificate.read_text(encoding="utf-8")) if transport_certificate.is_file() else {}
        transported_basis_equal = transported_basis.is_file() and transported_basis.read_bytes() == (EXCEPTION / f"{STEM}.transported.msolve.out").read_bytes()
        transport_equal = transport_semantics(rebuilt_transport) == transport_semantics(committed_transport)

        regenerated_d_path = temporary / "D_unit.certificate.json"
        d_run = run(
            [
                sys.executable, str(D_VERIFIER),
                "--parent", relative(PARENTS / "space_5_h0_g0_class1_inverse_root.msolve.in"),
                "--symbolic-input", relative(EXCEPTION / f"{STEM}.msolve.in"),
                "--input-packet", relative(EXCEPTION / f"{STEM}.input.packet.json"),
                "--basis-output", relative(EXCEPTION / f"{STEM}.transported.msolve.out"),
                "--basis-log", relative(EXCEPTION / f"{STEM}.transport.certificate.json"),
                "--space", "5", "--output", str(regenerated_d_path),
            ]
        )
        regenerated_d = json.loads(regenerated_d_path.read_text(encoding="utf-8")) if regenerated_d_path.is_file() else {}

        regenerated_summary_path = temporary / "summary.json"
        summary_run = run([sys.executable, str(CERTIFIER), "--output", str(regenerated_summary_path)])
        regenerated_summary = json.loads(regenerated_summary_path.read_text(encoding="utf-8")) if regenerated_summary_path.is_file() else {}

    committed_d = json.loads((EXCEPTION / f"{STEM}.D_unit.certificate.json").read_text(encoding="utf-8"))
    committed_summary = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    theorem = THEOREM.read_text(encoding="utf-8")
    accounting = regenerated_summary.get("accounting", {})
    checks = regenerated_summary.get("checks", {})
    gates = [
        Gate("all artifacts present", "PASS", f"files={len(required)}"),
        Gate("v1 source audit", "PASS" if v1_run.returncode == 0 else "FAIL", v1_run.stdout[-120:].strip()),
        Gate("space-6 family builder reruns", "PASS" if build_run.returncode == 0 else "FAIL", build_run.stdout[-140:].strip()),
        Gate("all 100 space-6 inputs reproduce", "PASS" if s6_inputs_equal else "FAIL", "byte-for-byte"),
        Gate("space-6 family packet reproduces", "PASS" if s6_packet_equal else "FAIL", "path-normalized"),
        Gate("canonical v-line emitter reruns", "PASS" if emitter_run.returncode == 0 else "FAIL", emitter_run.stdout[-120:].strip()),
        Gate("canonical v-line input reproduces", "PASS" if target_input_equal and target_packet_equal else "FAIL", "input bytes and packet"),
        Gate("two-sided basis transport reruns", "PASS" if transport_run.returncode == 0 else "FAIL", transport_run.stdout[-150:].strip()),
        Gate("transported basis reproduces", "PASS" if transported_basis_equal and transport_equal else "FAIL", "basis bytes and transport semantics"),
        Gate("dimension-10 D verifier reruns", "PASS" if d_run.returncode == 0 else "FAIL", d_run.stdout[-160:].strip()),
        Gate("D-unit certificate reproduces", "PASS" if regenerated_d == committed_d else "FAIL", "committed == regenerated"),
        Gate("summary certifier reruns", "PASS" if summary_run.returncode == 0 else "FAIL", summary_run.stdout[-160:].strip()),
        Gate("summary certificate reproduces", "PASS" if regenerated_summary == committed_summary else "FAIL", "committed == regenerated"),
        Gate(
            "seven-line accounting",
            "PASS" if accounting == {
                "space5_symbolic_lines_closed": 5,
                "space6_symbolic_lines_closed": 2,
                "cross_space_symbolic_lines_closed": 7,
                "R_only_unit_lines": 6,
                "D_augmented_unit_lines": 1,
                "canonical_fixed_F101_fibers_closed": 700,
                "cross_space_symbolic_lines_remaining_unclassified": 193,
            } else "FAIL",
            "7/200 lines; 700 fibers",
        ),
        Gate("all consolidated checks", "PASS" if len(checks) == 13 and all(checks.values()) else "FAIL", f"{sum(bool(value) for value in checks.values())}/13"),
        Gate(
            "claim boundary retained",
            "PASS" if "remaining unclassified symbolic-u2 lines:         193" in theorem and "`138/140`" in theorem else "FAIL",
            str(THEOREM),
        ),
        Gate("zero fit parameters", "PASS" if regenerated_summary.get("new_continuous_fit_parameters") == 0 else "FAIL", "zero"),
    ]

    print("q79 u1=2 cross-space seven-line symbolic prefix v2 audit")
    print("================================================")
    width = max(len(gate.label) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:4s}  {gate.detail}")
    if any(gate.status == "FAIL" for gate in gates):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
