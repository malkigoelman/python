import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
class SalesData:

    def __init__(self, data):
        self.data = data;
    #4 מחיקת שורות כפולות
    def eliminate_duplicates(self):
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplafe=True)
    # 5חישוב סך המכירות עבור כל מוצר
    def calculate_total_sales(self):
        total_sales=self.data.groupby('Product')['Quantity'].sum()
        return total_sales
    #חישוב סך המכירות עבור כל חודש6
    def _calculate_total_sales_por_month(self):
        self.data['month'] = self.data['Date'].dt.to_period('M')
        total_month = self.data.groupby('month')['Quantity'].sum()
        return total_month
    #task 6
    def plt_calculate_total_sales_por_month(self):
        total_month = self._calculate_total_sales_por_month()
        plt.scatter(total_month.index, total_month)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.show()
    def plt_calculate_total_sales_por_month2(self):
        total_month = self._calculate_total_sales_por_month()
        plt.hist(total_month, bins=10)
        plt.xlabel('Total Sales')
        plt.ylabel('Frequency')
        plt.title('Distribution of Total Sales')
        plt.show()
    def plt_calculate_total_sales_por_month3(self):
        total_month = self._calculate_total_sales_por_month()
        plt.boxplot(total_month)
        plt.ylabel('Total Sales')
        plt.title('Box Plot of Total Sales')
        plt.show()
    def plt_calculate_total_sales_por_month4(self):
        total_month = self._calculate_total_sales_por_month()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.arange(len(total_month.index))
        y = total_month.values
        ax.bar(x, y, zs=0, zdir='y')
        ax.set_xticks(x)
        ax.set_xticklabels(total_month.index)
        ax.set_xlabel('Month')
        ax.set_ylabel('Total Sales')
        ax.set_zlabel('Quantity')
        plt.title('Total Sales per Month')
        plt.show()
    def sns_calculate_total_sales_por_month(self):
        total_month = self._calculate_total_sales_por_month()
        sns.lineplot(data=total_month)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.show()
    def sns_calculate_total_sales_por_month2(self):
        total_month = self._calculate_total_sales_por_month()
        sns.barplot(x=total_month.index, y=total_month)
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.show()
    def sns_calculate_total_sales_por_month3(self):
        total_month = self._calculate_total_sales_por_month()
        sns.countplot(data=total_month, x='Product')
        plt.xlabel('Product')
        plt.ylabel('Count')
        plt.title('Number of Sales per Product')
        plt.show()
    def sns_calculate_total_sales_por_month4(self):
        total_month = self._calculate_total_sales_por_month()
        sns.boxplot(data=total_month, x='Product', y='Quantity')
        plt.xlabel('Product')
        plt.ylabel('Quantity')
        plt.title('Distribution of Quantity per Product')
        plt.show()
    #7 מזהה את הממוצר הכי נמכר
    def _identify_best_selling_product(self):
        best_selling_product = self.dataset.groupby('Product')['Quantity'].sum().idxmax()
        return best_selling_product
    #task 6
    def plt_best_product(self):
        best_product = self._identify_best_selling_product()
        plt.bar(best_product.index, best_product)
        plt.xlabel('Product')
        plt.ylabel('Sales Quantity')
        plt.title('Best Selling Product')
        plt.show()
    def plt_best_product2(self):
        best_product = self._identify_best_selling_product()
        plt.pie(best_product, labels=best_product.index, autopct='%1.1f%%')
        plt.title('Sales Composition')
        plt.show()
    def plt_best_product3(self):
        best_product = self._identify_best_selling_product()
        plt.bar(best_product.index, best_product)
        plt.xlabel('Product')
        plt.ylabel('Sales Quantity')
        plt.title('Product Sales')
        plt.show()
    def _identify_month_with_highest_sales(self):
       total=self._calculate_total_sales_por_month()
       month=total.idxmax()
       return month
#   # מחזיר מילון עם המוצר הנמכר ביותר והחודש הנמכר ביותר9
    def analyze_seles_data(self):
        self.eliminate_duplicates()
        best_product=self._identify_best_selling_product()
        best_month=self._identify_month_with_highest_sales()
        analysis_result={
            'best_selling_product':best_product,
            'month_with_highest_sales': best_month
        }
        return analysis_result
    def analyze_sales_data_extended(self):
        results=self.analyze_seles_data()
        total_month=self.calculate_total_sales_por_month()
        min_product=self.data.groupby('Product')['Quantity'].sum().min()
        average=total_month.mean()
        results['min_product']=min_product
        results['average']=average
        return results
    def calculate_cumulative_sales(self):
        self.data['calculate_sales'] = self.data.groupby('Product')['Quantity'].cumsum()
    def add_90_percent_values_column(self):
        values = self.data['Price'].quantile(0.9)
        self.data['90%'] = values

        # 13
    def bar_chart_category_sum(self):
        sns.barplot(x='Product', y='Quantity', data=self.data.groupby('Product')['Quantity'].sum().reset_index())

        # 14 מי זה טוטל
    def calculate_mean_quantity(self):
        mean = np.mean(self.data['Total'])
        median = np.median(self.data['Total'])
        sort = np.sort(self.data['Total'])
        max = sort[-2]
        return mean, median, max

        # 15
    def filter_by_sellings_or_and(self):
        filter = self.data[(self.data['Quantity'] > 5) | (self.data['Quantity'] == 0)]
        filter = filter[((self.data['Price'] > 300) & (self.data['Quantity'] < 2))]
        return filter
   def convert_date_format(self,date:List=None):
        if date is None:
            date=['Date']
        for x in date:
            self.data[x]=pd.to_datetime(self.data[x])
        return self.data
    def categorize_prices(self):
        blabka=self.data['Price'].quantile([0,0.25,0.5,0.75,1])
        labels=['Very low','low','medium','high','very high']
        self.data['PriceCategory']=pd.cut(self.data['Price'],bins=blabka,labels=labels)
        return self.data

