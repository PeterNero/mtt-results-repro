"""Audit the good-cover embedding or Deligne representative source-proof gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_chartatlas_delignecech_localfields_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_goodcoverembedding_or_deligne_representative_sourceproof_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_GoodCoverEmbedding_or_DeligneRepresentative_SourceProof_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_GOODCOVEREMBEDDING_DELIGNE_SOURCEPROOF_CURRENT_SOURCE_NOGO"
NEXT = "Selected_Heterotic_ProjectiveRhoE_ChartAtlas_DeligneCech_LocalFields_SourceAmendment_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    lane_a = data["lane_a_goodcover_embedding"]
    lane_b = data["lane_b_deligne_representative"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and request["status"] == "SOURCE_AMENDMENT_REQUIRED", (data["status"], cert["status"], request["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and request["next_required_artifact"] == NEXT, decision)
    check("both lanes attempted", lane_a["attempted"] is True and lane_b["attempted"] is True and cert["goodcover_embedding_attempted"] is True and cert["deligne_representative_attempted"] is True, (lane_a, lane_b))
    check("available scaffolds", decision["formal_nerve_incidence_available"] is True and decision["ctwist_deligne_template_available"] is True and cert["formal_nerve_incidence_available"] is True, decision)
    check("good cover not promoted", lane_a["selected_compact_iwasawa_nil_embedding_emitted"] is False and lane_a["coordinate_charts_emitted"] is False and lane_a["contractible_open_sets_emitted"] is False, lane_a)
    check("z3 not smooth-induced", lane_a["proof_z3_shadow_induced_by_smooth_cover"] is False and decision["tau_shadow_induced_by_smooth_cover"] is False, lane_a)
    check("deligne local fields absent", lane_b["local_B_i_A_ij_g_ijk_emitted"] is False and lane_b["explicit_good_cover_emitted"] is False and lane_b["tau_or_DD_class_emitted"] is False, lane_b)
    check("finite packet bridge guarded", data["finite_packet_bridge"]["finite_packet_can_supply_target_shadow"] is True and data["finite_packet_bridge"]["finite_packet_can_replace_smooth_local_fields"] is False, data["finite_packet_bridge"])
    check("request has both payload lanes", "required_good_cover_embedding_payload" in request and "required_deligne_cech_payload" in request and "finite_target_shadow_allowed_as_check_only" in request, request.keys())
    check("request leaves open", all(value is None for value in request["required_good_cover_embedding_payload"].values()) and all(value is None for value in request["required_deligne_cech_payload"].values()), request)
    check("forbidden shortcuts", "promoting the formal three-node nerve as a smooth cover" in request["forbidden_shortcuts"] and "using observed couplings, masses, or target residuals to choose the cover" in request["forbidden_shortcuts"], request["forbidden_shortcuts"])
    check("does not close S1", decision["S1_closed"] is False and cert["S1_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no target fitting", data["target_fitting_used"] is False and request["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("note records source request", NEXT in note and str(REQUEST.relative_to(ROOT)) in note and "not a substitute" in note, NOTE)

    print("\nSelected heterotic projective rho_E good-cover embedding / Deligne representative source-proof audit")


if __name__ == "__main__":
    main()
