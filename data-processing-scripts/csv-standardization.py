import pandas as pd
from pathlib import Path
import zipfile

path = Path(__file__).resolve().parent
filesPath = path / "files"

for fileName in filesPath.iterdir():
    if fileName.suffix == ".zip":
        with zipfile.ZipFile(fileName, 'r') as zipf:
            zipf.extractall(filesPath)
            df = pd.read_csv(filesPath/fileName.with_suffix('.csv'), delimiter=';', parse_dates=['DATA'], dayfirst=True)
            df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
            df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)
            df.to_csv(filesPath/fileName.with_suffix('.csv'), sep=';', index=False)