"""Smart Home Hub — MQTT broker bridge with SQLite logging."""
import paho.mqtt.client as mqtt
import sqlite3, json, time, logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
DB_PATH = "smarthome.db"


def init_db(conn):
    conn.execute("""CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        node TEXT, temp REAL, humidity REAL,
        motion INTEGER, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload)
        logging.info("Received: %s", data)
        userdata.execute(
            "INSERT INTO readings (node,temp,humidity,motion) VALUES (?,?,?,?)",
            (data["node"], data["temp"], data["humidity"], data["motion"])
        )
        userdata.commit()
    except Exception as e:
        logging.error("Error: %s", e)


def main():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    init_db(conn)

    client = mqtt.Client(userdata=conn)
    client.on_message = on_message
    client.connect("localhost", 1883)
    client.subscribe("home/+/sensors")
    logging.info("Hub started — listening on home/+/sensors")
    client.loop_forever()


if __name__ == "__main__":
    main()
