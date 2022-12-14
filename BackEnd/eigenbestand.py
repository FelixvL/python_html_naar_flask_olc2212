#import mysql.connector  # deprectated
import mariadb
import json
import pandas

def ganaardedb():
    mydb = mariadb.connect(
        host="localhost",
        username="root",
        password="",
        database="demopythonsql"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM auto")

    myresult = mycursor.fetchall()
    mijnlijst = []
    for x in myresult:
        print(x[1])
        mijnlijst.append(x[1])

    return json.dumps(mijnlijst)

#print(ganaardedb())

def eencsvuitlezen():
    pokemons = pandas.read_csv("Pokemon.csv")
    print(pokemons)
    return pokemons.to_json(orient="table")

#eencsvuitlezen()