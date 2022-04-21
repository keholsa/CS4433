from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

NAME_ARR = []
CRN_ARR = []
TUTORID_ARR = []
DATEID_ARR = []
TIME_ARR = []

#DEV ARRAYS
########################
NAME_ARR = ['Mitchel Murray', 'Will Roche', 'David Bruce', 'Sam Mulready', 'Kaitlyn Cotton', 'Jacob Proctor', 'Zoe Goldade', 'Katie Williams', 'Elizabeth Carlson', 'Natali Edwards']
CRN_ARR = ['1113', '1114', '1117', '1493', '1713', '2144', '2156', '2433', '3054', '3323']
TUTORID_ARR = ['A20198848', 'A30419345', 'A9450849', 'A9832055', 'A89403245', 'A948032832', 'A30345432', 'A48390223']
DATEID_ARR = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
TIME_ARR = ['01:00', '03:00', '04:00', '09:00', '13:00', '18:00']
########################


@app.route('/tutorupdate')
def tutee():
    return render_template("tutee.html")

@app.route('/userInfo')
def userInfo():
    return render_template("emailPhone.html")
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tuteeID = request.form['tutee-id']
        classID = request.form['class-id']
        nameID = request.form['name-id']
        nameTxt = request.form['name-txt']
        dateID = request.form['date-id']
        timeID = request.form['time-id']

        if tuteeID and classID and nameID and nameTxt and dateID and timeID != "":
            return userInfo()
        else:
            return render_template("index.html", testVar = tuteeID, crn_array = CRN_ARR, name_array = NAME_ARR, 
        tutorID_array = TUTORID_ARR, dateID_array = DATEID_ARR, time_array = TIME_ARR)
    else:
        return render_template("index.html",testVar = tuteeID, crn_array = CRN_ARR, name_array = NAME_ARR, 
        tutorID_array = TUTORID_ARR, dateID_array = DATEID_ARR, time_array = TIME_ARR)
#FOR DEV PURPOSES ONLY, login.html TAKES DOMAIN '/'

@app.route('/login')
def hello():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
