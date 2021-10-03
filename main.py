import mysql.connector as connector

class DBhelper:

    def __init__(self):
        try:
            self.con = connector.connect(host="localhost", port=3306, user="root",passwd="narasimha_123",database="pythontest")
            if (self.con.is_connected()):
                print("connected")
        except:
            print("unable to connect")

        # query to create a table
        query = "create table if not exists user(userId int primary key,userName varchar(50),phone varchar(12)) "

        cur = self.con.cursor()
        cur.execute(query)
        print("created")
    
    def insert_user(self,userid,username,phone):

            query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(userid,username,phone)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("user saved to db")

    def fetch_all(self,id=None):
            if id == None:
                query = "select * from user"
            else:
                query = "select * from user where userId={}".format(id)
            cur = self.con.cursor()
            cur.execute(query)

            try:
                for row in cur:
                    print("userId: ",row[0])
                    print("userNmae", row[1])
                    print("phone", row[2])
                    print()
                    print()
            except:
                print("Not found")

    def delete_user(self, id):
            query = "delete from user where userId={}".format(id)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()

    def update_user(self, userId, newName, newphone):
            query = "update user set userName='{}',phone='{}' where userId={}".format(newName,newphone,userId)
            cur =self.con.cursor()
            cur.execute(query)
            self.con.commit()

    def close_connection(self):
        self.con.close()
        if not (self.con.is_connected()):
            print("closed")


# using cursor we fire the queries
