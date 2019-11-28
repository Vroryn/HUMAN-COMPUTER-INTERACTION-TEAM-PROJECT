use pubcs_unlv;

DROP TRIGGER IF EXISTS after_new_bank_user;

delimiter //

CREATE TRIGGER after_new_bank_user
	AFTER INSERT ON main_users_bank FOR EACH ROW
	
BEGIN
         
  -- Select @last_id := customer_id from main_users_bank ORDER BY customer_id DESC LIMIT 1;
      

   INSERT INTO main_accounts(account_type, account_balance, customer_id_id)
                     VALUES('checking', 0.00, NEW.customer_id) ;
END//

delimiter ;
