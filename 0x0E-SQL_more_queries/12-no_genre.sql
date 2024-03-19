-- Lists all shows contained in hbtn_od_tvshows withouth a genre linked
-- Lists all rows of a database that don't have one column
SELECT tv_show.title,
tv_show_genres.genre_id
FROM tv_shows LEFT JOIN
tv_show_genres
ON tv_shows.id =
tv_shows_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC
tv_show_genres.genre_id ASC;
