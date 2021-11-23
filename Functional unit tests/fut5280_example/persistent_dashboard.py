import csv,os
import pandas as pd
import numpy as np

data=pd.read_csv(os.getcwd()+"/allure/allure_report/data/"+'behaviors.csv')
persistent_dashboard='persistent_dashboard.csv'
header=np.where(os.path.exists(persistent_dashboard),0,1)

with open(persistent_dashboard, 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["PASSED","SKIPPED","FAILED"]) if header else None
    writer.writerow([data["PASSED"][0],data["SKIPPED"][0],data["FAILED"][0]])