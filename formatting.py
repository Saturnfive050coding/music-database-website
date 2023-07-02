import json

def format_playlist(pl):
    response = ''
    try:
        response += pl[0][1]
    except:
        return 'Not a valid playlist.'
    tracks = json.loads(pl[0][2])
    for value in tracks:
        response += value
    return response