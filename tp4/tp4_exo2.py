import os, platform, schedule, time
import pandas as pd
from tp4 import amount

print("OS Name :", platform.system())
path = os.getcwd()
def job():
    print("Running scheduled task...")
    f='Rapport_benefice.xlsx'
    if os.path.exists(f):
        df = pd.read_excel(f)
        data= {'Quantité': amount(4)}
        df = pd.concat([df, pd.DataFrame(data)], axis=1)
        df['Total'] = df['Prix'] * df['Quantité']
        print(df)
        fichier_excel = 'Rapport_benefice_auto.xlsx'
        df.to_excel(fichier_excel, index=False, sheet_name='Recette')
        print(f"Fichier créé : {fichier_excel}")

if __name__ == '__main__':
    schedule.every(1).seconds.do(job)
    if int(time.strftime('%S'))>= 58: time.sleep(5)
    ti =int(time.strftime('%S'))
    while int(time.strftime('%S'))< ti+2:
        schedule.run_pending()