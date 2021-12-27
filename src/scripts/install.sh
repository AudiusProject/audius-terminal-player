echo "Installing audius-cli... 🎧"
mkdir -p ~/.local/bin && ln -sf $PWD/bin/audius ~/.local/bin/audius
echo "audius-cli successfully installed! Try playing a track with 'audius trending --rank=1'"