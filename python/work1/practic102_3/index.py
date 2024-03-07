import csv

main = [["Звёздные войны", "Терминатор", "Искуственный интелект"], ["Дурак", "Матильда", "Левиафан"], ["Люди в чёрном", "Я - робот", "Эволюция"]]

with open("practic102_3\excel.csv", "w+") as f:
    w = csv.writer(f, delimiter=",")

    w.writerow(main[0])
    w.writerow(main[1])
    w.writerow(main[2])
