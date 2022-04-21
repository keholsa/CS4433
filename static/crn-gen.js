function crnAdd(){

    var crnArrRaw = document.getElementById('crn-array-FLASK').innerHTML;
    var selectBox = document.getElementById('crn-list');

    crnArr = crnArrRaw.split(" ");

    rowIndex = crnArr.length()

    for(var i = 0; i < rowIndex; i++){
        var option = document.createElement('option');
        selectBox.appendChild(option);
        option.id = crnArr[i];
        option.value = crnArr[i];
        option.text = crnArr[i];
        option.className = "class-options";

    }

}
