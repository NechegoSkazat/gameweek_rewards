import psycopg2

conn = psycopg2.connect(
    database="gw_rewards",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432")

def transfer_data(dict):
    cur = conn.cursor()
    sql = "INSERT INTO rewards_leagues (name, rarity) VALUES (%s, %s)"
    data = ("value1", "value2")
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()