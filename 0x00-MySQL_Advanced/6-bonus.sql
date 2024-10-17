-- Add bonus
DELIMITER $$

CREATE PROCEDURE AddBonus
(IN user_id INT, IN project_name VARCHAR(255), in score INT)
BEGIN
  DECLARE projct_exists INT DEFAULT 0;
  SET projct_exists = (
    SELECT COUNT(*)
    FROM projects
    WHERE name = projct_name);

  IF projct_exists = 0
  THEN
    INSERT INTO projects(name)
    VALUES (project_name);
  END IF;

  INSERT INTO corrections(user_id, project_id, score) 
  VALUES (
    user_id,
    (SELECT id FROM projects WHERE name = project_name),
    score); 
END $$