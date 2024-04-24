import psycopg2

def joinpg():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        
        cursor = connection.cursor()          
        tablename = input("Enter Table name: ")
        tablename2 = input("Enter Second Table name: ")
        columnname = input("Enter Column name: ")
        columnname2 = input("Enter Second Column name: ")
        
        sql_join_query = """select * from "%s" inner join "%s" on  "%s"."%s" = "%s"."%s" """%(tablename, tablename2, tablename, columnname, tablename2, columnname2)
        cursor.execute(sql_join_query)
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