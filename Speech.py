import pyttsx3
import sqlite3

conn = sqlite3.connect('reddit_data.db')
cursor = conn.cursor()

def Read_From_db():
    Speech = []
    cursor.execute('SELECT body FROM reddit_comments')
    data = cursor.fetchall()
    print(data)
    for line in data:
        Speech.append(line)
    return(Speech)


engine = pyttsx3.init()
engine.save_to_file(str(Read_From_db()), 'output.mp3')
engine.runAndWait()
engine.stop()