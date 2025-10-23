

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    age integer,
    grade char(1)
);

SELECT * FROM students;