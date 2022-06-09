-- retrieve all the information from the cd.facilities table
select * from cd.facilities

--  list of all of the facilities and their cost to members
select name, membercost from cd.facilities

-- produce a list of facilities that charge a fee to members
select * from cd.facilities where membercost > 0

-- produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost
select facid, name, membercost, monthlymaintenance from cd.facilities
where membercost > 0 and membercost < monthlymaintenance / 50

-- produce a list of all facilities with the word 'Tennis' in their name
select * from cd.facilities where name like '%Tennis%'

-- produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly maintenance cost is more than $100
select name, 
	case when (monthlymaintenance > 100) then
		'expensive'
	else
		'cheap'
	end as cost
	from cd.facilities;


--produce an ordered list of the first 10 surnames in the members table? The list must not contain duplicates.
select distinct surname from cd.members order by surname limit 10

--produce a list of members who joined after the start of September 2012
SELECT memid, surname, firstname, joindate from cd.members where joindate > '2012-08-31';

--a combined list of all surnames and all facility names.
select surname from cd.members
union
select name from cd.facilities

-- get the signup date of your last member
select max(joindate) as latest
	from cd.members

-- get the first and last name of the last member(s) who signed up
select firstname, surname, joindate as latest
	from cd.members
	where joindate = 
		(select max(joindate) 
			from cd.members);

-- produce a list of the start times for bookings by members named 'David Farrell'
select bks.starttime 
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid
	where 
		mems.firstname='David' 
		and mems.surname='Farrell';

-- a list of all members, including the individual who recommended them (if any)
select mems.firstname as memfname, mems.surname as memsname, recs.firstname as recfname, recs.surname as recsname
	from 
		cd.members mems
		left outer join cd.members recs
			on recs.memid = mems.recommendedby
order by memsname, memfname;   
        
-- produce a list of all members who have used a tennis court? Include in your output the name of the court, and the name of the member formatted as a single column. Ensure no duplicate data, and order by the member name followed by the facility name.
select distinct mems.firstname || ' ' || mems.surname as member, facs.name as facility
	from 
		cd.members mems
		inner join cd.bookings bks
			on mems.memid = bks.memid
		inner join cd.facilities facs
			on bks.facid = facs.facid
	where
		facs.name in ('Tennis Court 2','Tennis Court 1')
order by member, facility

--  produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest) more than $30? Remember that guests have different costs to members (the listed costs are per half-hour 'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of the member formatted as a single column, and the cost. Order by descending cost, and do not use any subqueries. 
select mems.firstname || ' ' || mems.surname as member, 
	facs.name as facility, 
	case 
		when mems.memid = 0 then
			bks.slots*facs.guestcost
		else
			bks.slots*facs.membercost
	end as cost
        from
                cd.members mems                
                inner join cd.bookings bks
                        on mems.memid = bks.memid
                inner join cd.facilities facs
                        on bks.facid = facs.facid
        where
		bks.starttime >= '2012-09-14' and 
		bks.starttime < '2012-09-15' and (
			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or
			(mems.memid != 0 and bks.slots*facs.membercost > 30)
		)
order by cost desc;


-- The club is adding a new facility - a spa. We need to add it into the facilities table. Use the following values:
-- facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.	
insert into cd.facilities (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    values (9, 'Spa', 20, 30, 100000, 800);


-- In the previous exercise, you learned how to add a facility. Now you're going to add multiple facilities in one command. Use the following values:
--     facid: 9, Name: 'Spa', membercost: 20, guestcost: 30, initialoutlay: 100000, monthlymaintenance: 800.
--     facid: 10, Name: 'Squash Court 2', membercost: 3.5, guestcost: 17.5, initialoutlay: 5000, monthlymaintenance: 80.
insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    SELECT 9, 'Spa', 20, 30, 100000, 800
    UNION ALL
        SELECT 10, 'Squash Court 2', 3.5, 17.5, 5000, 80;

insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    values
        (9, 'Spa', 20, 30, 100000, 800),
        (10, 'Squash Court 2', 3.5, 17.5, 5000, 80);

--  automatically generate the value for the next facid
insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    select (select max(facid) from cd.facilities)+1, 'Spa', 20, 30, 100000, 800;

insert into cd.facilities
    (facid, name, membercost, guestcost, initialoutlay, monthlymaintenance)
    values ((select max(facid) from cd.facilities)+1, 'Spa', 20, 30, 100000, 800);

-- made a mistake when entering the data for the second tennis court. The initial outlay was 10000 rather than 8000: you need to alter the data to fix the error. 
update cd.facilities
    set initialoutlay = 10000
    where facid = 1;

-- Update the costs to be 6 for members, and 30 for guests. 
update cd.facilities
    set
        membercost = 6,
        guestcost = 30
    where name in ('Tennis Court 1', 'Tennis Court 2');

-- alter the price of the second tennis court so that it costs 10% more than the first one
update cd.facilities facs
    set
        membercost = (select membercost * 1.1 from cd.facilities where facid = 0),
        guestcost = (select guestcost * 1.1 from cd.facilities where facid = 0)
    where facs.facid = 1;

update cd.facilities facs
    set
        membercost = facs2.membercost * 1.1,
        guestcost = facs2.guestcost * 1.1
    from (select * from cd.facilities where facid = 0) facs2
    where facs.facid = 1;
