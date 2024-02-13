import pandas as pd
from SalesData import SalesData

def main():

        dataset =r'G:\פרויקט פייתון\חומרים לפרויקט\YafeNof.csv'
        print("Database:")
        print(dataset)
        SalesData.eliminate_duplicates(dataset)
        SalesData.add_90_percent_values_column(dataset)
        SalesData.analyze_sales_data_extended(dataset)
        print("After:")
        print(dataset)
        sum=SalesData.calculate_cumulative_sales()
        print(sum)
        sales_data_object.bar_chart_category_sum()

if __name__ == "__main__":
    main()