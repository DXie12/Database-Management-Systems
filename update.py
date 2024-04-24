import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice

def updatepg():   
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()  
               
        usrchoice = choice()
        
        if usrchoice == "1":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update circuits set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "2":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update constructor_results set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "3":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update constructor_standings set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "4":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update constructors set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "5":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update driver_standings set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "6":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update drivers set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "7":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update lap_times set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "8":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update pit_stops set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")

        if usrchoice == "9":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update qualifying set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "10":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update races set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "11":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update results set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "12":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update seasons set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "13":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update sprint_results set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "14":
            
            tableid = input("tableid: ")
            idnum = input("Enter ID number: ")
            tablename = input("Enter Table name: ")
            table = input("New Table value: ")
        
            
            sql_update_query = """Update status set "%s" = %s where "%s" = %s"""  % (tablename, table,tableid,idnum)
            cursor.execute(sql_update_query,(tablename, table,tableid,idnum))
            connection.commit()
            print("Record Updated successfully ")
    
        
    except (Exception, psycopg2.Error) as error:
            print(error)

    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")