import datetime
from makebill import rentinvoice , returninvoice
from write import write_data
def rentland(lands):
    rentedland = []
    total = 0
    n = input("Enter customer name  : ")
    while True:
        kitta = input("Enter kitta number to rent or enter q to exit: ")
        if kitta.lower() == 'q':
            break

        i = False
        for land in lands:
            if land['kitta'] == kitta and land['status'] == 'Available' and not land['rented']:
              while True:
               try:
                   monthin = input(f"Enter the number of months to rent land {kitta}: ")
                   if monthin.isdigit():
                       month = int(monthin)
                       if month <= 0:
                           print("Invalid rental duration, skipping this land.")
                       else:
                           break
                   else:
                       print("Please enter a valid number.")
               except ValueError:
                   print("Enter a valid month")
                   continue
              land['status'] = 'Not Available'
              land['rented'] = True
              land['startdate'] = str(datetime.date.today())
              enddate = datetime.date.today() + datetime.timedelta(days=month * 30)
              land['enddate'] = str(enddate) 
              rentedland.append(land)
              total += land['price'] * month
              i = True
              print(f"Land {kitta} rented successfully for {month} month.")
              break
        if not i:
            print(f"Kitta number  {kitta} is not available ")
    if rentedland:
        write_data(lands)
        invoicefile = rentinvoice(rentedland, n, total)
        print(f"Rent invoice generated: {invoicefile}")
        
        
    else:
        print("No lands rented.")

def finacalculate(land, returndate, y):
    enddate = datetime.datetime.strptime(land["enddate"], "%Y-%m-%d").date()    
    latedays = (returndate - enddate).days + 1
    latemonths = (latedays + 29) // 30  
    print(y)
    print(latemonths)
    fine = y * 0.02 * latemonths
    print(fine)
    if fine < 0:
        fine = 0
    return fine
def returntheland(lands):
  kitta = input("Enter the kitta number of the land you want to return:\n ")
  today = datetime.date.today()
  for land in lands:
     if land["kitta"] == kitta and land.get("rented", False):
         n = input("Enter customer name: ")
         start_date = datetime.datetime.strptime(land['startdate'], '%Y-%m-%d').date()
         end_date = datetime.datetime.strptime(land['enddate'], '%Y-%m-%d').date()
         daydiff = (end_date.year - start_date.year) * 12 + end_date.month - start_date.month
         total_amount_withoutfine = land["price"]*daydiff
         fine = finacalculate(land, today,total_amount_withoutfine)
         total_amount = total_amount_withoutfine + fine
         invoicefile = returninvoice(land, n, fine, total_amount, today)

         land["status"] = 'Available'
         land["rented"] = False
         land["startdate"] = None
         land["enddate"] = None
         write_data(lands)

         print(f"Land {kitta} returned successfully. Return invoice generated: {invoicefile}")
         return  
  print(f"Land {kitta} is not currently rented.")