
#this is my python lab mini project
#-------------------------SATHWIK.R
#-------------------------SHRADDESH 
#-------------------------SIDDANTH




#createing the menu

menu={
    "pizza":{
        "small":{
          "cost": 100,
            "quantity":0
        },
        "medium":{
            "cost": 200,
            "quantity":0
        },
        "large":{
            "cost": 300,
            "quantity":0

        }
    },
    "burger":{
        "small":{
            "cost":100,
            "quantity":0
        },
        "medium":{
            "cost":100,
            "quantity":0
        },
        "large":{
            "cost":100,
            "quantity":0
        }

    },
    "coke":{
        "small":{
            "cost":100,
            "quantity":0
        },
        "medium":{
            "cost":200,
            "quantity":0

        },
        "large":{
            "cost":300,
            "quantity":0
        }

    },
    "Chicken":{
        "small":{
            "cost":100,
            "quantity":0
        },
        "medium":{
            "cost":200,
            "quantity":0
        },
        "large":{
            "cost":300,
            "quantity":0
        }
    }


}



#bill the following


def bill(menu):
    total_bill=0
    for item in menu:
        for size in menu[item]:
           total_bill += menu[item][size]["cost"] * menu[item][size]["quantity"]
    return total_bill       


#order of the entire program

def order(menu):
    while(1):
        print("OUR MENU\n1.pizza\n2.burger\n3.coke\n4.chicken\n\n\n")
        item =input("\nENTER THE ITEM YOU NEED TO ORDER\n")
        
        if item not in menu:
            
            print("WE ARE SORRY!!!!!\nTHE ITEM IS NOT AVILABLE IN OUR HOTEL")
            continue
        print("THE SIZE AVILABLE ARE \n1.small\n2.medium\n3.large\n\n")
        size = input("\nENTER THE SIZE OF THE ITEM\n")
        if size not in menu[item]:
            print("WE ARE SORRY!!!!\nWE DONT WHAVE THAT SIZE ")
            continue
        quantity=int(input("\nENTER THE QUNTITY\n"))
        menu[item][size]["quantity"] += quantity
        print("YOUR ORDER HAS BEEN PLACED ")
        print("YOUR BILL IS",bill(menu))
        
        print("\nTHANK YOU FOR OUR ORDER \n VISIT AGAIN  :)")
        print("DO YOU WANT TO ORDER MORE??  (Y/N) ")
        choice = input()
        if choice == "N":
            break
        

order(menu)                  
