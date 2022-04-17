-- Tables
CREATE TABLE W_SCHEDULE(
schedule_id INT auto_increment PRIMARY KEY,  
Recurring INT,
Monday_schedule text,
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
tutor_num int unique,
Schedule_Id INT,
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
);

CREATE TABLE Tutors_for(
ID Integer auto_increment PRIMARY KEY,
Tutor_num INT,
Class_id varchar(8)
);

CREATE TABLE APPOINTMENT(
Appointment_ID Integer auto_increment PRIMARY KEY,
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

-- Code for making a tutor. First, we create their work schedule, then, we put them in the tutor class, and finally make them tutor class

-- Tutoring Schedules
-- If the reader is curious, these are all actual students working at the lasso center here on campus

-- Mitchel Murray, primary key = 1
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','2:00 PM, 3:00 PM','NA','10:00 PM, 11:00 PM', 'NA');

-- Will Roche, Primary key = 2
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','2:00 PM, 3:00 PM','NA','10:00 PM', '12:00 PM, 1:00 PM, 3:00 PM');

-- David Bruce, Primary key = 3
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM, 5:00 PM','NA','NA','NA','12:30 PM, 1:30 PM', 'NA');

-- Sam Mulready, Primary key = 4
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:00 AM, 4:00 PM','10:00 AM, 3:00 PM','10:00 AM, 4:00 PM','10:00 AM, 3:00 PM','10:00 PM', '12:00 PM, 1:00 PM, 3:00 PM');

-- Kaitlyn Cotton, Primary key = 5
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM, 6:00 PM, 7:00 PM','NA','NA','NA','NA', '3:00 PM, 4:00 PM, 5:00 PM, 6:00 PM, 7:00 PM');

-- Jacob Proctor, Primary key = 6
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'12:30 PM, 1:30 PM, 2:30 PM, 3:30 PM, 4:30 PM, 5:30 PM','NA','12:30 PM, 1:30 PM, 2:30 PM, 3:30 PM, 4:30 PM, 5:30 PM','NA','NA', 'NA');

-- Zoe Goldade, Primary key = 7
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','3:30 PM, 4:30 PM','NA','2:30 PM', 'NA');

-- Katie Willams, Primary key = 8
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'1:00 PM, 2:00 PM','1:00 PM, 2:00 PM, 3:00 PM','NA','NA','NA','NA');

-- Elizabeth Carlson, Primary key = 9
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30 AM, 11:30 AM, 12:30 PM, 1:30 PM, 2:30 PM','NA','8:00 AM','NA','NA','NA');

-- Natali Edwards, Primary key = 10
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30 AM, 11:30 AM, 12:30 PM, 1:30 PM, 2:30 PM','NA','8:00 AM','NA','NA','NA');



-- Class Schedules
--  Since the schedules for people and classes go into the same class, 
--  a useful way to know if a given schedule is for a person or a class is if the key is > 10. 
--  The max key for people is 10.


-- Calculus 3, primary key = 11
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','NA','11:30 AM', 'NA');

-- introduction to biology, primary key = 12
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'9:30 AM','NA','9:30 AM','NA','9:30 AM', 'NA');

-- Calculus 1, primary key = 13
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','11:30 AM','11:30 AM', 'NA');

-- Computer Science 1, primary key = 14
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','2:30 PM - 3:45','NA','2:30 PM - 3:45','NA', 'NA');

-- Spanish 1, Primary Key = 15
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30','NA','10:30','NA','10:30', 'NA');

-- Techincal Writing, Primary Key = 16
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM - 5:15 PM','NA','4:00 PM - 5:15 PM','NA','NA', 'NA');

-- Organic Chemistry, Primary Key = 17
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','NA','11:30 AM', 'NA');

-- C\C++ Programming, Primary Key = 18
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','2:30 PM - 3:45','NA','2:30 PM - 3:45','NA', 'NA');

-- Composition 1, Primary key = 19
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'9:30 AM','NA','9:30 AM','NA','9:30 AM', 'NA');

-- American History 1, Primary key = 20
INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM - 5:15 PM','NA','4:00 PM - 5:15 PM','NA','NA', 'NA');



-- Classes
INSERT INTO CLASS VALUES ('2156', 11, 'Calculus 3', 'MATH');

INSERT INTO CLASS VALUES ('1114', 12, 'Introduction To Biology', 'BIOL');

INSERT INTO CLASS VALUES ('2144', 13, 'Calculus 1', 'MATH');

INSERT INTO CLASS VALUES ('1113', 14, 'Computer Science 1', 'CS');

INSERT INTO CLASS VALUES ('1713', 15, 'Elementary Spanish 1', 'SPAN');

INSERT INTO CLASS VALUES ('3323', 16, 'Techincal Writing', 'ENGL');

INSERT INTO CLASS VALUES ('3054', 17, 'Organic Chemistry', 'CHEM');

INSERT INTO CLASS VALUES ('2433', 18, 'C\C++ Programming', 'CS');

INSERT INTO CLASS VALUES ('1117', 19, 'Compistion 1', 'ENGL');

INSERT INTO CLASS VALUES ('1493', 20, 'American History Since 1865', 'HIST');

-- Display Classes
SELECT name from CLASS;

-- Tutors. 
--  CWIDS were randomoly chosen and have no actual correlation to the students actual cwids. 
INSERT INTO Tutor VALUES ('A69420101', "Mitchel Murray", '806-867-5309', 1, 1);

INSERT INTO Tutor VALUES ('A69420102', "Will Roche", '806-867-5301', 2, 2);

INSERT INTO Tutor VALUES ('A69420103', "David Bruce", '806-867-5302', 3, 3);

INSERT INTO Tutor VALUES ('A69420104', "Sam Mulready", '806-867-5303', 4, 4);

INSERT INTO Tutor VALUES ('A69420106', "Kaitlyn Cotton", '806-867-5304', 5, 5);

INSERT INTO Tutor VALUES ('A69420108', "Jacob Proctor", '806-867-5305', 6, 6);

INSERT INTO Tutor VALUES ('A69420109', "Zoe Goldade", '806-867-5306', 7, 7);

INSERT INTO Tutor VALUES ('A69420110', "Katie Williams", '806-867-5307', 8, 8);

INSERT INTO Tutor VALUES ('A69420111', "Elizabeth Carlson", '806-867-5308', 9, 9);

INSERT INTO Tutor VALUES ('A69420112', "Natali Edwards", '806-867-5309', 10, 10);

-- Display tutors
SELECT name from Tutor;

-- Tutors for

-- Mitchel Murray's classes
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2156');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2144');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2433');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '1113');

-- Will Roche's classes
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2156');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2144');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2433');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '1113');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '3323');

-- David's Bruce
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (3, '1113');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (3, '3054');

-- Sam Mulready's classes
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (4, '1713');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (4, '1493');

-- Kaitlyn Cotton's classes
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (5, '1113');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (5, '3054');

-- Jacob Proctor
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (6, '1117');

-- Zoe Goldade
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (7, '2156');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (7, '2144');

-- Katie Willams
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (8, '3323');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (8, '1117');

-- Elizabeth Carlson
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (9, '1114');

-- Natali Edwards
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '2156');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '2144');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (4, '1493');
INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (6, '1117');
