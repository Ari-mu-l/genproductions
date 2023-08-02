from twiki page: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer

# activate McM tokens, must be done before setting cmsenv
cern-get-sso-cookie -u https://cms-pdmv-dev.cern.ch/mcm/ -o ~/private/dev-cookie.txt --krb --reprocess
cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt --krb --reprocess
source /afs/cern.ch/cms/PPD/PdmV/tools/McM/getCookie.sh

# setup the grid xertificate
# grid-proxy-init -debug -verify
voms-proxy-init -voms cms

# setup cmssw release (choose the CMSSW version according to datasets)
cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src
cmsenv

# add some modifications to display fraction of negative weights and equivalent luminosity for 1M events
# git cms-merge-topic perrozzi:xsecana_lumi
# the former line is still valid for some old CMSSW versions but we recommend to use the latter one currently

git cms-addpkg GeneratorInterface/Core
scram b -j8
cd ../../


# download the genproduction reposotory
git clone https://github.com/cms-sw/genproductions.git
cd genproductions/Utilities/calculateXSectionAndFilterEfficiency

# input parameters:
# -f wants the input file containing the list of dataset names (default) or McM prepID (requires -m)
# -c specifies the campaign, i.e. the string to be used to search for the secondary dataset name /.../*Moriond17*/*
# -d specifies the datatier to be used, i.e.  /.../*/MINIAODSIM
# -n number of events to be used for each dataset to compute the cross section
# -m use the McM prepID instead of the dataset names

# run using list of dataset names mode
./calculateXSectionAndFilterEfficiency.sh -f datasets.txt -c Moriond17 -d MINIAODSIM -n 1000000

# run using list of McM prepID mode
./calculateXSectionAndFilterEfficiency.sh -f datasets_mcm.txt  -m -n 1000000
