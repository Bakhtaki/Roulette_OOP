import mysql.connector

DB_User = 'hamid'
DB_Password = 'Beta@5959'
DB_Host = 'localHost'
DataBase = 'Roulette'


def validate_login(username):
    try:
        Connection = mysql.connector.connect(user=DB_User, passwd=DB_Password, host=DB_Host, database=DataBase)
        Cursor = Connection.cursor()
        Cursor.execute('SELECT Password FROM Player_Info WHERE UserName = %s', (username,))
        Row = Cursor.fetchall()
        Connection.close()
        return Row
    except Exception as error:
        error_type = type(error).__name__
        return error_type
    
def registerPlayer(playerId,username,password,first_name,last_name,gender,birth_date,account_date,PlayerGroup,status):
    try:
        Connection = mysql.connector.connect(user= DB_User,passwd=DB_Password,host=DB_Host, database=DataBase)
        Cursor =Connection.cursor()
        Cursor.execute('INSERT INTO Player_Info VALUES(?,?,?,?,?,?,?,?,?,?)',
                       (playerId,username,password,first_name,last_name,gender,birth_date,account_date,PlayerGroup,status))
        Cursor.commit()
        Connection.close()
    except Exception as error:
        error_type = type(error).__name__
        return error_type
    