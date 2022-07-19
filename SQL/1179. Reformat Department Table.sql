# https://leetcode.com/problems/reformat-department-table/

SELECT id,
SUM(CASE WHEN month = "Jan" THEN revenue ELSE NULL END) AS Jan_Revenue,
SUM(CASE WHEN month = "Feb" THEN revenue ELSE NULL END) AS Feb_Revenue,
SUM(CASE WHEN month = "Mar" THEN revenue ELSE NULL END) AS Mar_Revenue,
SUM(CASE WHEN month = "Apr" THEN revenue ELSE NULL END) AS Apr_Revenue,
SUM(CASE WHEN month = "May" THEN revenue ELSE NULL END) AS May_Revenue,
SUM(CASE WHEN month = "Jun" THEN revenue ELSE NULL END) AS Jun_Revenue,
SUM(CASE WHEN month = "Jul" THEN revenue ELSE NULL END) AS Jul_Revenue,
SUM(CASE WHEN month = "Aug" THEN revenue ELSE NULL END) AS Aug_Revenue,
SUM(CASE WHEN month = "Sep" THEN revenue ELSE NULL END) AS Sep_Revenue,
SUM(CASE WHEN month = "Oct" THEN revenue ELSE NULL END) AS Oct_Revenue,
SUM(CASE WHEN month = "Nov" THEN revenue ELSE NULL END) AS Nov_Revenue,
SUM(CASE WHEN month = "Dec" THEN revenue ELSE NULL END) AS Dec_Revenue
FROM Department
GROUP BY id
ORDER BY id;


If you don't use the group by and run such query:

SELECT id,
CASE WHEN month = "Jan" THEN revenue END as "Jan_Revenue",
CASE WHEN month = "Feb" THEN revenue END AS "Feb_Revenue"
FROM Department;

this will return multiple rows for each id + month pair:

+----+-------------+-------------+
| id | Jan_Revenue | Feb_Revenue |
+----+-------------+-------------+
|  1 |        NULL |        7000 |
|  1 |        8000 |        NULL |
|  1 |        NULL |        NULL |
|  2 |        9000 |        NULL |
|  3 |        NULL |       10000 |
+----+-------------+-------------+

To get one row for each id we need to aggregate by id using GROUP BY. 
But since we have multiple rows with the same id but different values (e.g. for id=1 we have Jan_Revenues: NULL, 8000 and NULL. 
When we merge these 3 together what value should be chosen? This is why we need either SUM (NULL+8000+NULL) or MAX, in both cases 8000 will be used. 



