# audius-terminal-player

<p align="center"><img src="demo.gif?raw=true"/></p>

Terminal-based music player written in Python for the best music in the world 🎵 🎧 💻

Browse and listen to [Audius](https://audius.co) from the comfort of your very own terminal. 🎶

Supported/tested platforms: MacOS 12+ 

## Install

📝 Prerequisites:

- ☕ [Homebrew](https://brew.sh/)

```
brew tap audiusproject/audius-terminal-player
brew install audius-terminal-player
```

## Features ✨

- ▶️ Play Trending tracks 🚀
- 🔎 Search Users 👥, Tracks 🎵, and Playlists 📜
- ▶️ Play Users' Favorited, Reposted, and Uploaded Tracks
- 💻 Terminal UI implemented in [py_cui](https://github.com/jwlodek/py_cui)

## Develop 🧑‍💻

📝 Prerequisites:

- Python 3.9+ 🐍

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m src
```

## Build & Release 📦 🚢

1. Bump version in [`setup.cfg`](setup.cfg) manually
2. Make a GitHub tagged release with the new version
3. Update [release URL and SHA](https://github.com/AudiusProject/homebrew-audius-terminal-player/blob/main/Formula/audius-terminal-player.rb#L6-L7) in [homebrew-audius-terminal-player](https://github.com/AudiusProject/homebrew-audius-terminal-player)

---

Created with ❤️ 🍕 🍾 (last but not least) for the Audius Engineering Team Hackathon 2021.
