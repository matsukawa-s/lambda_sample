import json
import mysql.connector as mydb
import requests


def lambda_handler(event, context):
    # コネクション作成
    conn = mydb.connect(
        host='',
        port='',
        user='',
        password='',
        database=''
    )

    # カーソル作成
    cur = conn.cursor()

    cur.execute("SELECT * FROM emp")
    rows = cur.fetchall()

    # カーソルとコネクションを閉じる
    cur.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps(rows),
    }