/*table generation dynamically creating table set for tutor information*/

//needs parameter for index values
function tutorTable(){
    //find table container
    var tableDiv = document.getElementById('tutor-info-table-container');
    
    //tutor data grab
    var tutorArrRaw = document.getElementById('tutor-array-FLASK').innerHTML;
    tutorArr = tutorArrRaw.split(" ");
    tutorArr = tutorArrRaw.split(" ");
    tutorArr = prettyTutors(tutorArr)

    //tutorID data grab
    var tutorIDArrRaw = document.getElementById('tutorID-array-FLASK').innerHTML;
    tutorIDArr = tutorIDArrRaw.split(" ");
    tutorIDArr = prettyTutors(tutorIDArr);

    //tutor array index specification
    rowIndex = tutorArr.length;
    //create table, does not exist without specified file
    var table = document.createElement('table');
    tableDiv.appendChild(table);

    table.setAttribute("id", "tutor-info-table");
    
    var tableBody = document.createElement('tbody');
    
    table.appendChild(tableBody);
                    
    //row index assigned  value for dev purposes only, equal to rows of incoming data

                    
    var count = 0;
    //tr auto generation with id application
    for(var i = 0; i < rowIndex / 2 ; i++){
    
    var tr = document.createElement('tr');
    tableBody.appendChild(tr);
    tr.setAttribute("id", "tutor-row-" + i);
        //td auto generate with id application
        for(var j = 0; j < 2; j++){
        var td = document.createElement('td');
        tr.appendChild(td);
            if(j == 0){
            td.setAttribute("id", "tutor-name-" + i);
            td.setAttribute("tag", tutorIDArr[count-2]);
            td.setAttribute("class", "tutor-td")
                if(count == 2){
                    td.innerHTML = tutorArr[count-2] + ' ' + tutorArr[count-1];

                }else{
                td.innerHTML = tutorArr[count] + ' ' + tutorArr[count+1];
                }
            }
            else{
            td.setAttribute("id", "tutor-rating-" + i);
            td.setAttribute("tag", "20" + [i]);
            }
        
        }
        count = count + 2;
    }   
    //initializing with table headers
    document.getElementById("tutor-name-0").innerHTML = "Tutor";
    document.getElementById("tutor-rating-0").innerHTML = "Rating";
}
                
    
//calling function for use               
tutorTable();


function prettyTutors(arr){

        for(var i = 0; i < arr.length; i++)
            if(i == 0){
            arr[0] = arr[0].replace('[','');
            arr[0] = arr[0].replace('\'','');
            arr[0] = arr[0].replace('\'','');
            arr[0] = arr[0].replace(',', '')
            }
            else{
                arr[i] = arr[i].replace('\'', '');
                arr[i] = arr[i].replace('\'','');
                arr[i] = arr[i].replace(',', '')
            }
        
        return arr
    
    
}
