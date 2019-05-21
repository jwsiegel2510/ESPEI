"""Databases and datasets used in common tests"""

import yaml

YAML_LOADER = yaml.FullLoader

CU_MG_TDB = """$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Date: 2017-09-27 21:10
$ Components: CU, MG, VA
$ Phases: CUMG2, FCC_A1, HCP_A3, LAVES_C15, LIQUID
$ Generated by brandon (pycalphad 0.5.2.post1)
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

ELEMENT CU BLANK 0 0 0 !
ELEMENT MG BLANK 0 0 0 !
ELEMENT VA BLANK 0 0 0 !

FUNCTION GFCCCU 298.15 GHSERCU#; 3200.0 N !
FUNCTION GFCCMG 298.15 -0.9*T + GHSERMG# + 2600; 3000.0 N !
FUNCTION GHCPCU 298.15 0.2*T + GHSERCU# + 600; 3200.0 N !
FUNCTION GHCPMG 298.15 GHSERMG#; 3000.0 N !
FUNCTION GHSERCU 298.15 1.29223E-7*T**3 - 0.00265684*T**2 - 24.112392*T*LN(T)
   + 130.485235*T - 7770.458 + 52478*T**(-1); 1357.77 Y -31.38*T*LN(T) +
   183.803828*T - 13542.026 + 3.64167E+29*T**(-9); 3200.0 N !
FUNCTION GHSERMG 298.15 -1.393669E-6*T**3 + 0.0004858*T**2 -
   26.1849782*T*LN(T) + 143.675547*T - 8367.34 + 78950*T**(-1); 923.0 Y
   -34.3088*T*LN(T) + 204.716215*T - 14130.185 + 1.038192E+28*T**(-9); 3000.0
   N !
FUNCTION GHSERVA 1 0; 10000 N !
FUNCTION GLAVCU 298.15 3.87669E-7*T**3 - 0.00797052*T**2 - 72.337176*T*LN(T)
   + 391.455705*T - 8311.374 + 157434*T**(-1); 1357.77 Y -94.14*T*LN(T) +
   551.411484*T - 25626.078 + 1.092501E+30*T**(-9); 3200.0 N !
FUNCTION GLAVMG 298.15 -4.181007E-6*T**3 + 0.0014574*T**2 -
   78.5549346*T*LN(T) + 431.026641*T - 10102.02 + 236850*T**(-1); 923.0 Y
   -102.9264*T*LN(T) + 614.148645*T - 27390.555 + 3.11458E+28*T**(-9); 3000.0
   N !
FUNCTION GLIQCU 298.15 -5.8489E-21*T**7 - 9.511904*T + GHSERCU# + 12964.735;
   1357.77 Y -31.38*T*LN(T) + 173.881484*T - 46.545; 3200.0 N !
FUNCTION GLIQMG 298.15 -8.0176E-20*T**7 - 8.83693*T + GHSERMG# + 8202.243;
   923.0 Y -34.3088*T*LN(T) + 195.324057*T - 5439.869; 3000.0 N !
FUNCTION VV0000 1 -32429.6; 10000 N !
FUNCTION VV0001 1 -4.12896; 10000 N !
FUNCTION VV0002 1 8.2363; 10000 N !
FUNCTION VV0003 1 -14.0865; 10000 N !
FUNCTION VV0004 1 -11.2723; 10000 N !
FUNCTION VV0005 1 11.1114; 10000 N !
FUNCTION VV0006 1 -8.29125; 10000 N !
FUNCTION VV0007 1 -14.9845; 10000 N !
FUNCTION VV0008 1 -40470.2; 10000 N !
FUNCTION VV0009 1 104160.0; 10000 N !
FUNCTION VV0010 1 17766.4; 10000 N !
FUNCTION VV0011 1 150325.0; 10000 N !
FUNCTION VV0012 1 21243.0; 10000 N !
FUNCTION VV0013 1 214671.0; 10000 N !
FUNCTION VV0014 1 14321.1; 10000 N !
FUNCTION VV0015 1 -4923.18; 10000 N !
FUNCTION VV0016 1 -1962.8; 10000 N !
FUNCTION VV0017 1 -31626.6; 10000 N !

TYPE_DEFINITION % SEQ * !
DEFINE_SYSTEM_DEFAULT ELEMENT 2 !
DEFAULT_COMMAND DEFINE_SYSTEM_ELEMENT VA !

PHASE CUMG2 %  2 1 2 !
CONSTITUENT CUMG2 :CU:MG: !

PHASE FCC_A1 %  2 1 1 !
CONSTITUENT FCC_A1 :CU,MG:VA: !

PHASE HCP_A3 %  2 1 0.5 !
CONSTITUENT HCP_A3 :CU,MG:VA: !

PHASE LAVES_C15 %  2 2 1 !
CONSTITUENT LAVES_C15 :CU,MG:CU,MG: !

PHASE LIQUID %  1 1 !
CONSTITUENT LIQUID :CU,MG: !



$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                     CU                                     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

PARAMETER G(FCC_A1,CU:VA;0) 1 GFCCCU#; 10000 N !
PARAMETER G(HCP_A3,CU:VA;0) 1 GHCPCU#; 10000 N !
PARAMETER G(LAVES_C15,CU:CU;0) 1 GLAVCU#; 10000 N !
PARAMETER G(LIQUID,CU;0) 1 GLIQCU#; 10000 N !


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                     MG                                     $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

PARAMETER G(FCC_A1,MG:VA;0) 1 GFCCMG#; 10000 N !
PARAMETER G(HCP_A3,MG:VA;0) 1 GHCPMG#; 10000 N !
PARAMETER G(LAVES_C15,MG:MG;0) 1 GLAVMG#; 10000 N !
PARAMETER G(LIQUID,MG;0) 1 GLIQMG#; 10000 N !


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$                                   CU-MG                                    $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

PARAMETER G(CUMG2,CU:MG;0) 1 GHSERCU# + 2*GHSERMG# + VV0000#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;0) 1 VV0003#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;1) 1 VV0002#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;2) 1 VV0001#; 10000 N !
PARAMETER L(HCP_A3,CU,MG:VA;0) 1 VV0007#; 10000 N !
PARAMETER L(HCP_A3,CU,MG:VA;1) 1 VV0006#; 10000 N !
PARAMETER L(HCP_A3,CU,MG:VA;2) 1 VV0005#; 10000 N !
PARAMETER L(HCP_A3,CU,MG:VA;3) 1 VV0004#; 10000 N !
PARAMETER G(LAVES_C15,CU:MG;0) 1 2*GHSERCU# + GHSERMG# + VV0008#; 10000 N !
PARAMETER G(LAVES_C15,MG:CU;0) 1 GHSERCU# + 2*GHSERMG# + VV0009#; 10000 N !
PARAMETER L(LAVES_C15,CU:CU,MG;0) 1 VV0010#; 10000 N !
PARAMETER L(LAVES_C15,CU,MG:CU;0) 1 VV0011#; 10000 N !
PARAMETER L(LAVES_C15,CU,MG:MG;0) 1 VV0012#; 10000 N !
PARAMETER L(LAVES_C15,MG:CU,MG;0) 1 VV0013#; 10000 N !
PARAMETER L(LIQUID,CU,MG;0) 1 VV0017#; 10000 N !
PARAMETER L(LIQUID,CU,MG;1) 1 VV0016#; 10000 N !
PARAMETER L(LIQUID,CU,MG;2) 1 VV0015#; 10000 N !
PARAMETER L(LIQUID,CU,MG;3) 1 VV0014#; 10000 N !

"""

CU_MG_TDB_FCC_ONLY = """$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$ Cu-Mg, FCC only
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

ELEMENT CU BLANK 0 0 0 !
ELEMENT MG BLANK 0 0 0 !
ELEMENT VA BLANK 0 0 0 !

FUNCTION GFCCCU 298.15 GHSERCU#; 3200.0 N !
FUNCTION GFCCMG 298.15 -0.9*T + GHSERMG# + 2600; 3000.0 N !
FUNCTION GHSERCU 298.15 1.29223E-7*T**3 - 0.00265684*T**2 - 24.112392*T*LN(T)
   + 130.485235*T - 7770.458 + 52478*T**(-1); 1357.77 Y -31.38*T*LN(T) +
   183.803828*T - 13542.026 + 3.64167E+29*T**(-9); 3200.0 N !
FUNCTION GHSERMG 298.15 -1.393669E-6*T**3 + 0.0004858*T**2 -
   26.1849782*T*LN(T) + 143.675547*T - 8367.34 + 78950*T**(-1); 923.0 Y
   -34.3088*T*LN(T) + 204.716215*T - 14130.185 + 1.038192E+28*T**(-9); 3000.0
   N !
FUNCTION GHSERVA 1 0; 10000 N !
FUNCTION VV0001 1 -4.12896; 10000 N !
FUNCTION VV0002 1 8.2363; 10000 N !
FUNCTION VV0003 1 -14.0865; 10000 N !

TYPE_DEFINITION % SEQ * !
DEFINE_SYSTEM_DEFAULT ELEMENT 2 !
DEFAULT_COMMAND DEFINE_SYSTEM_ELEMENT VA !

PHASE FCC_A1 %  2 1 1 !
CONSTITUENT FCC_A1 :CU,MG:VA: !

PARAMETER G(FCC_A1,CU:VA;0) 1 GFCCCU#; 10000 N !
PARAMETER G(FCC_A1,MG:VA;0) 1 GFCCMG#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;0) 1 VV0003#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;1) 1 VV0002#; 10000 N !
PARAMETER L(FCC_A1,CU,MG:VA;2) 1 VV0001#; 10000 N !

"""


CU_MG_EXP_ACTIVITY = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["LIQUID"],
  "solver": {
    "mode": "manual",
  },
  "reference_state": {
    "phases": ["LIQUID"],
    "conditions": {
      "P": 101325,
      "T": 1200,
      "X_CU": 0.0
    }
  },
  "conditions": {
    "P": 101325,
    "T": 1200,
    "X_CU": [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
  },

  "output": "ACR_MG",
    "values":   [[[0.0057,0.0264,0.0825,0.1812,0.2645,0.4374,0.5852,0.7296,0.882,1.0]]],
  "reference": "garg1973thermodynamic",
  "comment": "Digitized Figure "
}
""", Loader=YAML_LOADER)


CU_MG_HM_MIX_T_CUMG2 = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["CUMG2"],
  "solver": {
    "sublattice_site_ratios": [1, 2],
    "sublattice_configurations": [["CU", "MG"]],
    "mode": "manual"
  },
  "conditions": {
    "P": 101325,
    "T": [300, 400],
  },

  "output": "HM_MIX",
    "values":   [[[10], [100]]],
  "reference": "FAKE DATA",
  "comment": "FAKE DATA"
}
""", Loader=YAML_LOADER)


CU_MG_SM_MIX_T_X_FCC_A1 = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["FCC_A1"],
  "solver": {
    "sublattice_site_ratios": [1, 1],
    "sublattice_occupancies": [
    [[0.5, 0.5], 1],
    [[0.1, 0.9], 1]
    ],
    "sublattice_configurations": [
    [["CU", "MG"], "VA"],
    [["CU", "MG"], "VA"]
    ],
    "mode": "manual"
  },
  "conditions": {
    "P": 101325,
    "T": [300, 400],
  },

  "output": "SM_MIX",
    "values":   [[[10, 50], [100, 500]]],
  "reference": "FAKE DATA",
  "comment": "FAKE DATA",
  "excluded_model_contributions": ["idmix"]
}
""", Loader=YAML_LOADER)


CU_MG_CPM_MIX_X_HCP_A3 = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["HCP_A3"],
  "solver": {
    "sublattice_site_ratios": [1, 1],
    "sublattice_occupancies": [
    [[0.5, 0.5], 1],
    [[0.1, 0.9], 1]
    ],
    "sublattice_configurations": [
    [["CU", "MG"], "VA"],
    [["CU", "MG"], "VA"]
    ],
    "mode": "manual"
  },
  "conditions": {
    "P": 101325,
    "T": 300,
  },

  "output": "CPM_MIX",
    "values":   [[[10, 15]]],
  "reference": "FAKE DATA",
  "comment": "FAKE DATA"
}
""", Loader=YAML_LOADER)


CU_MG_HM_MIX_SINGLE_FCC_A1 = yaml.load("""
{
    "components": ["CU", "MG"],
    "phases": ["FCC_A1"],
    "solver": {
        "sublattice_site_ratios": [1],
        "sublattice_occupancies": [[[0.5, 0.5], 1]],
        "sublattice_configurations": [[["CU", "MG"], "VA"]],
        "mode": "manual"
    },
    "conditions": {
        "P": 101325,
        "T": 300.0
    },
    "output": "HM_MIX",
    "values": [[[-1000]]]
}
""", Loader=YAML_LOADER)


CU_MG_DATASET_ZPF_ZERO_ERROR = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["FCC_A1", "LAVES_C15"],
  "conditions": {
    "P": 101325,
    "T": 600
  },
  "output": "ZPF",
    "values":   [
    [["FCC_A1", ["CU"], [0.99980142076590905]], ["LAVES_C15", ["CU"], [0.66713918519314885]]]
    ],
  "reference": "testing",
  "comment": "From a calculation of: `equilibrium(Database(CU_MG_TDB), ['CU','MG','VA'], ['FCC_A1', 'LAVES_C15'], {v.P: 101325, v.X('MG'): 0.1, v.T: 600})`"
}
""", Loader=YAML_LOADER)


CU_MG_DATASET_ZPF_WORKING = yaml.load("""{
    "components": ["CU", "MG", "VA"],
    "phases": ["LIQUID", "FCC_A1"],
    "conditions": {
      "P": 101325,
      "T": [1337.97, 1262.238]
    },
    "broadcast_conditions": false,
    "output": "ZPF",
    "values":   [
        [["LIQUID", ["MG"], [0.0246992]], ["FCC_A1", ["MG"],  [null]]],
        [["LIQUID", ["MG"], [0.0712664]], ["FCC_A1", ["MG"],  [null]]]
    ],
    "reference": "Sahmen1908"
}
""", Loader=YAML_LOADER)


A_B_DATASET_BINARY_PHASE_EQUILIBRIA = yaml.load("""{
  "components": ["A", "B"],
  "phases": ["PHASE_1", "PHASE_2", "PHASE_3"],
  "conditions": {
    "P": 101325,
    "T": [100, 200, 300]
  },
  "output": "ZPF",
    "values":   [
    [["PHASE_1", ["B"], [0.25]], ["PHASE_2", ["B"], [null]]],
    [["PHASE_1", ["B"], [0.25]], ["PHASE_2", ["B"], [0.5]]],
    [["PHASE_1", ["B"], [0.25]], ["PHASE_2", ["B"], [0.5]], ["PHASE_3", ["B"], [0.75]]]
   ],
  "reference": "testing",
  "comment": "Examples for 1. one side of tieline, 2. a full tieline, 3. a 3 phase equilibria. For MPL visual checking that plot is correct"
}
""", Loader=YAML_LOADER)


A_B_C_DATASET_TERNARY_PHASE_EQUILIBRIA = yaml.load("""{
  "components": ["A", "B", "C"],
  "phases": ["PHASE_1", "PHASE_2", "PHASE_3"],
  "conditions": {
    "P": 101325,
    "T": [300, 300, 300]
  },
  "output": "ZPF",
    "values":   [
    [["PHASE_1", ["B", "C"], [0.1, 0.1]], ["PHASE_2", ["B", "C"], [null, null]]],
    [["PHASE_1", ["B", "C"], [0.2, 0.5]], ["PHASE_2", ["B", "C"], [0.3, 0.6]]],
    [["PHASE_1", ["B", "C"], [0.2, 0.2]], ["PHASE_1", ["B", "C"], [0.3, 0.3]], ["PHASE_2", ["B", "C"], [0.5, 0.1]]],
   ],
  "reference": "testing",
  "comment": "Examples for 1. one side of tieline, 2. a full tieline, 3. a 3 phase equilibria. For MPL visual checking that plot is correct"
}
""", Loader=YAML_LOADER)


CU_MG_DATASET_THERMOCHEMICAL_STRING_VALUES = yaml.load("""{
  "components": ["CU", "MG", "VA"],
  "phases": ["CUMG2"],
  "solver": {
    "sublattice_site_ratios": ["1", "2"],
    "sublattice_configurations": [["CU", "MG"]],
    "mode": "manual"
  },
  "conditions": {
    "P": "101325",
    "T": ["300", "400"],
  },

  "output": "HM_MIX",
    "values":   [[["10"], ["100"]]],
  "reference": "FAKE DATA",
  "comment": "FAKE DATA"
}
""", Loader=YAML_LOADER)


CU_MG_DATASET_ZPF_STRING_VALUES = yaml.load("""{
    "components": ["CU", "MG", "VA"],
    "phases": ["LIQUID", "FCC_A1"],
    "conditions": {
      "P": "101325",
      "T": ["1337.97", "1262.238"]
    },
    "broadcast_conditions": false,
    "output": "ZPF",
    "values":   [
        [["LIQUID", ["MG"], ["0.0246992"]], ["FCC_A1", ["MG"],  [null]]],
        [["LIQUID", ["MG"], ["0.0712664"]], ["FCC_A1", ["MG"],  [null]]]
    ],
    "reference": "Sahmen1908"
}
""", Loader=YAML_LOADER)


AL_CO_CR_A2_PHASE_MODELS = {
  "components": ["AL", "CO", "CR"],
  "phases": {
         "BCC_A2": {
            "sublattice_model": [["AL", "CO", "CR"]],
            "sublattice_site_ratios": [1]
         }
    }
}

AL_CO_CR_B2_PHASE_MODELS = {
  "components": ["AL", "CO", "CR"],
  "phases": {
         "BCC_B2": {
            "sublattice_model": [["AL", "CO", "CR"], ["AL", "CO", "CR"]],
            "sublattice_site_ratios": [0.5, 0.5]
         }
    }
}


AL_CO_CR_A2_TERNARY_SYMMETRIC_DATASET = {
    "components": ["AL", "CO", "CR"],
    "phases": ["BCC_A2"],
    "solver": {
        "mode": "manual",
        "sublattice_site_ratios": [1],
        "sublattice_occupancies": [[[0.333, 0.333, 0.334]]],
        "sublattice_configurations": [[["AL", "CO", "CR"]]]
    },
    "conditions": {
        "P": 101325,
        "T": 298.15
        },
    "output": "HM_MIX",
    "values":   [[[-7860.0]]],
    "reference": "liu2015first",
    "comment": "Ternary disordered BCC from Table 4"
}


AL_CO_A2_BINARY_SYMMETRIC_DATASET = {
    "components": ["AL", "CO"],
    "phases": ["BCC_A2"],
    "solver": {
        "mode": "manual",
        "sublattice_site_ratios": [1],
        "sublattice_occupancies": [[[0.5, 0.5]]],
        "sublattice_configurations": [[["AL", "CO"]]]
    },
    "conditions": {
        "P": 101325,
        "T": 298.15
    },
    "output": "HM_MIX",
    "values":   [[[-1000.0]]],
    "reference": "liu2015first",
    "comment": "Ternary disordered BCC from Table 4"
}


AL_CO_CR_BCC_A2_TERNARY_NON_SYMMETRIC_DATASET = {
    "components": ["AL", "CO", "CR"],
    "phases": ["BCC_A2"],
    "solver": {
        "mode": "manual",
        "sublattice_site_ratios": [1, 1],
        "sublattice_occupancies": [
            [[0.25, 0.25, 0.5]],
            [[0.25, 0.5, 0.25]],
            [[0.5, 0.25, 0.25]]
        ],
        "sublattice_configurations": [
            [["AL", "CO", "CR"]],
            [["AL", "CO", "CR"]],
            [["AL", "CO", "CR"]]
        ]
    },
    "conditions": {
        "P": 101325,
        "T": 298.15
    },
    "output": "HM_MIX",
    "values":   [[[-70.3125, -62.5, -54.6875]]],
    "reference": "",
    "comment": ""
}

AL_CO_CR_BCC_B2_TERNARY_NON_SYMMETRIC_DATASET = {
    "components": ["AL", "CO", "CR"],
    "phases": ["BCC_B2"],
    "solver": {
        "mode": "manual",
        "sublattice_site_ratios": [0.5, 0.5],
        "sublattice_occupancies": [

            [[0.25, 0.25, 0.5], 1],
            [[0.25, 0.5, 0.25], 1],
            [[0.5, 0.25, 0.25], 1]
        ],
        "sublattice_configurations": [
            [["AL", "CO", "CR"], "AL"],
            [["AL", "CO", "CR"], "AL"],
            [["AL", "CO", "CR"], "AL"]
        ]
    },
    "conditions": {
        "P": 101325,
        "T": 298.15
    },
    "output": "HM_MIX",
    "values":   [[[-140.625, -125.0, -109.375]]],
    "reference": "",
    "comment": ""
}

CU_ZN_LIQUID_PHASE_MODEL = {
  "components": ["CU", "ZN"], "refdata": "SGTE91",
  "phases": {"LIQUID" : {
	"sublattice_model": [["CU", "ZN"]],
	"sublattice_site_ratios": [1]}}
}

CU_ZN_CPM_MIX_EXPR_TO_FLOAT = {
"components": ["CU", "ZN"], "phases": ["LIQUID"],
"solver": {"mode": "manual", "sublattice_site_ratios": [1],
           "sublattice_configurations": [[["CU", "ZN"]],[["CU", "ZN"]],[["CU", "ZN"]]],
"sublattice_occupancies": [[[0.5, 0.5]], [[0.1, 0.9]], [[0.8, 0.2]]]},
"conditions": {"P": 101325, "T": 300},
"output": "CPM_MIX",
"values": [[[11.1425, -5.0, 5.0]]]
}

CU_ZN_SM_MIX_EXPR_TO_FLOAT = {
"components": ["CU", "ZN"],"phases": ["LIQUID"],
"solver": {"mode": "manual", "sublattice_site_ratios": [1],
           "sublattice_configurations": [[["CU", "ZN"]]],
"sublattice_occupancies": [[[0.25, 0.75]]]},
"conditions": {"P": 101325, "T": 600},
"output": "SM_MIX",
"values": [[[-9.952211364]]],
"excluded_model_contributions": ["idmix"]
}

###############################################################################
# CR-FE
###############################################################################

CR_FE_PHASE_MODELS = {
    "components": ["CR", "FE", "VA"],
    "phases": {
           "BCC_A2": {
              "sublattice_model": [["CR", "FE"], ["VA"]],
              "sublattice_site_ratios": [1, 3]
           }
      }
  }

CR_FE_HM_MIX_EXCLUDED_MAG = {
"components": ["CR", "FE", "VA"],"phases": ["BCC_A2"],
"solver": {"mode": "manual", "sublattice_site_ratios": [1, 3],
           "sublattice_configurations": [[["CR", "FE"], "VA"]],
"sublattice_occupancies": [[[0.5, 0.5], 1.0]]},
"conditions": {"P": 101325, "T": 300},
"output": "HM_MIX",
"values": [[[10000]]],
"excluded_model_contributions": ["mag"]
}

CR_FE_HM_MIX_WITH_MAG = {
"components": ["CR", "FE", "VA"],"phases": ["BCC_A2"],
"solver": {"mode": "manual", "sublattice_site_ratios": [1, 3],
           "sublattice_configurations": [[["CR", "FE"], "VA"]],
"sublattice_occupancies": [[[0.5, 0.5], 1.0]]},
"conditions": {"P": 101325, "T": 300},
"output": "HM_MIX",
"values": [[[7128.41104097]]]
}

CR_FE_INITIAL_TDB_CONTRIBUTIONS = """$ Cr-Fe database with only magnetic parts
$ As assessed by Xiong doi:10.1016/j.calphad.2011.05.002
 ELEMENT VA   VACUUM           0.0000E+00  0.0000E+00  0.0000E+00!
 ELEMENT FE   BCC_A2           5.5847E+01  4.4890E+03  2.7280E+01!
 ELEMENT CR   BCC_A2           5.1996E+01  4.0500E+03  2.3560E+01!
$             **********   FCC_A1   *********
 TYPE_DEFINITION G GES AM-PH FCC_A1 MAG -3 0.25 !
 PHASE FCC_A1  %G  2 1   1 !
    CONSTITUENT FCC_A1  :CR,FE : VA :  !
   PARAMETER TC(FCC_A1,FE:VA;0)  2.98150E+02  -201;    6000 N !
   PARAMETER BMAGN(FCC_A1,FE:VA;0)  2.98150E+02  -2.1; 6000 N !
   PARAMETER TC(FCC_A1,CR:VA;0)  2.98150E+02  -1109;   6000 N !
   PARAMETER BMAGN(FCC_A1,CR:VA;0)  2.98150E+02  -2.46; 6000 N !

$             *******   BCC_A2   ************
 TYPE_DEFINITION C GES AM-PH BCC MAG -1 0.37 !
 PHASE BCC_A2  %C  2 1   3 !
    CONSTITUENT BCC_A2  :CR,FE : VA :  !
   PARAMETER TC(BCC_A2,FE:VA;0)  2.98150E+02  1043; 6000 N !
   PARAMETER BMAGN(BCC_A2,FE:VA;0)  2.98150E+02  2.22; 6000 N !
   PARAMETER TC(BCC_A2,CR:VA;0)  2.98150E+02  -311.5; 6000 N !
   PARAMETER BMAGN(BCC_A2,CR:VA;0)  2.98150E+02  -.008; 6000 N !
   PARAMETER BMAGN(BCC_A2,CR,FE:VA;0)  2.98150E+02  -.45; 6000 N !
   PARAMETER TC(BCC_A2,CR,FE:VA;0)  2.98150E+02   865.5; 6000 N !
   PARAMETER TC(BCC_A2,CR,FE:VA;1)  2.98150E+02   -567.2; 6000 N !
"""
