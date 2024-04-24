import psycopg2

def circuits():
    circuitId = input("circuitId: ")
    circuitRef = input("circuitRef: ")
    name = input("name: ")
    location = input("location: ")
    country = input("country: ")
    return circuitId, circuitRef, name, location, country

def constructor_results():
    constructorResultsId = input("constructorResultsId: ")
    raceId = input("raceId: ")
    constructorId = input("constructorId: ")
    points = input("points: ")
    return constructorResultsId, raceId, constructorId, points

def constructor_standings():
    constructorStandingsId = input("constructorStandingsId: ")
    raceId = input("raceId: ")
    constructorId = input("constructorId: ")
    points = input("points: ")
    position = input("position: ")
    wins = input("wins: ")
    return constructorStandingsId, raceId, constructorId, points, position, wins

def constructors():
    constructorId = input("constructorId: ")
    constructorRef = input("constructorRef: ")
    name = input("name: ")
    nationality = input("nationality: ")
    return constructorId, constructorRef, name, nationality

def driver_standings():
    driverStandingsId = input("driverStandingsId: ")
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    points = input("points: ")
    position = input("position: ")
    wins = input("wins: ")
    return driverStandingsId, raceId, driverId, points, position, wins

def drivers():
    driverId = input("driverId: ")
    driverRef = input("driverRef: ")
    number = input("number: ")
    code = input("code: ")
    forename = input("forename: ")
    surname = input("surname: ")
    dob = input("dob: ")
    nationality = input("nationality: ")
    return driverId, driverRef, number, code, forename, surname, dob, nationality

def lap_times():
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    lap = input("lap: ")
    position = input("position: ")
    time = input("time: ")
    return raceId, driverId, lap, position, time

def pit_stops():
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    stop = input("stop: ")
    lap = input("lap: ")
    position = input("position: ")
    time = input("time: ")
    duration = input("duration: ")
    return raceId, driverId, stop, lap, position, time, duration

def qualifying():
    qualifyId = input("qualifyId: ")
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    constructorId = input("constructorId: ")
    number = input("number: ")
    position = input("position: ")
    q1 = input("q1: ")
    q2 = input("q2: ")
    q3 = input("q3: ")
    return qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3

def races():
    raceId = input("raceId: ")
    year = input("year: ")
    round = input("round: ")
    circuitId = input("circuitId: ")
    name = input("name: ")
    date = input("date: ")
    return raceId, year, round, circuitId, name, date

def results():
    resultId = input("resultId: ")
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    constructorId = input("constructorId: ")
    number = input("number: ")
    grid = input("grid: ")
    position = input("position: ")
    points = input("points: ")
    return resultId, raceId, driverId, constructorId, number, grid, position, points

def seasons():
    year = input("year: ")
    url = input("url: ")
    return year, url

def sprint_results():
    resultId = input("resultId: ")
    raceId = input("raceId: ")
    driverId = input("driverId: ")
    constructorId = input("constructorId: ")
    number = input("number: ")
    grid = input("grid: ")
    position = input("position: ")
    points = input("points: ")
    return resultId, raceId, driverId, constructorId, number, grid, position, points

def status():
    statusId = input("statusId: ")
    statuss = input("status: ")
    return statusId, statuss

def choice():
    usrchoice= input("Choose a table: circuits(1), constructor_results(2), constructor_standings(3), constructors(4), driver_standings(5), drivers(6), lap_times(7), pit_stops(8), qualifying(9), races(10), results(11), seasons(12), sprint_results(13), status(14): ")
    return usrchoice


def insertpg():    
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="hello5959",
                                        host="localhost",
                                        port="5432",
                                        database="postgres")
        c = connection.cursor()
         
        usrchoice = choice()
        if usrchoice == "1":
            circuitId, circuitRef, name, location, country = circuits()
            postgres_insert_query = """ INSERT INTO circuits ("circuitId", "circuitRef", "name", "location", "country") VALUES (%s,%s,%s,%s,%s) """        
            record_to_insert = (circuitId, circuitRef, name, location, country)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
        
        if usrchoice == "2":
            constructorResultsId, raceId, constructorId, points = constructor_results()
            postgres_insert_query = """ INSERT INTO constructor_results ("constructorResultsId", "raceId", "constructorId", "points") VALUES (%s,%s,%s,%s) """   
            record_to_insert = (constructorResultsId, raceId, constructorId, points)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
        
        if usrchoice == "3":
            constructorStandingsId, raceId, constructorId, points, position, wins = constructor_standings()
            postgres_insert_query = """ INSERT INTO constructor_standings ("constructorStandingsId", "raceId", "constructorId", "points", "position", "wins") VALUES (%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (constructorStandingsId, raceId, constructorId, points, position, wins)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "4":
            constructorId, constructorRef, name, nationality = constructors()
            postgres_insert_query = """ INSERT INTO constructors ("constructorId", "constructorRef", "name", "nationality") VALUES (%s,%s,%s,%s) """
            
            record_to_insert = (constructorId, constructorRef, name, nationality)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "5":
            driverStandingsId, raceId, driverId, points, position, wins = driver_standings()
            postgres_insert_query = """ INSERT INTO driver_standings ("driverStandingsId", "raceId", "driverId", "points", "position", "wins") VALUES (%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (driverStandingsId, raceId, driverId, points, position, wins)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "6":
            driverId, driverRef, number, code, forename, surname, dob, nationality = drivers()
            postgres_insert_query = """ INSERT INTO drivers ("driverId", "driverRef", "number", "code", "forename", "surname", "dob", "nationality") VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (driverId, driverRef, number, code, forename, surname, dob, nationality)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "7":
            raceId, driverId, lap, position, time = lap_times()
            postgres_insert_query = """ INSERT INTO lap_times ("raceId", "driverId", "lap", "position", "time") VALUES (%s,%s,%s,%s,%s) """
            
            record_to_insert = (raceId, driverId, lap, position, time)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "8":
            raceId, driverId, stop, lap, position, time, duration = pit_stops()
            postgres_insert_query = """ INSERT INTO pit_stops ("raceId", "driverId", "stop", "lap", "position", "time", "duration") VALUES (%s,%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (raceId, driverId, stop, lap, position, time, duration)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "9":
            qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3 = qualifying()
            postgres_insert_query = """ INSERT INTO qualifying ("qualifyId", "raceId", "driverId", "constructorId", "number", "position", "q1", "q2", "q3") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "10":
            raceId, year, round, circuitId, name, date = races()
            postgres_insert_query = """ INSERT INTO races ("raceId", "year", "round", "circuitId", "name", "date") VALUES (%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (raceId, year, round, circuitId, name, date)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
        if usrchoice == "11":
            resultId, raceId, driverId, constructorId, number, grid, position, points = results()
            postgres_insert_query = """ INSERT INTO results ("resultId", "raceId", "driverId", "constructorId", "number", "grid", "position", "points") VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (resultId, raceId, driverId, constructorId, number, grid, position, points)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")

        if usrchoice == "12":
            year, url = seasons()
            postgres_insert_query = """ INSERT INTO seasons ("year", "url") VALUES (%s,%s) """
            
            record_to_insert = (year, url)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
        
        if usrchoice == "13":
            resultId, raceId, driverId, constructorId, number, grid, position, points = sprint_results()
            postgres_insert_query = """ INSERT INTO sprint_results ("resultId", "raceId", "driverId", "constructorId", "number", "grid", "position", "points") VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
            
            record_to_insert = (resultId, raceId, driverId, constructorId, number, grid, position, points)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")

        if usrchoice == "14":
            statusId, statuss = status()
            postgres_insert_query = """ INSERT INTO status ("statusId", "status") VALUES (%s,%s) """
            
            record_to_insert = (statusId, statuss)
            c.execute(postgres_insert_query, record_to_insert)

            connection.commit()
            print("Record inserted successfully into table")
            
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table: ", error)

    finally:
    # closing database connection.
        if connection:
            c.close()
            connection.close()
            print("PostgreSQL connection is closed")