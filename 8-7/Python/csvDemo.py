import pandas

#csv url:https://github.com/jhnwllr/citizen-science/blob/master/data/citizenScienceTable.csv

df = pandas.read_csv("mijncsvdoethetwel.csv")

for data in df["url"]:
    print (data)

print ("het werkt");