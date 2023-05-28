import os

from client import Client

def main():
    spotify_client = Client(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                   os.getenv("SPOTIFY_USER_ID"),
                                   os.getenv("SPOTIFY_PLAYLIST_ID"))

    last_played_tracks = spotify_client.get_last_played_tracks()

    print(f"\nHere are the last 10 tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")

    seed_tracks = [last_played_tracks]

    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    playlist = spotify_client.get_my_playlist()
    print(f"\nUpdating playlist '{playlist.name}'...") # add playlist name

    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


if __name__ == "__main__":
    main()