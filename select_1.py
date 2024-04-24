import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def selectpg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()          
        usrchoice = choice()
        if usrchoice == "1":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")           
            sql_select_query = """select * from circuits where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "2":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from constructor_results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
        
        if usrchoice == "3":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from constructor_standings where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "4":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from constructors where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "5":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from driver_standings where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "6":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            sql_select_query = """select * from drivers where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "7":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from lap_times where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "8":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from pit_stops where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "9":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from qualifying where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "10":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from races where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
            
        if usrchoice == "11":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

        if usrchoice == "12":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from seasons where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
        
        if usrchoice == "13":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from sprint_results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)

        if usrchoice == "14":
            tablename = input("Enter Column name: ")
            value = input("Enter a value: ")   
            
            sql_select_query = """select * from status where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_select_query)
            record = cursor.fetchone()
            print(record)
        
        
    except (Exception, psycopg2.Error) as error:
            print(error)

    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            