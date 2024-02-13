import pandas as pd
from FileOperation import FileOperation

class UnitTeas:

    def setUp(self):
        self.file_operation = FileOperation()

    @staticmethod
    def test_read_excel():
        df=FileOperation.read_excel("lalala.xlsx")
        assert df is not None
        df = FileOperation.read_excel("non_existing.xlsx")
        assert df is  None

    @staticmethod
    def test_save_to_excel():
        data = pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})
        FileOperation.save_to_excel(data,"output.xlsx")
        try:
            pd.read_excel("output.xlsx")
        except FileNotFoundError:
            assert False
        else:
            assert True

    if __name__ == '__main__':
        unittest.main()