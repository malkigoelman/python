import pandas as pd
class FileOperation:

    # 1
    @staticmethod
    def read_excel(self, file_path:str):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError:
            print("ERROR")
            return None
    # 2
    def save_to_excel(self,data,file_name:str):
        data.to_excel(file_name,index=False)

