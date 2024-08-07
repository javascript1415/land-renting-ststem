def displaay(lands):
    print("Available Lands:")
    print(f"+{'_'*95}")
    print(f"|Kitta    City      Direction:      Area(in anna)     Price")
    print(f"+{'_'*95}")

    for land in lands:
        if land["status"] == "Available" and not land["rented"]:
            print(f"|{land['kitta']}     {land['city']}    {land['direction']}         {land['area']}                {land['price']}")
    print(f"+{'_'*95} \n")
    

    print("\nUnavailable lands:")
    print(f"+{'_'*95}")
    print(f"|Kitta    City      Direction:      Area(in anna)     Price")
    print(f"+{'_'*95}")

    for land in lands:  
        if land["status"] == "Not Available" or land["rented"]:
            if "start_date" in land and "end_date" in land:
              print(f"|{land['kitta']}     {land['city']}    {land['direction']}         {land['area']}                {land['price']}")
            else:
              print(f"|{land['kitta']}     {land['city']}    {land['direction']}         {land['area']}                {land['price']}")
    print(f"+{'_'*95}") 