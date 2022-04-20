function timeTable(){

    var tableDiv = document.getElementById('select-time-container');

    var table = document.createElement('table');

    tableDiv.appendChild(table);

    table.setAttribute("id", "select-time-container");

    var tableBody = document.createElement('tbody');

    table.appendChild(tableBody);

    var rowIndex = 4

    for(var i = 0; i < rowIndex; i++){

        var tr = document.createElement('tr');
        tableBody.appendChild(tr);
        tr.setAttribute("id", "time-row-" + i);

            for(var j = 0; j < 1; j++){
                var td = document.createElement('td');
                tr.appendChild(td);
                td.setAttribute("id", "time-id-" + i);
            }
    }

    document.getElementById("time-id-0").innerHTML = "Times Available";
}

timeTable()
