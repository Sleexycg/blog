import sqlite3, json, time, os

DB = r"C:\Users\LENOVO\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()

# 1. List all blog-main sessions
cur.execute("SELECT id, project_id, directory, title, time_created, time_updated FROM session WHERE directory LIKE '%blog-main%' ORDER BY time_created DESC")
print("=== Blog-main sessions ===")
for r in cur.fetchall():
    print(r)

# 2. For each non-checkpoint blog-main session, get user messages
print("\n=== User messages in blog-main sessions ===")
cur.execute("SELECT id, project_id, title, time_created FROM session WHERE directory LIKE '%blog-main%' AND title NOT LIKE '%checkpoint-writer%' ORDER BY time_created DESC")
sessions = cur.fetchall()
for s in sessions:
    sid = s[0]
    print(f"\n--- Session {sid}: {s[2]} ---")
    cur.execute("SELECT id, data FROM message WHERE session_id = ? ORDER BY time_created", (sid,))
    for msg in cur.fetchall():
        d = json.loads(msg[1])
        role = d.get("role", "?")
        content = d.get("content", "")
        if isinstance(content, list):
            texts = []
            for c in content:
                if isinstance(c, dict) and c.get("type") == "text":
                    texts.append(c.get("text", "")[:300])
            content = " ".join(texts)
        else:
            content = str(content)[:500]
        print(f"  [{role}] {content[:300]}")

# 3. Check what tables exist
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print(f"\n=== Tables: {tables}")

conn.close()
