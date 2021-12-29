# Documentation: https://docs.brew.sh/Formula-Cookbook
#                https://rubydoc.brew.sh/Formula
# PLEASE REMOVE ALL GENERATED COMMENTS BEFORE SUBMITTING YOUR PULL REQUEST!
class audius < Formula
    desc "Terminal-based music player written in Python for the best music in the world 🎵 🎧 💻"
    homepage "https://github.com/AudiusProject/audius-cli"
    url "https://github.com/AudiusProject/audius-cli/raw/main/audius"
    sha256 ""
    version "0.0.1"
  
    def install
      bin.install "audius"
    end
  end
