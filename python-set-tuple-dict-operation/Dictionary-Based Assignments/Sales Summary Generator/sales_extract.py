from sales_function import get_top_city,get_low_sales_cities,increase_sales

def main():
        sales = {
            "Bangalore": 75000,
            "Delhi": 60000,
            "Chennai": 45000,
            "Mumbai": 30000
        }
        print("Top city:", get_top_city(sales))
        print("Low sales cities:", get_low_sales_cities(sales, 50000))
        print("Increased sales (10%):", increase_sales(sales, 10))
        print("Original sales still intact:", sales)
       
if __name__ == "__main__":
        main()