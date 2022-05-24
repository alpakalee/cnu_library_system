import pymysql


#connect to mariaDB
def connection_db():
    try:
        connection = pymysql.connect(
            user="root",
            password="root",
            host="127.0.0.1",  # 127.0.0.1 = 내아이피를 의미
            port=3306,
            database="cnu_library",
            autocommit=True,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as e:
        print(f'MARIADB 연결 실패: {e}')