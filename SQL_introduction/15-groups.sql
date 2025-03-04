-- script that lists the number of records with the same score in the table second_table of the db hbtn_0c_0
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
