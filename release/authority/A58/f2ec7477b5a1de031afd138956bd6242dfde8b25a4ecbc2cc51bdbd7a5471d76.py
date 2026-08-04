from __future__ import annotations
import json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]; S="selected_sectorresolvedinternalfluctuationspectra_or_nonuniversalgaugethresholdpayload"; STATUS="MTT_SELECTED_SECTOR_SPECTRA_EIGHT_OF_TEN_CLOSED_SU2_SCALE_BINDING_AND_SU3_GAUGE_HESSIAN_OPEN"; NEXT="MTT_Selected_SU2FiniteScaleBinding_and_SU3AdjointGaugeHessianSource_v1"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def req(x,m):
    if not x: raise AssertionError(m)
def main():
    subprocess.run([sys.executable,str(R/"scripts"/f"build_{S}.py")],cwd=R,check=True); p=load(R/"candidate_data"/S/"eight_of_ten_spectra_and_two_gauge_candidates.packet.json"); c=load(R/"certificates"/f"{S}_certificate.json"); n=(R/"proof_corpus"/"MTT_Selected_SectorResolvedInternalFluctuationSpectra_or_NonUniversalGaugeThresholdPayload_v1.md").read_text(encoding="utf-8")
    req(p["status"]==c["status"]==STATUS,"status"); req(p["next_required_artifact"]==c["next_required_artifact"]==NEXT,"next"); req(all(p["checks"].values()),"checks"); req(p["closed_row_count"]==8 and c["matter_and_Higgs_rows_closed"]==7,"count"); req(p["remaining_rows"]==["SU2_gauge_ghost","SU3_gauge_ghost"],"remaining"); req(not p["rows"]["SU2_gauge_ghost"]["accepted"] and not p["rows"]["SU3_gauge_ghost"]["accepted"],"candidate promoted")
    for s in ["8/10","scale/basis intertwiner","eigenvalue `3`","not promoted",NEXT]: req(s.lower() in n.lower(),s)
    print(json.dumps(c,indent=2,sort_keys=True)); print("sector-resolved spectrum audit passed"); return 0
if __name__=="__main__": raise SystemExit(main())
