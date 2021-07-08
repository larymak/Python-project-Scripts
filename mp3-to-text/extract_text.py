from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
apikey = 'ADD API KEY HERE'
url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/7dd3d9f3-1fe0-496b-ae56-3876034e7f42'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator = authenticator)
stt.set_service_url(url)

filename = input('add file path > ')
results = []
with open(f"{filename}", 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel',speech_detector_sensitivity=1.0,background_audio_suppression=0.5, continuous=True, \
                        inactivity_timeout=360).get_result()
    results.append(res)
text = []
for file in results:
    for result in file['results']:
        text.append(result['alternatives'][0]['transcript'].rstrip() + '.\n')
with open('./mp3-to-text/output.txt', 'w') as out:
    out.writelines(text)
