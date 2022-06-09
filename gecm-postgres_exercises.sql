/*
Using the db in this example: https://pgexercises.com/questions/basic/
File: clubdata.sql
*/

/* ############## JOINS ############## */

/*Question
How can you produce a list of all members who have used a tennis court?
Include in your output the name of the court, and the name of the member formatted as a single column.
Ensure no duplicate data, and order by the member name followed by the facility name.
*/

SELECT distinct CONCAT(mmbrs.firstname, ' ', mmbrs.surname) AS member, fts.name AS facility
  FROM cd.members AS mmbrs
	  INNER JOIN cd.bookings AS bks
		  ON mmbrs.memid = bks.memid
	  INNER JOIN cd.facilities AS fts
		  ON bks.facid = fts.facid
  WHERE fts.name in ('Tennis Court 2', 'Tennis Court 1')
ORDER BY member, facility

/*Question
How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30?
Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0.
Include in your output the name of the facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries.
*/

SELECT  mems.firstname || ' ' || mems.surname AS member, facs.name AS facility,
		CASE
			WHEN mems.memid = 0 THEN
				bks.slots*facs.guestcost
			ELSE
				bks.slots*facs.membercost
		END AS cost
FROM cd.members AS mems
INNER JOIN cd.bookings AS bks
	ON mems.memid = bks.memid
INNER JOIN cd.facilities AS facs
	ON bks.facid = facs.facid
WHERE
	starttime >= '2012-09-14'
	AND
	starttime < '2012-09-15'
	AND
	(
	  (mems.memid = 0 AND bks.slots*facs.guestcost > 30)
	  OR
	  (mems.memid != 0 AND bks.slots*facs.membercost > 30)
  )
ORDER BY
	facs.membercost + facs.guestcost DESC

/*
Question
The Produce a list of costly bookings exercise contained some messy logic:
we had to calculate the booking cost in both the WHERE clause and the CASE statement.
Try to simplify this calculation using subqueries. For reference, the question was:

How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30?
Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0.
Include in your output the name of the facility, the name of the member formatted as a single column, and the cost.
Order by descending cost.
*/


SELECT member, facility, cost
FROM (
	SELECT
		mems.firstname || ' ' || mems.surname as member, facs.name as facility,
		CASE
			WHEN mems.memid = 0 THEN
				bks.slots*facs.guestcost
			ELSE
				bks.slots*facs.membercost
		END AS cost
	FROM
		cd.members mems
	INNER JOIN cd.bookings bks
		ON mems.memid = bks.memid
	INNER JOIN cd.facilities facs
		ON bks.facid = facs.facid
	WHERE
		bks.starttime >= '2012-09-14' AND
		bks.starttime < '2012-09-15'
	) as bookings
WHERE cost > 30
ORDER BY cost DESC;


/* ##############  Aggregation ##############  */

/*Question
Produce a list of the total number of slots booked per facility per month in the year of 2012.
Produce an output table consisting of facility id and slots, sorted by the id and month.
*/

SELECT facid, EXTRACT(month FROM starttime) AS month, SUM(slots) AS "Total Slots"
	FROM cd.bookings
	WHERE EXTRACT(year FROM starttime) = 2012
	GROUP BY facid, month
ORDER BY facid, month;


/*
Question
Produce a list of facilities with a total revenue less than 1000.
Produce an output table consisting of facility name and revenue, sorted by revenue.
Remember that there's a different cost for guests and members!
*/

SELECT agg.name, agg.revenue
FROM (
  SELECT name,
          sum(CASE
                WHEN memid = 0
                  THEN slots*guestcost
				 			  ELSE membercost*slots
				      END ) AS revenue
	FROM cd.bookings
	INNER JOIN cd.facilities ON cd.bookings.facid = cd.facilities.facid
	GROUP BY name ) as agg
WHERE revenue < 1000
ORDER BY revenue;

/*
Question
For any given timestamp, work out the number of days remaining in the month.
The current day should count as a whole day, regardless of the time.
Use '2012-02-11 01:00:00' as an example timestamp for the purposes of making the answer.
Format the output as a single interval value.
*/

SELECT DATE_TRUNC('month', (TIMESTAMP '2012-02-11 01:00:00' + INTERVAL '1 month')) -
		DATE_TRUNC('day', (TIMESTAMP '2012-02-11 01:00:00')) AS remaining


/*
Question
Work out the utilisation percentage for each facility by month,
sorted by name and month, rounded to 1 decimal place.
Opening time is 8am, closing time is 8.30pm.
You can treat every month as a full month, regardless of if there were some dates the club was not open.
*/

SELECT name, month,
  	ROUND((100*slots)/
  		CAST(
  			25*(cast((month + INTERVAL '1 month') AS DATE)
  			- cast (month AS DATE)) AS NUMERIC),1) AS utilisation
	FROM  (
		SELECT facs.name AS name, date_trunc('month', starttime) AS month, sum(slots) AS slots
			FROM cd.bookings bks
			INNER JOIN cd.facilities facs
				ON bks.facid = facs.facid
			GROUP BY facs.facid, month
	) AS inn
ORDER BY name, month


/* ############## Strings ############## */

/*
Question
Perform a case-insensitive search to find all facilities whose name begins with 'tennis'.
Retrieve all columns.
*/

SELECT * FROM cd.facilities WHERE LOWER(name) LIKE 'tennis%'

/*
Question
You've noticed that the club's member table has telephone numbers with very inconsistent formatting.
You'd like to find all the telephone numbers that contain parentheses, returning the member ID and telephone number sorted by member ID.
*/

SELECT memid, telephone FROM cd.members WHERE telephone LIKE '%(%)%'


/* ############## Recursive ############## */

/*Question
Find the upward recommendation chain for member ID 27:
that is, the member who recommended them, and the member who recommended that member, and so on.
Return member ID, first name, and surname. 
Order by descending member id.
*/

with recursive recommenders(recommender) as (
	select recommendedby from cd.members where memid = 27
	union all
	select mems.recommendedby
		from recommenders recs
		inner join cd.members mems
			on mems.memid = recs.recommender
)
select recs.recommender, mems.firstname, mems.surname
	from recommenders recs
	inner join cd.members mems
		on recs.recommender = mems.memid
order by memid desc
