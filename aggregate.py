import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def aggregate():
    mathchoice= input("What would you like to do?: sum(1), average(2), count(3), min(4), max(5): ")
    return mathchoice

def aggregatepg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()          
        usrchoice = choice()
        if usrchoice == "1":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM circuits"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM circuits"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM circuits"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM circuits"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM circuits"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
          
        if usrchoice == "2":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM constructor_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM constructor_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM constructor_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM constructor_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM constructor_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
        
        if usrchoice == "3":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM constructor_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM constructor_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM constructor_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM constructor_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM constructor_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "4":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM constructors"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM constructors"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM constructors"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM constructors"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM constructors"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "5":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM driver_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM driver_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM driver_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM driver_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM driver_standings"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "6":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM drivers"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM drivers"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM drivers"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM drivers"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM drivers"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "7":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM lap_times"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM lap_times"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM lap_times"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM lap_times"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM lap_times"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "8":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM pit_stops"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM pit_stops"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM pit_stops"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM pit_stops"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM pit_stops"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "9":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM qualifying"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM qualifying"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM qualifying"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM qualifying"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM qualifying"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "10":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM races"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM races"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM races"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM races"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM races"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
            
        if usrchoice == "11":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)

        if usrchoice == "12":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM seasons"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM seasons"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM seasons"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM seasons"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM seasons"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
        
        if usrchoice == "13":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM sprint_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM sprint_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM sprint_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM sprint_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM sprint_results"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)

        if usrchoice == "14":
            mathchoice = aggregate()
            
            if mathchoice == "1":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select sum("%s") FROM status"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "2":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select avg("%s") FROM status"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "3":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select count("%s") FROM status"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "4":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select min("%s") FROM status"""%(tablename)
                cursor.execute(sql_aggregate_query)
                record = cursor.fetchone()
                print(record)
                
            if mathchoice == "5":
                tablename = input("Enter Column name: ")
                sql_aggregate_query = """select max("%s") FROM status"""%(tablename)
                cursor.execute(sql_aggregate_query)
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