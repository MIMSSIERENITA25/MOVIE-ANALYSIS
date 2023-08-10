USE movie;
DROP VIEW IF EXISTS my_view;
CREATE VIEW my_view AS
SELECT year, category, AVG(`worldwide gross ($m)`) AS average_gross
FROM average_gross_by_year_category
GROUP BY year, category;
SELECT * FROM my_view;
GRANT CREATE VIEW, SELECT ON database_name.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
