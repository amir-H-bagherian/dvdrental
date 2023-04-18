import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="dvdrental", user='postgres', password='amir138064', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("""
                SELECT CONCAT(st.first_name, ' ', st.last_name), COUNT(r.rental_id) AS rental_count
                FROM staff st
                JOIN rental r USING (staff_id)
                GROUP BY st.staff_id
                ORDER BY rental_count DESC
               """)

#Print Data
data = cursor.fetchall()
print(*data, sep='\n')

#Commit Changes
conn.commit()
#Closing the connection
cursor.close()
conn.close()