import sqlite3
import os

def initialize_sanitation_task():
    # Ensure this matches the name in your app.config['SQLALCHEMY_DATABASE_URI']
    db_path = 'instance/nexus.db' 
    
    # If the file isn't in 'instance/', check your project root
    if not os.path.exists(db_path):
        db_path = 'nexus.db'

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # UPDATED: Table name is 'complaint' (lowercase) based on your SQLAlchemy Class 'Complaint'
        sql = """
            INSERT INTO complaint (description, dept, status, img_before, img_after, lat, lng, vote_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        values = (
            'Overflowing bin near market', 
            'Sanitation', 
            'Resolved', 
            'sanitation_before.jpg', 
            'sanitation_after.jpg', 
            12.825, 
            77.513,
            1
        )

        cursor.execute(sql, values)
        conn.commit()
        print("✅ Sanitation record added successfully!")

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_sanitation_task()