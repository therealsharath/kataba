from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io


def sample_recognize(local_file_path):
    """
    Transcribe a long audio file using asynchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech_v1.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count": 2,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}
    operation = client.long_running_recognize(config, audio)

    print(u"Processing Speech")
    response = operation.result()

    speech = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        speech.append(alternative.transcript)
    return speech