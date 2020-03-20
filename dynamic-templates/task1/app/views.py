from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'
    inflation_stat=[]
    with open('inflation_russia.csv', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        row_int = 0
        for row in reader:
            inflation_stat.append({'Year': row[reader.fieldnames[0]],
                                   'Jan': row[reader.fieldnames[1]],
                                   'Feb': row[reader.fieldnames[2]],
                                   'Mar': row[reader.fieldnames[3]],
                                   'Apr': row[reader.fieldnames[4]],
                                   'May': row[reader.fieldnames[5]],
                                   'Jun': row[reader.fieldnames[6]],
                                   'Jul': row[reader.fieldnames[7]],
                                   'Aug': row[reader.fieldnames[8]],
                                   'Sep': row[reader.fieldnames[9]],
                                   'Oct': row[reader.fieldnames[10]],
                                   'Nov': row[reader.fieldnames[11]],
                                   'Dec': row[reader.fieldnames[12]],
                                   'Sum': row[reader.fieldnames[13]]})
#            z = float(row[reader.fieldnames[8]])
 #           if z < 0:
  #              print ('green')
   #         else:
    #            if z > 5:
     #               print('darkred')

    context = {'inflation_stat': inflation_stat}
    return render(request, template_name,
                  context)