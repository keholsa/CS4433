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
classID varchar(8),
Foreign Key (classID) references CLASS (Class_id)
);


CREATE TABLE APPOINTMENT(
Appointment_ID Integer PRIMARY KEY,
Time_and_date DATETIME,
Tutor_id varchar(16),
Tutee_id varchar(16),
uOnline Integer,
Foreign Key (tutor_id) references Tutor(Cwid), 
Foreign Key (Tutee_id) references Tutee(Cwid)
);



-- insert a schedule. I hardcoded values here, but we can ->
-- put in other values as necessary. Here 1 on recurring means that this schedule recurrs. ->
-- This schecule is supposed to be for a person
INSERT INTO W_SCHEDULE VALUES (1,1,'11:30 AM - 12:20 PM, 2:30 PM - 5:15PM','10:30 AM - 1:15AM','11:30 AM - 12:20 PM, 2:30 PM - 5:15 PM','10:30 AM - 1:15 AM','11:30 AM - 12:20 PM', 'NA');

-- Here's another table to represent a class. Specifically, my calc 3 class.
INSERT INTO W_SCHEDULE VALUES (2,1,'11:30 AM - 12:20 PM','NA','11:30 AM - 12:20 PM','NA','11:30 AM - 12:20 PM', 'NA');

-- Insert a class. 
INSERT INTO CLASS VALUES ('2156', 2, 'Calculus 3', 'MATH');

-- Now, let's make a tutor
INSERT INTO Tutor VALUES ('A69420101', "Luke Gipson", '806-867-5309', '2156');


-- get all tutors, and all their info
SELECT * FROM Tutor;

-- Select all tutors names teaching Calculus 3. Here, it's just Luke Gipson,->
-- but then again, he's the only tutor in the Database, so who else could it be?
SELECT Tutor.name FROM Tutor, CLASS where Tutor.ClassId = CLASS.Class_id AND CLASS.name = "Calculus 3";