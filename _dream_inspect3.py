import sqlite3, json, time

DB = r"C:\Users\LENOVO\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check ALL sessions in the DB
cur.execute("SELECT id, project_id, directory, title, time_created FROM session ORDER BY time_created DESC LIMIT 50")
print("=== All sessions (newest first) ===")
for r in cur.fetchall():
    ts = time.strftime('%Y-%m-%d %H:%M', time.localtime(r[4]/1000))
    print(f"  [{ts}] {r[0]} proj={r[1]} dir={r[3]}")

# Check if there are any sessions with older timestamps for blog-main
print("\n=== blog-main sessions (all time) ===")
cur.execute("SELECT id, project_id, directory, title, time_created FROM session WHERE directory LIKE '%blog-main%'")
for r in cur.fetchall():
    ts = time.strftime('%Y-%m-%d %H:%M', time.localtime(r[4]/1000))
    print(f"  [{ts}] {r[0]} proj={r[1]} title={r[3]}")

# Check all projects in the DB
print("\n=== All unique projects ===")
cur.execute("SELECT DISTINCT project_id FROM session")
for r in cur.fetchall():
    print(f"  {r[0]}")

# Check the project table
print("\n=== Project table ===")
try:
    cur.execute("SELECT * FROM project")
    for r in cur.fetchall():
        print(f"  {r}")
except Exception as e:
    print(f"  Error: {e}")

# Check the Smart-Agriculture session checkpoints for comparison
print("\n=== Smart-Agriculture related sessions ===")
cur.execute("SELECT id, project_id, directory, title, time_created FROM session WHERE directory LIKE '%Smart-Agriculture%' AND title NOT LIKE '%checkpoint%' ORDER BY time_created DESC LIMIT 10")
for r in cur.fetchall():
    ts = time.strftime('%Y-%m-%d %H:%M', time.localtime(r[4]/1000))
    print(f"  [{ts}] {r[0]} title={r[3]}")

# Check recent sessions with substantial content (more than 5 messages)
print("\n=== Sessions with >5 messages (substantial work) ===")
cur.execute("""
    SELECT s.id, s.title, s.time_created, COUNT(m.id) as msg_count
    FROM session s
    JOIN message m ON m.session_id = s.id
    WHERE s.title NOT LIKE '%checkpoint%'
    GROUP BY s.id
    HAVING msg_count > 5
    ORDER BY s.time_created DESC
    LIMIT 20
""")
for r in cur.fetchall():
    ts = time.strftime('%Y-%m-%d %H:%M', time.localtime(r[2]/1000))
    print(f"  [{ts}] {r[0]} msgs={r[3]} title={r[1]}")

conn.close()
