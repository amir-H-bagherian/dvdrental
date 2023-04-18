import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="dvdrental", user='postgres', password='amir138064', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("""
            SELECT CONCAT(c.first_name, ' ', c.last_name) AS full_name,COUNT(r.rental_id) AS rental_count
            FROM customer c
            JOIN rental r USING (customer_id)
            WHERE c.activebool IS TRUE
            GROUP BY c.customer_id
            ORDER BY rental_count DESC
            LIMIT 5;
               """)

#Print Data
data = cursor.fetchall()
print(*data, sep='\n')

#Commit Changes
conn.commit()
#Closing the connection
cursor.close()
conn.close()