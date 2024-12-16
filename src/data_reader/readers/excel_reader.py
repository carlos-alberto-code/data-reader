import pandas as pd
from src.data_reader.readers.reader_strategy import ReaderStrategy


class ExcelReader(ReaderStrategy):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)
        if not file_path.endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
            raise ValueError("El archivo no es un Excel")


    def load(self) -> pd.DataFrame:
        excel_engine = 'xlrd' if self.filepath.endswith('.xls') else 'openpyxl'
        df = pd.read_excel(self.filepath, engine=excel_engine)
        if df.empty:
            raise ValueError("El archivo Excel está vacío")
        return df
