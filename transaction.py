import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def transaction():
    transchoice= input("What transaction operation?: update(1), rollback(2): ")
    return transchoice

def transactionpg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        connection.autocommit = False
        cursor = connection.cursor()
        
        transchoice=transaction()
        if transchoice == "1":
            table = input("Enter table name: ")
            columnname = input("Enter column name: ")
            newval = input("Enter new value: ")
            columnname2 = input("Enter column name: ")
            id = input("Enter id: ")


            query = """Update "%s" set "%s" = "%s" where "%s" = "%s" """%(table,columnname,newval,columnname2,id)
            cursor.execute(query)
            record = cursor.fetchone()
            print(record)

            connection.commit()
            print("Transaction completed successfully ")
    
        if transchoice == "2":
            connection.rollback()
            connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        connection.rollback()

    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")  