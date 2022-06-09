-- Retrieve everything from a table
SELECT * from cd.facilities;

-- Retrieve specific columns from a table
SELECT name, membercost FROM cd.facilities;

-- Control which rows are retrieved
SELECT * FROM cd.facilities
WHERE membercost > 0;

-- Control which rows are retrieved - part 2
SELECT facid, name, membercost, monthlymaintenance
FROM cd.facilities
WHERE membercost > 0 
AND membercost < (1./50) * monthlymaintenance;

-- Basic string searches
SELECT * 
FROM cd.facilities
WHERE name ~ 'Tennis';

-- Matching against multiple possible values
SELECT *
FROM cd.facilities
WHERE facid = 1
OR facid = 5;

-- Classify results into buckets
SELECT name,
	   case when (monthlymaintenance > 100) then
	   	'expensive'
	   else
	   	'cheap'
	   end
	   as cost
FROM cd.facilities;

-- Working with dates
SELECT memid, surname, firstname, joindate
FROM cd.members
WHERE joindate >= '2012-09-01';

-- Removing duplicates, and ordering results
SELECT distinct surname
FROM cd.members
ORDER BY surname
LIMIT 10;

-- Combining results from multiple queries
SELECT surname from cd.members
UNION
SELECT name from cd.facilities;

-- Simple aggregation
SELECT max(joindate) as latest
FROM cd.members;

-- More aggregation
SELECT firstname, surname, joindate
FROM cd.members
WHERE joindate = (SELECT max(joindate) FROM cd.members);