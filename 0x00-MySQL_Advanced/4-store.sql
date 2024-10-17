-- Trigger to dec on new order
DELIMITER $$

CREATE TRIGGER decr_on_order
AFTER INSERT
ON orders FOR EACH ROW
BEGIN
  DECLARE prev INT;
  
  SET prev = (
    SELECT quantity
    FROM items
    WHERE name = NEW.item_name
  );
  
  UPDATE items
  SET quantity = prev - 1
  WHERE name = NEW.item_name;

END $$

DELIMITER ;
