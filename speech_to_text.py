
import argparse
import os
import speech_recognition as sr
from recorder import record_to_file


def transcribe_audio_file(path: str, recognizer: sr.Recognizer, show_confidence: bool = False) -> str:
    """Transcribe a single audio file and return the recognized text."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    with sr.AudioFile(path) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return ''
    except sr.RequestError as e:
        raise RuntimeError(f'Speech recognition error: {e}')


def live_microphone_mode(recognizer: sr.Recognizer, save_to: str | None = None):
    print('Microphone mode. Press Ctrl+C to exit.')
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            while True:
                print('Listening... (speak now)')
                audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                    print('You said:', text)
                    if save_to:
                        with open(save_to, 'a', encoding='utf-8') as f:
                            f.write(text + '\n')
                except sr.UnknownValueError:
                    print('Could not understand audio')
                except sr.RequestError as e:
                    print('Request failed:', e)
    except KeyboardInterrupt:
        print('\nExiting microphone mode')


def main():
    parser = argparse.ArgumentParser(description='Speech-to-Text using SpeechRecognition')
    parser.add_argument('--file', '-f', help='Path to an audio file to transcribe')
    parser.add_argument('--record', '-r', help='Record from microphone and save to WAV file then transcribe (path to save wav)', nargs='?', const='recording.wav')
    parser.add_argument('--save', '-s', help='Append transcripts to a text file')
    args = parser.parse_args()

    recognizer = sr.Recognizer()

    if args.file:
        text = transcribe_audio_file(args.file, recognizer)
        print('Transcription:')
        print(text)
        if args.save:
            with open(args.save, 'w', encoding='utf-8') as f:
                f.write(text)
        return

    if args.record:
        wav_path = args.record
        record_to_file(wav_path)
        text = transcribe_audio_file(wav_path, recognizer)
        print('Transcription:')
        print(text)
        if args.save:
            with open(args.save, 'w', encoding='utf-8') as f:
                f.write(text)
        return

    live_microphone_mode(recognizer, save_to=args.save)


if __name__ == '__main__':
    main()
