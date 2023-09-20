# Musikunterlegung für Vokabel-Audio-Dateien

Dieses Projekt ermöglicht es, eine Hintergrundmusik zu Vokabel-Audio-Dateien hinzuzufügen. Die Musik wird fortlaufend für alle Vokabel-Audio-Dateien verwendet und am Ende wiederholt, wenn sie nicht ausreicht.

## Voraussetzungen

- Python 3.9 oder höher
- `pydub` Bibliothek
- FFmpeg

## Installation

1. Installieren Sie die `pydub` Bibliothek mit `pip`:
`pip install pydub`

2. Installieren Sie FFmpeg. Für macOS mit Homebrew:
`brew install ffmpeg`
Für andere Betriebssysteme besuchen Sie die [offizielle FFmpeg-Website](https://ffmpeg.org/download.html) für Installationsanweisungen.

3. Stellen Sie sicher, dass `ffmpeg` und `ffprobe` im PATH verfügbar sind, indem Sie:
ffmpeg -version
ffprobe -version
im Terminal ausführen.

## Verwendung

1. Ändern Sie die Pfade im Skript entsprechend:

- `musik_path`: Pfad zur Musikdatei, die als Hintergrund verwendet wird.
- `vokabel_folder`: Ordner mit den Vokabel-Audio-Dateien.
- `output_folder`: Zielordner für die generierten Audio-Dateien mit Musikunterlegung.

2. Führen Sie das Python-Skript aus:
`python main.py`

Nach der Ausführung sollten Sie im `output_folder` Audio-Dateien mit Musikunterlegung für jede Vokabel-Audio-Datei finden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.