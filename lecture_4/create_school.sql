CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    birth_year INTEGER NOT NULL
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade INTEGER CHECK (grade >= 1 AND grade <= 100),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE INDEX idx_student_id ON grades(student_id);
CREATE INDEX idx_birth_year ON students(birth_year);
CREATE INDEX idx_subject ON grades(subject);
CREATE INDEX idx_grade ON grades(grade);
CREATE INDEX idx_student_name ON students(full_name);