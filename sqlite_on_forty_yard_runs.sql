--1) Create 'first_runs_year_21_22' table
CREATE TABLE first_runs_year_21_22
(
student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
student_name TEXT,
run_time REAL,
the_date TEXT NOT NULL DEFAULT '2022'
);

--2) Fill 'first_runs_year_21_22' table
INSERT INTO first_runs_year_21_22 
(student_name, run_time)
SELECT
*
FROM
first_runs_22;

--3) Create 'subsequent_runs_year_21_22' table
CREATE TABLE subsequent_runs_year_21_22
(
subsequent_run_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
run_time REAL,
the_date TEXT NOT NULL DEFAULT '2022',
FOREIGN KEY (student_id) REFERENCES first_runs_year_21_22 (student_id)
);

PRAGMA foreign_keys=0;

--4) Fill 'subsequent_runs_year_21_22' table
INSERT INTO subsequent_runs_year_21_22
(student_id, run_time)
SELECT
first_runs_year_21_22.student_id,
subsequent_runs_22.subsequent_run_times_22
FROM
subsequent_runs_22
LEFT JOIN
first_runs_year_21_22
ON
first_runs_year_21_22.student_name=subsequent_runs_22.s_names_22;

PRAGMA foreign_keys=1;

--5) Drop 'first_runs_22' table
DROP TABLE first_runs_22;

--6) Drop 'subsequent_runs_22' table
DROP TABLE subsequent_runs_22;
