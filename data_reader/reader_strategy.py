from abc import ABC, abstractmethod
import pandas as pd
import os


class ReaderStrategy(ABC):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self._file_path = file_path
        if not os.path.exists(self._file_path):
            raise FileNotFoundError(f"El archivo {self._file_path} no existe")

    @property
    def filepath(self):
        return self._file_path

    @abstractmethod
    def load(self) -> pd.DataFrame: ...
