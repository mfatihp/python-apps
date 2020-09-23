import pandas as pd
import argparse



def topseller(min_date = "2020-01-01", max_date = "2020-06-30", top=3):
    
    # Read csv files
    product = pd.read_csv("product.csv")
    sales = pd.read_csv("sales.csv")
    store = pd.read_csv("store.csv")

    # Convert the date column into dtype datetime
    sales['date'] = pd.to_datetime(sales['date'])

    ### Check Arguments ###
    
    # Check 'top' argument, if type not equal int and float, set 3
    if (type(top) != int) and (type(top) != float):
        print("Not proper 'top' argument'...")
        print("It's set 3")
        print("-"*50)
        print("\n")
        top = 3
    # If type int or float, round it and set round result to 'top'
    else:
        top = round(top)

    # Try to convert dates to Timestamp 
    try:
        pd.to_datetime(min_date)
        pd.to_datetime(max_date)
    except ValueError as e:
        print(f"Error : {e}")
        print("-"*50)
        print("Type : str")
        print("Format: 'YYYY-MM-DD'")
        print("-"*50)
        pass

    # Convert dates to Timestamp
    min_date = pd.to_datetime(min_date)
    max_date = pd.to_datetime(max_date)

    # Check dates, if they not in data range, set them data.min and data.max
    if (min_date < sales['date'].min()) or (min_date > sales['date'].max()):
        print("min_date out of range...")
        print("It's set oldest record date")
        print("-"*50)
        print("\n")
        min_date = sales['date'].min()

    if (max_date < sales['date'].min()) or (max_date > sales['date'].max()):
        print("max_date out of range...")
        print("It's set newest record date")
        print("-"*50)
        print("\n")
        max_date = sales['date'].max()

    # Check min_date for has recent date from max_date
    if min_date > max_date:
        print("min_date has recent date from max_date...")
        print("It's set min_date as max_date, max_date as min_date")
        print("-"*50)
        print("\n")
        min_date, max_date = max_date, min_date 

    ###

    # Join dataframes
    joined = sales.join(store.set_index('id'), on='store', how='left')
    
    # Result table has name column, it's not informative, renamed it name_store
    joined = joined.join(product.set_index('id'), on='product', how='left', rsuffix='_product')

    # Rename name column with name_store
    joined = joined.rename(columns={'name': 'name_store'})

    # Apply dates
    filtered = joined[(joined['date'] >= min_date) & (joined['date'] <= max_date)]

    # Top Seller Product - grouped by product and sorted by quantity
    print("   Top Seller Product")
    print("="*24)
    prod_quant = filtered.groupby('name_product')['quantity'].sum()
    prod_quant = pd.DataFrame(prod_quant.sort_values(ascending=False))
    print(prod_quant.nlargest(top, 'quantity', keep='all'))
    print("\n")

    # Top Seller Store - grouped by store and sorted by quantity
    print("   Top Seller Store")
    print("="*24)
    store_quant = filtered.groupby('name_store')['quantity'].sum()
    store_quant = pd.DataFrame(store_quant.sort_values(ascending=False))
    print(store_quant.nlargest(top, 'quantity', keep='all'))
    print("\n")
    
    # Top Seller Brand - grouped by brand and sorted by quantity
    print("   Top Seller Brand")
    print("="*24)
    brand_quant = filtered.groupby('brand')['quantity'].sum()
    brand_quant = pd.DataFrame(brand_quant.sort_values(ascending=False))
    print(brand_quant.nlargest(top, 'quantity', keep='all'))
    print("\n")

    # Top Seller City - grouped by city and sorted by quantity
    print("   Top Seller City")
    print("="*24)
    city_quant = filtered.groupby('city')['quantity'].sum()
    city_quant = pd.DataFrame(city_quant.sort_values(ascending=False))
    print(city_quant.nlargest(top, 'quantity', keep='all'))
    print("\n")



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--min-date", nargs='?', type=str, default="2020-01-01")
    parser.add_argument("--max-date", nargs='?', type=str, default="2020-06-30")
    parser.add_argument("--top", nargs='?', const=3, type=int, default=3)

    args = parser.parse_args()

    topseller(min_date=args.min_date, max_date=args.max_date, top=args.top)

if __name__ == '__main__':
    main()