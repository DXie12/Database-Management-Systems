import psycopg2

def choice():
    usrchoice= input("Choose a value1: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
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
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
        
            
            sql_update_query = """Update circuits set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "2":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
            
            sql_update_query = """Update constructor_results set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "3":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
            
            sql_update_query = """Update constructor_standings set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "4":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
            
            sql_update_query = """Update constructors set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "5":
            

            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
            
            sql_update_query = """Update driver_standings set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "6":
            

            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
            
            sql_update_query = """Update drivers set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "7":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")        
            
            sql_update_query = """Update lap_times set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "8":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")        
            
            sql_update_query = """Update pit_stops set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")

        if usrchoice == "9":

            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")        
            
            sql_update_query = """Update qualifying set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "10":

            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")        
            
            sql_update_query = """Update races set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "11":

            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")        
            
            sql_update_query = """Update results set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "12":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")       
            
            sql_update_query = """Update seasons set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "13":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
        
            
            sql_update_query = """Update sprint_results set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
            connection.commit()
            print("Record Updated successfully ")
            
        if usrchoice == "14":
            
            column1 = input("Enter Column1 name: ")
            value1 = input("New value1 value: ")
            column2 = input("Enter Column2 name: ")
            value2 = input("New value2 value: ")
        
            
            sql_update_query = """Update circuits set "%s" = %s where "%s" = %s"""  % (column1, value1,column2,value2)
            cursor.execute(sql_update_query,(column1, value1,column2,value2))
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