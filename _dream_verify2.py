import sqlite3, json

DB = r"C:\Users\LENOVO\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Get ALL messages for the blog template query session
cur.execute("""
    SELECT m.id, json_extract(m.data, '$.role') as role, p.data, m.time_created
    FROM message m
    JOIN part p ON p.message_id = m.id
    WHERE m.session_id = 'ses_0949106a6ffemUOVDWAGdonPNl'
    ORDER BY m.time_created, p.time_created
""")
print("=== Full session trajectory ===")
for row in cur.fetchall():
    role = row[1]
    pdata = json.loads(row[2])
    ptype = pdata.get("type", "?")
    if ptype == "text":
        text = pdata.get("text", "")
        print(f"\n  [{role}] {text[:600]}")
    elif ptype == "tool":
        tool = pdata.get("tool", "?")
        state = pdata.get("state", {})
        inp = str(state.get("input", ""))[:200]
        out = str(state.get("output", ""))[:400]
        print(f"  [{role}] tool:{tool} in={inp}")
        if out:
            print(f"    out={out}")
    elif ptype == "step-start":
        print(f"  [{role}] --- step start ---")
    elif ptype == "step-finish":
        print(f"  [{role}] --- step finish ---")

# Check how many messages total
cur.execute("SELECT COUNT(*) FROM message WHERE session_id = 'ses_0949106a6ffemUOVDWAGdonPNl'")
print(f"\n  Total messages: {cur.fetchone()[0]}")

conn.close()
