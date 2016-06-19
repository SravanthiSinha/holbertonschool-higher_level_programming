\! echo "\nNumber of season by TVShow ordered by name (A-Z)?"
SELECT TVS.name, COUNT(tvshow_id) as 'nb_seasons' from Season S INNER JOIN
       TVShow TVS on  S.tvshow_id= TVS.id
       GROUP BY TVS.name  ORDER BY TVS.name;

\! echo "\nList of Network by TVShow ordered by name (A-Z)?"
SELECT TVS.name as 'TVShow name', N.name as  'Network name' from Network N INNER JOIN
       TVShow TVS on  N.id= TVS.network_id
       GROUP BY TVS.name, N.name  ORDER BY TVS.name;

\! echo "\nList of TVShows ordered by name (A-Z) in the Network 'Fox (US)'?"
SELECT  TVS.name from Network N INNER JOIN
       TVShow TVS on  N.id= TVS.network_id
       where N.name='Fox (US)'  ORDER BY TVS.name;

\! echo "\nNumber of episodes by TVShows ordered by name (A-Z)?"
SELECT  TVS.name, count(E.id) as 'nb_episodes' from TVShow TVS
	INNER JOIN Season S on TVS.id= S.tvshow_id
	INNER JOIN Episode E on S.id= E.season_id
	GROUP BY TVS.name
	ORDER BY TVS.name;

