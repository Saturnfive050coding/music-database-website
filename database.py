import sqlite3
import json

def playlist_count():
    conn = sqlite3.connect('bot_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Playlists")
    results = cur.fetchall()
    cur.close()
    conn.close()
    return len(results)

def insert_playlist(id, name, pl):
    jPl = json.dumps(pl)
    conn = sqlite3.connect('bot_database.db')
    cur = conn.cursor()
    print(id)
    print(name)
    print(jPl)
    query = '''INSERT INTO Playlists
                (id, name, tracks)
                VALUES
                (?, ?, ?)'''
    dataTuple = (id, name, jPl)
    cur.execute(query, dataTuple)
    conn.commit()
    cur.close()
    conn.close()

def retrieve_playlist(id):
    conn = sqlite3.connect('bot_database.db')
    cur = conn.cursor()
    cur.execute("SELECT * from Playlists where id = ?", (id,))
    playlist = cur.fetchall()
    cur.close()
    conn.close()
    return playlist

def delete_playlist(id):
    try:
        conn = sqlite3.connect('bot_database.db')
        cur = conn.cursor()
        cur.execute("DELETE from Playlists where id = ?", (id,))
        conn.commit()
        cur.close()
        return f"Deleted playlist with ID {id}"
    except sqlite3.Error as error:
        return "Failed to delete playlist" + error
    
