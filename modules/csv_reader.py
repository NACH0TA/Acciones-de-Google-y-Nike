import csv

def reader(archivo:str):
    csvlist = []

    with open(archivo, "r") as csvfile:
        csvfile = csvfile.read().replace(" ", ",")
        csvreader = csv.reader(csvfile.splitlines(), delimiter= ",")
        next(csvreader)

        for row in csvreader:
            csvlist.append(row)

    return csvlist