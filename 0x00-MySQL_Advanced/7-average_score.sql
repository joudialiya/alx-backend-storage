-- Avr score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser
(IN user_id IN)
BEGIN
  UPDATE users
  SET average_score = (
    SELECT AVG(score)
    FROM corrections
    WHERE user_id = user_id
  )
  WHERE id = user_id;

END $$
DELIMITER ;