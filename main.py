import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='postgres', password='amir138064', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select * from actor;")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
cursor.close()
conn.close()