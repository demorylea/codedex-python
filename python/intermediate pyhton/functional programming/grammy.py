from functools import reduce

# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    return song[1] > 5.00

def minutes_to_seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100

    return minutes * 60 + round(seconds)


def add_durations(total, song):
    duration = song[1]
    return total + duration

longer_than_five_min_songs = list(filter(longer_than_five_minutes, playlist))
playlist_in_seconds = list(map(minutes_to_seconds, playlist))
total_duration = reduce(add_durations, playlist, 0)

print(longer_than_five_min_songs)
print(playlist_in_seconds)
print(total_duration)