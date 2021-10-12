# importing the module
import pandas
  
# reading the files
f1 = pandas.read_excel("poki-analysis-happy.xlsx")
f2 = pandas.read_excel("poki.xlsx")
  
# merging the files
f3 = f1[["id", 
         "text"]].merge(f2[["id"]], 
                                     on = "id", 
                                     how = "left")
  
# creating a new file
f3.to_excel("poki-happy.xlsx", index = False)