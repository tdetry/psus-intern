-- Retrieve all columns
select * from cd.facilities;

-- Retrieve only some columns
select name, membercost from cd.facilities;

-- Filter rows by some condition
select * from cd.facilities where membercost > 0;

-- Complex filter conditions
select facid, name, membercost, monthlymaintenance
from cd.facilities
where membercost > 0
and membercost < (monthlymaintenance / 50);

-- LIKE patterns
select *
from cd.facilities
where name like '%Tennis%';

-- IN operator
select *
from cd.facilities
where facid in (1, 5);

-- CASE conditions
select name,
  case when (monthlymaintenance > 100) then
    'expensive'
  else
    'cheap'
  end as cost
from cd.facilities;

-- Timestamp comparisons
select memid, surname, firstname, joindate
from cd.members
where joindate > '2012-09-01';

-- DISTINCT, ORDER BY and LIMIT
select distinct surname
from cd.members
order by surname
limit 10;

-- UNION
select surname from cd.members
union
select name from cd.facilities;

-- MAX
select max(joindate) as latest
from cd.members;

-- Subqueries
select firstname, surname, joindate
	from cd.members
	where joindate =
		(select max(joindate)
			from cd.members);

-- Inner joins
select B.starttime
from cd.bookings B
inner join cd.members M
on
  B.memid = M.memid
where M.firstname = 'David'
and M.surname = 'Farrell';

-- Joins with complex filters
select
	B.starttime as start,
	F.name
from cd.bookings B
inner join cd.facilities F
on
	B.facid = F.facid
where B.starttime between '2012-09-21 00:00:00' and '2012-09-21 23:59:59'
and F.name like 'Tennis Court%'
order by B.starttime;

-- Self joins
select distinct M.firstname, M.surname
from cd.members M
inner join cd.members MM
on
	M.memid = MM.recommendedby
order by M.surname, M.firstname;

-- Outer joins
select
	M.firstname as memfname,
	M.surname as memsname,
	MM.firstname as recfname,
	MM.surname as recsname
from cd.members M
left outer join cd.members MM
on
	MM.memid = M.recommendedby
order by M.surname, M.firstname;

-- Complex join conditions
select
	distinct concat(M.firstname, ' ', M.surname) as member,
	F.name as facility
from cd.bookings B
inner join cd.facilities F
on
	B.facid = F.facid and
	F.name like 'Tennis%'
inner join cd.members M
on
	M.memid = B.memid
order by member, facility;
