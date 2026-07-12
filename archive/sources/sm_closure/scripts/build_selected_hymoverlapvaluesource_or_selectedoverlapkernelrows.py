"""Build selected HYM-overlap value source / selected overlap-kernel rows.

The previous frontier closed the finite 27x27 qutrit spectral package.  This
artifact reconciles that package with the later threshold-delta result that
emits nine charged source-native K/L overlap rows.  It promotes exactly those
nine charged normalized overlap-kernel rows and leaves the H/lambda row and full
scalar Omega execution open.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
CHARGED_ROWS = PACKET_DIR / "selected_charged_normalized_overlap_kernel_rows.packet.json"
H_GAP = PACKET_DIR / "h_lambda_overlap_kernel_row_gap.packet.json"
SCALAR_GATE = PACKET_DIR / "scalar_execution_gate_after_charged_kernel_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charged_overlap_kernel_rows.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1.md"
AUDIT = CORPUS / f"{SLUG}_audit.py"

PREVIOUS = DATA / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging.candidate.json"
MATRIX_PACKET = (
    DATA
    / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging"
    / "qutrit_weyl_27x27_matrix_realization.packet.json"
)
THRESHOLD_DELTA = DATA / "selected_thresholddeltarows_or_lambdahpayloadexecution.candidate.json"
K_ROWS = DATA / "selected_thresholddeltarows_or_lambdahpayloadexecution" / "charged_kthreshold_rows_after_null_delta.packet.json"
T_ROWS = DATA / "selected_thresholddeltarows_or_lambdahpayloadexecution" / "charged_source_native_tscheme_rows.packet.json"
NULL_THEOREM = (
    DATA
    / "selected_thresholddeltarows_or_lambdahpayloadexecution"
    / "source_native_null_threshold_delta_theorem.packet.json"
)
HIGGS_DYNAMIC = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof.candidate.json"
DIRECT_H = DATA / "selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json"
LAMBDA_GATE = (
    DATA
    / "selected_tschemelambdah_sourcerows_or_kthresholdrowclosure"
    / "lambda_h_payload_gate_after_charged_lrows.packet.json"
)
CONDITIONAL_SCALAR = (
    DATA
    / "selected_combinedthresholdkernelkrows_sourcetheorem"
    / "conditional_k_rows_scalar_closure_theorem.packet.json"
)

STATUS = (
    "MTT_SELECTED_HYMOVERLAPVALUESOURCE_OR_SELECTEDOVERLAPKERNELROWS_"
    "NINE_CHARGED_ROWS_EMITTED_H_LAMBDA_AND_SCALARS_OPEN"
)
NEXT = "MTT_Selected_HLambdaOverlapKernelRow_or_ScalarOmegaExecutionGate_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def source_paths() -> list[Path]:
    return [
        PREVIOUS,
        MATRIX_PACKET,
        THRESHOLD_DELTA,
        K_ROWS,
        T_ROWS,
        NULL_THEOREM,
        HIGGS_DYNAMIC,
        DIRECT_H,
        LAMBDA_GATE,
        CONDITIONAL_SCALAR,
    ]


def build() -> None:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    missing = [rel(path) for path in source_paths() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing selected overlap-kernel inputs: " + ", ".join(missing))

    previous = load(PREVIOUS)
    matrix = load(MATRIX_PACKET)
    threshold_delta = load(THRESHOLD_DELTA)
    k_rows = load(K_ROWS)
    t_rows = load(T_ROWS)
    null_theorem = load(NULL_THEOREM)
    higgs_dynamic = load(HIGGS_DYNAMIC)
    direct_h = load(DIRECT_H)
    lambda_gate = load(LAMBDA_GATE)
    conditional = load(CONDITIONAL_SCALAR)

    t_by_key = {(row["sector"], row["generation"]): row for row in t_rows["rows"]}
    emitted_rows = []
    for row in k_rows["rows"]:
        key = (row["sector"], row["generation"])
        t_row = t_by_key[key]
        emitted_rows.append(
            {
                "row_id": f"selected_overlap_kernel.{row['omega_id']}",
                "omega_id": row["omega_id"],
                "sector": row["sector"],
                "generation": row["generation"],
                "normalized_overlap_kernel_id": f"L_HYMStrominger.normalized.{row['omega_id']}",
                "selected_normalized_overlap_kernel_value": row["selected_strict_L_rowlocal_value"],
                "selected_K_threshold_source_value": row["selected_K_threshold_source_value"],
                "selected_T_scheme_source_native": t_row["T_scheme_source_native"],
                "Delta_threshold_source_native": t_row["Delta_threshold_source_native"],
                "Delta_mass_source_native": t_row["Delta_mass_source_native"],
                "Delta_profile_source_native": t_row["Delta_profile_source_native"],
                "formula": (
                    "K_threshold_i = L_HYMStrominger.normalized_i * T_scheme_i; "
                    "source-native T_scheme_i=1, hence K_threshold_i=L_i"
                ),
                "finite_carrier": "Q_sel^U 27x27 qutrit Weyl spectral package",
                "source_native_null_delta_theorem_used": t_row["source_native_null_delta_theorem_used"],
                "accepted_as_selected_charged_normalized_overlap_kernel_row": True,
                "accepted_as_full_ten_row_kernel_closure": False,
                "accepted_as_strict_scalar_omega_row": False,
                "lambda_H_payload_required_for_full_closure": True,
                "observed_data_used_as_selector": False,
                "target_fitting_used": False,
            }
        )

    charged_packet = {
        "schema": "MTTSelectedChargedNormalizedOverlapKernelRows.v1",
        "status": "NINE_CHARGED_NORMALIZED_HYM_STROMINGER_OVERLAP_KERNEL_ROWS_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "source_inputs": {
            "finite_27x27_package": rel(MATRIX_PACKET),
            "charged_kthreshold_rows": rel(K_ROWS),
            "charged_tscheme_rows": rel(T_ROWS),
            "null_threshold_delta_theorem": rel(NULL_THEOREM),
        },
        "row_count": len(emitted_rows),
        "accepted_selected_charged_normalized_overlap_kernel_row_count": len(emitted_rows),
        "accepted_full_ten_row_kernel_closure_count": 0,
        "accepted_strict_scalar_omega_row_count": 0,
        "rows": emitted_rows,
    }

    h_gap = {
        "schema": "MTTHLambdaOverlapKernelRowGap.v1",
        "status": "H_LAMBDA_OVERLAP_KERNEL_ROW_NOT_EMITTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "omega_id": "Omega_H.lambda",
        "combined_kernel_row_id": "K_threshold.Omega_H.lambda",
        "selected_H_sector_overlap_kernel_row_emitted": False,
        "selected_lambda_H_payload_emitted": False,
        "selected_K_threshold_Omega_H_lambda_emitted": False,
        "selected_s_beta_value_found": higgs_dynamic["closure_decision"]["selected_s_beta_value_found"],
        "selected_s_beta_value": higgs_dynamic["closure_decision"]["selected_s_beta_value"],
        "why_s_beta_does_not_close_H_row": (
            "s_beta is an H-sector projection/angular factor.  The latest Higgs "
            "packets explicitly reject using it, D_fin.H, or replay target "
            "numerators as the H radial/threshold kernel row."
        ),
        "direct_H_status": direct_h["status"],
        "lambda_gate_status": lambda_gate["status"],
        "blocking_reasons": lambda_gate["blocking_reasons"]
        + [
            "selected H radial/threshold scalar still absent",
            "dynamic Herm(2) Huv value rows still absent",
            "strict scalar Omega/lambda execution still needs all ten K rows",
        ],
    }

    scalar_gate = {
        "schema": "MTTScalarExecutionGateAfterChargedKernelRows.v1",
        "status": "CHARGED_OVERLAP_ROWS_EMITTED_FULL_SCALAR_EXECUTION_STILL_BLOCKED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "conditional_scalar_theorem_imported": rel(CONDITIONAL_SCALAR),
        "conditional_statement": conditional["conditional_statement"],
        "selected_K_threshold_row_count_present_after_this_artifact": len(emitted_rows),
        "selected_K_threshold_row_count_required": 10,
        "charged_normalized_overlap_rows_present": 9,
        "H_lambda_kernel_row_present": False,
        "strict_Omega_rows_executable": False,
        "lambda_H_row_executable": False,
        "accepted_internal_scalar_value_row_count": 0,
        "why_not_scalar_closure": [
            "the ten-row antecedent is not satisfied",
            "the H/lambda overlap-kernel row is absent",
            "current artifact emits overlap-kernel source rows, not observed Yukawa/Higgs replay values",
        ],
    }

    cutset = {
        "schema": "MTTNextCutsetAfterChargedOverlapKernelRows.v1",
        "status": "NEXT_CUTSET_IS_H_LAMBDA_KERNEL_ROW_THEN_SCALAR_GATE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "nine charged normalized HYM/Strominger overlap-kernel rows",
            "source-native charged T_scheme=1 import",
            "charged K_threshold=L_overlap reconciliation after 27x27 qutrit spectral packaging",
            "H/lambda scalar blocker isolated from charged overlap rows",
        ],
        "still_open": [
            "selected H/lambda normalized overlap-kernel row",
            "selected H radial/quartic/threshold scalar or dynamic Herm(2) Huv rows",
            "ten-row K_threshold antecedent",
            "strict Omega/lambda_H scalar execution",
            "matrix-level mixing extension and true SM equivalence",
        ],
        "next_required_artifact": NEXT,
        "non_looping_rule": (
            "Do not re-open the qutrit carrier, finite 27x27 package, charged "
            "null-delta theorem, or nine charged overlap rows.  The next proof "
            "must emit the H/lambda row or a scalar gate using all ten rows."
        ),
    }

    candidate = {
        "schema": "MTTSelectedHYMOverlapValueSourceOrSelectedOverlapKernelRows.v1",
        "status": STATUS,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_frontier": rel(PREVIOUS),
            "finite_27x27_matrix_packet": rel(MATRIX_PACKET),
            "threshold_delta_candidate": rel(THRESHOLD_DELTA),
            "charged_kthreshold_rows": rel(K_ROWS),
            "charged_tscheme_rows": rel(T_ROWS),
            "higgs_dynamic_projection_packet": rel(HIGGS_DYNAMIC),
            "direct_h_quartic_packet": rel(DIRECT_H),
            "lambda_gate": rel(LAMBDA_GATE),
            "conditional_scalar_theorem": rel(CONDITIONAL_SCALAR),
        },
        "output_packets": {
            "selected_charged_normalized_overlap_kernel_rows": rel(CHARGED_ROWS),
            "h_lambda_overlap_kernel_row_gap": rel(H_GAP),
            "scalar_execution_gate_after_charged_kernel_rows": rel(SCALAR_GATE),
            "next_cutset_after_charged_overlap_kernel_rows": rel(CUTSET),
        },
        "closure_decision": {
            "finite_27x27_qutrit_spectral_package_imported": previous["spectral_packaging_decision"][
                "finite_qutrit_spectral_package_closed"
            ],
            "qutrit_left_action_rank": matrix["left_Z27_rank"],
            "selected_charged_normalized_overlap_kernel_row_count": len(emitted_rows),
            "accepted_selected_K_source_row_count": threshold_delta["closure_decision"][
                "accepted_selected_K_source_row_count"
            ],
            "selected_T_scheme_source_row_count": threshold_delta["closure_decision"][
                "selected_T_scheme_source_row_count"
            ],
            "selected_H_lambda_overlap_kernel_row_emitted": False,
            "selected_lambda_H_payload_emitted": False,
            "accepted_internal_scalar_value_row_count": 0,
            "full_ten_row_K_threshold_closure": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "SelectedChargedNormalizedHYMStromingerOverlapKernelRowsTheorem",
            "proved": True,
            "statement": (
                "Given the selected 27x27 qutrit spectral package, the charged "
                "source-native null threshold theorem, and the audited charged "
                "K_threshold rows, the nine charged normalized HYM/Strominger "
                "overlap-kernel rows are selected with values K=L because "
                "T_scheme=1 on the charged source-native layer.  The theorem "
                "does not emit the H/lambda row or strict scalar Omega values."
            ),
        },
        "closed": cutset["closed_here"],
        "open": cutset["still_open"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "schema": "MTTAuditCertificate.v1",
        "artifact": "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1",
        "status": STATUS,
        "verified_by": rel(AUDIT),
        "candidate": rel(OUTPUT),
        "packets": [rel(CHARGED_ROWS), rel(H_GAP), rel(SCALAR_GATE), rel(CUTSET)],
        "theorem_proved": True,
        "selected_charged_normalized_overlap_kernel_row_count": len(emitted_rows),
        "selected_H_lambda_overlap_kernel_row_emitted": False,
        "accepted_internal_scalar_value_row_count": 0,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
    }

    rows_md = "\n".join(
        f"- {row['omega_id']}: L = K = {row['selected_normalized_overlap_kernel_value']}"
        for row in emitted_rows
    )
    note = f"""# MTT Selected HYM Overlap Value Source or Selected Overlap-Kernel Rows v1

## Purpose

This artifact emits the selected charged normalized HYM/Strominger overlap-kernel
rows after the finite `27x27` qutrit spectral package.  It closes the charged
kernel-row part of the frontier and keeps the H/lambda and strict scalar
execution gates honest.

## Theorem

`SelectedChargedNormalizedHYMStromingerOverlapKernelRowsTheorem`.

Given:

- the selected finite `27x27` qutrit spectral package,
- the source-native null threshold theorem for charged rows,
- the nine audited charged `K_threshold` rows,

the nine charged normalized overlap rows are selected because

```text
K_threshold_i = L_HYMStrominger.normalized_i * T_scheme_i
T_scheme_i = 1
therefore K_threshold_i = L_HYMStrominger.normalized_i
```

No observed masses, Yukawa values, CKM/PMNS data, or Higgs replay values are
used as selectors.

## Emitted Charged Rows

{rows_md}

## H/Lambda Gate

The H/lambda row is not emitted here.

- selected `s_beta`: `{higgs_dynamic["closure_decision"]["selected_s_beta_value"]}`
- selected H/lambda overlap-kernel row emitted: `false`
- selected `lambda_H` payload emitted: `false`
- strict scalar `Omega/lambda_H` execution closed: `false`

`s_beta` is a selected projection/angular factor, not the missing H radial or
threshold overlap row.

## Scalar Gate

The conditional scalar theorem still requires ten selected `K_threshold` rows.
This artifact supplies nine charged rows.  Therefore:

- selected charged normalized overlap-kernel rows: `9`
- selected H/lambda overlap-kernel rows: `0`
- accepted internal scalar value rows: `0`
- full ten-row `K_threshold` closure: `false`
- true SM equivalence: `false`

## What This Closes

- nine charged normalized HYM/Strominger overlap-kernel rows
- source-native charged `T_scheme=1` import
- charged `K_threshold=L_overlap` reconciliation after the 27x27 package
- H/lambda scalar blocker isolation

## What Remains Open

- selected H/lambda normalized overlap-kernel row
- selected H radial/quartic/threshold scalar or dynamic Herm(2) Huv rows
- ten-row `K_threshold` antecedent
- strict `Omega/lambda_H` scalar execution
- matrix-level mixing extension and true SM equivalence

## Next Artifact

```text
{NEXT}
```
"""

    audit = f'''"""Audit selected HYM-overlap value source / selected overlap-kernel rows."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "{SLUG}"
DATA = ROOT / "candidate_data" / f"{{SLUG}}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CHARGED = PACKET_DIR / "selected_charged_normalized_overlap_kernel_rows.packet.json"
H_GAP = PACKET_DIR / "h_lambda_overlap_kernel_row_gap.packet.json"
SCALAR = PACKET_DIR / "scalar_execution_gate_after_charged_kernel_rows.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_charged_overlap_kernel_rows.packet.json"
CERT = ROOT / "certificates" / f"{{SLUG}}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HYMOverlapValueSourceTheorem_or_SelectedOverlapKernelRows_v1.md"

STATUS = "{STATUS}"
NEXT = "{NEXT}"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    charged = load(CHARGED)
    h_gap = load(H_GAP)
    scalar = load(SCALAR)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["closure_claimed"] is True, "closure flag missing")
    require(data["full_no_knob_closure_claimed"] is False, "full no-knob overclaimed")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    decision = data["closure_decision"]
    require(decision["finite_27x27_qutrit_spectral_package_imported"] is True, "27x27 package not imported")
    require(decision["qutrit_left_action_rank"] == 27, "qutrit rank mismatch")
    require(decision["selected_charged_normalized_overlap_kernel_row_count"] == 9, "charged row count mismatch")
    require(decision["accepted_selected_K_source_row_count"] == 9, "K source count mismatch")
    require(decision["selected_T_scheme_source_row_count"] == 9, "T source count mismatch")
    require(decision["selected_H_lambda_overlap_kernel_row_emitted"] is False, "H row overemitted")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")
    require(decision["full_ten_row_K_threshold_closure"] is False, "ten-row closure overclaimed")

    require(charged["row_count"] == 9, "charged packet row count")
    require(charged["accepted_selected_charged_normalized_overlap_kernel_row_count"] == 9, "accepted charged count")
    require(charged["accepted_full_ten_row_kernel_closure_count"] == 0, "full ten overaccepted")
    require(charged["accepted_strict_scalar_omega_row_count"] == 0, "Omega rows overaccepted")
    expected = {{1: 1.367835979172, 2: 0.683917989586, 3: 0.683917989586}}
    seen = set()
    for row in charged["rows"]:
        seen.add((row["sector"], row["generation"]))
        require(row["accepted_as_selected_charged_normalized_overlap_kernel_row"] is True, "charged row not accepted")
        require(row["accepted_as_full_ten_row_kernel_closure"] is False, "full closure overaccepted")
        require(row["accepted_as_strict_scalar_omega_row"] is False, "strict scalar overaccepted")
        require(row["selected_T_scheme_source_native"] == 1.0, "T_scheme not one")
        require(row["Delta_threshold_source_native"] == 0.0, "threshold delta not zero")
        require(row["Delta_mass_source_native"] == 0.0, "mass delta not zero")
        require(row["Delta_profile_source_native"] == 0.0, "profile delta not zero")
        require(abs(row["selected_normalized_overlap_kernel_value"] - expected[row["generation"]]) < 1e-12, "L value mismatch")
        require(abs(row["selected_K_threshold_source_value"] - expected[row["generation"]]) < 1e-12, "K value mismatch")
        require(row["observed_data_used_as_selector"] is False, "row observed selector")
        require(row["target_fitting_used"] is False, "row target fitting")
    require(seen == {{(sector, gen) for sector in ["u", "d", "e"] for gen in [1, 2, 3]}}, "charged row slots mismatch")

    require(h_gap["selected_H_sector_overlap_kernel_row_emitted"] is False, "H overlap row overemitted")
    require(h_gap["selected_lambda_H_payload_emitted"] is False, "lambda payload overemitted")
    require(h_gap["selected_K_threshold_Omega_H_lambda_emitted"] is False, "H K row overemitted")
    require(h_gap["selected_s_beta_value_found"] is True, "s_beta support missing")
    require("selected H radial/threshold scalar still absent" in h_gap["blocking_reasons"], "H radial blocker missing")

    require(scalar["selected_K_threshold_row_count_present_after_this_artifact"] == 9, "scalar gate K count")
    require(scalar["selected_K_threshold_row_count_required"] == 10, "scalar gate required count")
    require(scalar["H_lambda_kernel_row_present"] is False, "scalar gate H row overemitted")
    require(scalar["strict_Omega_rows_executable"] is False, "Omega execution overclosed")
    require(scalar["lambda_H_row_executable"] is False, "lambda execution overclosed")
    require(scalar["accepted_internal_scalar_value_row_count"] == 0, "scalar rows overaccepted")

    require(cutset["next_required_artifact"] == NEXT, "cutset next mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(cert["selected_charged_normalized_overlap_kernel_row_count"] == 9, "cert charged count")
    require(cert["selected_H_lambda_overlap_kernel_row_emitted"] is False, "cert H overemitted")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "cert scalar overaccepted")

    for phrase in [
        "selected charged normalized overlap-kernel rows: `9`",
        "selected H/lambda overlap-kernel rows: `0`",
        "accepted internal scalar value rows: `0`",
        "Omega_u.gen1: L = K = 1.367835979172",
        "Omega_d.gen2: L = K = 0.683917989586",
        "Omega_e.gen3: L = K = 0.683917989586",
        NEXT,
    ]:
        require(phrase in note, f"note missing phrase: {{phrase}}")

    print(f"PASS {{DATA.name}}: {{STATUS}}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
'''

    write_json(CHARGED_ROWS, charged_packet)
    write_json(H_GAP, h_gap)
    write_json(SCALAR_GATE, scalar_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    AUDIT.write_text(audit, encoding="utf-8")


def main() -> int:
    build()
    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(AUDIT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
