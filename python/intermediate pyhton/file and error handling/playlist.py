liked_songs = {
  'City Walls': 'Twenty One Pilots',
  'La terre est ronde': 'Orelsan',
  'Les lacs du Connemara': 'Michel Sardou',
  'La mort avec toi': 'GARGÄNTUA',
  'The Real Slim Shady': 'Eminem'
}

def write_liked_songs_to_file(liked_songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked Songs:\n')
    for song, artist in liked_songs.items():
      file.write(f'{song} by {artist}\n')

write_liked_songs_to_file(liked_songs, 'playlist.txt')