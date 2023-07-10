var xhr = null;

getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function dataCallback() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("User data received!");
        rText = JSON.parse(xhr.responseText)
        dataDiv = document.getElementById('result-container');
        // Set current data text
        dataDiv.innerHTML = rText;
    }
}

function getTracks() {
    var artist = document.getElementById('artist').value
    document.getElementById('artist').value = ''
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("POST", "http://localhost:8000/artist10", true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    xhr.send("name=" + artist);
}