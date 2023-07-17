#import subprocess
import os
import numpy as np

#process = subprocess.Popen(['calculateXSectionAndFilterEfficiency.sh', 'datasets.txt', 'Moriond17', 'MINIAODSIM', '1000000'])
#process.wait()

file_list = [f for f in os.listdir(".") if f.startswith("xsec") and f.endswith(".log")]

dt = {'names':['totX_beforeMat', 'totX_afterMat', 'matchingEff', 'filterEff(weights)', 'filterEff(event)', 'totX_final', 'negWeightFrac', 'equivLumi'], 'formats':[np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64, np.float64]}

for fname in sorted(file_list):
    xsec_arr = np.zeros((2,8))
    xsec_arr.dtype=dt
    with open(fname) as f:
        contents = f.read().split("\n")
        try:
            dset = fname.split("xsec_")[-1].split(".")[0] # dataset name

            x_valerr = [c for c in contents if "Before matching: total cross section" in c][0].split("= ")[-1].split() # value
            xsec_arr["totX_beforeMat"][0]=float(x_valerr[0])
            xsec_arr["totX_beforeMat"][1]=float(x_valerr[2])
            
            x_valerr = [c for c in contents if "After matching: total cross section" in c][0].split("= ")[-1].split()
            xsec_arr["totX_afterMat"][0]=float(x_valerr[0])
            xsec_arr["totX_afterMat"][1]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Matching efficiency" in c][0].split("= ")[-1].split()
            xsec_arr["matchingEff"][0]=float(x_valerr[0])
            xsec_arr["matchingEff"][1]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Filter efficiency (taking into account weights)" in c][0].split("= ")[-1].split()
            xsec_arr["filterEff(weights)"][0]=float(x_valerr[0])
            xsec_arr["filterEff(weights)"][1]=float(x_valerr[2])

            x_valerr = [c for c in contents if "Filter efficiency (event-level)" in c][0].split("= ")[-1].split()
            xsec_arr["filterEff(event)"][0]=float(x_valerr[0])
            xsec_arr["filterEff(event)"][1]=float(x_valerr[2])

            x_valerr = [c for c in contents if "After filter: final cross section" in c][0].split("= ")[-1].split()
            xsec_arr["totX_final"][0]=float(x_valerr[0])
            xsec_arr["totX_final"][1]=float(x_valerr[2])

            x_valerr = [c for c in contents if "After filter: final fraction of events with negative weights" in c][0].split("= ")[-1].split()
            xsec_arr["negWeightFrac"][0]=float(x_valerr[0])
            xsec_arr["negWeightFrac"][1]=float(x_valerr[2])

            x_valerr  = [c for c in contents if "final equivalent lumi for 1M events (1/fb)" in c][0].split("= ")[-1].split()
            xsec_arr["equivLumi"][0]=float(x_valerr[0])
            xsec_arr["equivLumi"][1]=float(x_valerr[2])
        except:
	    print("Couldn't parse {}".format(fname))

    np.save(dset, xsec_arr)
    #print(xsec_arr)
