
# Exercise: Sales Data Analysis

# **Objective**: Write a Python program to analyze a dataset of sales records. 
# The dataset is represented as a list of dictionaries, where each dictionary 
# contains information about a single sale, including the product name, quantity 
# sold, and sale price.


sales_data = [

    {"product": "Laptop", "quantity": 1, "price": 1200.00},

    {"product": "Mouse", "quantity": 2, "price": 35.50},

    {"product": "Keyboard", "quantity": 1, "price": 65.00},

    # Add more records...

]

# **Tasks**:

# 1. **Total Sales Calculation**: Create a function to calculate the total sales amount.
def total_sales(list_of_products):
    sales_counter = 0
    for product in sales_data:
        sales_counter += (product["quantity"]*product["price"])
    print(sales_counter)
    return sales_counter
total_sales(sales_data)

# 2. **Sales Summary by Product**: Generate a summary report showing total quantities and total revenue for each product.
print('\n')
def generate_summary(list_of_products):
    for product in sales_data:
        print(f"The quantity for the {product['product']} is {product['quantity']} and the the total revenue for it is {product['quantity']*product['price']}")
generate_summary(sales_data)

# 3. **Top Selling Product**: Determine which product generated the most revenue.
print('\n')
def most_revenued_product(list_of_products):
    most_revenue = 0
    top_selling_product = ""
    for product in list_of_products:
        best_revenue = product['quantity']*product['price']
        if best_revenue > most_revenue:
            most_revenue = best_revenue
            top_selling_product = product['product']
            print(f"The {top_selling_product} has the highest revenue which is {most_revenue}")
        
most_revenued_product(sales_data)

# 4. **Average Sale Price Per Product**: Calculate the average sale price of each product.
print('\n')
def average_sale_price(list_of_products):
    total_sales_made = 0
    total_quantity = 0
    for product in sales_data:
        total_quantity += product['quantity']
        total_sales_made += product['quantity']*product['price']
    average_price = total_sales_made / total_quantity
    print(f"The average sale price per product is {average_price}")

average_sale_price(sales_data)


# **Key Concepts to Apply**:

# - Data aggregation and manipulation.

# - Use of dictionaries and lists.

# - Functions and control structures (loops, conditionals).