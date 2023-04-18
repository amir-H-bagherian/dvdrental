import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="dvdrental", user='postgres', password='amir138064', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("""
               SELECT film.title, COUNT(rental.rental_id) AS rental_count
               FROM film INNER JOIN inventory ON film.film_id = inventory.film_id
               INNER JOIN rental ON inventory.inventory_id = rental.inventory_id
               GROUP BY film.film_id ORDER BY rental_count DESC LIMIT 10;
               """)

#Print Data
data = cursor.fetchall()
print(*data, sep='\n')

#Commit Changes
conn.commit()
#Closing the connection
cursor.close()
conn.close()