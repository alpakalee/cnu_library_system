from config.config_db import connection_db


#회원목록 조회
def get_members():
    conn = connection_db()


    try:
        curs = conn.cursor()
        sql = "SELECT * FROM tbl_member;"
        curs.execute(sql)
        rows = curs.fetchall()
    finally:
        conn.close()

    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: ID\tNAME\tPHONE\tDATE')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')

#회원유무 판단
def member_match(member_num):
    conn = connection_db()

    try:
        curs = conn.cursor()
        sql = f'''
                SELECT *
                FROM tbl_member
                WHERE member_id = "{member_num}"
            '''
        curs.execute(sql)
        result = curs.rowcount
        #rowcount = 해당하는 줄이 있는지
        # 있으면 줄의 수 만큼 반환(여기서는 하나밖에 해당안됨==> 1) 없으면 0 반환
    finally:
        conn.close()

    return result

#회원 검색
def search_members():
    print(':: 검색하고 싶은 회원의 이름을 입력해주세요')
    keyword = input('>> 검색 회원 이름: ')
    conn = connection_db()
    try:
        curs = conn.cursor()
        sql = f'''
                    SELECT *
                    FROM tbl_member
                    WHERE member_name LIKE '%{keyword}%'
                          OR member_id LIKE '%{keyword}%'
                  '''
        curs.execute(sql)
        rows = curs.fetchall()
    finally:
        conn.close()
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(':: MEMBER_ID\tMEMBER_NAME\tMEMBER_PHONE\tREGISTER_AT')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    for row in rows:
        print(f':: {row.values()}')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::')