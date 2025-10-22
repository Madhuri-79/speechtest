# speechtest(python)
   #overview
     -The speech to text converter is a python based project that transforms your spoken words
    into text in real time.
    It uses SpeechRecognition,PyAudio and tkinter to provide both a command line and graphical
    interface.

    Use this project to:
      -Create:voice controlled tools
      -Generate:automatic transcriptions
      -Build:AI voice assistants
      -Enable:Hands free note taking

  #features:
     -Live voice Recognition,
     -Audio File Support,
     -Auto Save,
     -User friendly GUI,
     -Modular code,
     -Test Suite,

  #Technologies Used:
     -Python 3.8+,
     -SpeechRecognition,
     -PyAudio,
     -ffmpeg,
     -Tkinter,
     -pytest,
  ##instal dependencies:
     -pip install -r requirements.txt
  ##instal audio libraries:
     -pip install pipwin
     -pipwin install pyaudio

     
#Project Structure:
    requirements.txt
    speech_to_text.py
    gui_transcriber.py
    transcribe_files.py
    recorder.py
    tests
      --test_transcription.py

  #usage
     1.Live speech transcription-
        python speech_to_text.py
      speak into mic and see words appear in real time
       press Ctrl+c to stop

     2.GUI Mode
         python gui_transcriber.py
        click start listening ->speak ->click Stop & Save to save transcript.


    #Working process
         speech Input
             |
         Audio Preprocessing
             |
         SpeechRecognition
             |
         Text Output



               #output
               https://github.com/Madhuri-79/speechtest/blob/a633dcd1d965642ae6dfd824f5ad811cc8d55cb0/speech.png
  

     
     
    
