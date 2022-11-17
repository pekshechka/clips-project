import zipfile
from tqdm import tqdm
import pandas as pd


def take_from_zip(inputPath, filename, outputPath):
    with zipfile.ZipFile(f"{inputPath}/{filename}", "r") as zf:
        for entry in tqdm(zf.infolist(), desc="Extracting "):
            try:
                zf.extract(entry, outputPath)
            except zipfile.error as e:
                pass


def take_columns(path, filename):
    """
    params:
        path: path to folder with parquet files
        filename: filename of parquet file
    """
    columns = pd.read_parquet(
        f"{path}/{filename}",
        engine="pyarrow",
        columns=None,
    ).columns.tolist()
    return columns
