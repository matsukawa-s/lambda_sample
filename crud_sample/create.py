import json
import mysql.connector as mydb
import requests


def lambda_handler(event, context):
    # # データ受け取り
    data = json.loads(event["body"])
    id = data["id"]
    name = data["name"]
    job = data["job"]

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

    # INSERT
    cur.execute("INSERT INTO emp VALUES(%s,%s,%s)",(id,name,job))

    # emp表、全件取得
    cur.execute("SELECT * FROM emp")
    rows = cur.fetchall()

    # カーソルとコネクションを閉じる
    cur.close()
    conn.close()

    return {
        "statusCode": 200,
        "body": json.dumps(rows),
    }