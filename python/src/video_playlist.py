"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, playlist_title: str):
        """Video constructor."""
        self._title = playlist_title

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title
