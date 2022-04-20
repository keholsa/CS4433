#DataBase file
#  Pip install sqlalchemy
#  Pip install sqlalchemy.orm
from sqlalchemy import *
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from markupsafe import escape # Standard library

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
session = sessionmaker(bind=engine)

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
VALUES (1,'NA','NA','14:00, 15:00','NA','10:00, 11:00', 'NA')"""))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'NA','NA','12:00, 15:00','NA','10:00', '12:00, 13:00, 15:00')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'16:00, 17:00','NA','NA','NA','12:30, 13:30 PM', 'NA')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'10:00, 16:00 PM','10:00 AM, 3:00 PM','10:00 AM, 4:00 PM','10:00 AM, 3:00 PM','10:00 PM', '12:00 PM, 1:00 PM, 3:00 PM')""" ))
    conn.execute(text("""INSERT INTO W_SCHEDULE(Recurring, Monday_schedule, Tuesday_schedule, Wednesday_schedule, Thursday_schedule, Friday_schedule, Sunday_schedule) 
VALUES (1,'16:00, 18:00, 20:00','NA','NA','NA','NA', '15:00, 12:00, 5:00 PM, 6:00 PM, 7:00 PM') """ ))
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
    conn.execute(text("""
CREATE TABLE Tutee(
Cwid varchar(16) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
)
""" ))
    #For testing
    conn.execute(text("INSERT INTO Tutee VALUES ('A5879321', 4, 'TestBoi')"))
    #No other prefill. Filled at runtime.
    

#Class table

    conn.execute(text("""
CREATE TABLE CLASS(
Class_id varchar(8) PRIMARY KEY,
Schedule_Id INT,
name varchar(32),
dept varchar(5),
Foreign Key (Schedule_Id) references W_SCHEDULE(schedule_id)
)
""" ))
    #Fill table
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
    
    
    
#Tutor table

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
    #Fill table
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420101', 'Mitchel Murray', '806-867-5309', 1, 1)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420102', 'Will Roche', '806-867-5301', 2, 2)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420103', 'David Bruce', '806-867-5302', 3, 3)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420104', 'Sam Mulready', '806-867-5303', 4, 4)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420106', 'Kaitlyn Cotton', '806-867-5304', 5, 5)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420108', 'Jacob Proctor', '806-867-5305', 6, 6)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420109', 'Zoe Goldade', '806-867-5306', 7, 7)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420110', 'Katie Williams', '806-867-5307', 8, 8)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420111', 'Elizabeth Carlson', '806-867-5308', 9, 9)"))
    conn.execute(text("INSERT INTO Tutor VALUES ('A69420112', 'Natali Edwards', '806-867-5309', 10, 10)"))
    print()
    print("MMMMMOREEE RESULTS LOOKIE HERE VVVVVVVVVV")
    result = conn.execute(text("SELECT name from Tutor"))
    for row in result:
        print(f"{row.name}")
    print("WEOOOOOWWWWEE RESULTS LOOKIE HERE" )
    print()
    
#Tutors for table
    #Create Table
    conn.execute(text("""
CREATE TABLE Tutors_for(
ID Integer auto_increment PRIMARY KEY,
Tutor_num INT,
Class_id varchar(8)
)
""" ))
    #Fill table
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2156')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2144')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '2433')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (1, '1113')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2156')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2144')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '2433')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '1113')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (2, '3323')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (3, '1113')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (3, '3054')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (4, '1713')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (4, '1493')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (5, '1113')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (5, '3054')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (6, '1117')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (7, '2156')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (7, '2144')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (8, '3323')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (8, '1117')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (9, '1114')"))
    
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '2156')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '2144')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '1493')"))
    conn.execute(text("INSERT INTO Tutors_for(Tutor_num, Class_id) VALUES (10, '1117')"))
        
    
#Appointment table    

    conn.execute(text("""
CREATE TABLE APPOINTMENT(
Appointment_ID Integer PRIMARY KEY,
a_date varchar(16),
a_time varchar(16),
Tutor_id varchar(16),
Tutee_id varchar(16),
Class_id varchar(8),
Foreign Key (Class_id) references CLASS(Class_id),
Foreign Key (tutor_id) references Tutor(Cwid), 
Foreign Key (Tutee_id) references Tutee(Cwid)
)
"""))
    


    conn.commit()
    
     
### Here on out is simply testing code, not database code. 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    name = get_Tutor("'Mitchel Murray'")
    return f"{escape(name)}"

@app.route("/SignUp")
def sign_up():
    #Oh yeah. I'm that guy. On server html. 
    return ("""<form action="action_page.php" style="border:1px solid #ccc">
  <div class="container">
    <h1>Sign Up</h1>
    <p>Please fill in this form to create an account.</p>
    <hr>

    <label for="email"><b>cwid</b></label>
    <input type="text" placeholder="Enter cwid" name="cwid" required>
    
    <label for="Name"><b>Name</b></label>
    <input type="text" placeholder="Enter name" name="Name" required>
    

    <label for="psw-repeat"><b>Repeat Password</b></label>
    <input type="password" placeholder="Repeat Password" name="psw-repeat" required>

    <label>
      <input type="checkbox" checked="checked" name="remember" style="margin-bottom:15px"> Remember me
    </label>

    <p>By creating an account you agree to our <a href="#" style="color:dodgerblue">Terms & Privacy</a>.</p>

    <div class="clearfix">
      <button type="button" class="cancelbtn">Cancel</button>
      <button type="submit" class="signupbtn">Sign Up</button>
    </div>
  </div>
</form>
""")

def get_Tutor(name):
    with engine.connect() as conn:
        query=text(f"""Select * from Tutor where name = {name}""")
        Result = conn.execute((query))
        return Result.first()
    
def get_all_Tutors():
    with engine.connect() as conn:
        query=text(f"""Select name from Tutor""")
        Result = conn.execute((query))
        return Result.fetchall()

def get_all_Tutors_by_class(class_id):
    with engine.connect() as conn:
        query=text(f"""SELECT Tutor.name from Tutor, Tutors_for where Tutor.tutor_num = Tutors_for.Tutor_num AND Tutors_for.Class_id = {class_id}""")
        Result = conn.execute((query))
        return Result.fetchall()
    
def get_all_classCodes():
    with engine.connect() as conn:
        query=text(f"""SELECT Class_id from CLASS""")
        Result = conn.execute((query))
        return Result.fetchall()
    
def make_appointment(mykey,mydate, mytime, tutor_id, tutee_id, Class_id):
    with engine.connect() as conn:
        mystring = f"INSERT INTO APPOINTMENT(Appointment_ID, a_date, a_time, Tutor_id, Tutee_id, Class_id) VALUES('{mykey}','{mydate}', '{mytime}', '{tutor_id}', '{tutee_id}', '{Class_id}')"
        query = text(mystring)
        conn.execute(query)
        conn.commit()
        return
    
def get_all_appointments():
    with engine.connect() as conn:
        query=text(f"""SELECT * from APPOINTMENT""")
        Result = conn.execute((query))
        return Result.fetchall()
    
def get_appointment(a_id):
    with engine.connect() as conn:
        query=text(f"""SELECT * from APPOINTMENT where Appointment_ID = {a_id}""")
        Result = conn.execute((query))
        return Result.fetchall()
    

print(get_all_appointments())
make_appointment('1','1-28-2018', '13:30', 'A69420112', 'A5879321', '2156')
print(get_all_appointments())
print(get_all_Tutors())
print(get_all_Tutors_by_class('1113'))
print(get_all_classCodes())




""" Working code. Use me if shit breaks:

#For Testing
    -- Was right below the appointment table --
    mydate = '1-28-2018'
    mytime = '13:00'
    tutor_id = 'A69420112'
    tutee_id = 'A5879321'
    Class_id = '2156'
    mystring = f"INSERT INTO APPOINTMENT(a_date, a_time, Tutor_id, Tutee_id, Class_id) VALUES('{mydate}', '{mytime}', '{tutor_id}', '{tutee_id}', '{Class_id}')"
    query = text(mystring)
    conn.execute(query)
    #conn.execute(text("INSERT INTO APPOINTMENT(a_date, a_time, Tutor_id, Tutee_id, Class_id) VALUES('1-28-2018','13:30', 'A69420112','A5879321', '2156')"))
    #No other prefill. Filled at runtime."""
