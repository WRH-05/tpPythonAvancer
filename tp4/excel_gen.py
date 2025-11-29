import pandas as pd
from openpyxl import load_workbook

# Traitement des données avec Pandas (Création du DataFrame)
data = {
'Produit' : ['cahier','carnet','crayon','stylo'],
'Prix': [80,50,15,30],
}
df = pd.DataFrame(data)

# 2. Écriture initiale du DataFrame vers un fichier Excel
fichier_excel = 'Rapport_benefice.xlsx'
df.to_excel(fichier_excel, index=False, sheet_name='Recette')
print(f"Fichier initial créé : {fichier_excel}")

# 3. Formatage et enrichissement avec OpenPyXL
wb = load_workbook(fichier_excel)
ws = wb['Recette']

# Ajuster la largeur des colonnes (optionnel)
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter # 'A', 'B', etc.
for cell in col:
    try:
        if len(str(cell.value)) > max_length:
            max_length = len(cell.value)
    except:
        pass
    
adjusted_width = (max_length + 2)
ws.column_dimensions[column].width = adjusted_width

# 4. Sauvegarde
wb.save(fichier_excel)
print("Formatage OpenPyXL appliqué et fichier sauvegardé.")