-- SQL version of seed data

-- Seed users
INSERT INTO users (id, email, password_hash) VALUES
(gen_random_uuid(), 'admin@taskmaster.com', 'adminhash'),
(gen_random_uuid(), 'user1@taskmaster.com', 'user1hash'),
(gen_random_uuid(), 'user2@taskmaster.com', 'user2hash');

-- Seed tasks
INSERT INTO tasks (id, user_id, title, description, due_date, priority, status)
SELECT gen_random_uuid(), users.id, 'Task ' || i, 'Description for task ' || i, NOW()::date + (i * interval '1 day'), 'medium', 'pending'
FROM generate_series(1, 10) AS s(i), users;

-- Seed notifications
INSERT INTO notifications (id, user_id, message, read)
SELECT gen_random_uuid(), users.id, 'Notification for user ' || users.id, false
FROM users, generate_series(1, 3);