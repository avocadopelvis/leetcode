# https://leetcode.com/problems/article-views-i

# using DISTINCT keyword
SELECT DISTINCT author_id AS id 
FROM Views 
where author_id = viewer_id 
ORDER BY id

# using GROUP BY
SELECT author_id as id
FROM Views
WHERE author_id = viewer_id
GROUP BY id
ORDER BY id


