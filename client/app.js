function onPageLoad() {
    console.log("Document loaded successfully.");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url, function(data, status) {  // get the locations from url to variable data
        console.log("Data received");
        if(data){
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations){ // iterate through the locations and add them to the dropdown
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
        
    });
    
}

// get the integer value of the selected location
function getBathValue(){
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms){
        if(uiBathrooms[i].checked){
            return parseInt(i) + 1; // return the index of the checked radio button + 1 to get the value
        }
    }

    return -1; // if no radio button is checked, return -1
}

// get the integer value of the selected BHK
function getBHKValue(){
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK){
        if(uiBHK[i].checked){
            return parseInt(i) + 1; // return the index of the checked radio button + 1 to get the value
        }
    }
    return -1; // if no radio button is checked, return -1
}

function onClickedEstimatePrice(){
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");
    
    var url = "http://127.0.0.1:5000/predict_home_price"; // URL to send the request to

    $.post(url, {     // jquery post call to send the data to the server
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakhs</h2>";
        console.log(status);
        
    });
}

window.onload = onPageLoad;
