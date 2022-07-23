# https://leetcode.com/problems/group-sold-products-by-the-date/


SELECT sell_date, 
COUNT(DISTINCT(product)) AS num_sold, 
# to aggregate the product names in one celL, GROUP_CONCAT is used
GROUP_CONCAT(DISTINCT(product)) AS products
FROM Activities
GROUP BY sell_date;



