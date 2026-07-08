from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).parent.parent.resolve()


data = {
    "Name": ["Karu", "Saru", "Paru"],
    "Age": [13, 14, 15],
    "City": ["Delhi", "Pune", "Bangalore"]
}


df = pd.DataFrame(
    data= data
)


data_dir = ROOT_DIR / "data" / "raw"
data_dir.mkdir(parents= True, exist_ok= True)


df.to_csv(path_or_buf= (data_dir / "sample.csv"), index= False)