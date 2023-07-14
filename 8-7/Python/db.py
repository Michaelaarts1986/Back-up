import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "appeltjes",
  port = "3306",
)

dbc = db.cursor()
dbc.execute("SELECT * FROM `appels`")

appeltjes = dbc.fetchall()

# print (appeltjes)

for appel in appeltjes:
  print(appel[1])
  print(appel[2])

naamInput = input("Naam van appel")
prijsInput = input("Prijs van de appel per kilo")
kleurInput = input("Kleur van de appel")



sql = "INSERT INTO appels (naam, prijsperkilo, kleur) VALUES (%s, %s, %s)"

values = (naamInput, prijsInput, kleurInput)

dbc.execute(sql, values)

db.commit()

print("het werkt beter toch?");
