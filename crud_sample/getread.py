import json
import mysql.connector as mydb
import requests


def lambda_handler(event, context):
    id = event["pathParameters"]["id"]
    # コネクション作成
    conn = mydb.connect(
        host='',
        port='',
        user='',
        password='',
        database=''
    )

    # カーソル作成
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM emp WHERE id = %s",(id,))
    rows = cur.fetchall()

    # カーソルとコネクションを閉じる
    cur.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps(rows),
    }