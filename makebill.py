import datetime
from pathlib import Path
def rentinvoice(rentedlands, name, total):
        invoicefile = f"{name}rent.txt"
        file = open(invoicefile, 'w')
        file.write(f"{'_'*30}Techno Property Nepal{'_'*30}\n\n")
        file.write(f"    {'_'*30}Rent Invoice{'_'*30}\n\n")
        file.write(f"Customer Name: {name}\n")
        file.write(f"{'-'*80}")
        print(f"{'_'*30}Techno Property Nepal{'_'*30}\n\n")
        print(f"    {'_'*30}Rent Invoice{'_'*30}\n\n")
        print(f"Customer Name: {name}\n")
        print(f"{'-'*80}")
        for land in rentedlands:
              file.write(f"\nKitta Number: {land['kitta']}\n")
              file.write(f"City: {land['city']}\n")
              file.write(f"Direction: {land['direction']}\n")
              file.write(f"Area: {land['area']} anna\n")
              file.write(f"Rent Start Date: {land['startdate']}\n")
              file.write(f"Rent End Date: {land['enddate']}\n")
              file.write(f"Rent Amount(per month): Rs. {land['price'] * (datetime.datetime.strptime(land['enddate'], '%Y-%m-%d') - datetime.datetime.strptime(land['startdate'], '%Y-%m-%d')).days // 30}\n")
              print(f"\nKitta Number: {land['kitta']}\n")
              print(f"City: {land['city']}\n")
              print(f"Direction: {land['direction']}\n")
              print(f"Area: {land['area']} anna\n")
              print(f"Rent Start Date: {land['startdate']}\n")
              print(f"Rent End Date: {land['enddate']}\n")
              print(f"Rent Amount(per month): Rs. {land['price'] * (datetime.datetime.strptime(land['enddate'], '%Y-%m-%d') - datetime.datetime.strptime(land['startdate'], '%Y-%m-%d')).days // 30}\n")

        vat = total * 0.13
        total_cost_with_vat = total + vat
        file.write(f"{'-'*80}\n")
        file.write(f"\nSubtotal: Rs. {total}\n")
        file.write(f"VAT (13%): Rs. {vat:.2f}\n")
        file.write(f"Total Amount (including VAT): Rs. {total_cost_with_vat:.2f}\n")
        file.write(f"{'-'*80}\n")
        print(f"{'-'*80}\n")
        print(f"\nSubtotal: Rs. {total}\n")
        print(f"VAT (13%): Rs. {vat:.2f}\n")
        print(f"Total Amount (including VAT): Rs. {total_cost_with_vat:.2f}\n")
        print(f"{'-'*80}\n")
         
        file.close()
        return invoicefile
 

def returninvoice(land, name, fine, total_amount, returneddate):
     invoicefile = f"{name}_{land['kitta']}return.txt"
     file = open(invoicefile, 'w')
     file.write(f"{'_'*30}Techno Property Nepal{'_'*30}\n\n")
     file.write(f"{'_'*30}Return Invoice{'_'*30}\n\n")
     file.write(f"Customer Name: {name}\n")
     file.write(f"{'-'*80}\n")
     file.write(f"Kitta Number: {land['kitta']}\n")
     file.write(f"City: {land['city']}\n")
     file.write(f"Direction: {land['direction']}\n")
     file.write(f"Area: {land['area']} anna\n")
     file.write(f"Return Date: {returneddate.strftime('%Y-%m-%d')}\n")
     file.write(f"Rent Amount: Rs. {land['price']}\n")
     file.write(f"{'-'*80}\n")
     print("_"*30 + "Techno Property Nepal" + "_"*30 + "\n\n")
     print("_"*30 + "Return Invoice" + "_"*30 + "\n\n")
     print("Customer Name: " + name)
     print("-"*80)
     print("Kitta Number: " + land['kitta'])
     print("City: " + land['city'])
     print("Direction: " + land['direction'])
     print("Area: " + str(land['area']) + " anna")
     print("Return Date: " + returneddate.strftime('%Y-%m-%d'))
     print("Rent Amount: Rs. " + str(land['price']))
     print("-"*80 + "\n")
     if fine > 0:
         file.write(f"Late Return Fine : Rs. {fine:.2f}\n")
         print(f"Late Return Fine : Rs. {fine:.2f}\n")
     fine = float(fine)
     total_amount = float(total_amount)
     file.write(f"Total Amount: Rs. {total_amount:.2f}\n")
     print(f"Total Amount: Rs. {total_amount:.2f}\n")
     vat = total_amount * 0.13
     total_cost_with_vat = total_amount  + vat
     file.write(f"Total Amount (including VAT): Rs. {total_cost_with_vat:.2f}\n")
     print(f"Total Amount (including VAT): Rs. {total_cost_with_vat:.2f}\n")
     print(f"{'-'*80}\n")
     file.write(f"{'-'*80}\n")
     file.close()
     return invoicefile
