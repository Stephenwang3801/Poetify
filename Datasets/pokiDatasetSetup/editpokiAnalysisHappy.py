import csv
joy = 16
sadness=15
fear=14
anger=13
header=True
with open('poki-analysis.csv', 'r', encoding='utf-8') as inp, open('poki-analysis-happy.csv', 'w', newline='',encoding = 'utf-8') as out:

    writer = csv.writer(out)

    for row in csv.reader(inp):
        if header:
            writer.writerow(row)
            header = False
            continue
        
        #make sure poem is happy
        if row[joy] != 'NA' and float(row[joy]) > 0.5:
            pass
        else:
            continue


        #make sure poem is also not sad/angry/fearful
        if row[sadness] != 'NA':
            if float(row[sadness]) > 0.4:
                continue
        if row[fear] != 'NA':
            if float(row[fear]) > 0.4:
                continue
        if row[anger] != 'NA':
            if float(row[anger]) > 0.4:
                continue

        writer.writerow(row)