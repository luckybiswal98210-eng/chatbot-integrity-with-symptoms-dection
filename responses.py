import unicodedata
from googletrans import Translator

# English response dictionary
RESPONSES_EN = {
    "fever": "Please consult to doctor and stay hydrated.",
    "cough": "For cough, try honey and ginger tea. If severe, consult a doctor.",
    "cold": "Rest well, drink warm fluids, and consider saline nasal spray.",
    "headache": "Avoid bright lights; take ibuprofen if needed.",
    "diabetes": "Monitor blood sugar regularly; follow your doctor's instructions.",
    "hypertension": "Eat low sodium, exercise, and take prescribed meds.",
    "asthma": "Use inhaler as prescribed; avoid smoke and allergens.",
    "allergy": "Avoid allergens; take antihistamines prescribed by doctor.",
    "flu": "Rest, drink fluids, and use fever reducers if needed.",
    "stomach ache": "Eat light foods and stay hydrated; see doctor if severe.",
    "diarrhea": "Hydrate with oral rehydration solutions; avoid greasy foods.",
    "back pain": "Rest, apply heat, and do gentle stretches; consult specialist.",
    "depression": "Seek mental health support; counseling and medication help.",
    "anxiety": "Practice relaxation, mindfulness; seek professional help.",
    "arthritis": "Exercise joints gently; use anti-inflammatories as prescribed.",
    "bronchitis": "Avoid irritants; use medications as advised by doctor.",
    "bronchiectasis": "Follow respiratory therapy; take antibiotics as needed.",
    "anemia": "Eat iron-rich foods and take supplements as prescribed.",
    "urinary tract infection": "Drink lots of fluids; antibiotics may be needed.",
    "ear infection": "Use prescribed ear drops; keep ear dry.",
    "sinusitis": "Use decongestants and nasal sprays; rest well.",
    "skin rash": "Avoid irritants; use topical creams if advised.",
    "eczema": "Moisturize regularly; avoid triggers.",
    "psoriasis": "Use prescribed creams; manage stress.",
    "gastroenteritis": "Stay hydrated; follow diet; seek help if severe.",
    "constipation": "Increase fiber intake; drink water.",
    "insomnia": "Maintain sleep hygiene; consider counseling.",
    "migraine": "Avoid triggers; use medications prescribed.",
    "obesity": "Balanced diet and exercise; medical support if needed.",
    "thyroid disorder": "Take prescribed thyroid medications regularly.",
    "cholesterol": "Diet control, exercise; take meds if prescribed.",
    "osteoporosis": "Calcium, vitamin D; weight-bearing exercises.",
    "stroke": "Emergency care; follow rehab protocols.",
    "cancer": "Consult oncologist for treatment options.",
    "tuberculosis": "Complete prescribed antibiotic course.",
    "hepatitis": "Avoid alcohol; follow medical advice.",
    "HIV/AIDS": "Antiretroviral therapy and regular monitoring.",
    "malaria": "Complete antimalarial treatment; prevent mosquito bites.",
    "chickenpox": "Relieve itch; isolate to prevent spread.",
    "measles": "Supportive care; isolate to prevent spread.",
    "dengue": "Hydrate and rest; seek hospital if severe.",
    "zika virus": "Prevent mosquito bites; symptomatic treatment.",
    "polio": "Vaccination is preventive; supportive care.",
    "rabies": "Post-exposure prophylaxis immediately.",
    "typhoid": "Complete antibiotic course.",
    "cholera": "Oral rehydration and antibiotics if needed.",
    "hospital": "Nearest hospital is City Health Center, contact: 1234567890.",
    "doctor": "Dr. Sharma is available at 9876543210.",
    "default": "Sorry, I didn't understand. Please consult your healthcare provider."
}

# Multilingual input keywords mapped to English keys
INPUT_KEYWORDS = {
    'hi': {
        "बुखार": "fever",
        "फ़ीवर": "fever",
        "खांसी": "cough",
        "कफ़": "cough",
        "जुकाम": "cold",
        "सर्दी": "cold",
        "सिरदर्द": "headache",
        "मधुमेह": "diabetes",
        "शुगर": "diabetes",
        "उच्च रक्तचाप": "hypertension",
        "ब्लड प्रेशर": "hypertension",
        "दमा": "asthma",
        "एलर्जी": "allergy",
        "फ्लू": "flu",
        "पेट दर्द": "stomach ache",
        "दस्त": "diarrhea",
        "पीठ दर्द": "back pain",
        "अवसाद": "depression",
        "चिंता": "anxiety",
        "गठिया": "arthritis",
    },
    'ta': {
        "காய்ச்சல்": "fever",
        "படர்ப்பு": "cough",
        "காய்ச்சல் மற்றும் போது குளிர்ச்சி": "cold",
        "தலைவலி": "headache",
        "பருமன் நீர் சர்க்கரை": "diabetes",
        "உயர் இரத்த அழுத்தம்": "hypertension",
        "அஸ்துமா": "asthma",
        "அலெர்ஜி": "allergy",
    },
    'te': {
        "జ్వరం": "fever",
        "చప్పుడు": "cough",
        "జలుబు": "cold",
        "తలనొప్పి": "headache",
        "మధుమేహం": "diabetes",
        "ఉన్నత రక్తపోటు": "hypertension",
        "దమ": "asthma",
        "అలర్జీ": "allergy",
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
    },
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


def detect_symptom(user_input, lang_code='en'):
    """Detect symptom from user input."""
    normalized = unicodedata.normalize('NFC', user_input).lower()
    
    # Try language-specific keywords first
    if lang_code in INPUT_KEYWORDS:
        keywords_map = INPUT_KEYWORDS[lang_code]
        for local_word, eng_key in keywords_map.items():
            if local_word in normalized:
                return eng_key
    
    # Try translating to English and matching
    try:
        translated = translator.translate(normalized, dest='en')
        translated_text = (translated.text or normalized).lower()
        
        for key in RESPONSES_EN.keys():
            if key in translated_text:
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
    
    # Stage 1: Initial symptom detection
    if session['stage'] == 'initial':
        symptom = detect_symptom(user_input, lang_code)
        
        if symptom and symptom != 'default':
            conversation_state.update_session(
                session_id,
                symptom=symptom,
                stage='ask_duration'
            )
            response = f"I understand you're experiencing {symptom}. How long have you been experiencing this symptom? (e.g., a few hours, 2 days, a week)"
            return translate_text(response, lang_code)
        else:
            response = "I'm here to help with your health concerns. Could you please describe your main symptom? (e.g., fever, cough, headache)"
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
        personalized_response = f"Based on your {symptom} for {duration} with severity {severity}"
        
        if additional.lower() not in ['none', 'no', 'नहीं', 'இல்லை', 'లేదు', 'ಇಲ್ಲ']:
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
    response = "I'm here to help. Please describe your symptom."
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
