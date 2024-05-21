class DBmanager:
    def h():
        return;

    def initDB(): # 인자로 host,,이런걸 받을지
        conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '0000',
            db = 'trDB',
            charset = 'utf8'
        ) 
        
        #    cur = conn.cursor()
        #    cur.execute(
        #        "CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)"
        #        )