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