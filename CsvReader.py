import csv
matrix = []
dict = {}
questions = False
i = 9
media = 0


with open("/Users/filippobotti/Desktop/Personale/Intelligenza Artificiale/report-2016-2017.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        matrix.append(row)

while i < len(matrix)-2:
    if matrix[i][0] == "Dipartimento:":
        dict[modulo] = media/(votanti*11)
        media = 0
        questions = False
    if matrix[i][0] == "UD:":
        modulo = matrix[i][1].split()[0]
        i += 5
        questions = True
    if questions:
        media += (int(matrix[i][4])*10 + int(matrix[i][6])*20 + int(matrix[i][8])*30)
        votanti = int(matrix[i][2])
    i+=1


try:
    with open("/Users/filippobotti/Desktop/Personale/Intelligenza Artificiale/results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("Modulo", "Media"))
        for key,value in dict.items():
            writer.writerow((key,value))
except IOError as err:
    print("Error while opening the file")


        
        