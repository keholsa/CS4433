#DataBase file
#  Pip install sqlalchemy
from sqlalchemy import create_engine, text
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


#schedule table
with engine.connect() as conn:
    conn.execute(text("""
CREATE TABLE W_SCHEDULE(
schedule_id INT auto_increment PRIMARY KEY,  
Recurring INT,
Monday_schedule text,
Tuesday_schedule varchar(40),
Wednesday_schedule varchar(40),
Thursday_schedule varchar(40),
Friday_schedule varchar(40),
Sunday_schedule varchar(40)
)
"""))
    #Fill table
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','2:00 PM, 3:00 PM','NA','10:00 PM, 11:00 PM', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','2:00 PM, 3:00 PM','NA','10:00 PM', '12:00 PM, 1:00 PM, 3:00 PM')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM, 5:00 PM','NA','NA','NA','12:30 PM, 1:30 PM', 'NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:00 AM, 4:00 PM','10:00 AM, 3:00 PM','10:00 AM, 4:00 PM','10:00 AM, 3:00 PM','10:00 PM', '12:00 PM, 1:00 PM, 3:00 PM')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM, 6:00 PM, 7:00 PM','NA','NA','NA','NA', '3:00 PM, 4:00 PM, 5:00 PM, 6:00 PM, 7:00 PM') """ ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'12:30 PM, 1:30 PM, 2:30 PM, 3:30 PM, 4:30 PM, 5:30 PM','NA','12:30 PM, 1:30 PM, 2:30 PM, 3:30 PM, 4:30 PM, 5:30 PM','NA','NA', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','3:30 PM, 4:30 PM','NA','2:30 PM', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'1:00 PM, 2:00 PM','1:00 PM, 2:00 PM, 3:00 PM','NA','NA','NA','NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30 AM, 11:30 AM, 12:30 PM, 1:30 PM, 2:30 PM','NA','8:00 AM','NA','NA','NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30 AM, 11:30 AM, 12:30 PM, 1:30 PM, 2:30 PM','NA','8:00 AM','NA','NA','NA')""" ))
    
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','NA','11:30 AM', 'NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'9:30 AM','NA','9:30 AM','NA','9:30 AM', 'NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','NA','11:30 AM', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','2:30 PM - 3:45','NA','2:30 PM - 3:45','NA', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:30','NA','10:30','NA','10:30', 'NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM - 5:15 PM','NA','4:00 PM - 5:15 PM','NA','NA', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'11:30 AM','NA','11:30 AM','NA','11:30 AM', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','2:30 PM - 3:45','NA','2:30 PM - 3:45','NA', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'9:30 AM','NA','9:30 AM','NA','9:30 AM', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'4:00 PM - 5:15 PM','NA','4:00 PM - 5:15 PM','NA','NA', 'NA')"""))
    
    
    

#Tutee table
with engine.connect() as conn:
    #Create table
    conn.execute(text("""
CREATE TABLE Tutee(
Cwid varchar(16) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
)
""" ))
    #Fill table
    #In this case, no pre fill
    

#Class table
with engine.connect() as conn:
    conn.execute(text("""
CREATE TABLE CLASS(
Class_id varchar(8) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
dept varchar(5),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
)
""" ))
    conn.execute(text("INSERT INTO CLASS VALUES ('2156', 11, 'Calculus 3', 'MATH')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('1114', 12, 'Introduction To Biology', 'BIOL')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('2144', 13, 'Calculus 1', 'MATH')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('1113', 14, 'Computer Science 1', 'CS')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('1713', 15, 'Elementary Spanish 1', 'SPAN')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('3323', 16, 'Techincal Writing', 'ENGL')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('3054', 17, 'Organic Chemistry', 'CHEM')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('2433', 18, 'C\C++ Programming', 'CS')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('1117', 19, 'Compistion 1', 'ENGL')"))
    conn.execute(text("INSERT INTO CLASS VALUES ('1493', 20, 'American History Since 1865', 'HIST')"))
    
    print("RESULTS LOOKIE HERE VVVVVVVVVV")
    result = conn.execute(text("SELECT name from CLASS"))
    for row in result:
        print(f"{row.name}")
    print("RESULTS LOOKIE HERE ^^^^^^^^^^^" )
    
    
#Tutor table
with engine.connect() as conn:
    conn.execute(text("""
CREATE TABLE Tutor(
Cwid varchar(16) PRIMARY KEY,
name varchar(32),
Phone varchar(16),
tutor_num int unique,
Schedule_Id INT,
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
)
""" ))

#Tutors for table
with engine.connect() as conn:
    conn.execute(text("""
CREATE TABLE Tutors_for(
ID Integer auto_increment PRIMARY KEY,
Tutor_num INT,
Class_id varchar(8)
)
""" ))
    
#Appointment table    
with engine.connect() as conn:
    conn.execute(text("""
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
)
"""))
conn.commit()

