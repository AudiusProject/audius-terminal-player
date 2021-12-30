# audius-cli

[![asciicast](https://asciinema.org/a/1qiv8eHbwUktlfqwLnjFG3NkV.svg)](https://asciinema.org/a/1qiv8eHbwUktlfqwLnjFG3NkV)

Terminal-based music player written in Python for the best music in the world 🎵 🎧 💻

Why open [Audius](audius.co) when you can browse and listen from the comfort of your very own terminal? 🧐

Supported/tested platforms: MacOS 12+ 

## Install

📝 Prerequisites:

- ☕ [Homebrew](https://brew.sh/)

```
$ brew tap audiusproject/audius-cli
$ brew install audius
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
3. Update [release URL and SHA](https://github.com/AudiusProject/homebrew-audius-cli/blob/main/Formula/audius.rb#L6-L7) in [homebrew-audius-cli](https://github.com/AudiusProject/homebrew-audius-cli)

---

Created with ❤️ 🍕 🍾 (last but not least) for the Audius Engineering Team Hackathon 2021.
