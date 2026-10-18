import os

filename = "orders.txt"
orders = []

if os.path.exists(filename):
  with open(filename, "r") as f:
    for line in  f:
      orders.append(line.strip())

def save_orders():
  with open(filename, "w") as f:
    for order in orders:
      f.write(order + "\n")

print("Welcome to your commission  trackers!")

while True:
  print("\n--- Commission Tracker ---")
  print("1. View orders")
  print("2. Add an order")
  print("3. Mark an order as delivered")
  print("4. Delete an order")
  print("5. Quit")

  choice = input("Choose an option: ")

  if choice == "1":
    if len(orders) == 0:
      print("No orders yet!")
    else:
      delivered = 0
      for i in range(len(orders)):
        print(i + 1, "-", orders[i])
        if "[DELIVERED]" in orders[i]:
          delivered += 1
      print("Total orders:", len(orders), "| Delivered:", delivered)
      
  elif choice == "2":
        customer = input("Customer name ")
        item = input("What did they order? ")
        if customer == "" or item == "":
            print("Enter name and order")
        else:
            orders.append(customer + " - " + item)
            save_orders()
            print("Order added!")

  elif choice == "3":
    for i in range(len(orders)):
        print(i + 1, "-", orders[i])
    try:
        order_number = int(input("Enter the number of the order to mark as delivered: "))
        if 1 <= order_number <= len(orders):
            orders[order_number - 1] = orders[order_number - 1] + " [DELIVERED]"
            save_orders()
            print("Order marked as delivered!")
        else:
            print("Order number doesn't exist.")
    except ValueError:
        print("Please enter a number.")
        
        
  elif choice == "4":
    for i in range(len(orders)):
        print(i + 1, "-", orders[i])
    try:
        order_number = int(input("Enter the number of the order to delete: "))
        if 1 <= order_number <= len(orders):
            orders[order_number - 1] 
            save_orders()
            print("Order deleted!")#
        else:
            print("That order number does not exist.")
    except ValueError:
        print("Please enter a number.")

  elif choice == "5":
    print("Goodbye!")
    break
else:
    print("Please choose a number from 1 to 5")
