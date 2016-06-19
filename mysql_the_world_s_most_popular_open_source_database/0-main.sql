# Show the non-temporary tables in the database.
\! echo "\nList of all tables?"
SHOW TABLES;

\! echo "\nDisplay the table structure of TVShow, Genre and TVShowGenre?"
# Show the CREATE TABLE statement that creates a TVShow.
SHOW CREATE TABLE TVShow;
SHOW CREATE TABLE Genre;
SHOW CREATE TABLE TVShowGenre;

\! echo "\nList of TVShows, only id and name ordered by name (A-Z)?"
SELECT id, name FROM TVShow ORDER BY name ASC;

\! echo "\nList of Genres, only id and name ordered by name (Z-A)?"
SELECT id, name FROM Genre ORDER BY name DESC;

\! echo "\nList of Network, only id and name?"
SELECT id, name FROM Network;

\! echo "\nNumber of episodes in the database?"
SELECT COUNT(id) FROM Episode;
