import os
def readdata():
    lands = []
    try:
       file = open("lands.txt", "r")
       for line in file:
           indexx = line.strip().split(", ")
           if len(indexx) >= 6:
               kitta, city, direction, area, price, status = indexx[:6]
               land = {
                   "kitta": kitta,
                   "city": city,
                   "direction": direction,
                   "area": int(area),
                   "price": int(price),
                   "status": status,
                   "rented": False
               }
               if len(indexx) > 6:
                   land["startdate"] = indexx[6]
                   land["enddate"] = indexx[7]
                   land["rented"] = True
               lands.append(land)
       file.close()
    except FileNotFoundError:
      print("Land file not found")
    return lands

a = readdata()
print(a)