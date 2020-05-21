import mysql.connector
from dotenv import load_dotenv
import os

def answerTwo():
    while True:
                mycursor.execute("select distinct Είδος from Ζώο")
                a=mycursor.fetchall()
                print (a)
                sel = input('Επιλογή Ζώου ή Enter για να πας πίσω:')
                if sel == '': break
                mycursor.execute("select column_name from information_schema.columns where table_name=\"Ζώο\"")
                b=mycursor.fetchall()
                print(b)
                mycursor.execute("select * from Ζώο where Είδος=\""+sel+"\"")
                for j in mycursor:
                    print("->",j)

def answerThree():
    while True:
                mycursor.execute("select distinct Ειδικότητα from Υπάλληλος")
                a=mycursor.fetchall()
                print (a)
                sel = input('Επιλογή Ειδικότητας ή Enter για να πας πίσω:')
                if sel == '': break
                mycursor.execute("select * from Υπάλληλος where Ειδικότητα=\""+sel+"\"")
                for j in mycursor:
                    print("->",j)

def answerFour():
    while True:
                mycursor.execute("select distinct Είδος from Ζώο")
                a=mycursor.fetchall()
                print (a)
                sel = input('Επιλογή Ζώου ή Enter για να πας πίσω:')
                if sel == '': break
                mycursor.execute("select distinct Όνομα, Επώνυμο, Ιδιότητα from `Υπάλληλος` AS y JOIN `Υπεύθυνος για Ζώο` AS yz ON y.ΑΦΜ=yz.ΑΦΜ JOIN `Ζώο` AS z ON yz.Ζώο=z.Κωδικός where Είδος=\""+sel+"\"")
                for j in mycursor:
                    print("->",j)

def answerFive():
    mycursor.execute("select DATE_FORMAT(`Ημερ/Ώρα`, '%m/%d/%Y %H:%i'), Ομάδα, Τηλέφωνο from `Προκαθορισμένη ξενάγηση` where `Ημερ/Ώρα`>NOW()")
    for j in mycursor:
        print("->",j)

def manualQuery():
    while True:
        try:
            query = input("Type your query or cancel to exit:  ")

            if (query=="cancel" or query=="CANCEL"):
                break
        
            mycursor.execute(query)
        
            for i in mycursor:
                print("->",i)
        
        except:
            print("Invalid SQL command or problem executing the query.")
            continue

def main_menu():
    print('\nΕΠΙΛΟΓΕΣ')
    print('1: Εισαγωγή ερωτήματος mySQL')
    print('2: Εμφάνιση πληροφοριών για το ζώο: ')
    print('3: Αναζήτηση εργαζομένων με βάση την ειδικότητα.')
    print('4: Εμφάνιση υπαλλήλων που ασχολούνται με το ζώο: ')
    print('5: Εμφάνιση όλων των μελλοντικών ξεναγήσεων.')
    print('Enter για τερματισμό.')
    answer = ' '
    while not answer in '1 2 3 4 5'.split():
        answer = input('επιλογή.....')
        if answer == '': return 0
    else:
        return answer

load_dotenv()

HOST = os.getenv("ZOO_DB_HOST")
DB = os.getenv("ZOO_DB_NAME")
USER = os.getenv("ZOO_DB_USER")
PASSWORD = os.getenv("ZOO_DB_PASSWORD")

mydb = mysql.connector.connect(
  host=HOST,
  database=DB,
  user=USER,
  passwd=PASSWORD
)

mycursor = mydb.cursor()

while True:
        answer = main_menu()
        if not answer: break
        elif answer == '1': manualQuery()
        elif answer == '2': answerTwo()
        elif answer == '3': answerThree()
        elif answer == '4': answerFour()
        elif answer == '5': answerFive()

mycursor.close()

mydb.close()

print("Program Terminated.")
