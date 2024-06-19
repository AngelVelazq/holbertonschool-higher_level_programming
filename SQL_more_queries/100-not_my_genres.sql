-- List all genres not linked to the show Dexter in hbtn_0d_tvshows

-- Step 1: Get the genre_id linked to the show Dexter
SELECT genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter';

-- Step 2: List all genres that are not linked to the genre_id obtained from Step 1
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN (
    SELECT DISTINCT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
) AS linked_genres ON tv_genres.id = linked_genres.genre_id
WHERE linked_genres.genre_id IS NULL
ORDER BY tv_genres.name ASC;
