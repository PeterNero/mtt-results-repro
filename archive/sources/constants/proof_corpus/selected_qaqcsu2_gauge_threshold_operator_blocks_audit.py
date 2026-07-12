"""Audit the selected Qa/Qc/SU2 gauge-threshold operator block scaffold."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "selected_qaqcsu2_gauge_threshold_operator_blocks_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Qa_Qc_SU2_Gauge_Threshold_Operator_Blocks_v1.md"
SCRIPT = REPO / "scripts" / "build_selected_qaqcsu2_gauge_threshold_operator_blocks.py"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def run_script() -> dict:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def report(name: str, ok: bool, detail: object = "") -> bool:
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")
    return ok


def main() -> int:
    cert = json.loads(read(CERT))
    note = read(NOTE)
    computed = run_script()
    failures = []

    failures.append(
        not report(
            "certificate status",
            cert["status"] == "QA_QC_SU2_OPERATOR_BLOCK_SCAFFOLD_BUILT_VALUES_OPEN",
            cert["status"],
        )
    )
    failures.append(
        not report(
            "script agrees with certificate status",
            computed["status"] == cert["status"]
            and computed["determinant_handoff"]["can_fill_template_now"] is False,
            computed["determinant_handoff"],
        )
    )
    failures.append(
        not report(
            "all three operator blocks exist",
            set(computed["operator_blocks"]) == {"D_Qa", "D_Qc", "D_SU2"},
            list(computed["operator_blocks"]),
        )
    )
    failures.append(
        not report(
            "candidate heat coefficients carried but not closed",
            computed["operator_blocks"]["D_Qa"]["trace_and_representation"]["heat_coefficient_candidate"] == 3.0
            and computed["operator_blocks"]["D_Qc"]["trace_and_representation"]["heat_coefficient_candidate"] == 1.0
            and computed["operator_blocks"]["D_SU2"]["trace_and_representation"]["heat_coefficient_candidate"] == 2.0
            and computed["operator_blocks"]["D_Qa"]["trace_and_representation"]["status"]
            == "CANDIDATE_NOT_DERIVED_FROM_FULL_BLOCK",
            {
                key: value["trace_and_representation"]
                for key, value in computed["operator_blocks"].items()
            },
        )
    )
    failures.append(
        not report(
            "ghost rules distinguish abelian and nonabelian",
            "field-independent" in computed["operator_blocks"]["D_Qc"]["ghost_and_quotient_rule"]["rule"]
            and "Faddeev-Popov" in computed["operator_blocks"]["D_Qa"]["ghost_and_quotient_rule"]["rule"]
            and "Faddeev-Popov" in computed["operator_blocks"]["D_SU2"]["ghost_and_quotient_rule"]["rule"],
            {
                key: value["ghost_and_quotient_rule"]["rule"]
                for key, value in computed["operator_blocks"].items()
            },
        )
    )
    failures.append(
        not report(
            "spectra and determinants remain open",
            all(
                block["spectral_data"]["status"] == "OPEN_SELECTED_SPECTRUM_REQUIRED"
                and block["spectral_data"]["finite_determinant_part"] is None
                for block in computed["operator_blocks"].values()
            )
            and computed["verdict"]["finite_determinants_closed"] is False,
            computed["verdict"],
        )
    )
    failures.append(
        not report(
            "note records next spectrum/heat coefficient gate",
            "Selected_Qa_Qc_SU2_Operator_Spectra_or_Heat_Coefficients_v1" in note
            and "It is not closure." in note
            and "measured gauge couplings" in note,
            NOTE,
        )
    )
    failures.append(
        not report(
            "no new no-knob prediction claimed",
            cert["verdict"]["new_no_knob_prediction_certified"] is False,
            cert["verdict"],
        )
    )

    print("\nSelected Qa/Qc/SU2 gauge-threshold operator blocks audit")
    if any(failures):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
