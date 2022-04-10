CREATE TABLE W_SCHEDULE(
schedule_id INT PRIMARY KEY,  
Recurring INT,
Monday_schedule varchar(40),
Tuesday_schedule varchar(40),
Wednesday_schedule varchar(40),
Thursday_schedule varchar(40),
Friday_schedule varchar(40),
Sunday_schedule varchar(40)
);

CREATE TABLE Tutee(
Cwid varchar(16) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
);

CREATE TABLE CLASS(
Class_id varchar(8) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
dept varchar(5),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
);

CREATE TABLE Tutor(
Cwid varchar(16) PRIMARY KEY,
name varchar(32),
Phone varchar(16),
tutor_num varchar(8)
);

CREATE TABLE Tutors_for(
ID Integer PRIMARY KEY,
Tutor_num varchar(8),
Class_id varchar(8)
);

CREATE TABLE APPOINTMENT(
Appointment_ID Integer PRIMARY KEY,
a_date DATE,
a_time TIME,
Tutor_id varchar(16),
Tutee_id varchar(16),
uOnline Integer,
Class_id varchar(8),
Foreign Key (Class_id) references CLASS(Class_id),
Foreign Key (tutor_id) references Tutor(Cwid), 
Foreign Key (Tutee_id) references Tutee(Cwid)
);



-- insert a schedule. I hardcoded values here, but we can ->
-- put in other values as necessary. Here 1 on recurring means that this schedule recurrs. ->
-- This schecule is supposed to be for a person
INSERT INTO W_SCHEDULE VALUES (1,1,'11:30 AM - 12:20 PM, 2:30 PM - 5:15PM','10:30 AM - 1:15AM','11:30 AM - 12:20 PM, 2:30 PM - 5:15 PM','10:30 AM - 1:15 AM','11:30 AM - 12:20 PM', 'NA');

-- Here's another table to represent a class schedule. Specifically, my calc 3 class.
INSERT INTO W_SCHEDULE VALUES (2,1,'11:30 AM - 12:20 PM','NA','11:30 AM - 12:20 PM','NA','11:30 AM - 12:20 PM', 'NA');

-- Insert a class. 
INSERT INTO CLASS VALUES ('2156', 2, 'Calculus 3', 'MATH');

-- Make a tutor
INSERT INTO Tutor VALUES ('A69420101', "Luke Gipson", '806-867-5309', '3');

-- Now, let's make them tutor a class. 
INSERT INTO Tutors_for VALUES (6,'3','2156');


-- get all tutors, and all their info
SELECT * FROM Tutor;

-- Select all tutors names teaching Calculus 3. Here, it's just Luke Gipson,->
-- but then again, he's the only tutor in the Database, so who else could it be?
 SELECT Tutor.name FROM Tutor, Tutors_for where Tutor.tutor_num = Tutors_for.tutor_num AND Tutors_for.Class_id = '2156';

-- make tutee
INSERT INTO Tutee VALUES ('A69420102', 1, 'Ricky Bobby');

-- Make appointment 
INSERT INTO APPOINTMENT VALUES(5, '2022-04-10',  '12:32', 'A69420101', 'A69420102', 0, '2156');


-- Appointments with tutor Luke Gipson
SELECT APPOINTMENT.a_time, APPOINTMENT.a_date, APPOINTMENT.Class_id from APPOINTMENT, Tutor where APPOINTMENT.tutor_id = Tutor.Cwid and Tutor.name = "Luke Gipson";

-- All appointments today
SELECT * from APPOINTMENT where CURRENT_DATE = a_date;

-- All appointments today, ordered by time in ascending order
SELECT * from APPOINTMENT where CURRENT_DATE = a_date ORDER BY a_time ASC;


