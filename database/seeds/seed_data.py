import asyncpg
import asyncio
from datetime import datetime, timedelta

async def seed_data():
    conn = await asyncpg.connect(user='user', password='password', database='dbname', host='127.0.0.1')
    try:
        # Seed users
        users = [
            ('admin@taskmaster.com', 'adminhash'),
            ('user1@taskmaster.com', 'user1hash'),
            ('user2@taskmaster.com', 'user2hash')
        ]
        user_ids = []
        for email, password_hash in users:
            user_id = await conn.fetchval(
                'INSERT INTO users (email, password_hash) VALUES ($1, $2) RETURNING id',
                email, password_hash
            )
            user_ids.append(user_id)

        # Seed tasks
        for user_id in user_ids:
            for i in range(10):
                due_date = datetime.now().date() + timedelta(days=i)
                await conn.execute(
                    'INSERT INTO tasks (user_id, title, description, due_date, priority, status) '
                    'VALUES ($1, $2, $3, $4, $5, $6)',
                    user_id, f'Task {i}', f'Description for task {i}', due_date, 'medium', 'pending'
                )

        # Seed notifications
        for user_id in user_ids:
            for i in range(3):
                message = f'Notification {i} for user {user_id}'
                await conn.execute(
                    'INSERT INTO notifications (user_id, message, read) VALUES ($1, $2, $3)',
                    user_id, message, False
                )
    finally:
        await conn.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(seed_data())