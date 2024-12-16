from readers import CSVReader, ExcelReader, ReaderStrategy


class _Strategies:
    CSV = CSVReader
    EXCEL = ExcelReader


def _charge_data_frame(path: str) -> ReaderStrategy:
        if path.endswith('.csv'):
            return _Strategies.CSV(path)
        elif path.endswith('.xlsx'):
            return _Strategies.EXCEL(path)
        else:
            raise ValueError("Unsupported file format")


class DataReader:
    def __init__(self, resource: str) -> None:
        self._resource = resource
        self._reader = _charge_data_frame(resource)
        self._data = self._reader.load()

    @property
    def data(self):
        return self._data