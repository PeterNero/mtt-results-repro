"""Build a versioned RG engine smoke execution / selected SM packet certificate gate."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rgengineexecution_or_selectedsmpacketcertificateintegration"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ENGINE = PACKET_DIR / "one_loop_sm_rg_engine_contract.packet.json"
SMOKE = PACKET_DIR / "diagnostic_one_loop_transport_smoke_run.packet.json"
CERT_GATE = PACKET_DIR / "selected_sm_packet_certificate_integration_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RGEngineExecution_or_SelectedSMPacketCertificateIntegration_v1.md"

STATUS = "MTT_SELECTED_RGENGINEEXECUTION_OR_SELECTEDSMPACKETCERTIFICATEINTEGRATION_BUILT_DIAGNOSTIC_RUN_ONLY"
NEXT_ARTIFACT = "MTT_Selected_ThresholdMassSchemeCovarianceFill_or_QaSU3PacketIntegration_v1"
MZ = 91.18797809193725


Matrix = list[list[complex]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_complex_matrix(value: list) -> Matrix:
    out: Matrix = []
    for row in value:
        out_row: list[complex] = []
        for item in row:
            if isinstance(item, list):
                out_row.append(complex(float(item[0]), float(item[1])))
            else:
                out_row.append(complex(float(item), 0.0))
        out.append(out_row)
    return out


def from_complex_matrix(value: Matrix) -> list:
    return [[[z.real, z.imag] for z in row] for row in value]


def zero(n: int = 3) -> Matrix:
    return [[0j for _ in range(n)] for _ in range(n)]


def ident(n: int = 3) -> Matrix:
    out = zero(n)
    for i in range(n):
        out[i][i] = 1.0 + 0j
    return out


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    n = len(a)
    m = len(b[0])
    kmax = len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(kmax)) for j in range(m)] for i in range(n)]


def dagger(a: Matrix) -> Matrix:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(len(a)))


def frob_norm(a: Matrix) -> float:
    return math.sqrt(sum(abs(z) ** 2 for row in a for z in row))


def beta_yukawa(yu: Matrix, yd: Matrix, ye: Matrix, g1: float, g2: float, g3: float) -> tuple[Matrix, Matrix, Matrix]:
    yu2 = matmul(dagger(yu), yu)
    yd2 = matmul(dagger(yd), yd)
    ye2 = matmul(dagger(ye), ye)
    tr_y = (3 * trace(yu2) + 3 * trace(yd2) + trace(ye2)).real
    pref = 1.0 / (16.0 * math.pi * math.pi)

    bu_bracket = add(
        add(scale(1.5, sub(yu2, yd2)), scale(tr_y, ident())),
        scale(-(17.0 / 20.0 * g1 * g1 + 9.0 / 4.0 * g2 * g2 + 8.0 * g3 * g3), ident()),
    )
    bd_bracket = add(
        add(scale(1.5, sub(yd2, yu2)), scale(tr_y, ident())),
        scale(-(1.0 / 4.0 * g1 * g1 + 9.0 / 4.0 * g2 * g2 + 8.0 * g3 * g3), ident()),
    )
    be_bracket = add(
        add(scale(1.5, ye2), scale(tr_y, ident())),
        scale(-(9.0 / 4.0 * g1 * g1 + 9.0 / 4.0 * g2 * g2), ident()),
    )
    return scale(pref, matmul(yu, bu_bracket)), scale(pref, matmul(yd, bd_bracket)), scale(pref, matmul(ye, be_bracket))


def beta_lambda(lam: float, yu: Matrix, yd: Matrix, ye: Matrix, g1: float, g2: float) -> float:
    yu2 = matmul(dagger(yu), yu)
    yd2 = matmul(dagger(yd), yd)
    ye2 = matmul(dagger(ye), ye)
    t = (3 * trace(yu2) + 3 * trace(yd2) + trace(ye2)).real
    h = (3 * trace(matmul(yu2, yu2)) + 3 * trace(matmul(yd2, yd2)) + trace(matmul(ye2, ye2))).real
    beta = (
        24 * lam * lam
        + 4 * lam * t
        - 2 * h
        - lam * (9 * g2 * g2 + 9.0 / 5.0 * g1 * g1)
        + 27.0 / 200.0 * g1**4
        + 9.0 / 20.0 * g1 * g1 * g2 * g2
        + 9.0 / 8.0 * g2**4
    )
    return beta / (16.0 * math.pi * math.pi)


def rk4_step(yu: Matrix, yd: Matrix, ye: Matrix, lam: float, h: float, g1: float, g2: float, g3: float) -> tuple[Matrix, Matrix, Matrix, float]:
    def deriv(a: Matrix, b: Matrix, c: Matrix, l: float) -> tuple[Matrix, Matrix, Matrix, float]:
        byu, byd, bye = beta_yukawa(a, b, c, g1, g2, g3)
        return byu, byd, bye, beta_lambda(l, a, b, c, g1, g2)

    k1 = deriv(yu, yd, ye, lam)
    k2 = deriv(
        add(yu, scale(h / 2, k1[0])),
        add(yd, scale(h / 2, k1[1])),
        add(ye, scale(h / 2, k1[2])),
        lam + h * k1[3] / 2,
    )
    k3 = deriv(
        add(yu, scale(h / 2, k2[0])),
        add(yd, scale(h / 2, k2[1])),
        add(ye, scale(h / 2, k2[2])),
        lam + h * k2[3] / 2,
    )
    k4 = deriv(
        add(yu, scale(h, k3[0])),
        add(yd, scale(h, k3[1])),
        add(ye, scale(h, k3[2])),
        lam + h * k3[3],
    )
    next_yu = add(yu, scale(h / 6, add(add(k1[0], scale(2, k2[0])), add(scale(2, k3[0]), k4[0]))))
    next_yd = add(yd, scale(h / 6, add(add(k1[1], scale(2, k2[1])), add(scale(2, k3[1]), k4[1]))))
    next_ye = add(ye, scale(h / 6, add(add(k1[2], scale(2, k2[2])), add(scale(2, k3[2]), k4[2]))))
    next_lam = lam + h / 6 * (k1[3] + 2 * k2[3] + 2 * k3[3] + k4[3])
    return next_yu, next_yd, next_ye, next_lam


def run_smoke(yu: Matrix, yd: Matrix, ye: Matrix, lam: float, mu0: float, g1: float, g2: float, g3: float) -> dict[str, Any]:
    steps = 256
    t0 = math.log(mu0)
    t1 = math.log(MZ)
    h = (t1 - t0) / steps
    start_norms = {"Y_u": frob_norm(yu), "Y_d": frob_norm(yd), "Y_e": frob_norm(ye), "lambda_H": lam}
    for _ in range(steps):
        yu, yd, ye, lam = rk4_step(yu, yd, ye, lam, h, g1, g2, g3)
    end_norms = {"Y_u": frob_norm(yu), "Y_d": frob_norm(yd), "Y_e": frob_norm(ye), "lambda_H": lam}
    return {
        "from_scale_GeV": mu0,
        "to_scale_GeV": MZ,
        "steps": steps,
        "start_norms": start_norms,
        "end_norms": end_norms,
        "diagnostic_Y_u_MZ_like": from_complex_matrix(yu),
        "diagnostic_Y_d_MZ_like": from_complex_matrix(yd),
        "diagnostic_Y_e_MZ_like": from_complex_matrix(ye),
        "diagnostic_lambda_H_MZ_like": lam,
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    transport = load(DATA / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit.candidate.json")
    kernel = load(
        DATA
        / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
        / "yukawa_higgs_common_scale_transport_kernel.packet.json"
    )
    final_packet = load(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json")
    anomaly = load(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json")
    qasu3 = load(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json")

    native = kernel["native_values_to_transport"]
    gauges = kernel["available_common_scale_inputs"]
    yu = to_complex_matrix(native["Y_u_native"])
    yd = to_complex_matrix(native["Y_d_native_complex_up_diagonal_convention"])
    ye = to_complex_matrix(native["Y_e_native"])
    lam = float(native["lambda_H_tree_native"])
    g1 = float(gauges["g_1_GUT_MZ"]["central_value"])
    g2 = float(gauges["g_2_MZ"]["central_value"])
    g3 = float(gauges["g_3_MZ"]["central_value"])

    smoke = run_smoke(yu, yd, ye, lam, mu0=172.5590883453979, g1=g1, g2=g2, g3=g3)
    smoke_packet = {
        "schema": "MTTDiagnosticOneLoopTransportSmokeRun.v1",
        "status": "DIAGNOSTIC_ONE_LOOP_SMOKE_RUN_FINITE_NOT_ACCEPTANCE_VALUES",
        "engine": "one-loop SM matrix Yukawa/lambda beta equations with frozen M_Z gauge couplings",
        "acceptance_value_status": {
            "Y_u_MZ": "NOT_EMITTED_ACCEPTANCE_VALUE",
            "Y_d_MZ": "NOT_EMITTED_ACCEPTANCE_VALUE",
            "Y_e_MZ": "NOT_EMITTED_ACCEPTANCE_VALUE",
            "lambda_H_MZ": "NOT_EMITTED_ACCEPTANCE_VALUE",
        },
        "diagnostic_run": smoke,
        "known_limitations": [
            "gauge couplings held fixed at M_Z",
            "single common diagnostic start scale used for native mixed-scale inputs",
            "no pole-to-running mass conversion",
            "no threshold matching",
            "no covariance propagation",
            "not a replacement for accepted SM RG packages",
        ],
        "finite_values_emitted": True,
        "accepted_for_SM_parity": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    engine = {
        "schema": "MTTOneLoopSMRGEngineContract.v1",
        "status": "ONE_LOOP_RG_ENGINE_CONTRACT_AND_SMOKE_EXECUTION_BUILT",
        "equations": {
            "Y_u": "16pi^2 dY_u/dlnmu = Y_u[3/2(Y_u^dagY_u-Y_d^dagY_d)+T-(17/20 g1^2+9/4 g2^2+8g3^2)I]",
            "Y_d": "16pi^2 dY_d/dlnmu = Y_d[3/2(Y_d^dagY_d-Y_u^dagY_u)+T-(1/4 g1^2+9/4 g2^2+8g3^2)I]",
            "Y_e": "16pi^2 dY_e/dlnmu = Y_e[3/2 Y_e^dagY_e+T-(9/4 g1^2+9/4 g2^2)I]",
            "lambda_H": "16pi^2 dlambda/dlnmu = 24lambda^2+4lambda T-2H-lambda(9g2^2+9/5g1^2)+27/200g1^4+9/20g1^2g2^2+9/8g2^4",
        },
        "definitions": {
            "g1": "GUT-normalized U(1) coupling",
            "T": "Tr(3Yu^dagYu+3Yd^dagYd+Ye^dagYe)",
            "H": "Tr(3(Yu^dagYu)^2+3(Yd^dagYd)^2+(Ye^dagYe)^2)",
        },
        "numerical_method": "fixed-step RK4 over ln(mu)",
        "diagnostic_smoke_run_packet": rel(SMOKE),
        "acceptance_requirements_before_value_promotion": [
            "running gauge couplings or declared frozen-gauge approximation accepted by policy",
            "mass-scheme conversion for pole/rest/direct masses",
            "threshold matching at top, bottom, charm, tau, W, Z, and H conventions",
            "covariance or tolerance policy execution",
            "comparison against an external accepted SM RG implementation or analytic benchmark",
        ],
        "accepted_for_SM_parity": False,
    }

    cert_gate = {
        "schema": "MTTSelectedSMPacketCertificateIntegrationGate.v1",
        "status": "CERTIFICATE_GATE_RECHECKED_QA_SU3_STILL_OPEN",
        "source_certificate_status": final_packet["final_packet_certificate"]["status"],
        "critical_open_row": final_packet["final_packet_certificate"]["critical_open_row"],
        "actual_selected_sm_packet_anomaly_status": anomaly["status"],
        "qasu3_crossrepo_status": qasu3["status"],
        "can_attach_final_packet_certificate_now": False,
        "why_not": (
            "The selected SM packet certificate still needs a closed Qa/SU3 color/operator packet. "
            "The RG smoke run cannot substitute for source-side color/operator maps."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedRGEngineExecutionOrSelectedSMPacketCertificateIntegration",
        "status": STATUS,
        "inputs": {
            "transport_kernel_gate": rel(DATA / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit.candidate.json"),
            "common_scale_transport_kernel": rel(
                DATA
                / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
                / "yukawa_higgs_common_scale_transport_kernel.packet.json"
            ),
            "final_packet_certificate": rel(DATA / "sm_equivalence_commonscale_value_transport_and_final_packet_certificate.candidate.json"),
            "actual_selected_sm_packet_anomaly_audit": rel(DATA / "actual_selected_sm_packet_anomaly_audit.candidate.json"),
            "qasu3_crossrepo_import": rel(DATA / "sm_equivalence_crossrepo_qasu3_status_import.candidate.json"),
        },
        "output_packets": {
            "one_loop_sm_rg_engine_contract": rel(ENGINE),
            "diagnostic_one_loop_transport_smoke_run": rel(SMOKE),
            "selected_sm_packet_certificate_integration_gate": rel(CERT_GATE),
        },
        "theorem": {
            "name": "DiagnosticRGEngineExecutionAndPacketGateSeparationTheorem",
            "proved": True,
            "statement": (
                "A versioned one-loop SM RG engine can be executed on the native replay packet as a finite "
                "diagnostic smoke run, but it does not emit accepted common-scale Yukawa/Higgs values until "
                "threshold, mass-scheme, covariance, and benchmark-validation data are supplied. Independently, "
                "selected SM packet certification remains blocked by the Qa/SU3 color/operator packet."
            ),
        },
        "what_closes_now": {
            "one_loop_RG_engine_contract_built": True,
            "diagnostic_RG_smoke_run_executed": True,
            "finite_RG_outputs_verified_diagnostic_only": True,
            "SM_packet_certificate_gate_rechecked": True,
            "RG_value_gate_separated_from_QaSU3_source_gate": True,
        },
        "what_remains_open": {
            "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values": True,
            "accepted_lambda_H_MZ_value": True,
            "threshold_matching_values": True,
            "mass_scheme_conversion": True,
            "covariance_profile_likelihood_execution": True,
            "external_or_internal_RG_benchmark_validation": True,
            "QaSU3_color_operator_packet": True,
            "final_integrated_empirical_replay_audit": True,
            "SM_parity_closure": True,
        },
        "closure_decision": {
            "patched_SM_parity_closed": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": transport["status"],
        "next_required_artifact": NEXT_ARTIFACT,
        "observed_data_used": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_Selected_RGEngineExecution_or_SelectedSMPacketCertificateIntegration_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "observed_data_used": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT_ARTIFACT,
    }

    note = f"""# MTT Selected RGEngineExecution or SelectedSMPacketCertificateIntegration v1

Status: `{STATUS}`.

This artifact adds an executable one-loop SM RG diagnostic engine and runs a
finite smoke test on the current replay packet. The output is deliberately not
accepted as `Y_u(M_Z)`, `Y_d(M_Z)`, `Y_e(M_Z)`, or `lambda_H(M_Z)` because the
threshold, mass-scheme, covariance, and benchmark-validation gates are still
open.

It also rechecks the source-side certificate gate: Qa/SU3 color/operator packet
integration is still open and cannot be replaced by RG replay.

Next artifact: `{NEXT_ARTIFACT}`.
"""

    ENGINE.write_text(json.dumps(engine, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SMOKE.write_text(json.dumps(smoke_packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT_GATE.write_text(json.dumps(cert_gate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
