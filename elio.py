import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
import os
import random
from dotenv import load_dotenv
load_dotenv()

class StateManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or self.get_db_path()
        self._create_table()

    def get_db_path(self):
        return 'elio_state.db'

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS state (
                    id INTEGER PRIMARY KEY,
                    state TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            ''')
            conn.commit()

    def get_state(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT state, date FROM state ORDER BY id DESC LIMIT 1')
            row = cursor.fetchone()
            if row:
                return {"state": row[0], "date": row[1]}
            else:
                # Default state if none exists
                return {"state": "morning", "date": datetime(1990, 1, 1)}

    def set_state(self, new_state):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO state (state, date) VALUES (?, ?)', (new_state, datetime.now(ZoneInfo('America/Chicago')).isoformat()))
            conn.commit()

    def get_feed_history(self, max_entries=5):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, state, date FROM state ORDER BY id DESC LIMIT ?', (max_entries,))
            rows = cursor.fetchall()
            return [{"id": row[0], "state": row[1], "date": row[2]} for row in rows]

    def remove_feed_entry(self, entry_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM state WHERE id = ?', (entry_id,))
            conn.commit()


def get_random_image(state=None, add_food_images=False):
    all_files = [f'static/img/elio/elio_pics/{x}' for x in os.listdir('static/img/elio/elio_pics')]

    if state != None and add_food_images:
        all_files.extend([f'static/img/elio/{state}/{x}' for x in os.listdir(f'static/img/elio/{state}')])

    random_img = random.choice(all_files)
    return random_img