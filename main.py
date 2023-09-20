# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pydub import AudioSegment

def combine_audio(vokabel_path, musik_path, output_path, music_volume=-15):
    # Laden Sie die Audio-Dateien
    vokabel = AudioSegment.from_file(vokabel_path, format="mp3")
    musik = AudioSegment.from_file(musik_path, format="mp3")
    musik = musik + music_volume  # Musik leiser machen

    # Wiederholen Sie die Musik, bis sie die gleiche Länge wie die Vokabel-Datei hat
    while len(musik) < len(vokabel):
        musik += musik

    # Schneiden Sie die Musik auf die gleiche Länge wie die Vokabel-Datei
    musik = musik[:len(vokabel)]

    # Kombinieren Sie Vokabel und Musik
    combined = vokabel.overlay(musik)

    # Exportieren Sie die kombinierte Audio-Datei
    combined.export(output_path, format="mp3")

def main():
    # Pfad zur Musikdatei
    musik_path = 'musik/musiklofi.wav'
    vokabel_folder = 'vokabeln/'
    output_folder = 'output/'

    # Gehe durch jeden Vokabel-Audio im Vokabel-Ordner
    import os
    for filename in os.listdir(vokabel_folder):
        if filename.endswith(".mp3"):
            vokabel_path = os.path.join(vokabel_folder, filename)
            output_path = os.path.join(output_folder, "" + filename)
            combine_audio(vokabel_path, musik_path, output_path)

if __name__ == "__main__":
    main()