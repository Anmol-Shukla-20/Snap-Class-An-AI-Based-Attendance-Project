import streamlit as st

from resemblyzer import VoiceEncoder, preprocess_wav  # Helps in Pre-processing the files and normalizing it so that ML techniques can be applied...
import numpy as np
import io  # Helps in loading audio Files...
import librosa

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIo(audio_bytes),sr=16000)  # here sr is sample rate...

        wav = preprocess_wav(audio)

        #To get Embeddings....
        embedding = encoder.embed_utterance(wav)

        return embedding.toList()  # 256 numbers/embeddings for the audio..

    except Exception as e:
        st.error('Voice recog error')
        return None


def identify_speaker(new_embedding, candidates_dict, threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None,0.0

    best_sid = None
    best_score = -1.0

    for sid,stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding, stored_embedding) # comparing the voice of the stored and new embeddings...
            if similarity > best_score:
                best_score = similarity
                best_sid = sid

    if best_score >=threshold:
        return best_sid, best_score

    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict,threshold=0.65):

    try: 
        encoder = load_voice_encoder()   # Initialising Encoder

        audio,sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)  # processing large audios of ultiple students...

        segments = librosa.effects.split(audio,top_db=30)   # top_db is used for voice sensitivity....  If too high then it will only catch those voice where person is shouting and if too low then it can hear the whisper sound also....

        identified_results = {}

        for start,end in segments:
            if (end-start) < sr * 0.5: # audio containing very short audio/noice  will be completely ignored...
                continue

            segment_audio = audio[start:end]     # fetching one segment of the audio at a time...  

            wav = preprocess_wav(segment_audio)   # preprocessing the aduio wave...
            embedding = encoder.embed_utterance(wav)   

            sid, score = identify_speaker(embedding,candidates_dict,threshold)

            if sid:
                if sid not in identify_speaker or score > identified_results[sid]:
                    identified_results[sid] = score

        return identified_results

    except Exception as e:
        st.error("Bulk Processing Error")
        return {}
    






