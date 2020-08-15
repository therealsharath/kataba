from google.cloud import speech_v1
from google.cloud.speech_v1 import enums


def sample_recognize(storage_uri):
    """
    Transcribe long audio file from Cloud Storage using asynchronous speech
    recognition

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
    """

    client = speech_v1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw'

    # Sample rate in Hertz of the audio data sent
    # sample_rate_hertz = 16000

    # The language of the supplied audio
    language_code = "en-US"

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        # "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
        "audio_channel_count" : 2,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Processing Speech")
    response = operation.result()

    speech = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        speech.append(alternative.transcript)
    return speech