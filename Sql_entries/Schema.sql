CREATE TABLE Student(
Cwid varchar(16) PRIMARY KEY,
Schedule_ID Integer,
Foreign Key (Schedule_ID) references W_SCHEDULE(schedule_id)
);

CREATE TABLE Tutee(
Cwid varchar(16) PRIMARY KEY,
Appointment_ID integer,
Foreign Key (Appointment_ID) references APPOINTMENT(Appointment_ID)
);
CREATE TABLE Tutor(
Cwid varchar(16) PRIMARY KEY,
Appointment_ID integer,
classID varchar(8),
Foreign Key (Appointment_ID) references APPOINTMENT(Appointment_ID), 
Foreign Key (classID) references CLASS (Class_id)
);
CREATE TABLE CLASS(
Class_id varchar(8) PRIMARY KEY,
Schedule_Id INT,
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
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

CREATE TABLE W_SCHEDULE(
schedule_id INT PRIMARY KEY,
Recurring INT,
Monday_schedule varchar(32),
Tuesday_schedule varchar(32),
Wednesday_schedule varchar(32),
Thursday_schedule varchar(32),
Friday_schedule varchar(32),
Sunday_schedule varchar(32)
);

