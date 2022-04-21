function crnAdd(){

    var crnArrRaw = document.getElementById('crn-array-FLASK').innerHTML;
    var selectBox = document.getElementById('crn-list');

    crnArr = crnArrRaw.split(" ");


    rowIndex = crnArr.length

    crnArr = crnPretty(crnArr);

    for(var i = 0; i < rowIndex; i++){
        var option = document.createElement('option');
        selectBox.appendChild(option);
        option.id = crnArr[i];
        option.value = crnArr[i];
        option.text = crnArr[i];
        option.className = "class-options";

    }

}

crnAdd();

function crnPretty(arr){

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
