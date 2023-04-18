import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="dvdrental", user='postgres', password='amir138064', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("""
                SELECT store.store_id, SUM(amount) AS total_revenue
                FROM store
                JOIN staff USING (store_id)
                JOIN payment USING (staff_id)
                GROUP BY store.store_id
                ORDER BY total_revenue DESC
               """)

#Print Data
data = cursor.fetchall()
print(*data, sep='\n')

#Commit Changes
conn.commit()
#Closing the connection
cursor.close()
conn.close()