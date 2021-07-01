"""A video player class."""

from .video_library import VideoLibrary
import random
import re


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current = ""
        self.isPaused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print(f"Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        list = []

        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            list += [f"   {vid.title} ({vid.video_id}) [{tags}]"]

        sorted_list = sorted(list)
        for vid in sorted_list:
            print(vid)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        videos = self._video_library.get_all_videos()
        id_list = []
        for vid in videos:
            id = vid.video_id
            id_list.append(id)

        if video_id not in id_list:
            print("Cannot play video: Video does not exist")
        else:
            if self.current != "":
                print(f"Stopping video: {self.current}")
            for vid in videos:
                if video_id == vid.video_id:
                    print(f"Playing video: {vid.title}")
                    self.current = vid.title
                    self.isPaused = False

    def stop_video(self):
        """Stops the current video."""

        if self.current != "":
            print(f"Stopping video: {self.current}")
            self.isPaused = False
            self.current = ""
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()

        vid = random.choice(videos)

        if self.current != "":
            print(f"Stopping video: {self.current}")
            print(f"Playing video: {vid.title}")
            self.current = vid.title
        else:
            print(f"Playing video: {vid.title}")
            self.current = vid.title

    def pause_video(self):
        """Pauses the current video."""
        if self.current == "":
            print("Cannot pause video: No video is currently playing")
        elif self.isPaused == False:
            print(f"Pausing video: {self.current}")
            self.isPaused = True
        elif self.isPaused == True:
            print(f"Video already paused: {self.current}")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.current == "":
            print("Cannot continue video: No video is currently playing")
        elif self.isPaused == False:
            print("Cannot continue video: Video is not paused")
        elif self.isPaused == True:
            print(f"Continuing video: {self.current}")
            self.isPaused = False

    def show_playing(self):
        """Displays video currently playing."""
        videos = self._video_library.get_all_videos()
        list = []
        names = []

        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            list += [f"{vid.title} ({vid.video_id}) [{tags}]"]

        for vid in videos:
            names += [f"{vid.title}"]

        if self.current == "":
            print("No video is currently playing")
        elif self.isPaused == False:
            vid = list[names.index(self.current)]
            print(
                f"Currently playing: {vid}")
        elif self.isPaused == True:
            vid = list[names.index(self.current)]
            print(
                f"Currently playing: {vid} - PAUSED")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        list = []
        matches = []
        id_list = []

        term = search_term.lower()

        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            list += [f"{vid.title} ({vid.video_id}) [{tags}]"]

        for vid in list:
            match = vid.find(term)
            if match > 0:
                matches.append(vid)

        for vid in videos:
            id_match = vid.title.lower().find(term)
            if id_match > 0:
                id = vid.video_id
                id_list.append(id)

        if len(matches) > 0:
            print(f"Here are the results for {term}:")
            sorted_match = sorted(matches)
            i = 1
            for match in sorted_match:
                print(f"{i}) {match}")
                i += 1
            answer = input(
                "Would you like to play any of the above? If yes, specify the number of the video.\n""If your answer is not a valid number, we will assume it's a no.\n")
            if answer.isdigit():
                answer = int(answer)
                if answer > 0 and answer <= len(matches):
                    self.play_video(id_list[answer - 1])
        elif len(matches) == 0:
            print(f"No search results for {term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        videos = self._video_library.get_all_videos()
        list = []
        matches = []
        id_list = []

        search_tag = video_tag.lower()

        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            list += [f"{vid.title} ({vid.video_id}) [{tags}]"]

        for vid in list:
            match = vid.find(search_tag)
            if match > 0:
                matches.append(vid)

        for vid in videos:
            tag_list = ""
            for tag in vid.tags:
                tag_list += tag + " "
            id_match = tag_list.find(search_tag)
            if id_match > 0:
                id = vid.video_id
                id_list.append(id)

        print(tag_list)
        if len(matches) > 0:
            print(f"Here are the results for {search_tag}:")
            sorted_match = sorted(matches)
            i = 1
            for match in sorted_match:
                print(f"{i}) {match}")
                i += 1
            answer = input(
                "Would you like to play any of the above? If yes, specify the number of the video.\n""If your answer is not a valid number, we will assume it's a no.\n")
            if answer.isdigit():
                answer = int(answer)
                print(type(answer))
                if answer > 0 and answer <= len(matches):
                    self.play_video(id_list[answer - 1])
        elif len(matches) == 0:
            print(f"No search results for {search_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
