"""Audit the twisted-source promotion gate."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
CERT_DIR = REPO / "certificates"
CERT = CERT_DIR / "iwasawa_twisted_source_promotion_gate_certificate.json"
SOURCE_HUNT_CERT = CERT_DIR / "iwasawa_projective_twist_source_hunt_certificate.json"
PAPER = ROOT / "Iwasawa_Twisted_Source_Promotion_Gate_v1.md"
VALIDATOR = REPO / "scripts" / "validate_iwasawa_twisted_source_promotion.py"
PROJECTIVE_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_projective_magnetic_carrier.py"
PUREGAUGE_CONSTRUCTOR = REPO / "scripts" / "construct_iwasawa_puregauge_nonabelian_mesh.py"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def run_command(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode, proc.stdout


def emit_candidate(script: Path, out_path: Path) -> None:
    code, output = run_command(
        [sys.executable, str(script), "--mesh-N", "1", "--emit-candidate", str(out_path)]
    )
    if code != 0:
        raise RuntimeError(output)


def base_packet(candidate_path: Path, *, selected: bool = True) -> dict[str, Any]:
    return {
        "schema": "IwasawaTwistedSourcePromotionPacket.v1",
        "status": "CANDIDATE",
        "selected_twist_verified": selected,
        "fixed_topological_sector": selected,
        "no_observed_flavor_inputs": True,
        "uses_execution_ii_benchmarks": False,
        "uses_observed_masses_or_mixings": False,
        "uses_projective_prototype_as_selected": not selected,
        "uses_zeta3_twist_as_q79_replacement": False,
        "gerbe_source": {
            "source_kind": "Deligne_Cech_gerbe",
            "selected_by_mtt": True,
            "fixed_differential_cohomology_class": True,
            "map_to_central_cocycle_verified": True,
            "green_schwarz_bianchi_verified": True,
            "freed_witten_verified": True,
            "twisted_projector_retains_sector": True,
            "coherent_spectral_projector_verified": True,
            "period_denominator": 3,
            "central_phase_label": "zeta_3^2",
        },
        "central_cocycle": {
            "base_group": "F_3^2",
            "omega_order": 3,
            "commutator_rank_over_F3": 2,
            "finite_heisenberg_extension_order": 27,
            "center_order": 3,
            "ordinary_bundle_coboundary_possible": False,
        },
        "paths": {
            "projective_rhoE_mesh": str(candidate_path),
            "rhoE_metric": str(candidate_path),
            "sector_maps": str(candidate_path),
        },
    }


def validate(packet_path: Path) -> tuple[int, str]:
    return run_command([sys.executable, str(VALIDATOR), str(packet_path)])


def main() -> None:
    cert = load_json(CERT)
    source_hunt = load_json(SOURCE_HUNT_CERT)
    paper = read(PAPER)
    validator_text = read(VALIDATOR)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        projective_path = temp / "projective.json"
        puregauge_path = temp / "puregauge.json"
        emit_candidate(PROJECTIVE_CONSTRUCTOR, projective_path)
        emit_candidate(PUREGAUGE_CONSTRUCTOR, puregauge_path)

        open_path = temp / "open_packet.json"
        write_json(
            open_path,
            {
                "schema": "IwasawaTwistedSourcePromotionPacket.v1",
                "status": "OPEN",
            },
        )
        open_code, open_output = validate(open_path)

        unselected_path = temp / "unselected_projective_packet.json"
        write_json(unselected_path, base_packet(projective_path, selected=False))
        unselected_code, unselected_output = validate(unselected_path)

        missing_map_path = temp / "missing_map_packet.json"
        missing_map = base_packet(projective_path, selected=True)
        del missing_map["gerbe_source"]["map_to_central_cocycle_verified"]
        write_json(missing_map_path, missing_map)
        missing_map_code, missing_map_output = validate(missing_map_path)

        puregauge_path_packet = temp / "puregauge_twist_packet.json"
        write_json(puregauge_path_packet, base_packet(puregauge_path, selected=True))
        puregauge_code, puregauge_output = validate(puregauge_path_packet)

        missing_projector_path = temp / "missing_projector_packet.json"
        missing_projector = base_packet(projective_path, selected=True)
        del missing_projector["paths"]["sector_maps"]
        write_json(missing_projector_path, missing_projector)
        missing_projector_code, missing_projector_output = validate(missing_projector_path)

    implemented = cert.get("implemented_checks", {})
    audit_cases = cert.get("audit_cases", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "FORMULATED"
            if cert.get("status") == "IWASAWA_TWISTED_SOURCE_PROMOTION_GATE_FORMULATED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "source hunt dependency",
            "PASS"
            if source_hunt.get("verdict", {}).get("projective_route_corpus_aligned") is True
            and source_hunt.get("verdict", {}).get("selected_projective_twist_source_found")
            is False
            else "FAIL",
            str(SOURCE_HUNT_CERT),
        ),
        Gate(
            "validator script",
            "PASS"
            if contains_all(
                validator_text,
                [
                    "IwasawaTwistedSourcePromotionPacket.v1",
                    "map_to_central_cocycle_verified",
                    "green_schwarz_bianchi_verified",
                    "freed_witten_verified",
                    "validate_iwasawa_projective_rhoE_mesh.py",
                    "nontrivial central twist required",
                ],
            )
            else "FAIL",
            str(VALIDATOR),
        ),
        Gate(
            "implemented checks",
            "PASS" if all(implemented.values()) else "FAIL",
            str(implemented),
        ),
        Gate(
            "open packet refused",
            "PASS"
            if open_code == 2 and "OPEN" in open_output
            else "FAIL",
            f"exit={open_code}; output={open_output.strip()}",
        ),
        Gate(
            "unselected projective rejected",
            "PASS"
            if unselected_code == 1
            and "selected_twist_verified must be true" in unselected_output
            and "uses_projective_prototype_as_selected must be false" in unselected_output
            else "FAIL",
            f"exit={unselected_code}; output={unselected_output.strip()}",
        ),
        Gate(
            "missing gerbe map incomplete",
            "PASS"
            if missing_map_code == 2
            and "gerbe_source.map_to_central_cocycle_verified" in missing_map_output
            else "FAIL",
            f"exit={missing_map_code}; output={missing_map_output.strip()}",
        ),
        Gate(
            "strict projective case rejected",
            "PASS"
            if puregauge_code == 1
            and "nontrivial central twist required" in puregauge_output
            else "FAIL",
            f"exit={puregauge_code}; output={puregauge_output.strip()}",
        ),
        Gate(
            "current projective lacks projectors",
            "PASS"
            if missing_projector_code == 2 and "paths.sector_maps" in missing_projector_output
            else "FAIL",
            f"exit={missing_projector_code}; output={missing_projector_output.strip()}",
        ),
        Gate(
            "audit cases",
            "PASS" if all(audit_cases.values()) else "FAIL",
            str(audit_cases),
        ),
        Gate(
            "what this closes",
            "PASS" if all(cert.get("what_this_closes", {}).values()) else "FAIL",
            str(cert.get("what_this_closes", {})),
        ),
        Gate(
            "still open",
            "OPEN" if all(cert.get("still_open", {}).values()) else "FAIL",
            str(cert.get("still_open", {})),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("twisted_promotion_gate_ready") is True
            and verdict.get("current_projective_carrier_remains_unpromoted") is True
            and "IwasawaTwistedSourcePromotionPacket" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records gate",
            "PASS"
            if contains_all(
                paper,
                [
                    "IwasawaTwistedSourcePromotionPacket.v1",
                    "nontrivial central twist",
                    "does not pass selected-source promotion",
                    "filled IwasawaTwistedSourcePromotionPacket.v1",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa twisted-source promotion gate audit")
    print("===========================================")
    print()
    print(f"open_packet_exit={open_code}")
    print(f"unselected_projective_exit={unselected_code}")
    print(f"missing_map_exit={missing_map_code}")
    print(f"puregauge_twist_exit={puregauge_code}")
    print(f"missing_projector_exit={missing_projector_code}")
    print()

    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
