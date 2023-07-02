function getPlaylist() {
    var id = document.getElementById('playlist-id').value
    document.getElementById('playlist-id').value = ''
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    xhr.open("POST", "http://localhost:8000/playlist", true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
    xhr.send("id=" + id);
}