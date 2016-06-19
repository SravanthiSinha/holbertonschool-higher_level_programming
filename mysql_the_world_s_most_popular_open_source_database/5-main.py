import MySQLdb

connect = MySQLdb.connect(host="173.246.108.142",
                       user="student",
                       passwd="aLQQLXGQp2rJ4Wy5",
                       db="Project_169",
                       port=3306,
                       )

curse = connect.cursor()

get_shows_query = "SELECT TVShow.name, TVShow.id FROM TVShow ORDER BY TVShow.name"

get_seasons_query = "SELECT Season.id, Season.number FROM Season WHERE Season.tvshow_id = "



shows = []
curse.execute(get_shows_query);

fetched = curse.fetchall()
for show in fetched:
    curse.execute(get_seasons_query + str(show[1]))
    seasons_fetched = curse.fetchall()
    print show[0]+":"
    for season in seasons_fetched:
        print "\t Season" + str(season[1]) +":"
        get_episodes_query = "SELECT Episode.name, Episode.number FROM Episode WHERE Episode.season_id = " + str(season[0]) + " ORDER BY Episode.number"
        curse.execute(get_episodes_query)
        episodes = curse.fetchall()
        for episode in episodes:
            print "\t\t" + str(episode[1]) + ": " + str(episode[0])
