import psycopg2



def create_connection():
    try: 
        connection = psycopg2.connect(
            dbname = "users",
            user = "admin",
            password = "admin",
            host = "localhost",
            port = "5432" 
        )
        
        return connection
    
    except Exception as e:
        print(f"Error : {e}")
        return None 

