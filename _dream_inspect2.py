import sqlite3, json, time

DB = r"C:\Users\LENOVO\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# Check part table for blog-main sessions
cur.execute("SELECT id, project_id, title, time_created FROM session WHERE directory LIKE '%blog-main%' ORDER BY time_created DESC")
sessions = cur.fetchall()

for s in sessions:
    sid = s[0]
    print(f"\n=== Session {sid}: {s[2]} ===")
    cur.execute("""
        SELECT m.id, m.agent_id, p.data, p.time_created
        FROM message m
        JOIN part p ON p.message_id = m.id
        WHERE m.session_id = ?
        ORDER BY m.time_created, p.time_created
    """, (sid,))
    for row in cur.fetchall():
        agent = row[1] or "main"
        pdata = json.loads(row[2])
        ptype = pdata.get("type", "?")
        if ptype == "text":
            text = pdata.get("text", "")[:200]
            print(f"  [text] agent={agent}: {text}")
        elif ptype == "tool":
            tool = pdata.get("tool", "?")
            state = pdata.get("state", {})
            inp = str(state.get("input", ""))[:150]
            out = str(state.get("output", ""))[:150]
            print(f"  [tool:{tool}] agent={agent} in={inp}")
        else:
            print(f"  [{ptype}] agent={agent}")

# Now check sessions from last 7 days across all projects for potential consolidation
print("\n\n=== Sessions from last 7 days (all projects) ===")
week_ago = int((time.time() - 7*86400) * 1000)
cur.execute("""
    SELECT id, project_id, directory, title, time_created
    FROM session
    WHERE time_created > ? AND title NOT LIKE '%checkpoint-writer%'
    ORDER BY time_created DESC
""", (week_ago,))
for r in cur.fetchall():
    print(r)

# Check notes.md files that exist
print("\n\n=== All notes.md files ===")
cur.execute("SELECT session_id, data FROM part WHERE session_id IN (SELECT id FROM session WHERE directory LIKE '%blog-main%') ORDER BY time_created")
for row in cur.fetchall():
    pdata = json.loads(row[1])
    ptype = pdata.get("type", "?")
    if ptype == "text":
        text = pdata.get("text", "")[:200]
        print(f"  [{row[0]}] {text}")

conn.close()
