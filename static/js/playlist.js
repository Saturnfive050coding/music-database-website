function getPlaylist() {
    var id = document.getElementById('get-playlist').value
    document.getElementById('get-playlist').value = ''
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("POST", "http://localhost:8000/playlist", true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    xhr.send("id=" + id);
}

function deletePlaylist() {
    var id = document.getElementById('delete-playlist').value
    document.getElementById('delete-playlist').value = ''
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("POST", "http://localhost:8000/delete", true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    xhr.send("id=" + id);
}

function formatPlaylist(playlist) {
    var pl = JSON.parse(playlist);
    var response = "";
    try {
        response += pl[0][1];
    }
    catch(err) {
        return "Not a valid playlist"
    }
    for(let i = 0; i < pl[0][2].length; i++) {
        response += pl[0][2][i];
    }
    return response
}

function searchAll() {
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = listcallback;
    xhr.open("GET", "http://localhost:8000/lists", true);
    xhr.send(null);
}

function listcallback() {
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("User data received!");
        rText = JSON.parse(xhr.responseText)
        dataDiv = document.getElementById('total-playlists');
        // Set current data text
        dataDiv.innerHTML = rText;
    }
}