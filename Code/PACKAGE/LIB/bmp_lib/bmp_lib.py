import os
from gtts import gTTS
from io import BytesIO
import pandas as pd             
import openpyxl

import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest



# gtts pandas spacy openpyxl wheel


###################################################################################


def spacyExtractiveSummarizer(text, percentage=0.4):
    model_name = "fr_core_news_sm"

    try:
        spacy.load(model_name)
        print(f"Le modèle '{model_name}' est déjà installé.")
    except OSError:
        print(f"Téléchargement du modèle '{model_name}'...")
        spacy.cli.download(model_name)
        print(f"Le modèle '{model_name}' a été téléchargé et est prêt à être utilisé.")
    print("\n\n\n\n")

    # load the model into spaCy
    model = spacy.load(model_name)    
    doc= model(text)
    
    ## The score of each word is kept in a frequency table
    tokens=[token.text for token in doc]
    freq_of_word=dict()
    
    # Text cleaning and vectorization 
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in freq_of_word.keys():
                    freq_of_word[word.text] = 1
                else:
                    freq_of_word[word.text] += 1
                    
    # Maximum frequency of word
    max_freq=max(freq_of_word.values())
    
    # Normalization of word frequency
    for word in freq_of_word.keys():
        freq_of_word[word]=freq_of_word[word]/max_freq
        
    # In this part, each sentence is weighed based on how often it contains the token
    sent_tokens= [sent for sent in doc.sents]
    sent_scores = dict()
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in freq_of_word.keys():
                if sent not in sent_scores.keys():                            
                    sent_scores[sent]=freq_of_word[word.text.lower()]
                else:
                    sent_scores[sent]+=freq_of_word[word.text.lower()]
    
    
    len_tokens=int(len(sent_tokens)*percentage)
    
    summary = nlargest(n = len_tokens, iterable = sent_scores,key=sent_scores.get)    
    final_summary = [word.text for word in summary]    
    summary=" ".join(final_summary)    
    return summary



###################################################################################

MEDIAS = ['bmp_media1', 'bmp_media22']


def update_historique(id, text, extractiveSummary, abstractiveSummary, extractiveAudioBuffer, abstractiveAudioBuffer):
    xl_file = 'https://raw.githubusercontent.com/Taoufiq-Ouedraogo/pfe_brief_my_press_AI/main/Code/WEBAPI/ressources/historique_articles.xlsx'
    df = pd.read_excel(xl_file)

    new_data = pd.DataFrame([{'mediaID': 'id', 'article': 'text',
    'extractiveSummary': 'extractiveSummary', 'abstractiveSummary': 'abstractiveSummary',
    'extractiveAudioBuffer': 'extractiveAudioBuffer', 'abstractiveAudioBuffer': 'abstractiveAudioBuffer'}])
    
    df = pd.concat([df, new_data], ignore_index=True)




def bmp_summaries_and_audio(text, mediaID):
    assert mediaID in MEDIAS
    
    articleItem = ArticleItem(mediaID, text)
    extractiveSummary, abstractiveSummary = articleItem.get_summaries()
    extractiveAudioBuffer, abstractiveAudioBuffer = articleItem.get_audios()

    ## 
    update_historique(id, text, extractiveSummary, abstractiveSummary, extractiveAudioBuffer, abstractiveAudioBuffer)

    return {'extractiveSummary': extractiveSummary, 
            'abstractiveSummary': abstractiveSummary,
            'extractiveAudioBuffer': extractiveAudioBuffer, 
            'abstractiveAudioBuffer': abstractiveAudioBuffer}





###################################################################################


class ArticleItem:
    def __init__(self, mediaID, text, extr_model=spacyExtractiveSummarizer, abs_model=None):
        self.n = 0
        self.extractiveSummary = None
        self.abstractiveSummary = None

        self.extractiveAudioBuffer = None
        self.abstractiveAudioBuffer = None
        
        ######## Get Summaries ########
        if text and extr_model:
            self.extractiveSummary = extr_model(text)
        if text and abs_model:
            self.abstractiveSummary = abs_model(text)

        ######## Get Audios ########
        self.generate_extractiveSummaryAudio()
        self.generate_abstractiveSummaryAudio()


    #################### Getters ####################

    def get_summaries(self):
        return self.extractiveSummary, self.abstractiveSummary
    
    def get_audios(self):
        return self.extractiveAudioBuffer, self.abstractiveAudioBuffer
    
    #################### Summary to Audio ####################

    def generate_abstractiveSummaryAudio(self):
        filename = f'abstractiveAudio_{self.n}.mp3'
        audio_buffer = self.summary2speech(self.abstractiveSummary, filename=filename)
        if audio_buffer:
            self.abstractiveAudioBuffer = audio_buffer

    def generate_extractiveSummaryAudio(self):
        filename = f'extractiveAudio_{self.n}.mp3'
        audio_buffer = self.summary2speech(self.extractiveSummary, filename=filename)
        if audio_buffer:
            self.extractiveAudioBuffer = audio_buffer

    def summary2speech(self, text_, filename=None):
        if not text_:
            return None
        try:
            tts = gTTS(text_, lang='fr')
            if filename:
                #tts.save(filename)  # Sauvegarde l'audio dans un fichier
                
                audio_buffer = BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)  
                return audio_buffer
        except Exception as e:
            print(f"Une erreur est survenue : {e}")
            return None
    





