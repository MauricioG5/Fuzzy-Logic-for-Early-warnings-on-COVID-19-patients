import numpy as np
import skfuzzy as fuzz
import csv
import random
import math
from skfuzzy import control as ctrl
from datetime import datetime
from pathlib import Path



age=27 #Edad de prueba

T_m = random.randint(35, 40)        # Temperatura medida
SPO2_m = random.randint(84, 94)     # Saturación de oxigeno medida
HR_m = random.randint(46, 118)      # Frecuencia cardiaca medida

T_m= 46
SPO2_m= 92
HR_m= 39.7

t_m = 8;                            # Mod. horario de medición de datos

print(T_m,SPO2_m,HR_m)



# =============================================================================
# FUZZY LOGIC
# =============================================================================

def PMEW(HR_m,SPO2_m,T_m,age): # PMEW.compute



    
    #-----------------------------------------------------

    """
    HR=
    SPO2=
    T=
    """
    
    #---------16-25---------------
    if (age >= 16) and (age < 26):
        
        b=1
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(36, 129, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(74, 105, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(33.9, 39, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 48, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 50, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 55, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [50, 58, 100, 108])
        HR['1'] = fuzz.gaussmf(HR.universe, 103, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 112, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 116, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 86, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 87, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 92, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 92, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 35.1, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.3, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35, 35.8, 37, 37.8])
        T['1'] = fuzz.gaussmf(T.universe, 37.5, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 38.1, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
    
    
    #---------26-35---------------    
    if (age >= 26) and (age < 36):
        
        b=2
        
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(35, 127, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(79, 106, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(34.5, 40.7, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 47, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 49, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 55, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [49, 57, 98, 106])
        HR['1'] = fuzz.gaussmf(HR.universe, 100, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 111, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 114, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 91, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 91, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 94, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 93, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 35.3, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.8, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35.3, 36.1, 37.5, 38.3])
        T['1'] = fuzz.gaussmf(T.universe, 38.5, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 39.8, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
        
        P.view()
    
    #---------36-45---------------
    if (age >= 36) and (age < 46):
        
        b=3
        
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(36, 127, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(81, 107, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(34.5, 40.6, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 48, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 50, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 56, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [51, 59, 99, 107])
        HR['1'] = fuzz.gaussmf(HR.universe, 101, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 109, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 114, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 93, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 93, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 95, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 94, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 35.3, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.8, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35.3, 36.1, 37.5, 38.3])
        T['1'] = fuzz.gaussmf(T.universe, 38.5, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 39.8, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
        
    #---------46-55---------------
    if (age >= 46) and (age < 56):
        
        b=4
        
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(36, 125, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(80, 106, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(34.3, 39.6, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 48, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 50, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 56, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [51, 59, 97, 105])
        HR['1'] = fuzz.gaussmf(HR.universe, 99, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 107, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 116, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 93, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 93, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 94, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 93, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 34.5, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.6, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35.2, 36.0, 37.1, 37.9])
        T['1'] = fuzz.gaussmf(T.universe, 37.7, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 38.6, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
        
    
    #---------56-65---------------
    if (age >= 56) and (age < 66):
        
        b=4
        
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(36, 123, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(79, 103, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(34.5, 39.4, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 44, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 50, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 56, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [51, 59, 97, 105])
        HR['1'] = fuzz.gaussmf(HR.universe, 99, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 106, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 114, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 91, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 91, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 94, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 93, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 35.3, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.8, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35.3, 36.1, 37.4, 38.2])
        T['1'] = fuzz.gaussmf(T.universe, 38.3, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 39.5, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
        
    #---------66-75---------------
    if (age >= 66) and (age < 76):
        
        b=4
        
    #-----------------------------------------------------    
        HR = ctrl.Antecedent(np.arange(36, 121, 1), 'Frec. Cardiaca')# 46 BPM - 118 BPM
        P = ctrl.Consequent(np.arange(0, 3.05, 0.05), 'P.MEWS')# Puntaje MEWS
        SPO2 = ctrl.Antecedent(np.arange(79, 106, 1), 'Sat. Oxigeno')# 84 SPO2 - 95 SPO2 
        T = ctrl.Antecedent(np.arange(34.5, 40.3, 0.1), 'Temperatura')# 33.9 °C - 38.9 °C
    #-----------------------------------------------------
    # FUNCION DE MEMBRESIA
    #-----------------------------------------------------
        HR['-3'] = fuzz.sigmf(HR.universe, 44, -1)
        HR['-2'] = fuzz.gaussmf(HR.universe, 50, 3)
        HR['-1'] = fuzz.gaussmf(HR.universe, 55, 3)
        HR['0'] = fuzz.trapmf(HR.universe, [49, 57, 95, 103])
        HR['1'] = fuzz.gaussmf(HR.universe, 97, 3)
        HR['2'] = fuzz.gaussmf(HR.universe, 104, 3)
        HR['3'] = fuzz.sigmf(HR.universe, 112, 1)
    #-----------------------------------------------------
        SPO2['-3'] = fuzz.sigmf(SPO2.universe, 91, -3)
        SPO2['-2'] = fuzz.gaussmf(SPO2.universe, 91, 2)
        SPO2['-1'] = fuzz.gaussmf(SPO2.universe, 94, 2)
        SPO2['0'] = fuzz.sigmf(SPO2.universe, 93, 3)
    #-----------------------------------------------------
        T['-3'] = fuzz.sigmf(T.universe, 35.3, -15)
        T['-1'] = fuzz.gaussmf(T.universe, 35.8, 0.2)
        T['0'] = fuzz.trapmf(T.universe, [35.3, 36.1, 37.4, 38.2])
        T['1'] = fuzz.gaussmf(T.universe, 38.3, 0.2)
        T['2'] = fuzz.sigmf(T.universe, 39.3, 15)
    #-----------------------------------------------------
        P['0'] = fuzz.trimf(P.universe, [0, 0, 0.75])
        P['1'] = fuzz.trimf(P.universe, [0.25, 1, 1.75])
        P['2'] = fuzz.trimf(P.universe, [1.25, 2, 2.75])
        P['3'] = fuzz.trimf(P.universe, [2.25, 3, 3])
     
    
    # CONJUNTOS DIFUSOS
    #-----------------------------------------------------
    # SPO2 = -3
    
    #T = -3
    r1 = ctrl.Rule(SPO2['-3'] & HR['-3'] & T['-3'],P['3'])
    r2 = ctrl.Rule(SPO2['-3'] & HR['-2'] & T['-3'],P['3'])
    r3 = ctrl.Rule(SPO2['-3'] & HR['-1'] & T['-3'],P['3'])
    r4 = ctrl.Rule(SPO2['-3'] & HR['0'] & T['-3'],P['3'])
    r5 = ctrl.Rule(SPO2['-3'] & HR['1'] & T['-3'],P['3'])
    r6 = ctrl.Rule(SPO2['-3'] & HR['2'] & T['-3'],P['3'])
    r7 = ctrl.Rule(SPO2['-3'] & HR['3'] & T['-3'],P['3'])
    
    #T = -1
    r8 = ctrl.Rule(SPO2['-3'] & HR['-3'] & T['-1'],P['3'])
    r9 = ctrl.Rule(SPO2['-3'] & HR['-2'] & T['-1'],P['3'])
    r10 = ctrl.Rule(SPO2['-3'] & HR['-1'] & T['-1'],P['2'])
    r11 = ctrl.Rule(SPO2['-3'] & HR['0'] & T['-1'],P['1'])
    r12 = ctrl.Rule(SPO2['-3'] & HR['1'] & T['-1'],P['2'])
    r13 = ctrl.Rule(SPO2['-3'] & HR['2'] & T['-1'],P['3'])
    r14 = ctrl.Rule(SPO2['-3'] & HR['3'] & T['-1'],P['3'])
    
    #T = 0
    r15 = ctrl.Rule(SPO2['-3'] & HR['-3'] & T['0'],P['3'])
    r16 = ctrl.Rule(SPO2['-3'] & HR['-2'] & T['0'],P['2'])
    r17 = ctrl.Rule(SPO2['-3'] & HR['-1'] & T['0'],P['1'])
    r18 = ctrl.Rule(SPO2['-3'] & HR['0'] & T['0'],P['1'])
    r19 = ctrl.Rule(SPO2['-3'] & HR['1'] & T['0'],P['1'])
    r20 = ctrl.Rule(SPO2['-3'] & HR['2'] & T['0'],P['2'])
    r21 = ctrl.Rule(SPO2['-3'] & HR['3'] & T['0'],P['3'])
    
    #T=1
    r22 = ctrl.Rule(SPO2['-3'] & HR['-3'] & T['1'],P['3'])
    r23 = ctrl.Rule(SPO2['-3'] & HR['-2'] & T['1'],P['3'])
    r24 = ctrl.Rule(SPO2['-3'] & HR['-1'] & T['1'],P['2'])
    r25 = ctrl.Rule(SPO2['-3'] & HR['0'] & T['1'],P['1'])
    r26 = ctrl.Rule(SPO2['-3'] & HR['1'] & T['1'],P['2'])
    r27 = ctrl.Rule(SPO2['-3'] & HR['2'] & T['1'],P['3'])
    r28 = ctrl.Rule(SPO2['-3'] & HR['3'] & T['1'],P['3'])
    
    #T=2
    r29 = ctrl.Rule(SPO2['-3'] & HR['-3'] & T['2'],P['3'])
    r30 = ctrl.Rule(SPO2['-3'] & HR['-2'] & T['2'],P['3'])
    r31 = ctrl.Rule(SPO2['-3'] & HR['-1'] & T['2'],P['3'])
    r32 = ctrl.Rule(SPO2['-3'] & HR['0'] & T['2'],P['2'])
    r33 = ctrl.Rule(SPO2['-3'] & HR['1'] & T['2'],P['3'])
    r34 = ctrl.Rule(SPO2['-3'] & HR['2'] & T['2'],P['3'])
    r35 = ctrl.Rule(SPO2['-3'] & HR['3'] & T['2'],P['3'])
    #-----------------------------------------------------
    # SPO2 = -2
    
    #T = -3
    r36 = ctrl.Rule(SPO2['-2'] & HR['-3'] & T['-3'],P['3'])
    r37 = ctrl.Rule(SPO2['-2'] & HR['-2'] & T['-3'],P['3'])
    r38 = ctrl.Rule(SPO2['-2'] & HR['-1'] & T['-3'],P['3'])
    r39 = ctrl.Rule(SPO2['-2'] & HR['0'] & T['-3'],P['2'])
    r40 = ctrl.Rule(SPO2['-2'] & HR['1'] & T['-3'],P['3'])
    r41 = ctrl.Rule(SPO2['-2'] & HR['2'] & T['-3'],P['3'])
    r42 = ctrl.Rule(SPO2['-2'] & HR['3'] & T['-3'],P['3'])     
    
    #T = -1
    r43 = ctrl.Rule(SPO2['-2'] & HR['-3'] & T['-1'],P['3'])
    r44 = ctrl.Rule(SPO2['-2'] & HR['-2'] & T['-1'],P['2'])
    r45 = ctrl.Rule(SPO2['-2'] & HR['-1'] & T['-1'],P['1'])
    r46 = ctrl.Rule(SPO2['-2'] & HR['0'] & T['-1'],P['1'])
    rex = ctrl.Rule(SPO2['-2'] & HR['1'] & T['-1'],P['1'])
    r47 = ctrl.Rule(SPO2['-2'] & HR['2'] & T['-1'],P['2'])
    r48 = ctrl.Rule(SPO2['-2'] & HR['3'] & T['-1'],P['3'])    
    
    #T = 0
    r49 = ctrl.Rule(SPO2['-2'] & HR['-3'] & T['0'],P['2'])
    r50 = ctrl.Rule(SPO2['-2'] & HR['-2'] & T['0'],P['1'])
    r51 = ctrl.Rule(SPO2['-2'] & HR['-1'] & T['0'],P['1'])
    r52 = ctrl.Rule(SPO2['-2'] & HR['0'] & T['0'],P['1'])
    r53 = ctrl.Rule(SPO2['-2'] & HR['1'] & T['0'],P['1'])
    r54 = ctrl.Rule(SPO2['-2'] & HR['2'] & T['0'],P['1'])
    r55 = ctrl.Rule(SPO2['-2'] & HR['3'] & T['0'],P['2'])
    
    #T = 1
    r56 = ctrl.Rule(SPO2['-2'] & HR['-3'] & T['1'],P['3'])
    r57 = ctrl.Rule(SPO2['-2'] & HR['-2'] & T['1'],P['2'])
    r58 = ctrl.Rule(SPO2['-2'] & HR['-1'] & T['1'],P['1'])
    r59 = ctrl.Rule(SPO2['-2'] & HR['0'] & T['1'],P['1'])
    r60 = ctrl.Rule(SPO2['-2'] & HR['1'] & T['1'],P['1'])
    r61 = ctrl.Rule(SPO2['-2'] & HR['2'] & T['1'],P['2'])
    r62 = ctrl.Rule(SPO2['-2'] & HR['3'] & T['1'],P['3'])   
    
    
    #T = 2
    r63 = ctrl.Rule(SPO2['-2'] & HR['-3'] & T['2'],P['3'])
    r64 = ctrl.Rule(SPO2['-2'] & HR['-2'] & T['2'],P['3'])
    r65 = ctrl.Rule(SPO2['-2'] & HR['-1'] & T['2'],P['2'])
    r66 = ctrl.Rule(SPO2['-2'] & HR['0'] & T['2'],P['1'])
    r67 = ctrl.Rule(SPO2['-2'] & HR['1'] & T['2'],P['2'])
    r68 = ctrl.Rule(SPO2['-2'] & HR['2'] & T['2'],P['3'])
    r69 = ctrl.Rule(SPO2['-2'] & HR['3'] & T['2'],P['3']) 
    #-----------------------------------------------------
    # SPO2 = -1
    
    #T = -3
    r70 = ctrl.Rule(SPO2['-1'] & HR['-3'] & T['-3'],P['3'])
    r71 = ctrl.Rule(SPO2['-1'] & HR['-2'] & T['-3'],P['3'])
    r72 = ctrl.Rule(SPO2['-1'] & HR['-1'] & T['-3'],P['2'])
    r73 = ctrl.Rule(SPO2['-1'] & HR['0'] & T['-3'],P['1'])
    r74 = ctrl.Rule(SPO2['-1'] & HR['1'] & T['-3'],P['2'])
    r75 = ctrl.Rule(SPO2['-1'] & HR['2'] & T['-3'],P['3'])
    r76 = ctrl.Rule(SPO2['-1'] & HR['3'] & T['-3'],P['3'])     
    
    #T = -1
    r78 = ctrl.Rule(SPO2['-1'] & HR['-3'] & T['-1'],P['2'])
    r79 = ctrl.Rule(SPO2['-1'] & HR['-2'] & T['-1'],P['1'])
    r80 = ctrl.Rule(SPO2['-1'] & HR['-1'] & T['-1'],P['1'])
    r81 = ctrl.Rule(SPO2['-1'] & HR['0'] & T['-1'],P['1'])
    r82 = ctrl.Rule(SPO2['-1'] & HR['1'] & T['-1'],P['1'])
    r83 = ctrl.Rule(SPO2['-1'] & HR['2'] & T['-1'],P['1'])
    r84 = ctrl.Rule(SPO2['-1'] & HR['3'] & T['-1'],P['2'])    
    
    #T = 0
    r85 = ctrl.Rule(SPO2['-1'] & HR['-3'] & T['0'],P['1'])
    r86 = ctrl.Rule(SPO2['-1'] & HR['-2'] & T['0'],P['1'])
    r87 = ctrl.Rule(SPO2['-1'] & HR['-1'] & T['0'],P['1'])
    r88 = ctrl.Rule(SPO2['-1'] & HR['0'] & T['0'],P['0'])
    r89 = ctrl.Rule(SPO2['-1'] & HR['1'] & T['0'],P['1'])
    r90 = ctrl.Rule(SPO2['-1'] & HR['2'] & T['0'],P['1'])
    r91 = ctrl.Rule(SPO2['-1'] & HR['3'] & T['0'],P['1'])
    
    #T = 1
    r92 = ctrl.Rule(SPO2['-1'] & HR['-3'] & T['1'],P['2'])
    r93 = ctrl.Rule(SPO2['-1'] & HR['-2'] & T['1'],P['1'])
    r94 = ctrl.Rule(SPO2['-1'] & HR['-1'] & T['1'],P['1'])
    r95 = ctrl.Rule(SPO2['-1'] & HR['0'] & T['1'],P['1'])
    r96 = ctrl.Rule(SPO2['-1'] & HR['1'] & T['1'],P['1'])
    r97 = ctrl.Rule(SPO2['-1'] & HR['2'] & T['1'],P['1'])
    r98 = ctrl.Rule(SPO2['-1'] & HR['3'] & T['1'],P['2'])   
    
    
    #T = 2
    r99 = ctrl.Rule(SPO2['-1'] & HR['-3'] & T['2'],P['3'])
    r100 = ctrl.Rule(SPO2['-1'] & HR['-2'] & T['2'],P['2'])
    r101 = ctrl.Rule(SPO2['-1'] & HR['-1'] & T['2'],P['1'])
    r102 = ctrl.Rule(SPO2['-1'] & HR['0'] & T['2'],P['1'])
    r103 = ctrl.Rule(SPO2['-1'] & HR['1'] & T['2'],P['1'])
    r104 = ctrl.Rule(SPO2['-1'] & HR['2'] & T['2'],P['2'])
    r105 = ctrl.Rule(SPO2['-1'] & HR['3'] & T['2'],P['3']) 
    
    #-----------------------------------------------------
    # SPO2 = 0
    
    #T = -3
    r106 = ctrl.Rule(SPO2['0'] & HR['-3'] & T['-3'],P['3'])
    r107 = ctrl.Rule(SPO2['0'] & HR['-2'] & T['-3'],P['2'])
    r108 = ctrl.Rule(SPO2['0'] & HR['-1'] & T['-3'],P['1'])
    r109 = ctrl.Rule(SPO2['0'] & HR['0'] & T['-3'],P['1'])
    r110 = ctrl.Rule(SPO2['0'] & HR['1'] & T['-3'],P['1'])
    r111 = ctrl.Rule(SPO2['0'] & HR['2'] & T['-3'],P['2'])
    r112 = ctrl.Rule(SPO2['0'] & HR['3'] & T['-3'],P['3'])     
    
    #T = -1
    r113 = ctrl.Rule(SPO2['0'] & HR['-3'] & T['-1'],P['1'])
    r114 = ctrl.Rule(SPO2['0'] & HR['-2'] & T['-1'],P['1'])
    r115 = ctrl.Rule(SPO2['0'] & HR['-1'] & T['-1'],P['1'])
    r116 = ctrl.Rule(SPO2['0'] & HR['0'] & T['-1'],P['0'])
    r117 = ctrl.Rule(SPO2['0'] & HR['1'] & T['-1'],P['1'])
    r118 = ctrl.Rule(SPO2['0'] & HR['2'] & T['-1'],P['1'])
    r119 = ctrl.Rule(SPO2['0'] & HR['3'] & T['-1'],P['1'])    
    
    #T = 0
    r120 = ctrl.Rule(SPO2['0'] & HR['-3'] & T['0'],P['1'])
    r121 = ctrl.Rule(SPO2['0'] & HR['-2'] & T['0'],P['1'])
    r122 = ctrl.Rule(SPO2['0'] & HR['-1'] & T['0'],P['0'])
    r123 = ctrl.Rule(SPO2['0'] & HR['0'] & T['0'],P['0'])
    r124 = ctrl.Rule(SPO2['0'] & HR['1'] & T['0'],P['0'])
    r125 = ctrl.Rule(SPO2['0'] & HR['2'] & T['0'],P['1'])
    r126 = ctrl.Rule(SPO2['0'] & HR['3'] & T['0'],P['1'])
    
    #T = 1
    r127 = ctrl.Rule(SPO2['0'] & HR['-3'] & T['1'],P['1'])
    r128 = ctrl.Rule(SPO2['0'] & HR['-2'] & T['1'],P['1'])
    r129 = ctrl.Rule(SPO2['0'] & HR['-1'] & T['1'],P['1'])
    r130 = ctrl.Rule(SPO2['0'] & HR['0'] & T['1'],P['0'])
    r131 = ctrl.Rule(SPO2['0'] & HR['1'] & T['1'],P['1'])
    r132 = ctrl.Rule(SPO2['0'] & HR['2'] & T['1'],P['1'])
    r133 = ctrl.Rule(SPO2['0'] & HR['3'] & T['1'],P['1'])
    
    #T = 2
    r134 = ctrl.Rule(SPO2['0'] & HR['-3'] & T['2'],P['2'])
    r135 = ctrl.Rule(SPO2['0'] & HR['-2'] & T['2'],P['1'])
    r136 = ctrl.Rule(SPO2['0'] & HR['-1'] & T['2'],P['1'])
    r137 = ctrl.Rule(SPO2['0'] & HR['0'] & T['2'],P['1'])
    r138 = ctrl.Rule(SPO2['0'] & HR['1'] & T['2'],P['1'])
    r139 = ctrl.Rule(SPO2['0'] & HR['2'] & T['2'],P['1'])
    r140 = ctrl.Rule(SPO2['0'] & HR['3'] & T['2'],P['2'])
     
    PMEW_ctrl = ctrl.ControlSystem([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,r34,r35,r36,r37,r38,r39,r40,r41,r42,r43,r44,r45,r46,r47,r48,r49,r50,r51,r52,r53,r54,r55,r56,r57,r58,r59,r60,r61,r62,r63,r64,r65,r66,r67,r68,r69,r70,r71,r72,r73,r74,r75,r76,rex,r78,r79,r80,r81,r82,r83,r84,r85,r86,r87,r88,r89,r90,r91,r92,r93,r94,r95,r96,r97,r98,r99,r100,r101,r102,r103,r104,r105,r106,r107,r108,r109,r110,r111,r112,r113,r114,r115,r116,r117,r118,r119,r120,r121,r122,r123,r124,r125,r126,r127,r128,r129,r130,r131,r132,r133,r134,r135,r136,r137,r138,r139,r140])
    PMEW = ctrl.ControlSystemSimulation(PMEW_ctrl)
    
    PMEW.input['Frec. Cardiaca'] = HR_m   #Variable de prueba
    PMEW.input['Sat. Oxigeno'] = SPO2_m   #Varieble de prueba
    PMEW.input['Temperatura'] = T_m        #Variable de prueba
    
    PMEW.compute()
    
    PMEW_r = PMEW.output['P.MEWS']
    PMEW_r = math.ceil(PMEW_r) 
    print (PMEW_r)
    
    P.view(sim=PMEW)
    
    return PMEW_r
     
PMEW_r = PMEW(HR_m,SPO2_m,T_m,age) # FuzzyLogic

if PMEW_r >= 2 and PMEW_r < 2.5:
    t_m = 4

elif PMEW_r >= 2.5:
    t_m = 1

# VISTA DE LAS FUNCIONES DE MEMBRESIA    
           
    # HR.view() 
    # SPO2.view()
    # T.view()
    # P.view() 
        
    
    
# =============================================================================
# BASE DE DATOS 
# =============================================================================

fileName = r"C:\Users\User\Dropbox\INTEGRADOR bffos\2da Entrega\DatabaseCode\mediciones.csv"
fileObj = Path(fileName)
file_exists = fileObj.is_file()

print(file_exists)

def get_time(v):
    now = datetime.now()
    v[0] = now.year
    v[1] = now.month
    v[2] = now.day
    v[3] = now.hour
    v[4] = now.minute
    return v

v = [None, None, None, None, None]
get_time(v)

# hour_PMEW = v[3]+t_m


row_list =["Año","Mes","Día","Hora","Minuto","Edad","Temperatura","Saturación de Oxígeno","Frecuencia Cardiaca","PMEW"]


# Creación de archivo

if file_exists == 0:
    
    with open('mediciones.csv', 'w',newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,
                            delimiter=';', quotechar=' ')
        writer.writerow(row_list)
        Fila = [v[0],v[1],v[2],v[3],v[4], age, T_m, SPO2_m, HR_m, PMEW_r]
        writer.writerow(Fila)
        print("NO EXISTO BRO, im a live")
        file.close()

# Anexar a archivo existente

else:
    
    with open('mediciones.csv', 'a',newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,
                            delimiter=';', quotechar=' ')
        
        Fila = [v[0],v[1],v[2],v[3],v[4], age, T_m, SPO2_m, HR_m, PMEW_r]# v[3] = hour_PMEW
        writer.writerow(Fila)
        print("YA EXISTIA BRO, ME ANEXÉ")    
        file.close()