
SELECT people.name
FROM people JOIN stars
ON people.id = stars.person_id
WHERE movie_id IN (
    SELECT movies.id FROM movies JOIN stars ON movies.id = stars.movie_id WHERE person_id iN (
        SELECT id FROM people WHERE name = "Kevin Bacon" AND birth = 1958
        )
    ) AND name != "Kevin Bacon" ;

