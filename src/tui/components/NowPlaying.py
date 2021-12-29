class NowPlaying:
    def __init__(self, player, x_offset, y_offset, width, height, padx, pady, command):
        self.player = player
        self.master = player.root
        self.label = self.master.add_button(
            self.get_now_playing(),
            x_offset,
            y_offset,
            row_span=height,
            column_span=width,
            padx=padx,
            pady=pady,
            command=command,
            # auto_focus_buttons=False,
        )

    def get_now_playing(self):
        current_track = self.player.current_track
        if current_track:
            return f"📻 Now Playing -> {current_track.title} by {current_track.artist}"
        return "💫 Pick a track to listen to awesome music!"
