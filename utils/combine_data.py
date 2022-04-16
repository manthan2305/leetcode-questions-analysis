import os, sys
import pandas as pd

CWD_DIR = os.path.abspath(__file__)
ROOT_DIR = "/".join(CWD_DIR.split('/')[:-2])
print(ROOT_DIR)
sys.path.append(ROOT_DIR)

DATA_DIR = os.path.join(ROOT_DIR, 'data/all_questions_data')

all_files = os.listdir(DATA_DIR)

all_data = pd.DataFrame()
for file_ in all_files:

    df = pd.read_csv(os.path.join(DATA_DIR, file_))
    all_data = all_data.append(df)

all_data.to_csv(os.path.join(ROOT_DIR, 'data', 'all_questions_data.csv'), index=False)
