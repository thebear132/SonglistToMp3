import subprocess

def download_songs(song_list, output_directory='output'):
    # Create the output directory if it doesn't exist
    subprocess.run(['mkdir', '-p', output_directory])

    for song_name in song_list:
        print(f"Downloading: {song_name}")

        # Use youtube-dl to search for and download the song
        subprocess.run(['./youtube-dl', f'ytsearch:{song_name}', '--extract-audio', '--audio-format', 'mp3', '--output', f'{output_directory}/%(title)s.%(ext)s'])

if __name__ == "__main__":
    try:
        fhand = open("songlist.txt", 'r')
    except IOError:
        print('File does not exist')
        exit(1)
    songs = []
    # Iterating over the lines in file
    for song in fhand:
        songs.append(song.strip())
    fhand.close()

    # Specify the output directory (optional, defaults to 'output')
    output_dir = "my_music"
    # Download the songs
    download_songs(songs, output_directory=output_dir)
