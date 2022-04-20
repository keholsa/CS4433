/*table generation dynamically creating table set for tutor information*/

//needs parameter for index values
function tutorTable(){
    //find table container
    var tableDiv = document.getElementById('tutor-info-table-container');
                    
    //create table, does not exist without specified file
    var table = document.createElement('table');
    tableDiv.appendChild(table);

    table.setAttribute("id", "tutor-info-table");
    
    var tableBody = document.createElement('tbody');
    
    table.appendChild(tableBody);
                    
    //row index assigned  value for dev purposes only, equal to rows of incoming data
    var rowIndex = 4
                    
    //tr auto generation with id application
    for(var i = 0; i < rowIndex; i++){
    
    var tr = document.createElement('tr');
    tableBody.appendChild(tr);
    tr.setAttribute("id", "tutor-row-" + i);
                        
        //td auto generate with id application
        for(var j = 0; j < 2; j++){
        var td = document.createElement('td');
        tr.appendChild(td);
            if(j == 0){
            td.setAttribute("id", "tutor-name-" + i);
            }
            else{
            td.setAttribute("id", "tutor-rating-" + i);
            }
        }
    }   
    //initializing with table headers
    document.getElementById("tutor-name-0").innerHTML = "Tutor";
    document.getElementById("tutor-rating-0").innerHTML = "Rating";
}
                
    
//calling function for use               
tutorTable();
