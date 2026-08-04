from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG="selected_gaugeinsertedheatsupertracesecondvariation_or_commonschemethresholdpayload"
STATUS="MTT_SELECTED_FINITE_GAUGE_SUPERTRACE_EXECUTED_ORDINARY_UNIVERSAL_KO6_ZERO_FULL_FLUCTUATION_COMPLEX_OPEN"
NEXT="MTT_Selected_GaugeFixedFluctuationComplexHessians_or_OneLoopThresholdSupertracePayload_v1"

def load(p): return json.loads(p.read_text(encoding="utf-8"))
def require(x,m):
    if not x: raise AssertionError(m)

def main():
    subprocess.run([sys.executable,str(ROOT/"scripts"/f"build_{SLUG}.py")],cwd=ROOT,check=True)
    p=load(ROOT/"candidate_data"/SLUG/"finite_grading_supertrace_and_fluctuation_complex_cutset.packet.json")
    c=load(ROOT/"certificates"/f"{SLUG}_certificate.json")
    t=load(ROOT/"candidate_data"/SLUG/"gauge_fixed_fluctuation_complex.template.json")
    n=(ROOT/"proof_corpus"/"MTT_Selected_GaugeInsertedHeatSupertraceSecondVariation_or_CommonSchemeThresholdPayload_v1.md").read_text(encoding="utf-8")
    require(p["status"]==c["status"]==STATUS,"status")
    require(p["next_required_artifact"]==c["next_required_artifact"]==NEXT,"next")
    require(all(p["checks"].values()),"checks")
    require(p["gauge_inserted_base_logdet_rows"]["relative_row_rank"]==0,"relative rank")
    require(c["KO6_supertrace_zero"] and not c["full_gauge_fixed_fluctuation_complex_closed"],"scope")
    require(all(not x["accepted"] for x in t["complex_rows"].values()),"empty block accepted")
    for s in ["KO6 chirality is not statistics grading","gauge one-forms","ghosts",NEXT]: require(s.lower() in n.lower(),s)
    print(json.dumps(c,indent=2,sort_keys=True)); print("gauge supertrace cutset audit passed"); return 0

if __name__=="__main__": raise SystemExit(main())
