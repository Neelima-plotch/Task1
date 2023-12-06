import mysql.connector as MySQLdb

# MySQL Configuration
mydb = MySQLdb.connect (
     
  host="localhost",
  user="root",
  password="neelima_2012",
  database="movies"
)
  
mycursor = mydb.cursor()

def get_num_of_visitors(movie_id):
    
    try:
        # Fetching the number of visitors for the given movie ID from the database
        query = "SELECT SUM(visits) FROM visitors WHERE movie_id = %s"
        mycursor.execute(query, (movie_id,))
        result = mycursor.fetchone()

        if result is not None:
            num_of_visitors = result[0]
            return num_of_visitors
        else:
            return 0  
        
    except Exception as e:
        print(f'Error{e}')

def __del__(self):
       mycursor.close()
       mydb.close()



   