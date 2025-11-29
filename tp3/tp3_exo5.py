# excel_creator.py

import pandas as pd
from openpyxl import load_workbook
# Traitement des données avec Pandas (Création du DataFrame)
data = {
 'Bias' : [0,1,2,3,4],
 'Current': [0,0.01,0.012, 0.016, 0.020 ]
 }
df = pd.DataFrame(data)
fichier_excel = 'Rapport_IV.xlsx'
df.to_excel(fichier_excel, index=False, sheet_name='Data')
print(f"Fichier initial créé : {fichier_excel}")