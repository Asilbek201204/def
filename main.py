import psycopg2
class User:
    def __init__(self,database,user,host,password,port=5432):
        self.con = psycopg2.connect(
        database=database,
        user=user,
        host=host,
        password=password,
        port=port,
        )
        self.con.autocommit = True
        self.cursor = self.con.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                            id SERIAL PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            email VARCHAR(100) NOT NULL
        )""")

    def create_user(self,name,email):
        self.cursor.execute("INSERT INTO users(name, email) VALUES(%s, %s) RETURNING id",(name, email))  
        use_id = self.cursor.fetchone()[0]  
        return {'id':use_id, 'name': name, 'email': email }
    def read_user(self,user_id):
        self.cursor.execute(
            "SELECT * FROM users WHERE id = %s",
       (user_id,)
        )

        row = self.cursor.fetchone()
        if row:
            return {'id': row[0], 'name': row[1],'email':row[2]}
        return None
    
    def update_user(self,user_id,name,email):
        if name:
            self.cursor.execute(
                "UPDATE users SET name = %s WHERE id = %s",
                (name,user_id)
            )
        if email:
            self.cursor.execute(
                "UPDATE users SET email = %s WHERE id =%s",
                (email,user_id)
            )
        return self.read_user(user_id=user_id)
    
    def delete_user(self,user_id):
        self.cursor.execute(
            "DELETE FROM users WHERE id = %s",
            (user_id,)
        )
        return True
    

database = 'education'
user = 'postgres'
host = 'localhost'
password = 1210
port = 5432

user_obj = User(database=database,user=user,host=host,password=password,port=5432)



# create_user = user_obj.create_user(name='asilbek',email='asilbek@gmail.con')
# print('User created')

# read_user = user_obj.read_user(user_id=1)
# print(read_user)

object_user = user_obj.update_user(user_id=1,name='sardor',email='sardor@gmail.com')
print(object_user)














































