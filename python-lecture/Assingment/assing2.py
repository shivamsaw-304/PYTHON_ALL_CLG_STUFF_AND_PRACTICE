orders = [ 
    { 
        'id': 101, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)] 
    }, 
    { 
        'id': 102, 
        'customer': 'Ravi', 
        'status': 'CANCELLED', 
        'items': [('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 103, 
        'customer': 'Asha', 
        'status': 'DELIVERED', 
        'items': [('cable', 5, 199.0)] 
    }, 
    { 
        'id': 104, 
        'customer': 'Meera', 
        'status': 'SHIPPED', 
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)] 
    }, 
    { 
        'id': 105, 
        'customer': 'Ravi', 
        'status': 'DELIVERED', 
        'items': [('mouse', 3, 599.0)] 
    } 
] 

# Write a function:  analyse(orders) which return a dictionary with the following details.

# A. Customer Revenue  
# 1. Calculate the total amount spent by each customer. 
# • Ignore cancelled orders. 
# • Order value = Quantity × Unit Price 
# Store the result in: "revenue" 

# B. Top Selling Products  
# Find the top 2 products sold. 
# • Ignore cancelled orders. 
# • Count the total quantity sold for each product. 
# FYMCA Semester 1 (2026-28 batch) 
# • Arrange products from highest to lowest quantity sold. 
# • If quantities are the same, sort alphabetically. 
# Store the result in:  "top_products" 

# C. Fully Delivered Customers  
# Find customers whose all orders are DELIVERED. 
# • Even one SHIPPED or CANCELLED order makes the customer ineligible. 
# • Use a set or comprehension. 
# • Return names in sorted order. 
# Store the result in: "fully_delivered" 


def anylisis():

    revenue = {}
    topProducts = {}

    
    for data in orders :

        if data.get("status") == "CANCELLED":
            continue

        customer = data.get("customer")

        if  customer not in revenue :
            revenue[data.get("customer" )] = 0 

        item = data.get("items")
        orderValue = item[0][1] * item[0][2]

        revenue[customer] = revenue[customer] + orderValue

        for items  in item :
            topProducts[items[0]] = 0 

        topProducts[items[0]] += items[1]
        print(sorted(topProducts))

    print(topProducts)
        



    return revenue




       


#  ok so dict.get() method takes keys as argument and return value of the key 


         

#         for customers in data.keys():
#             if customers.get("status") == "CANCELLED":
#                 print(customers.values())
#                 continue
#             print(customers.get())
#             pass
            
#         print("-------")


anylisis()

# print(orders)
