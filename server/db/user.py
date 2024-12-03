from db.connection import create_connection

from model.user import UserCreate, UserUpdate, UserAuthenticate

from utils.hash import verify, encrypt

def createUser(user : UserCreate):
    connection = create_connection()
    user.password = encrypt(user.password) 
    if connection:
        try:
            cursor = connection.cursor()
            query = f"INSERT INTO users (username, password, first_name, last_name, dob, gender, type)\
            values ('{user.username}', '{user.password}', '{user.firstName}', '{user.lastName}', '{user.dob}'\
            , '{user.gender}', '{user.type}')\
            RETURNING id;"
            cursor.execute(query) 
            user_id = cursor.fetchone()[0]
            connection.commit()
            print(f"User {user.username} added to the database") 
            return user_id
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e) 
        finally:
            cursor.close()
            connection.close()

def fetchUser(user_id : str):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM users\
            where id = {user_id};"
            cursor.execute(query) 
            user = list(cursor.fetchone())
            user[5] = user[5].isoformat() 
            return user
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e)
        finally:
            cursor.close() 
            connection.close() 

def updateUser(user_id : str, user : UserUpdate):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor() 
            query = f"UPDATE users\
            SET username = '{user.username}',\
            first_name = '{user.firstName}'\
            , last_name = '{user.lastName}',\
            dob = '{user.dob}',\
            gender = '{user.gender}',\
            profile_pic = '{user.profilePic}'\
            where id = {user_id};" 
            cursor.execute(query) 
            connection.commit()
            print(f"Updated") 
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e)
        finally:
            cursor.close() 
            connection.close() 
            

def authenticateUser(user : UserAuthenticate):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor() 
            query = f"SELECT password,id FROM users WHERE username = '{user.username}';" 
            cursor.execute(query) 
            password = cursor.fetchone() 
            if password:
                return verify(user.password, password[0]), password[1] 
                
            else: 
                return False, -1
        except Exception as e:
            print(f"Error : {e}")
            raise ConnectionError(e)
        finally:
            cursor.close() 
            connection.close() 
            
            