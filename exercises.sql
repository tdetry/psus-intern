/* Basic Exercises */

SELECT * FROM cd.facilities;

SELECT name, membercost FROM cd.facilities;

SELECT * FROM cd.facilities
    WHERE membercost > 0;

SELECT facid, name, membercost, monthlymaintenance
	FROM cd.facilities
		WHERE membercost < monthlymaintenance / 50
		AND membercost > 0;

SELECT * FROM cd.facilities
	WHERE name LIKE '%Tennis%';

SELECT * FROM cd.facilities
	WHERE facid = 1
	OR facid = 5;

SELECT name,
	CASE WHEN (monthlymaintenance > 100) THEN
		'expensive'
	ELSE
		'cheap'
	END AS cost
FROM cd.facilities;

SELECT memid, surname, firstname, joindate
	FROM cd.members
	WHERE joindate >= '2012-09-01'::date;

SELECT DISTINCT surname 
	FROM cd.members
	ORDER BY surname
	LIMIT 10;

SELECT surname FROM cd.members
UNION
SELECT name FROM cd.facilities;

SELECT MAX(joindate) AS latest
FROM cd.members;

SELECT firstname, surname, joindate
	FROM cd.members
	WHERE joindate = 
		(SELECT MAX(joindate)
		FROM cd.members);

/* Join Exercises */

SELECT bks.starttime
	FROM cd.bookings bks
		INNER JOIN cd.members mems
			ON mems.memid = bks.memid
	WHERE
		mems.firstname = 'David'
		AND mems.surname = 'Farrell';

SELECT bks.starttime, fac.name
	FROM cd.facilities fac
		INNER JOIN cd.bookings bks
			ON bks.facid = fac.facid
	WHERE fac.name LIKE '%Tennis Court%'
	AND bks.starttime >= '2012-09-21'::date
	AND bks.starttime < '2012-09-22'::date
ORDER BY bks.starttime;

SELECT DISTINCT sec.firstname, sec.surname
	FROM cd.members sec
	INNER JOIN cd.members mems 
	ON mems.recommendedby = sec.memid
ORDER BY surname, firstname;

SELECT mems.firstname as memfname, mems.surname as memsname, 
	recs.firstname as recfname, recs.surname as recsname
	FROM cd.members mems
	LEFT OUTER JOIN cd.members recs
	ON mems.recommendedby = recs.memid
ORDER BY mems.surname, mems.firstname;

SELECT DISTINCT mems.firstname || ' ' || mems.surname AS member, 
	facs.name AS facname
	FROM cd.members mems
	INNER JOIN cd.bookings bks
		ON bks.memid = mems.memid
	INNER JOIN cd.facilities facs
		ON facs.facid = bks.facid
	WHERE facs.name = 'Tennis Court 1' 
	OR facs.name = 'Tennis Court 2'
ORDER BY member, facname;

SELECT mems.firstname || ' ' || mems.surname as members, facs.name as facilitiy, 
	CASE 
		WHEN(mems.memid = 0) THEN
			facs.guestcost * bks.slots
		ELSE
			facs.membercost * bks.slots
	END AS cost
	FROM cd.members mems
		INNER JOIN cd.bookings bks
			ON mems.memid = bks.memid
		INNER JOIN cd.facilities facs
			ON bks.facid = facs.facid
	
	WHERE bks.starttime >= '2012-09-14'::date 
		AND bks.starttime < '2012-09-15'::date
		AND (
		  	(mems.memid = 0 AND bks.slots*facs.guestcost > 30) 
		  	OR (mems.memid != 0 AND bks.slots*facs.membercost > 30))
ORDER BY cost desc;

/* Modifying Data Exercises */

INSERT INTO cd.facilities(facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
	VALUES (9, 'Spa', 20, 30, 100000, 800);

INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
	VALUES (9, 'Spa', 20, 30, 100000, 800),
		(10, 'Squash Court 2', 3.5, 17.5, 5000, 80);

INSERT INTO cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
	VALUES ((SELECT MAX(facid) AS id FROM cd.facilities)+1, 'Spa', 20, 30, 100000, 800);

	
