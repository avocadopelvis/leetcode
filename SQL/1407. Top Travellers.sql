# https://leetcode.com/problems/top-travellers/

Note: 
not every user has travelled, therefore distance travelled would be NULL.
so we use IFNULL to return 0 instead of NULL.

we use LEFT JOIN since we want to know the distance traveled by each user.

SELECT u.name, IFNULL(SUM(r.distance), 0) as travelled_distance
FROM Users u LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY r.user_id
ORDER BY travelled_distance DESC, u.name


