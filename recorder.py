import speech_recognition as sr


def record_to_file(filename: str, timeout: float = 5, phrase_time_limit: float = 10):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Adjusting for ambient noise...')
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('Recording — please speak')
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

    # Write WAV file
    with open(filename, 'wb') as f:
        f.write(audio.get_wav_data())
    print(f'Saved recording to {filename}')
    return filename


if __name__ == '__main__':
    record_to_file('output.wav')


