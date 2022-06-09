-- Retrieve everything from a table
SELECT * FROM tablename;

-- Retrieve specific columns from table
SELECT col1,col2,col3 FROM tablename;

--Where clause 
SELECT * FROM tablename WHERE parameter >2;

--More where clause
SELECT col1, col2,col3 from tablename WHERE parameter > 0 and (parameter2< parameter3 );

--String searches
SELECT * FROM tablename WHERE param LIKE '%string%';

--Matching against multiple possible values
SELECT * FROM tablename WHERE id IN (2,4);

--Classify results into buckets
SELECT param, 
    CASE WHEN (param2 >100 ) THEN
        'sometag1'
    else
        'sometag2'
    end as classifiedcol
    FROM tablename

--Dates
SELECT param1,param2,param3, date FROM tablename WHERE date >= '2022-04-02';

--Remove duplicates, order by
SELECT DISTINCT param1 FROM tablename ORDER BY param1 LIMIT 10;

--Combine results from multiple queries (unions)
SELECT param1 FROM tablename 
UNION 
SELECT param2 FROM tablename2

--Simple aggregation
SELECT max(date) AS latest FROM tablename;

SELECT param1,param2,param3,date 
    FROM tablename
    WHERE date =
        (SELECT max(date) FROM tablename);

--Joins
SELECT bks.starttime 
	FROM 
		cd.bookings bks
		INNER JOIN cd.members mems
		on mems.memid =bks.memid
		
	WHERE
		mems.firstname ='David'
		and mems.surname ='Farrell';

--Joins2
SELECT bks.starttime,f.name 
	FROM 
		cd.bookings bks
		INNER JOIN cd.facilities f
		ON f.facid =bks.facid
	WHERE 
		f.name in ('Tennis Court 2','Tennis Court 1') AND
		bks.starttime >='2012-09-21' AND
		bks.starttime <= '2012-09-22'
ORDER BY bks.starttime;

--Self join
SELECT DISTINCT recs.firstname as firstname, recs.surname as surname
	FROM 
		cd.members mems
		INNER JOIN cd.members recs
			ON recs.memid =mems.recommendedby

ORDER BY surname, firstname

--Self join 2
SELECT mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
	FROM 
		cd.members mems
		LEFT OUTER JOIN cd.members recs
			ON recs.memid = mems.recommendedby
	
	ORDER BY memsname,memfname


--Threejoin
SELECT DISTINCT mems.firstname || ' ' || mems.surname as member, facs.name as facility
    FROM 
        cd.members mems
        INNER JOIN cd.bookings bks
            ON mems.memid =bks.memid
        INNER JOIN cd.facilities facs
            ON bks.facid =facs.facid
    WHERE
        facs.name in ('Tennis Court 2','Tennis Court 1')
ORDER BY member,facility


