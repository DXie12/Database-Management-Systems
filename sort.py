import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def sqlsort():
    sortchoice= input("How would you like to sort?: ascent(1), descent(2): ")
    return sortchoice

def sortpg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()          
        usrchoice = choice()
        if usrchoice == "1":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from circuits order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from circuits order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
 
        if usrchoice == "2":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructor_results order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructor_results order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
        
        if usrchoice == "3":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructor_standings order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructor_standings order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "4":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructors order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from constructors order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "5":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from driver_standings order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from driver_standings order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "6":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from drivers order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from drivers order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "7":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from lap_times order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from lap_times order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "8":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from pit_stops order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from pit_stops order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "9":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from qualifying order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from qualifying order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "10":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from races order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from races order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
            
        if usrchoice == "11":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from results order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from results order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)

        if usrchoice == "12":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from seasons order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from seasons order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
        
        if usrchoice == "13":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from sprint_results order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from sprint_results order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)

        if usrchoice == "14":
            sortchoice = sqlsort()
            if sortchoice == "2":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from status order by  "%s" desc; """%(tablename)
                cursor.execute(sql_sort_query)
                record = cursor.fetchall()
                print(record)
                
            if sortchoice == "1":
                tablename = input("Enter Column name: ")
                sql_sort_query = """select * from status order by  "%s" asc; """%(tablename)
                cursor.execute(sql_sort_query)
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