DROP TABLE IF EXISTS events;
CREATE TABLE events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  category TEXT NOT NULL,
  st_date TEXT NOT NULL, -- date in MM/DD/YYYY
  st_time TEXT NOT NULL, -- time in HH:MM AM/PM
  en_date TEXT NOT NULL, -- date in MM/DD/YYYY
  en_time TEXT NOT NULL, -- time in HH:MM AM/PM
  check_status TEXT DEFAULT 'event_planner_unchecked',
  description TEXT,
  repeat_frequency INT DEFAULT 0,
  user_id TEXT

  -- Check the start and end date format
    CHECK ( (CAST(SUBSTR(st_date, 1, 2) AS INTEGER) BETWEEN 1 AND 12)
                    AND (CAST(SUBSTR(st_date, 4, 2) AS INTEGER) BETWEEN 1 AND 31)
					AND (CAST(SUBSTR(st_date, 7, 4) AS INTEGER))),
	CHECK ( (CAST(SUBSTR(en_date, 1, 2) AS INTEGER) BETWEEN 1 AND 12)
                    AND (CAST(SUBSTR(en_date, 4, 2) AS INTEGER) BETWEEN 1 AND 31)
					AND (CAST(SUBSTR(en_date, 7, 4) AS INTEGER))),
  	-- Check start and end time format
	CHECK (	(CAST(SUBSTR(st_time, 1, 2) AS INTEGER) BETWEEN 00 AND 12)
					AND (CAST(SUBSTR(st_time, 4, 2) AS INTEGER) BETWEEN 00 AND 60)),
	CHECK (SUBSTR(st_time,7,2) IN ('AM','PM','am','pm','Am','Pm')),
	CHECK (	(CAST(SUBSTR(en_time, 1, 2) AS INTEGER) BETWEEN 00 AND 12)
					AND (CAST(SUBSTR(en_time, 4, 2) AS INTEGER) BETWEEN 00 AND 60)),
	CHECK (SUBSTR(st_time,7,2) IN ('AM','PM','am','pm','Am','Pm'))
);

DROP TABLE IF EXISTS todos;
CREATE TABLE todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  description TEXT NOT NULL,
  status TEXT DEFAULT 'todo_unchecked'
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique user_id
    first_name TEXT NOT NULL,
    last_name TEXT,
    email_addr TEXT NOT NULL,
    user_name TEXT NOT NULL,
    user_hash TEXT NOT NULL,
    random_string TEXT
)
