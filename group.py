import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def grouppg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()          
        usrchoice = choice()
        if usrchoice == "1":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from circuits group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "2":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from constructor_results group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
        
        if usrchoice == "3":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from constructor_standings group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "4":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from constructors group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "5":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from driver_standings group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "6":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from drivers group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "7":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from lap_times group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "8":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from pit_stops group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "9":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from qualifying group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "10":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from races group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
            
        if usrchoice == "11":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from results group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)

        if usrchoice == "12":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from seasons group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
        
        if usrchoice == "13":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from sprint_results group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)

        if usrchoice == "14":
            columnname = input("Enter column name: ")
            columnname2 = input("Enter second column name: ")
                 
            sql_grouping_query = """select count(*), "%s" from status group by "%s" """%(columnname,columnname2)
            cursor.execute(sql_grouping_query)
            record = cursor.fetchall()
            print(record)
        
    except (Exception, psycopg2.Error) as error:
            print(error)

    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")