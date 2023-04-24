import psycopg2
from config import config

def delete_user(person_name):
    conn = None
    rows_deleted = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("DELETE FROM phonebook WHERE firstname = %s", (person_name,))
        rows_deleted = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_user("Nursultan")
    print('The number of deleted rows: ', deleted_rows)