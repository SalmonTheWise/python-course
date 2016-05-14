-- 1 Alphabet user names
SELECT * FROM users 
ORDER BY username;

-- 2 Five last users
SELECT * FROM Users 
ORDER BY registered DESC LIMIT 5;

-- 3 Five top users
SELECT username, user_id, count(*) as sng FROM listened
INNER JOIN users on users.id = user_id 
GROUP BY user_id ORDER BY sng DESC LIMIT 5;

-- 4 Artist by albums
SELECT Artists.name, count(*) as nms FROM Artists 
INNER JOIN Albums on Artists.id = Albums.artist_id 
GROUP BY Artists.id ORDER BY Artists.name;

-- 5 Artists by songs
SELECT Artists.name, count(*) as nms FROM Artists 
INNER JOIN Albums on Artists.id = Albums.artist_id 
INNER JOIN Songs on Songs.album_id = Albums.id 
GROUP BY Artists.id ORDER BY nms desc;


-- 6 longest album by songs count
SELECT Artists.name, Albums.name, count(*) as nms FROM Artists 
INNER JOIN Albums on Artists.id = Albums.artist_id 
INNER JOIN Songs on Songs.album_id = Albums.id 
GROUP BY Albums.id ORDER BY nms desc limit 1;

-- 7 Longest album
SELECT Artists.name, Albums.name, total(duration) as dur FROM Artists 
INNER JOIN Albums on Artists.id = Albums.artist_id 
INNER JOIN Songs on Songs.album_id = Albums.id 
GROUP BY Albums.id ORDER BY dur desc limit 1;


-- 9 Five top songs
SELECT Artists.name, Albums.name, count(*) as nms FROM Artists 
INNER JOIN Albums on Artists.id = Albums.artist_id 
INNER JOIN Songs on Songs.album_id = Albums.id 
INNER JOIN Listened on Listened.song_id = Songs.id 
GROUP BY Songs.id ORDER BY nms desc limit 5;

















