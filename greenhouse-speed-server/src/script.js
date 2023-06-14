function onSeconds() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };
      
    fetch("/data/on_seconds", requestOptions)
        .then(response => response.text())
        .then(result => document.getElementById("ontime").innerHTML = result)
        .catch(error => console.log('error', error));
}

function offSeconds() {
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };
      
    fetch("/data/off_seconds", requestOptions)
        .then(response => response.text())
        .then(result => document.getElementById("offtime").innerHTML = result)
        .catch(error => console.log('error', error));
}

function setOnSeconds() {
    
}

function setOffSeconds() {

}


// run on page load
onSeconds();
offSeconds();