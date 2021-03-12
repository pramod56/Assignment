grocery_list=[]
def choice(items,Amount):
    value=0
    for products in grocery_list:
        value=value+products[2]
    value=Amount-value
    for item in grocery_list:
        if item[0]==items[0]:
            if items[2]<=value:
                item[1]=item[1]+items[1]
                item[2]=item[2]+items[2]
                break;
        if items[2]> value:
            print("Can't buy the product because purchase price gretaer")
            break;
    else:
        grocery_list.append(items)    
    sum_products=0
    for product in grocery_list:
        sum_products =sum_products+product[2]

    bugdet=Amount-sum_products
    print()
    print("Amount left in the bugdet is",bugdet)

def print_list(Amount):
    value=0
    for product in grocery_list:
        value =value+product[2]
    after_value=Amount-value
    if after_value:
        print("Amount still left  you can buy ",end=" ") 
        for product in grocery_list:
            if(after_value>=product[2]):
                print (product[0],end=" ")
        print()
        print()
        print()
        print("GROCERY LIST is:")
        print("Product name","Quantity","Price",sep="\t")
        for products in grocery_list:
            print(products[0],products[1],products[2],sep="\t\t")

if __name__=="__main__":
    
    total_budget=int(input("enter your budget:"))
    while True:
        items=[]
        print()
        print("1. Add an item")
        print()
        print("2. Exit")
        print()
        choice_input=int(input("Enter your choice:"))
        print()
        if(choice_input==1):
            product=input("enter your product:")
            items.append(product)
            print()
            quantity=float(input("enetr quantity:"))
            items.append(quantity)
            print()
            price=int(input("enter price:"))
            items.append(price)
            choice(items,total_budget)
        if(choice_input==2):
            print_list(total_budget)
            break;

                      
            
        
