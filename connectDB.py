import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                  password="LXOosx35855",
                                  host="node7551-itstaff.app.ruk-com.cloud",
                                  #host="node7074-itstaff-cloud00.googlejp.app.ruk-com.cloud",
                                  port="11073",
                                  database="cloudDB")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        