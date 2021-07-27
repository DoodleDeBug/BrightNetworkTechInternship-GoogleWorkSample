"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.current = ""
        self.isPaused = False
        self.isFlagged = False
        self.playlists = {}

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
        formatted_name = playlist_name.lower()

        if formatted_name in self.playlists:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self.playlists[formatted_name] = []
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        formatted_name = playlist_name.lower()
        videos = self._video_library.get_all_videos()

        vid_list = []
        
        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            vid_list += [f"{vid.title} ({vid.video_id}) [{tags}]"]


        
        id_list = []
        for vid in videos:
            id = vid.video_id
            id_list.append(id)

        if video_id in id_list:
            index = id_list.index(video_id)
            name = videos[index].title
            info = vid_list[index]

        # playlist_list = []

        # for playlist in self.playlists:
        #     playlist_list.append(str(playlist).lower())

        # key = self.playlists.get(formatted_name)
        # if type(key) == None:
        #     key = self.playlists.get(playlist_name)

        if formatted_name not in self.playlists:
            print(
                f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video_id not in id_list:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif info in self.playlists[formatted_name]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            self.playlists[formatted_name].append(info)
            print(f"Added video to {playlist_name}: {name}")

    def show_all_playlists(self):
        """Display all playlists."""

        if self.playlists == {}:
            print(
                "No playlists exist yet")
        else:
            print(
                "Showing all playlists:")
            ordered_names = []
            for playlist_name in self.playlists.keys():
                
                ordered_names.append(playlist_name)
                sorted_list = sorted(ordered_names)

            for playlist_name in sorted_list:
                print(playlist_name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        formatted_name = playlist_name.lower()

        if formatted_name in self.playlists.keys():
            print(f"Showing playlist: {playlist_name}")
            if self.playlists[formatted_name] == []:
                print(
                "No videos here yet")
            else:
                for vid in self.playlists[formatted_name]:
                    print(vid)
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        formatted_name = playlist_name.lower()
        videos = self._video_library.get_all_videos()

        vid_list = []
        
        for vid in videos:

            tags = ""
            for tag in vid.tags:
                tags += tag + " "

            if tags != []:
                tags = tags[0:len(tags)-1]

            vid_list += [f"{vid.title} ({vid.video_id}) [{tags}]"]

        id_list = []
        for vid in videos:
            id = vid.video_id
            id_list.append(id)

        if video_id in id_list:
            index = id_list.index(video_id)
            name = videos[index].title
            info = vid_list[index]

        if (formatted_name not in self.playlists) or (formatted_name not in self.playlists and video_id not in id_list):
            print(
                f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif video_id not in id_list:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif info not in self.playlists[formatted_name]:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            self.playlists[formatted_name].remove(info)
            print(f"Removed video from {playlist_name}: {name}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        formatted_name = playlist_name.lower()

        if (formatted_name not in self.playlists):
            print(
                f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists[formatted_name] = []
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        formatted_name = playlist_name.lower()

        if (formatted_name not in self.playlists):
            print(
                f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            self.playlists.pop(formatted_name)
            print(f"Deleted playlist: {playlist_name}")

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
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
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
            if id_match >= 0:
                id = vid.video_id
                id_list.append(id)

        if len(matches) > 0:
            print(f"Here are the results for {search_tag}:")
            sorted_match = sorted(matches)
            i = 1
            for match in sorted_match:
                print(f"  {i}) {match}")
                i += 1
            print(
                "Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            answer = input()
            if answer.isdigit():
                answer = int(answer)
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
        videos = self._video_library.get_all_videos()
        id_list = []
        for vid in videos:
            id = vid.video_id
            id_list.append(id)

        for vid in videos:
            if video_id == vid.video_id:
                name = vid.title

        if video_id not in id_list:
            print("Cannot flag video: Video does not exist")
        elif self.isFlagged == True:
            print("Cannot flag video: Video is already flagged")
        else:
            self.isFlagged = True
            if flag_reason == "":
                print(
                    f"Successfully flagged video: {name} (reason: Not supplied)")
            else:
                print(
                    f"Successfully flagged video: {name} (reason: {flag_reason})")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        videos = self._video_library.get_all_videos()
        id_list = []
        for vid in videos:
            id = vid.video_id
            id_list.append(id)

        for vid in videos:
            if video_id == vid.video_id:
                name = vid.title

        if video_id not in id_list:
            print("Cannot remove flag from video: Video does not exist")
        elif self.isFlagged == False:
            print("Cannot remove flag from video: Video is not flagged")
        elif self.isFlagged == True:
            print(f"Successfully removed flag from video: {name}")
            self.isFlagged = False
