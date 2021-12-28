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
        )

    def get_now_playing(self):
        current_track = self.player.current_track
        now_playing = "Pick a track!"
        if current_track:
            now_playing = f"{current_track.title} by {current_track.artist}\n\tPress <ENTER> to ⏹️"
        return f"\t📻 Now playing:\n\t{now_playing}"
        # TODO format so that line doesn't cut off
