
import os
import argparse
import speech_recognition as sr

SUPPORTED_EXT = ('.wav', '.flac', '.aiff', '.mp3', '.m4a')


def transcribe_directory(input_dir: str, output_dir: str):
    r = sr.Recognizer()
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(input_dir):
        if not fname.lower().endswith(SUPPORTED_EXT):
            continue
        in_path = os.path.join(input_dir, fname)
        base = os.path.splitext(fname)[0]
        out_path = os.path.join(output_dir, base + '.txt')
        print('Transcribing', in_path)
        try:
            with sr.AudioFile(in_path) as source:
                audio = r.record(source)
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            text = ''
        except sr.RequestError as e:
            text = f'ERROR: {e}'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print('Saved to', out_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', required=True)
    parser.add_argument('--output_dir', required=True)
    args = parser.parse_args()
    transcribe_directory(args.input_dir, args.output_dir)
