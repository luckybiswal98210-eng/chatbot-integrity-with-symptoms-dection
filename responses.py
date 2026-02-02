import unicodedata
from googletrans import Translator

# English response dictionary - Comprehensive health advice
RESPONSES_EN = {
    "fever": "Rest well, drink plenty of water or oral rehydration fluids, and consult a doctor if fever is high or lasts more than a few days.",
    "cough": "Try honey with warm water or ginger tea to soothe the throat, and consult a doctor if cough is severe or persistent.",
    "cold": "Rest properly, drink warm fluids like soup or herbal tea, and consider saline nasal spray for congestion.",
    "headache": "Rest in a quiet place, avoid bright lights, stay hydrated, and see a doctor if pain is severe or frequent.",
    "migraine": "Rest in a dark, quiet room, use a cold compress on the forehead, and seek medical care if attacks are frequent.",
    "sinusitis": "Steam inhalation and warm fluids may help relieve pressure; consult a doctor if facial pain or fever occurs.",
    "sore_throat": "Gargle with warm salt water and drink warm fluids like tea or soup; see a doctor if swallowing is painful.",
    "flu": "Get enough rest, drink fluids regularly, and consult a doctor if weakness or fever worsens.",
    "asthma": "Avoid smoke and allergens, use inhalers as prescribed, and seek medical help if breathing becomes difficult.",
    "allergy": "Avoid known triggers, keep surroundings clean, and consult a doctor if symptoms worsen.",
    "bronchitis": "Rest well, drink warm fluids, avoid smoke, and follow doctor-recommended treatment if symptoms persist.",
    "pneumonia": "Seek medical care promptly, rest adequately, and follow professional treatment guidance.",
    "stomach_ache": "Eat light foods, drink water, and consult a doctor if pain is severe or persistent.",
    "indigestion": "Eat smaller meals, avoid spicy food, and drink warm water; see a doctor if discomfort continues.",
    "acidity": "Avoid oily or spicy foods, drink warm water, and consult a doctor if symptoms are frequent.",
    "diarrhea": "Prevent dehydration by drinking oral rehydration solution and water, and avoid greasy foods.",
    "constipation": "Increase fiber intake, drink plenty of water, and stay physically active.",
    "vomiting": "Take small sips of water or ORS and seek medical care if vomiting continues.",
    "nausea": "Rest, avoid strong smells, and sip ginger tea or warm water.",
    "food_poisoning": "Rest, drink ORS and water, and consult a doctor if fever or blood in stool appears.",
    "diabetes": "Monitor blood sugar regularly, follow a healthy diet, and follow your doctor's instructions.",
    "hypertension": "Reduce salt intake, exercise regularly, manage stress, and follow medical advice.",
    "low_blood_pressure": "Drink fluids, rise slowly from sitting, and consult a doctor if dizziness occurs.",
    "chest_pain": "Rest immediately and seek urgent medical care, especially if pain is severe or spreading.",
    "back_pain": "Rest the back, maintain good posture, apply heat if helpful, and consult a doctor if pain persists.",
    "neck_pain": "Avoid strain, do gentle stretches, and use a warm compress if needed.",
    "joint_pain": "Rest affected joints, do gentle movement, and consult a doctor if swelling occurs.",
    "arthritis": "Keep joints active with gentle exercise and follow medical guidance for pain management.",
    "muscle_pain": "Rest the muscle, apply warm compress, and hydrate well.",
    "leg_cramps": "Stretch gently and drink enough water throughout the day.",
    "fatigue": "Ensure adequate sleep, eat balanced meals, and stay hydrated.",
    "dehydration": "Drink water, oral rehydration solution, or coconut water and seek care if symptoms worsen.",
    "dizziness": "Sit or lie down safely, drink fluids, and consult a doctor if fainting occurs.",
    "anxiety": "Practice deep breathing and relaxation techniques, and seek professional help if anxiety interferes with daily life.",
    "depression": "Seek mental health support, talk to a trusted person, and consult a professional for proper care.",
    "stress": "Take breaks, practice relaxation techniques, and maintain a balanced routine.",
    "insomnia": "Maintain a regular sleep schedule, reduce screen time at night, and seek help if sleeplessness continues.",
    "skin_rash": "Keep the area clean and dry, avoid irritants, and consult a doctor if rash spreads.",
    "itching": "Avoid scratching, apply soothing lotion, and seek care if itching is severe.",
    "fungal_infection": "Keep the area dry and clean, and consult a doctor if infection spreads.",
    "ear_pain": "Avoid water entry into the ear and consult a doctor if pain or discharge occurs.",
    "eye_strain": "Rest your eyes, reduce screen time, and use proper lighting.",
    "toothache": "Rinse the mouth with warm salt water, avoid hard foods, and see a dentist if pain persists.",
    "mouth_ulcer": "Avoid spicy foods, rinse with salt water, and consult a doctor if ulcers last more than two weeks.",
    "bad_breath": "Maintain oral hygiene, drink water frequently, and consult a dentist if the problem continues.",
    "hospital": "Nearest hospital is City Health Center, contact: 1234567890.",
    "doctor": "Dr. Sharma is available at 9876543210.",
    "default": "I'm sorry, I didn't quite understand that. Could you please describe your symptom differently?"
}

# Multilingual input keywords mapped to English keys
INPUT_KEYWORDS = {
    'hi': {
        "बुखार": "fever", "फ़ीवर": "fever",
        "खांसी": "cough", "कफ़": "cough",
        "जुकाम": "cold", "सर्दी": "cold",
        "सिरदर्द": "headache",
        "मधुमेह": "diabetes", "शुगर": "diabetes",
        "उच्च रक्तचाप": "hypertension", "ब्लड प्रेशर": "hypertension",
        "दमा": "asthma",
        "एलर्जी": "allergy",
        "फ्लू": "flu",
        "पेट दर्द": "stomach_ache",
        "दस्त": "diarrhea",
        "पीठ दर्द": "back_pain",
        "अवसाद": "depression",
        "चिंता": "anxiety",
        "गठिया": "arthritis",
        "धन्यवाद": "thank_you",
        "शुक्रिया": "thank_you",
        "ठीक है": "okay",
        "अस्पताल": "hospital",
        "डॉक्टर": "doctor",
    },
    'ta': {
        "காய்ச்சல்": "fever",
        "படர்ப்பு": "cough",
        "குளிர்ச்சி": "cold",
        "தலைவலி": "headache",
        "சர்க்கரை": "diabetes",
        "உயர் இரத்த அழுத்தம்": "hypertension",
        "அஸ்துமா": "asthma",
        "அலெர்ஜி": "allergy",
        "நன்றி": "thank_you",
        "சரி": "okay",
        "மருத்துவமனை": "hospital",
        "மருத்துவர்": "doctor",
    },
    'te': {
        "జ్వరం": "fever",
        "చప్పుడు": "cough",
        "జలుబు": "cold",
        "తలనొప్పి": "headache",
        "మధుమేహం": "diabetes",
        "రక్తపోటు": "hypertension",
        "దమ": "asthma",
        "అలర్జీ": "allergy",
        "ధన్యవాదాలు": "thank_you",
        "సరే": "okay",
        "హాస్పిటల్": "hospital",
        "డాక్టర్": "doctor",
    },
    'kn': {
        "ಜ್ವರ": "fever",
        "ತಸು": "cough",
        "ಜರಳು": "cold",
        "ತಲೆಯನೋವು": "headache",
        "ಮಧುಮೇಹ": "diabetes",
        "ಹೈಪರ್ಟೆನ್ಷನ್": "hypertension",
        "ಅಸ್ಥಮಾ": "asthma",
        "ಅಲರ್ಜಿ": "allergy",
        "ಧನ್ಯವಾದ": "thank_you",
        "ಸರಿ": "okay",
        "ಆಸ್ಪತ್ರೆ": "hospital",
        "ಡಾಕ್ಟರ್": "doctor",
    },
}

# Closing/Thank you responses
CLOSING_RESPONSES = {
    "thank_you": "You're welcome! Take care of your health. Feel free to ask if you have any other health concerns.",
    "okay": "Alright! I hope the advice helps. Stay healthy and don't hesitate to reach out if you need more help.",
    "bye": "Goodbye! Wishing you good health. Come back anytime you need health advice.",
    "thanks": "You're welcome! Take care and stay healthy!",
}

translator = Translator()

# Conversation state management
class ConversationState:
    def __init__(self):
        self.sessions = {}
    
    def get_session(self, session_id):
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                'stage': 'initial',
                'symptom': None,
                'duration': None,
                'severity': None,
                'additional_symptoms': None,
                'language': 'en'
            }
        return self.sessions[session_id]
    
    def update_session(self, session_id, **kwargs):
        session = self.get_session(session_id)
        session.update(kwargs)
        return session
    
    def reset_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

# Global conversation state
conversation_state = ConversationState()


def translate_text(text, target_lang='en'):
    """Translate text to target language."""
    if not text or target_lang == 'en':
        return text
    try:
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text


def detect_closing_statement(user_input, lang_code='en'):
    """Detect if user is saying thank you, okay, bye, etc."""
    normalized = user_input.lower().strip()
    
    # English closing keywords
    closing_keywords = [
        'thank you', 'thanks', 'thankyou', 'thank u', 'thnx', 'thx',
        'ok', 'okay', 'alright', 'got it', 'understood',
        'bye', 'goodbye', 'see you', 'take care'
    ]
    
    # Check if input matches closing keywords
    for keyword in closing_keywords:
        if keyword in normalized:
            return True
    
    # Check language-specific keywords
    if lang_code in INPUT_KEYWORDS:
        keywords_map = INPUT_KEYWORDS[lang_code]
        for local_word, eng_key in keywords_map.items():
            if local_word in normalized and eng_key in ['thank_you', 'okay', 'bye']:
                return True
    
    return False


def detect_symptom(user_input, lang_code='en'):
    """Detect symptom from user input."""
    normalized = unicodedata.normalize('NFC', user_input).lower()
    
    # Try language-specific keywords first
    if lang_code in INPUT_KEYWORDS:
        keywords_map = INPUT_KEYWORDS[lang_code]
        for local_word, eng_key in keywords_map.items():
            if local_word in normalized and eng_key in RESPONSES_EN:
                return eng_key
    
    # Try translating to English and matching
    try:
        translated = translator.translate(normalized, dest='en')
        translated_text = (translated.text or normalized).lower()
        
        for key in RESPONSES_EN.keys():
            if key in translated_text or key.replace('_', ' ') in translated_text:
                return key
    except Exception:
        pass
    
    return None


def get_conversational_response(user_input, session_id, lang_code='en'):
    """
    Generate conversational response based on conversation state.
    Asks follow-up questions before providing final advice.
    """
    session = conversation_state.get_session(session_id)
    session['language'] = lang_code
    
    normalized_input = user_input.lower().strip()
    
    # Check if user is saying thank you or closing the conversation
    if detect_closing_statement(user_input, lang_code):
        # Randomly select a closing response
        import random
        closing_msg = random.choice(list(CLOSING_RESPONSES.values()))
        # Reset session for next conversation
        conversation_state.reset_session(session_id)
        return translate_text(closing_msg, lang_code)
    
    # Stage 1: Initial symptom detection
    if session['stage'] == 'initial':
        symptom = detect_symptom(user_input, lang_code)
        
        if symptom and symptom in RESPONSES_EN and symptom not in ['default', 'hospital', 'doctor']:
            conversation_state.update_session(
                session_id,
                symptom=symptom,
                stage='ask_duration'
            )
            response = f"I understand you're experiencing {symptom.replace('_', ' ')}. How long have you been experiencing this symptom? (e.g., a few hours, 2 days, a week)"
            return translate_text(response, lang_code)
        elif symptom in ['hospital', 'doctor']:
            # Direct information request
            response = RESPONSES_EN.get(symptom, RESPONSES_EN['default'])
            return translate_text(response, lang_code)
        else:
            # Symptom not found in database
            response = "I'm sorry, but information about that specific symptom is currently unavailable in my database. I'm continuously being updated with more health information. For now, I recommend consulting a healthcare professional for personalized advice. Is there another symptom I can help you with?"
            return translate_text(response, lang_code)
    
    # Stage 2: Ask about duration
    elif session['stage'] == 'ask_duration':
        conversation_state.update_session(
            session_id,
            duration=user_input,
            stage='ask_severity'
        )
        response = "Thank you. On a scale of 1-10, how severe is your symptom? (1 = mild, 10 = very severe)"
        return translate_text(response, lang_code)
    
    # Stage 3: Ask about severity
    elif session['stage'] == 'ask_severity':
        conversation_state.update_session(
            session_id,
            severity=user_input,
            stage='ask_additional'
        )
        response = "Are you experiencing any additional symptoms? (e.g., nausea, fatigue, body aches) Or say 'none' if you don't have any."
        return translate_text(response, lang_code)
    
    # Stage 4: Ask about additional symptoms and provide final advice
    elif session['stage'] == 'ask_additional':
        conversation_state.update_session(
            session_id,
            additional_symptoms=user_input,
            stage='complete'
        )
        
        # Generate personalized response
        symptom = session['symptom']
        duration = session['duration']
        severity = session['severity']
        additional = user_input
        
        base_advice = RESPONSES_EN.get(symptom, RESPONSES_EN['default'])
        
        # Create personalized response
        personalized_response = f"Based on your {symptom.replace('_', ' ')} for {duration} with severity {severity}"
        
        if additional.lower() not in ['none', 'no', 'नहीं', 'இல்லை', 'లేదు', 'ಇಲ್ಲ', 'না']:
            personalized_response += f" and additional symptoms ({additional})"
        
        personalized_response += f", here's my advice:\n\n{base_advice}"
        
        # Add urgency note based on severity
        try:
            severity_num = int(''.join(filter(str.isdigit, severity)) or '5')
            if severity_num >= 8:
                personalized_response += "\n\n⚠️ Given the high severity, I strongly recommend seeking immediate medical attention."
            elif severity_num >= 6:
                personalized_response += "\n\n⚠️ Please consider consulting a doctor soon."
        except:
            pass
        
        personalized_response += "\n\nWould you like to ask about another symptom? (Type 'yes' to start over or describe a new symptom)"
        
        # Reset for next conversation
        conversation_state.update_session(session_id, stage='initial')
        
        return translate_text(personalized_response, lang_code)
    
    # Fallback
    response = "I'm here to help with your health concerns. Please describe your symptom, or say 'thank you' if you're done."
    return translate_text(response, lang_code)


def get_response(user_input, lang_code='en', session_id='default'):
    """
    Main entry point for getting chatbot response.
    Now supports conversational flow with session management.
    """
    if not user_input:
        return RESPONSES_EN.get("default")
    
    return get_conversational_response(user_input, session_id, lang_code)


def reset_conversation(session_id):
    """Reset conversation for a given session."""
    conversation_state.reset_session(session_id)
    return "Conversation reset. How can I help you today?"
