"""Audit the selected-radius import no-go for visible rank-two L^2."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SCRIPT = REPO / "scripts" / "analyze_visible_rank2_l2_selected_radius_import_nogo.py"
CANDIDATE = REPO / "candidate_data" / "visible_rank2_l2_selected_radius_import_nogo.candidate.json"
CERT = REPO / "certificates" / "visible_rank2_l2_selected_radius_import_nogo_certificate.json"
PAPER = ROOT / "Visible_Rank2_L2_Selected_Radius_Import_NoGo_v1.md"


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> int:
    proc = run([sys.executable, str(SCRIPT)])
    cert = load_json(CERT)
    candidate = load_json(CANDIDATE)
    paper = read(PAPER)

    imported = cert.get("imported_certificates", {})
    geometry = cert.get("imported_selected_radius_geometry", {})
    slope = cert.get("visible_slope_dictionary", {})
    chambers = cert.get("branch_chambers", {})
    theorem = cert.get("no_go_theorem", {})
    closes = cert.get("what_this_closes", {})
    still_open = cert.get("still_open", {})
    guardrails = cert.get("guardrails", {})

    target_wall = chambers.get("target_wall", {})
    symmetric = chambers.get("symmetric_import", {})
    swapped_wall = chambers.get("swapped_wall", {})

    gates = [
        Gate("script exits 0", "PASS" if proc.returncode == 0 else "FAIL", proc.stdout[:1000]),
        Gate("certificate exists", "PASS" if CERT.exists() else "FAIL", str(CERT)),
        Gate("candidate exists", "PASS" if CANDIDATE.exists() else "FAIL", str(CANDIDATE)),
        Gate("paper exists", "PASS" if PAPER.exists() else "FAIL", str(PAPER)),
        Gate(
            "status no-go",
            "PASS"
            if cert.get("status")
            == "VISIBLE_RANK2_L2_SELECTED_RADIUS_IMPORT_NO_GO_EQUAL_RADIUS"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate mirrors certificate",
            "PASS"
            if candidate.get("status") == cert.get("status")
            and candidate.get("branch_chambers") == cert.get("branch_chambers")
            else "FAIL",
            str(CANDIDATE),
        ),
        Gate(
            "constants certificates imported",
            "PASS"
            if imported.get("constants_final_radius", {}).get("status")
            == "FINAL_INTERNAL_RHO_UV_BRANCH_CLOSED"
            and imported.get("constants_horizontal_scale_law", {}).get("status")
            == "H2_HORIZONTAL_SCALE_LAW_SELECTED"
            else "FAIL",
            str(imported),
        ),
        Gate(
            "import is equal radius",
            "PASS"
            if geometry.get("source_branch") == "(r1,r2,r3)=(R,R,r3(R))"
            and geometry.get("r1_equals_r2") is True
            and geometry.get("p1_equals_p2") is True
            and math.isclose(float(geometry.get("r1_over_r2")), 1.0, abs_tol=1e-12)
            else "FAIL",
            str(geometry),
        ),
        Gate(
            "import misses target wall",
            "PASS"
            if geometry.get("matches_target_wall") is False
            and math.isclose(
                float(geometry.get("target_wall_r1_over_r2")), math.sqrt(2.0), rel_tol=1e-12
            )
            and slope.get("target_selector_condition")
            == "p1:p2=1:2, equivalently r1:r2=sqrt(2):1"
            else "FAIL",
            str({"geometry": geometry, "slope": slope}),
        ),
        Gate(
            "target wall selects target",
            "PASS"
            if target_wall.get("negative") == [[1, -2, 0]]
            and target_wall.get("zero") == [[-2, 1, 0], [2, -1, 0]]
            else "FAIL",
            str(target_wall),
        ),
        Gate(
            "symmetric import remains degenerate",
            "PASS"
            if symmetric.get("negative") == [[-2, 1, 0], [1, -2, 0]]
            and symmetric.get("zero") == []
            else "FAIL",
            str(symmetric),
        ),
        Gate(
            "swapped wall sanity check",
            "PASS"
            if swapped_wall.get("negative") == [[-2, 1, 0]]
            and swapped_wall.get("zero") == [[-1, 2, 0], [1, -2, 0]]
            else "FAIL",
            str(swapped_wall),
        ),
        Gate(
            "no-go theorem scoped",
            "PASS"
            if "cannot be the visible L2 target-wall selector" in theorem.get("theorem", "")
            and "the constants rho_UV theorem is wrong" in theorem.get("does_not_claim", [])
            and "full SM closure" in theorem.get("does_not_claim", [])
            else "FAIL",
            str(theorem),
        ),
        Gate(
            "closes exactly this import",
            "PASS"
            if closes.get("constants_selected_radius_import_tested") is True
            and closes.get("constants_import_is_equal_horizontal_radius") is True
            and closes.get("constants_import_does_not_match_target_wall") is True
            and closes.get("constants_import_leaves_target_and_swapped_degenerate") is True
            else "FAIL",
            str(closes),
        ),
        Gate(
            "still open",
            "OPEN"
            if still_open.get("selected_non_equal_radius_wall_source_r1_over_r2_sqrt2")
            is True
            and still_open.get("selected_ordered_integral_Cech_automorphy_D_E_source")
            is True
            and still_open.get("same_source_D_E_dotD_Hessian_base_ordering") is True
            and still_open.get("full_SM_closure") is True
            else "FAIL",
            str(still_open),
        ),
        Gate(
            "guardrails",
            "PASS" if all(value is False for value in guardrails.values()) else "FAIL",
            str(guardrails),
        ),
        Gate(
            "paper records theorem",
            "PASS"
            if contains_all(
                paper,
                [
                    "selected constants radius",
                    "(r1,r2,r3)=(R,R,r3(R))",
                    "p1:p2=1:1",
                    "r1:r2=sqrt(2):1",
                    "target and swapped",
                    "not a rejection of the constants result",
                    "ordered integral Cech/automorphy/D_E source",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Visible rank-two L2 selected-radius import no-go audit")
    print("======================================================")
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    failures: list[Gate] = []
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")
        if gate.status == "FAIL":
            failures.append(gate)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
