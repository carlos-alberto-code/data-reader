import pandas as pd
from data_reader.reader_strategy import ReaderStrategy


class CSVReader(ReaderStrategy):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

        if not file_path.endswith('.csv'):
            raise ValueError("El archivo debe tener extensión .csv")

    def load(self) -> pd.DataFrame:
        df = pd.read_csv(self.filepath)
        if df.empty:
            raise ValueError("El archivo CSV está vacío")
        return df
