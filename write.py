import os

def write_data(lands):
    try:
        file = open("lands.txt", "w")
        for land in lands:
            values = [land["kitta"], land["city"], land["direction"], str(land["area"]), str(land["price"]), land["status"]]
            if land.get("rented", False):
                values.append(str(land["startdate"]))
                values.append(str(land["enddate"]))
            line = ", ".join(values)
            file.write(line + "\n")
        file.close()
    except IOError:
        print("Error writing to the land data file.")