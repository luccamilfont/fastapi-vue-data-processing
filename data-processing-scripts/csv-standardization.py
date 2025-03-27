import tabula
import pandas as pd
from pathlib import Path
import zipfile

path = Path(__file__).resolve().parent
filesPath = path / "files"

for fileName in filesPath.iterdir():
    if fileName.suffix == ".zip":
        with zipfile.ZipFile(fileName, 'r') as zipf:
            zipf.extractall(filesPath)
            df = pd.read_csv(filesPath/fileName.with_suffix('.csv'), delimiter=';')
            print(df)
