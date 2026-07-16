import sqlite3, json

DB = r"C:\Users\LENOVO\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Verify: Check the blog template query session's assistant response
cur.execute("""
    SELECT m.id, p.data
    FROM message m
    JOIN part p ON p.message_id = m.id
    WHERE m.session_id = 'ses_0949106a6ffemUOVDWAGdonPNl'
    ORDER BY m.time_created, p.time_created
""")
print("=== Blog template query - full trajectory ===")
for row in cur.fetchall():
    pdata = json.loads(row[1])
    ptype = pdata.get("type", "?")
    if ptype == "text":
        text = pdata.get("text", "")
        print(f"  [text] {text[:500]}")
    elif ptype == "tool":
        tool = pdata.get("tool", "?")
        state = pdata.get("state", {})
        inp = str(state.get("input", ""))[:200]
        out = str(state.get("output", ""))[:300]
        print(f"  [tool:{tool}] in={inp}")
        print(f"    out={out}")

# Check if there are any older sessions for blog-main that we missed
cur.execute("SELECT id, title, time_created FROM session WHERE directory LIKE '%blog-main%' ORDER BY time_created")
print("\n=== All blog-main sessions ===")
for r in cur.fetchall():
    print(f"  {r}")

# Check for any sessions in the last 7 days that might be related
import time
week_ago = int((time.time() - 7*86400) * 1000)
cur.execute("""
    SELECT id, title, time_created, directory
    FROM session
    WHERE time_created > ? AND title NOT LIKE '%checkpoint%'
    ORDER BY time_created DESC
""", (week_ago,))
print("\n=== All non-checkpoint sessions in last 7 days ===")
for r in cur.fetchall():
    print(f"  [{r[2]}] {r[0]} title={r[1]} dir={r[3]}")

conn.close()
