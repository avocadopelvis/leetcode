# https://leetcode.com/problems/find-followers-count/

# get count of followers for each user

SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id

