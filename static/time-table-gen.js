function timeTable(){

    //find container for time table
    var tableDiv = document.getElementById('select-time-container');

    //create table in container
    var table = document.createElement('table');
    tableDiv.appendChild(table);

    //set id attribute for 
    table.setAttribute("id", "select-time-table");

    //create table body
    var tableBody = document.createElement('tbody');
    table.appendChild(tableBody);

    //variable grab for available times
    var timeArrRaw = document.getElementById("time-array-FLASK").innerHTML;
    timeArr = timeArrRaw.split(" ");

    //definining row index
    var rowIndex = timeArr.length

    //dynamic row creation
    for(var i = 0; i < rowIndex + 1; ++i){

        var tr = document.createElement('tr');
        tableBody.appendChild(tr);
        tr.setAttribute("id", "time-row-" + i);

            //dynamic data creation per row
            for(var j = 0; j < 1; j++){
                var td = document.createElement('td');
                td.innerHTML = timeArr[i -1];
                tr.appendChild(td);
                td.setAttribute("id", "time-id-" + i);
                td.setAttribute("tag", timeArr[i - 1]);
                td.setAttribute("class", "time-td");
            }
    }

    //initilize row definitition
    document.getElementById("time-id-0").innerHTML = "Times Available";
}

timeTable()
