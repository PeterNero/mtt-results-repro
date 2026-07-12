from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];S="selected_su2holomorphicprojection_and_su3p0brstnormalization_lock";STATUS="MTT_SELECTED_SU3_P0_BRST_MEASURE_CLOSED_FINAL_SOURCE_LOCKED_SU2_PROJECTION_AND_SU3_PNONZERO_OPERATOR_OPEN";NEXT="MTT_Selected_SU2HolomorphicFiniteProjectionIntertwiner_and_SU3PNonzeroStromingerOperator_v1"
def l(p):return json.loads(p.read_text(encoding="utf-8"))
def q(x,m):
 if not x:raise AssertionError(m)
def main():
 subprocess.run([sys.executable,str(R/"scripts"/f"build_{S}.py")],cwd=R,check=True);p=l(R/"candidate_data"/S/"p0_brst_theorem_and_final_source_lock.packet.json");c=l(R/"certificates"/f"{S}_certificate.json");n=(R/"proof_corpus"/"MTT_Selected_SU2HolomorphicProjection_and_SU3P0BRSTNormalizationLock_v1.md").read_text(encoding="utf-8")
 q(p["status"]==c["status"]==STATUS,"status");q(p["next_required_artifact"]==c["next_required_artifact"]==NEXT,"next");q(all(p["checks"].values()),"checks");q(p["p0_BRST"]["net_logdet_coefficient"]==0 and c["SU3_p0_finite_part"]==0,"p0");q(c["final_open_source_obligations"]==2,"count");q(len(p["frontier_lock"]["authorities"])==3,"hash lock");q(not c["SU3_full_row_closed"] and not c["SU2_full_row_closed"],"overclaim")
 for s in ["Hodge decomposition","exactly two","certificate hashes","without using the old Qa target",NEXT]:q(s.lower() in n.lower(),s)
 print(json.dumps(c,indent=2,sort_keys=True));print("final gauge frontier lock audit passed");return 0
if __name__=="__main__":raise SystemExit(main())
