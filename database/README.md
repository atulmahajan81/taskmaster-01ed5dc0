# TaskMaster Database Schema

This document describes the database schema for TaskMaster, a productivity application designed to help users manage tasks and notifications.

## Schema Diagram

### Tables

- **users**: Stores user account information.
  - `id`: UUID primary key.
  - `email`: User email, unique.
  - `password_hash`: Hashed password.
  - `created_at`: Timestamp of creation.
  - `updated_at`: Timestamp of last update.

- **tasks**: Stores tasks created by users.
  - `id`: UUID primary key.
  - `user_id`: Foreign key to users.
  - `title`: Title of the task.
  - `description`: Description of the task.
  - `due_date`: Due date of the task.
  - `priority`: Task priority.
  - `status`: Status of the task.
  - `created_at`: Timestamp of creation.
  - `updated_at`: Timestamp of last update.

- **notifications**: Stores notifications for users.
  - `id`: UUID primary key.
  - `user_id`: Foreign key to users.
  - `message`: Notification message.
  - `read`: Read status.
  - `created_at`: Timestamp of creation.
  - `updated_at`: Timestamp of last update.

## Setup Instructions

1. **Create the Database**
   ```bash
   createdb taskmaster_db
   ```

2. **Apply Schema**
   ```bash
   psql -d taskmaster_db -f database/schema.sql
   ```

3. **Run Migrations**
   ```bash
   alembic upgrade head
   ```

4. **Seed Data**
   - Using Python script:
     ```bash
     python database/seeds/seed_data.py
     ```
   - Using SQL script:
     ```bash
     psql -d taskmaster_db -f database/seeds/seed_data.sql
     ```

## Additional Configuration

- **Caching Strategy**: Redis with a 5-minute TTL.
- **Horizontal Scaling**: Supported.
- **Async Tasks**: Celery for background jobs.