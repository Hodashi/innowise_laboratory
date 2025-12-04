SELECT 
    s.full_name,
    g.subject,
    g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

SELECT 
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC;

SELECT 
    full_name,
    birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year;

SELECT 
    subject,
    ROUND(AVG(grade), 2) as average_grade,
    COUNT(*) as number_of_grades
FROM grades
GROUP BY subject
ORDER BY average_grade DESC;

SELECT 
    s.full_name,
    ROUND(AVG(g.grade), 2) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.full_name
ORDER BY average_grade DESC
LIMIT 3;

SELECT DISTINCT
    s.full_name,
    g.subject,
    g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name, g.grade;