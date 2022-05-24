import pymysql

from config.config_db import connection_db


# 도서목록 조회
def get_books():
    # 1. MariaDB와 Connection 성공하면
    conn = connection_db()  # Connection -> Maria DB

    try:
        curs = conn.cursor()  # 2. cursor() 객체를 이용해 작업(노동자)
        sql = "SELECT * FROM tbl_book;"  # 3. MariaDB 실행 sql문 (실행x)
        curs.execute(sql)  # 4. cursor() 객체를 통하여 sql문 실행 (실행o)
        # fetchall() -> 모든 row 반환
        # fetchone() -> 1개 row 반환
        # fetchmany(n) -> n개 row 반환
        rows = curs.fetchall()  # 5. 실행 결과 받기

    finally:
        conn.close()  # 6. MariaDB Connection 끊기


    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: ISBN\tTITLE\tWRITER\tPUBLISHER\tPRICE\tDATE')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# 도서 검색
def search_books():
    print(':: 검색하고 싶은 책 이름을 입력해주세요')
    keyword = input('>> 검색 키워드: ')
    conn = connection_db()
    try:
        curs = conn.cursor()
        sql = f'''
                SELECT *
                FROM tbl_book
                WHERE book_name LIKE '%{keyword}%'
                      OR book_writer LIKE '%{keyword}%'
              '''
        curs.execute(sql)
        rows = curs.fetchall()
    finally:
        conn.close()

    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: ISBN\tTITLE\tWRITER\tPUBLISHER\tPRICE\tDATE')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')


# keyword = "파이썬'
# SELECT문 (DB로부터 데이터를 GET)
# 3: SELECT *      # 데이터의 어떤 Column을 가져올지 # *의 의미 = 전부(book_name , book_LSBN 등등)
# 1: FROM tbl_book # table 설정
# 2: WHERE book_name LIKE '%{keyword}%' # 필터: book_name에 keyword 포함된 것!
# LIKE는 포함을 의미
# WHERE절은 2줄이상 중복불가 but OR을 이용해서 사용
#