-- Need metting view
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL 
    OR DATEDIFF(NOW(), last_meeting) >= 30);
