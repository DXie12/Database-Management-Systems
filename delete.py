import psycopg2

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice


def deletepg():       
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
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from circuits where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
        
        if usrchoice == "2":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from constructor_results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
        
        if usrchoice == "3":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from constructor_standings where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "4":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from constructors where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "5":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from driver_standings where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "6":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from drivers where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "7":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from lap_times where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "8":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from pit_stops where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "9":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from qualifying where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "10":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from races where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
            
        if usrchoice == "11":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")

        if usrchoice == "12":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from seasons where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
        
        if usrchoice == "13":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from sprint_results where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")

        if usrchoice == "14":
            tablename = input("Enter Column name: ")
            value = input("Value of Column to delete: ")
            
            sql_delete_query = """Delete from status where "%s" = %s"""%(tablename,value)
            cursor.execute(sql_delete_query)
            connection.commit()
            print("Record deleted successfully ")
        
        
    except (Exception, psycopg2.Error) as error:
            print(error)

    finally:
    # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")