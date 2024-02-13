import pandas as pd
import  unittest

class UnitTast:

    @staticmethod
    def test_eliminate_duplicates():
        dataset = pd.DataFrame({
            'Product': ['A', 'B', 'A', 'C', 'A'],
            'Sales': [100, 200, 100, 150, 100]
        })

        dataset.drop_duplicates(inplace=True)
        dataset.dropna(inplace=True)

        assert dataset.equals(pd.DataFrame({
            'Product': ['A', 'B', 'C'],
            'Sales': [100, 200, 150]
        }))

    @staticmethod
    def test_calculate_total_sales():
        dataset = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'A', 'B'],
            'Sales': [100, 200, 150, 250, 300]
        })

        total_sales = dataset.groupby('Product')['Sales'].sum()
        assert total_sales.equals(pd.Series([350, 500, 150], index=['A', 'B', 'C']))

    @staticmethod
    def test_identify_best_selling_product():
        dataset = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'A', 'B'],
            'Sales': [100, 200, 150, 250, 300]
        })

        best_selling_product = dataset.groupby('Product')['Sales'].sum().idxmax()
        assert best_selling_product == 'B'

    @staticmethod
    def test_identify_month_with_highest_sales():
        dataset = pd.DataFrame({
            'Date': ['2022-01-01', '2022-02-01', '2022-02-01', '2022-03-01'],
            'Sales': [100, 200, 150, 300]
        })

        dataset['Month'] = pd.to_datetime(dataset['Date']).dt.month
        total_sales_per_month = dataset.groupby('Month')['Sales'].sum()
        month_with_highest_sales = total_sales_per_month.idxmax()
        assert month_with_highest_sales == 3

# @staticmethod
# def run_tests():
#     UnitTest.test_calculate_total_sales()
#     UnitTest.test_identify_best_selling_product()
#     UnitTest.test_eliminate_duplicates()
#     UnitTest.test_identify_month_with_highest_sales()