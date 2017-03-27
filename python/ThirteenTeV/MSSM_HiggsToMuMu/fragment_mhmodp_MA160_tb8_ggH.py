COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2 = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     8.00000000E+00   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.52500000E+03   # At
        12     1.52500000E+03   # Ab
        13     1.52500000E+03   # Atau
        23     2.00000000E+02   # MUE
        25     8.00000000E+00   # TB
        26     1.60000000E+02   # MA0
        27     1.79063783E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95953966E+02   # MSf(1,1,1)
   1000011     5.02230315E+02   # MSf(1,2,1)
   2000011     5.01791166E+02   # MSf(2,2,1)
   1000002     1.49905523E+03   # MSf(1,3,1)
   2000002     1.49960120E+03   # MSf(2,3,1)
   1000001     1.50114342E+03   # MSf(1,4,1)
   2000001     1.50019935E+03   # MSf(2,4,1)
   1000014     4.95953966E+02   # MSf(1,1,2)
   1000013     5.02287423E+02   # MSf(1,2,2)
   2000013     5.01734023E+02   # MSf(2,2,2)
   1000004     1.49905557E+03   # MSf(1,3,2)
   2000004     1.49960196E+03   # MSf(2,3,2)
   1000003     1.50114608E+03   # MSf(1,4,2)
   2000003     1.50019670E+03   # MSf(2,4,2)
   1000016     9.97983134E+02   # MSf(1,1,3)
   1000015     1.00087980E+03   # MSf(1,2,3)
   2000015     1.00113715E+03   # MSf(2,2,3)
   1000006     8.76459993E+02   # MSf(1,3,3)
   2000006     1.13480602E+03   # MSf(2,3,3)
   1000005     1.00029110E+03   # MSf(1,4,3)
   2000005     1.00173863E+03   # MSf(2,4,3)
        25     1.19899947E+02   # Mh0
        35     1.64444533E+02   # MHH
        36     1.60000000E+02   # MA0
        37     1.78983060E+02   # MHp
   1000022     8.55232676E+01   # MNeu(1)
   1000023     1.48533508E+02   # MNeu(2)
   1000025    -2.08544382E+02   # MNeu(3)
   1000035     2.69959259E+02   # MNeu(4)
   1000024     1.42538558E+02   # MCha(1)
   1000037     2.69463237E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.92294412E-01   # Delta Mh0
        35     8.46041812E-02   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     1.24675580E-01   # Delta MHp
BLOCK NMIX
     1   1     9.16524941E-01   # ZNeu(1,1)
     1   2    -1.48827015E-01   # ZNeu(1,2)
     1   3     3.28768379E-01   # ZNeu(1,3)
     1   4    -1.72464213E-01   # ZNeu(1,4)
     2   1    -3.60533507E-01   # ZNeu(2,1)
     2   2    -6.94553422E-01   # ZNeu(2,2)
     2   3     4.87589577E-01   # ZNeu(2,3)
     2   4    -3.87127290E-01   # ZNeu(2,4)
     3   1     8.88164034E-02   # ZNeu(3,1)
     3   2    -1.23495912E-01   # ZNeu(3,2)
     3   3    -6.79839468E-01   # ZNeu(3,3)
     3   4    -7.17411112E-01   # ZNeu(3,4)
     4   1    -1.48691861E-01   # ZNeu(4,1)
     4   2     6.92960910E-01   # ZNeu(4,2)
     4   3     4.38162133E-01   # ZNeu(4,3)
     4   4    -5.52910348E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.16600092E-01   # UCha(1,1)
     1   2     7.87276525E-01   # UCha(1,2)
     2   1     7.87276525E-01   # UCha(2,1)
     2   2     6.16600092E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.87276525E-01   # VCha(1,1)
     1   2     6.16600092E-01   # VCha(1,2)
     2   1     6.16600092E-01   # VCha(2,1)
     2   2     7.87276525E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     2.68542985E-01   # USf(1,1)
     1   2     9.63267702E-01   # USf(1,2)
     2   1     9.63267702E-01   # USf(2,1)
     2   2    -2.68542985E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08219880E-01   # USf(1,1)
     1   2    -7.05991927E-01   # USf(1,2)
     2   1     7.05991927E-01   # USf(2,1)
     2   2     7.08219880E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     1.05560993E-01   # USf(1,1)
     1   2     9.94412830E-01   # USf(1,2)
     2   1     9.94412830E-01   # USf(2,1)
     2   2    -1.05560993E-01   # USf(2,2)
BLOCK ALPHA
              -3.74250012E-01   # Alpha
BLOCK DALPHA
               1.34372647E-02   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     8.00000000E+00   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.52500000E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.52500000E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.52500000E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     2.36628643E-05   # Yf(1,1)
     2   2     4.89272942E-03   # Yf(2,2)
     3   3     8.22890607E-02   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.73651530E-05   # Yf(1,1)
     2   2     7.44386224E-03   # Yf(2,2)
     3   3     1.00254816E+00   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     2.75587622E-04   # Yf(1,1)
     2   2     4.36339446E-03   # Yf(2,2)
     3   3     1.87825439E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.25490818E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.52888595E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     2.86433795E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99998281E-01   # UASf(1,1)
     1   4    -1.85432469E-03   # UASf(1,4)
     2   2     9.46979903E-01   # UASf(2,2)
     2   5    -3.21292799E-01   # UASf(2,5)
     3   3     2.68542985E-01   # UASf(3,3)
     3   6     9.63267702E-01   # UASf(3,6)
     4   1     1.85432469E-03   # UASf(4,1)
     4   4     9.99998281E-01   # UASf(4,4)
     5   2     3.21292799E-01   # UASf(5,2)
     5   5     9.46979903E-01   # UASf(5,5)
     6   3     9.63267702E-01   # UASf(6,3)
     6   6    -2.68542985E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     9.99999999E-01   # UASf(1,1)
     1   4     4.58109695E-05   # UASf(1,4)
     2   2     9.99807386E-01   # UASf(2,2)
     2   5     1.96262875E-02   # UASf(2,5)
     3   3     7.08219880E-01   # UASf(3,3)
     3   6    -7.05991927E-01   # UASf(3,6)
     4   1    -4.58109695E-05   # UASf(4,1)
     4   4     9.99999999E-01   # UASf(4,4)
     5   2    -1.96262875E-02   # UASf(5,2)
     5   5     9.99807386E-01   # UASf(5,5)
     6   3     7.05991927E-01   # UASf(6,3)
     6   6     7.08219880E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99994353E-01   # UASf(1,1)
     1   4    -3.36058680E-03   # UASf(1,4)
     2   2     9.98595312E-01   # UASf(2,2)
     2   5    -5.29849306E-02   # UASf(2,5)
     3   3     1.05560993E-01   # UASf(3,3)
     3   6     9.94412830E-01   # UASf(3,6)
     4   1     3.36058680E-03   # UASf(4,1)
     4   4     9.99994353E-01   # UASf(4,4)
     5   2     5.29849306E-02   # UASf(5,2)
     5   5     9.98595312E-01   # UASf(5,5)
     6   3     9.94412830E-01   # UASf(6,3)
     6   6    -1.05560993E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.89778867E-01   # UH(1,1)
     1   2     1.42610636E-01   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -1.42610636E-01   # UH(2,1)
     2   2     9.89778867E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     2.06641926E-02   # Gamma(h0)
     3.88108535E-04   2        22        22   # BR(h0 -> photon photon)
     1.63969461E-04   2        22        23   # BR(h0 -> photon Z)
     2.49705200E-03   2        23        23   # BR(h0 -> Z Z)
     2.28534959E-02   2       -24        24   # BR(h0 -> W W)
     8.85180984E-03   2        21        21   # BR(h0 -> gluon gluon)
     8.02928889E-09   2       -11        11   # BR(h0 -> Electron electron)
     3.57152576E-04   2       -13        13   # BR(h0 -> Muon muon)
     1.02369541E-01   2       -15        15   # BR(h0 -> Tau tau)
     3.32206153E-08   2        -2         2   # BR(h0 -> Up up)
     4.60115277E-03   2        -4         4   # BR(h0 -> Charm charm)
     1.30600827E-06   2        -1         1   # BR(h0 -> Down down)
     3.27981629E-04   2        -3         3   # BR(h0 -> Strange strange)
     8.57588389E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     1.77791730E-01   # Gamma(HH)
    -9.10110081E-06   2        22        22   # BR(HH -> photon photon)
    -4.43409246E-05   2        22        23   # BR(HH -> photon Z)
    -1.83084044E-03   2        23        23   # BR(HH -> Z Z)
    -7.52407082E-02   2       -24        24   # BR(HH -> W W)
    -1.91578764E-03   2        21        21   # BR(HH -> gluon gluon)
    -8.25068171E-09   2       -11        11   # BR(HH -> Electron electron)
     3.67035411E-04   2       -13        13   # BR(HH -> Muon muon)
    -1.04981589E-01   2       -15        15   # BR(HH -> Tau tau)
    -7.55174480E-10   2        -2         2   # BR(HH -> Up up)
    -1.04680127E-04   2        -4         4   # BR(HH -> Charm charm)
    -1.25614758E-06   2        -1         1   # BR(HH -> Down down)
    -3.15460513E-04   2        -3         3   # BR(HH -> Strange strange)
    -8.15189182E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -9.67594140E-09   2        23        36   # BR(HH -> Z A0)
DECAY        36     1.81452954E-01   # Gamma(A0)
     1.94421439E-06   2        22        22   # BR(A0 -> photon photon)
     1.78536638E-06   2        22        23   # BR(A0 -> photon Z)
     4.80850947E-04   2        21        21   # BR(A0 -> gluon gluon)
     8.89196716E-09   2       -11        11   # BR(A0 -> Electron electron)
     3.95560724E-04   2       -13        13   # BR(A0 -> Muon muon)
     1.13206008E-01   2       -15        15   # BR(A0 -> Tau tau)
     7.76606481E-11   2        -2         2   # BR(A0 -> Up up)
     1.08548750E-05   2        -4         4   # BR(A0 -> Charm charm)
     1.36127008E-06   2        -1         1   # BR(A0 -> Down down)
     3.41860473E-04   2        -3         3   # BR(A0 -> Strange strange)
     8.85531066E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     2.86985087E-05   2        23        25   # BR(A0 -> Z h0)
DECAY        37     2.36480017E-02   # Gamma(Hp)
     8.01692202E-08   2       -11        12   # BR(Hp -> Electron nu_e)
     3.42748157E-03   2       -13        14   # BR(Hp -> Muon nu_mu)
     9.69329923E-01   2       -15        16   # BR(Hp -> Tau nu_tau)
     1.07051959E-05   2        -1         2   # BR(Hp -> Down up)
     1.20170071E-04   2        -3         2   # BR(Hp -> Strange up)
     7.39494475E-05   2        -5         2   # BR(Hp -> Bottom up)
     4.52226604E-06   2        -1         4   # BR(Hp -> Down charm)
     2.76889442E-03   2        -3         4   # BR(Hp -> Strange charm)
     1.03546109E-02   2        -5         4   # BR(Hp -> Bottom charm)
     1.79849651E-06   2        -1         6   # BR(Hp -> Down top)
     3.91980869E-05   2        -3         6   # BR(Hp -> Strange top)
     1.15526806E-02   2        -5         6   # BR(Hp -> Bottom top)
     2.16009756E-03   2        24        25   # BR(Hp -> W h0)
     3.15663929E-05   2        24        35   # BR(Hp -> W HH)
     1.24322249E-04   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)