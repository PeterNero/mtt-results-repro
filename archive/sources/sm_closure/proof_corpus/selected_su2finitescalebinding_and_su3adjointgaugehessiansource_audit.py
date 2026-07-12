from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];S="selected_su2finitescalebinding_and_su3adjointgaugehessiansource";STATUS="MTT_SELECTED_SU2_SIMPLE_RESCALE_INSUFFICIENT_SU3_FINITE_ADJOINT_LIFT_RETIRED_FULL_STROMINGER_HESSIAN_PRIMARY";NEXT="MTT_Selected_SU2HolomorphicFiniteProjectionIntertwiner_and_SU3FullRealStromingerHessian_v1"
def l(p):return json.loads(p.read_text(encoding="utf-8"))
def q(x,m):
 if not x:raise AssertionError(m)
def main():
 subprocess.run([sys.executable,str(R/"scripts"/f"build_{S}.py")],cwd=R,check=True);p=l(R/"candidate_data"/S/"two_binding_attempt_and_route_decision.packet.json");c=l(R/"certificates"/f"{S}_certificate.json");n=(R/"proof_corpus"/"MTT_Selected_SU2FiniteScaleBinding_and_SU3AdjointGaugeHessianSource_v1.md").read_text(encoding="utf-8")
 q(p["status"]==c["status"]==STATUS,"status");q(p["next_required_artifact"]==c["next_required_artifact"]==NEXT,"next");q(all(p["checks"].values()),"checks");q(p["SU3_finite_adjoint_test"]["dimension"]==72,"dim");q(p["SU3_finite_adjoint_test"]["best_l2_residual"]>1e-3,"failed candidate");q(c["SU3_finite_adjoint_route_retired_as_color_threshold_source"],"retirement");q(not c["SU2_simple_scale_binding_closed"],"su2 overclaim")
 for s in ["four real torus","Kronecker sum","retired","8/10",NEXT]:q(s.lower() in n.lower(),s)
 print(json.dumps(c,indent=2,sort_keys=True));print("two final binding attempt audit passed");return 0
if __name__=="__main__":raise SystemExit(main())
