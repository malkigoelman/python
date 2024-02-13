from FileOperation import FileOperation

    def main():
        fileOperation=FileOperation()

        file =r'G:\פרויקט פייתון\חומרים לפרויקט\YafeNof.csv'
        df=fileOperation.read_excel(file)
        print(df)

        new_file=r'G:\פרויקט פייתון\חומרים לפרויקט'
        fileOperation.save_to_excel(df,new_file)

    if __name__== "__main__":
        main()

