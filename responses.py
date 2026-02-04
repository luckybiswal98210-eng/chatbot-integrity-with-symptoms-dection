import unicodedata
from googletrans import Translator

# English response dictionary - Comprehensive health advice
RESPONSES_EN = {
    # Fever-related conditions
    "fever": "Rest well, drink plenty of water or oral rehydration fluids, and consult a doctor if fever is high or lasts more than a few days.",
    "dengue": "⚠️ Dengue requires immediate medical attention. Rest completely, drink plenty of fluids (ORS, coconut water), monitor platelet count, avoid painkillers like aspirin or ibuprofen. Watch for warning signs: severe abdominal pain, persistent vomiting, bleeding gums, or difficulty breathing. Seek emergency care immediately if these occur.",
    "malaria": "⚠️ Seek immediate medical care for proper diagnosis and antimalarial treatment. Rest well, stay hydrated, and take prescribed medications on time. Prevent mosquito bites by using nets and repellents.",
    "typhoid": "⚠️ Consult a doctor immediately for antibiotics. Rest completely, drink plenty of safe water, eat light easily digestible foods. Maintain strict hygiene to prevent spreading. Complete the full course of antibiotics even if you feel better.",
    "chikungunya": "Rest adequately, drink plenty of fluids, use prescribed pain relievers for joint pain. Avoid mosquito bites. Joint pain may persist for weeks; gentle exercises may help recovery. Consult a doctor for proper management.",
    
    # Respiratory conditions
    "cough": "Try honey with warm water or ginger tea to soothe the throat, and consult a doctor if cough is severe or persistent.",
    "cold": "Rest properly, drink warm fluids like soup or herbal tea, and consider saline nasal spray for congestion.",
    "flu": "Get enough rest, drink fluids regularly, and consult a doctor if weakness or fever worsens.",
    "asthma": "Avoid smoke and allergens, use inhalers as prescribed, and seek medical help if breathing becomes difficult.",
    "bronchitis": "Rest well, drink warm fluids, avoid smoke, and follow doctor-recommended treatment if symptoms persist.",
    "pneumonia": "⚠️ Seek medical care promptly, rest adequately, and follow professional treatment guidance. Take prescribed antibiotics completely.",
    "tuberculosis": "⚠️ Critical: Follow the complete 6-9 month treatment course without missing doses. Cover your mouth when coughing, maintain good ventilation, eat nutritious food, and attend all follow-up appointments. TB is curable with proper treatment.",
    "covid": "Isolate immediately, rest well, monitor oxygen levels, stay hydrated. Consult a doctor if breathing difficulty, persistent chest pain, or oxygen drops below 94%. Get vaccinated when eligible. Follow local health guidelines.",
    "sore_throat": "Gargle with warm salt water and drink warm fluids like tea or soup; see a doctor if swallowing is painful.",
    
    # Digestive issues
    "stomach_ache": "Eat light foods, drink water, and consult a doctor if pain is severe or persistent.",
    "indigestion": "Eat smaller meals, avoid spicy food, and drink warm water; see a doctor if discomfort continues.",
    "acidity": "Avoid oily or spicy foods, drink warm water, and consult a doctor if symptoms are frequent.",
    "gastritis": "Eat small frequent meals, avoid spicy and acidic foods, don't skip meals, reduce stress. Consult a doctor if pain persists or you see blood in vomit/stool.",
    "gerd": "Avoid lying down immediately after meals, elevate head while sleeping, eat smaller portions, avoid trigger foods (spicy, fatty, citrus). Consult a doctor for persistent symptoms.",
    "ulcer": "⚠️ Consult a doctor for proper diagnosis and treatment. Avoid NSAIDs, alcohol, and smoking. Eat regular meals, manage stress, and complete prescribed medication course.",
    "diarrhea": "Prevent dehydration by drinking oral rehydration solution and water, and avoid greasy foods.",
    "constipation": "Increase fiber intake, drink plenty of water, and stay physically active.",
    "vomiting": "Take small sips of water or ORS and seek medical care if vomiting continues.",
    "nausea": "Rest, avoid strong smells, and sip ginger tea or warm water.",
    "food_poisoning": "Rest, drink ORS and water, and consult a doctor if fever or blood in stool appears.",
    
    # Infections
    "uti": "Drink plenty of water (8-10 glasses daily), urinate frequently, avoid holding urine. Consult a doctor for antibiotics. Avoid caffeine and alcohol. Women should wipe front to back. Complete the full antibiotic course.",
    "kidney_stones": "⚠️ Drink lots of water (3-4 liters daily), consult a doctor for pain management and treatment. Avoid high-oxalate foods if advised. Seek immediate care for severe pain, fever, or blood in urine.",
    "chickenpox": "Isolate to prevent spreading, keep skin clean, avoid scratching (trim nails), apply calamine lotion for itching. Stay hydrated, rest well. Consult a doctor if fever is very high or breathing difficulty occurs.",
    "measles": "Isolate immediately, rest in a dark room (light sensitivity), drink fluids, manage fever. ⚠️ Consult a doctor as complications can be serious. Vaccination prevents measles.",
    "mumps": "Rest well, apply warm/cold compress to swollen areas, eat soft foods, drink plenty of fluids. Isolate to prevent spreading. Consult a doctor if severe headache or abdominal pain occurs.",
    
    # Chronic conditions
    "diabetes": "Monitor blood sugar regularly, follow a healthy diet, exercise daily, take medications on time. Regular check-ups are essential. Maintain healthy weight and manage stress.",
    "hypertension": "Reduce salt intake, exercise regularly, manage stress, avoid smoking and alcohol, take medications as prescribed. Monitor BP regularly and attend follow-ups.",
    "thyroid": "Take thyroid medication on empty stomach at the same time daily. Regular blood tests to monitor levels. Eat balanced diet, manage stress. Consult endocrinologist for proper management.",
    "anemia": "Eat iron-rich foods (spinach, dates, jaggery, meat), take iron supplements if prescribed, include vitamin C for better absorption. Rest adequately. Consult a doctor to identify the cause.",
    
    # Pain and musculoskeletal
    "headache": "Rest in a quiet place, avoid bright lights, stay hydrated, and see a doctor if pain is severe or frequent.",
    "migraine": "Rest in a dark, quiet room, use a cold compress on the forehead, and seek medical care if attacks are frequent.",
    "sinusitis": "Steam inhalation and warm fluids may help relieve pressure; consult a doctor if facial pain or fever occurs.",
    "chest_pain": "⚠️ Rest immediately and seek urgent medical care, especially if pain is severe or spreading.",
    "back_pain": "Rest the back, maintain good posture, apply heat if helpful, and consult a doctor if pain persists.",
    "neck_pain": "Avoid strain, do gentle stretches, and use a warm compress if needed.",
    "joint_pain": "Rest affected joints, do gentle movement, and consult a doctor if swelling occurs.",
    "arthritis": "Keep joints active with gentle exercise and follow medical guidance for pain management.",
    "muscle_pain": "Rest the muscle, apply warm compress, and hydrate well.",
    "leg_cramps": "Stretch gently and drink enough water throughout the day.",
    
    # Mental health
    "anxiety": "Practice deep breathing and relaxation techniques, and seek professional help if anxiety interferes with daily life.",
    "depression": "Seek mental health support, talk to a trusted person, and consult a professional for proper care.",
    "stress": "Take breaks, practice relaxation techniques, and maintain a balanced routine.",
    "insomnia": "Maintain a regular sleep schedule, reduce screen time at night, and seek help if sleeplessness continues.",
    
    # Skin conditions
    "skin_rash": "Keep the area clean and dry, avoid irritants, and consult a doctor if rash spreads.",
    "itching": "Avoid scratching, apply soothing lotion, and seek care if itching is severe.",
    "fungal_infection": "Keep the area dry and clean, and consult a doctor if infection spreads.",
    "eczema": "Moisturize regularly, avoid triggers (harsh soaps, stress), use prescribed creams. Keep skin hydrated and avoid scratching.",
    "psoriasis": "Keep skin moisturized, avoid triggers (stress, infections), follow prescribed treatment. Sunlight in moderation may help. Consult dermatologist for management.",
    
    # Other conditions
    "allergy": "Avoid known triggers, keep surroundings clean, and consult a doctor if symptoms worsen.",
    "fatigue": "Ensure adequate sleep, eat balanced meals, and stay hydrated.",
    "dehydration": "Drink water, oral rehydration solution, or coconut water and seek care if symptoms worsen.",
    "dizziness": "Sit or lie down safely, drink fluids, and consult a doctor if fainting occurs.",
    "low_blood_pressure": "Drink fluids, rise slowly from sitting, and consult a doctor if dizziness occurs.",
    "ear_pain": "Avoid water entry into the ear and consult a doctor if pain or discharge occurs.",
    "eye_strain": "Rest your eyes, reduce screen time, and use proper lighting.",
    "toothache": "Rinse the mouth with warm salt water, avoid hard foods, and see a dentist if pain persists.",
    "mouth_ulcer": "Avoid spicy foods, rinse with salt water, and consult a doctor if ulcers last more than two weeks.",
    "bad_breath": "Maintain oral hygiene, drink water frequently, and consult a dentist if the problem continues.",
    
    # Information
    "hospital": "Nearest hospital is City Health Center, contact: 1234567890.",
    "doctor": "Dr. Sharma is available at 9876543210.",
    "default": "I'm sorry, I didn't quite understand that. Could you please describe your symptom differently?"
}

# Symptom-to-Disease Mapping - Maps symptoms to possible conditions
SYMPTOM_DISEASE_MAP = {
    "high_temperature": ["fever", "dengue", "malaria", "typhoid", "flu", "covid", "chikungunya"],
    "body_aches": ["dengue", "flu", "malaria", "chikungunya", "covid"],
    "rash": ["dengue", "chickenpox", "measles", "allergy", "eczema"],
    "severe_headache": ["migraine", "dengue", "malaria", "sinusitis", "hypertension"],
    "joint_pain": ["chikungunya", "dengue", "arthritis"],
    "abdominal_pain": ["gastritis", "food_poisoning", "ulcer", "typhoid", "dengue"],
    "nausea_vomiting": ["food_poisoning", "gastritis", "migraine", "dengue", "typhoid"],
    "breathing_difficulty": ["asthma", "covid", "pneumonia", "anxiety"],
    "chest_pain": ["chest_pain", "gerd", "anxiety"],
    "persistent_cough": ["tuberculosis", "covid", "bronchitis", "asthma"],
    "burning_urination": ["uti", "kidney_stones"],
    "skin_spots": ["chickenpox", "measles", "dengue"],
    "weakness": ["anemia", "dengue", "typhoid", "diabetes"],
    "bleeding": ["dengue"],
}

# Diagnostic Questions - Context-aware questions based on initial symptoms
DIAGNOSTIC_QUESTIONS = {
    "high_temperature": [
        "Do you have any rash or red spots on your skin?",
        "Are you experiencing severe body aches or joint pain?",
        "Have you traveled to any tropical or mosquito-prone areas recently?",
        "Do you have a headache, especially behind your eyes?",
        "Are you experiencing nausea or vomiting?"
    ],
    "body_aches": [
        "Do you have fever along with the body aches?",
        "Are your joints particularly painful or swollen?",
        "Do you have any rash or skin changes?",
        "Have you been bitten by mosquitoes recently?"
    ],
    "abdominal_pain": [
        "Where exactly is the pain located? (upper, lower, left, right)",
        "Is the pain constant or does it come and go?",
        "Do you have nausea, vomiting, or diarrhea?",
        "Have you eaten anything unusual or outside food recently?",
        "Do you have fever along with the pain?"
    ],
    "cough": [
        "Is your cough dry or are you coughing up mucus?",
        "Do you have fever or difficulty breathing?",
        "Have you been coughing for more than 2 weeks?",
        "Do you have chest pain when coughing?",
        "Have you been in contact with anyone who has COVID-19 or TB?"
    ],
    "rash": [
        "Is the rash itchy or painful?",
        "Do you have fever along with the rash?",
        "Are there fluid-filled blisters or just red spots?",
        "Is the rash spreading rapidly?"
    ],
    "headache": [
        "Is the headache on one side or both sides?",
        "Do you have sensitivity to light or sound?",
        "Do you have nausea or vomiting with the headache?",
        "Do you have fever or neck stiffness?"
    ],
    "breathing_difficulty": [
        "Do you have a history of asthma or allergies?",
        "Do you have fever or cough?",
        "Are you experiencing chest pain or tightness?",
        "Have you been in contact with COVID-19 positive individuals?"
    ],
    "burning_urination": [
        "Do you need to urinate more frequently than usual?",
        "Do you have lower abdominal pain?",
        "Is there any blood in your urine?",
        "Do you have fever or back pain?"
    ],
    "weakness": [
        "Do you feel dizzy or lightheaded?",
        "Have you noticed pale skin or pale nails?",
        "Do you have fever or other symptoms?",
        "Are you eating properly and staying hydrated?"
    ]
}

# Multilingual input keywords mapped to English keys
INPUT_KEYWORDS = {
    'hi': {
        "बुखार": "fever", "फ़ीवर": "fever", "तेज बुखार": "fever",
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
        "डेंगू": "dengue",
        "मलेरिया": "malaria",
        "टाइफाइड": "typhoid",
        "चिकनगुनिया": "chikungunya",
        "गैस्ट्राइटिस": "gastritis",
        "यूटीआई": "uti",
        "चिकनपॉक्स": "chickenpox",
        "खसरा": "measles",
        "कोविड": "covid",
        "टीबी": "tuberculosis",
        "एनीमिया": "anemia",
        "थायराइड": "thyroid",
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
        "டெங்கு": "dengue",
        "மலேரியா": "malaria",
        "டைபாய்டு": "typhoid",
        "கோவிட்": "covid",
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
        "డెంగ్యూ": "dengue",
        "మలేరియా": "malaria",
        "టైఫాయిడ్": "typhoid",
        "కోవిడ్": "covid",
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
        "ಡೆಂಗ್ಯೂ": "dengue",
        "ಮಲೇರಿಯಾ": "malaria",
        "ಟೈಫಾಯಿಡ್": "typhoid",
        "ಕೋವಿಡ್": "covid",
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


def categorize_symptom(symptom_text):
    """Categorize symptom into broader categories for diagnostic questions."""
    symptom_lower = symptom_text.lower()
    
    # Map specific symptoms to categories
    if any(word in symptom_lower for word in ['fever', 'temperature', 'hot', 'burning up', 'तेज बुखार', 'बुखार']):
        return 'high_temperature'
    elif any(word in symptom_lower for word in ['body ache', 'body pain', 'muscle pain', 'joint pain']):
        return 'body_aches'
    elif any(word in symptom_lower for word in ['rash', 'spots', 'skin', 'red marks']):
        return 'rash'
    elif any(word in symptom_lower for word in ['stomach', 'abdominal', 'belly', 'tummy', 'पेट']):
        return 'abdominal_pain'
    elif any(word in symptom_lower for word in ['cough', 'coughing', 'खांसी']):
        return 'cough'
    elif any(word in symptom_lower for word in ['headache', 'head pain', 'सिरदर्द']):
        return 'headache'
    elif any(word in symptom_lower for word in ['breath', 'breathing', 'suffocate']):
        return 'breathing_difficulty'
    elif any(word in symptom_lower for word in ['urine', 'urination', 'pee', 'burning']):
        return 'burning_urination'
    elif any(word in symptom_lower for word in ['weak', 'tired', 'fatigue', 'exhausted']):
        return 'weakness'
    
    return None


def analyze_symptoms(collected_responses):
    """Analyze collected symptom responses to suggest possible conditions."""
    possible_conditions = set()
    confidence_scores = {}
    
    # Check each response for symptom indicators
    for response in collected_responses:
        response_lower = response.lower()
        
        # Check for specific symptom mentions
        if any(word in response_lower for word in ['yes', 'हां', 'हाँ', 'yeah', 'yep']):
            # Positive response - check what symptom was being asked about
            for symptom_category, diseases in SYMPTOM_DISEASE_MAP.items():
                for disease in diseases:
                    if disease not in confidence_scores:
                        confidence_scores[disease] = 0
                    confidence_scores[disease] += 1
        
        # Direct symptom detection
        for symptom_category, diseases in SYMPTOM_DISEASE_MAP.items():
            if any(word in response_lower for word in symptom_category.split('_')):
                for disease in diseases:
                    possible_conditions.add(disease)
                    if disease not in confidence_scores:
                        confidence_scores[disease] = 0
                    confidence_scores[disease] += 2
    
    # Sort by confidence
    sorted_conditions = sorted(confidence_scores.items(), key=lambda x: x[1], reverse=True)
    
    return [condition for condition, score in sorted_conditions[:3]]  # Top 3 conditions


def get_diagnostic_questions(symptom_category):
    """Get relevant diagnostic questions based on symptom category."""
    return DIAGNOSTIC_QUESTIONS.get(symptom_category, [])


def suggest_conditions(primary_symptom, diagnostic_answers):
    """Suggest possible conditions based on primary symptom and diagnostic answers."""
    # Categorize the primary symptom
    symptom_category = categorize_symptom(primary_symptom)
    
    if not symptom_category or symptom_category not in SYMPTOM_DISEASE_MAP:
        return []
    
    # Get base possible conditions
    possible_conditions = SYMPTOM_DISEASE_MAP[symptom_category].copy()
    confidence_scores = {condition: 1 for condition in possible_conditions}
    
    # Analyze diagnostic answers to refine suggestions
    for answer in diagnostic_answers:
        answer_lower = answer.lower()
        
        # Positive indicators
        if any(word in answer_lower for word in ['yes', 'yeah', 'yep', 'हां', 'हाँ', 'ஆம்', 'అవును', 'ಹೌದು']):
            # Check for specific symptom mentions in the answer
            if 'rash' in answer_lower or 'spots' in answer_lower:
                for condition in ['dengue', 'chickenpox', 'measles']:
                    if condition in confidence_scores:
                        confidence_scores[condition] += 2
            
            if 'body ache' in answer_lower or 'joint pain' in answer_lower:
                for condition in ['dengue', 'chikungunya', 'flu']:
                    if condition in confidence_scores:
                        confidence_scores[condition] += 2
            
            if 'vomit' in answer_lower or 'nausea' in answer_lower:
                for condition in ['dengue', 'typhoid', 'food_poisoning']:
                    if condition in confidence_scores:
                        confidence_scores[condition] += 1
            
            if 'mosquito' in answer_lower or 'travel' in answer_lower:
                for condition in ['dengue', 'malaria', 'chikungunya']:
                    if condition in confidence_scores:
                        confidence_scores[condition] += 2
            
            if 'headache' in answer_lower and 'eye' in answer_lower:
                if 'dengue' in confidence_scores:
                    confidence_scores['dengue'] += 2
    
    # Sort by confidence and return top 3
    sorted_conditions = sorted(confidence_scores.items(), key=lambda x: x[1], reverse=True)
    return [condition for condition, score in sorted_conditions[:3] if score > 1]


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
            # Initialize diagnostic answers list
            conversation_state.update_session(
                session_id,
                symptom=symptom,
                stage='ask_duration',
                diagnostic_answers=[]
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
            stage='ask_diagnostic'
        )
        
        # Get diagnostic questions based on symptom
        symptom_category = categorize_symptom(session['symptom'])
        diagnostic_questions = get_diagnostic_questions(symptom_category) if symptom_category else []
        
        if diagnostic_questions:
            conversation_state.update_session(
                session_id,
                diagnostic_questions=diagnostic_questions,
                current_question_index=0
            )
            response = f"To better understand your condition, I'll ask a few specific questions.\n\n{diagnostic_questions[0]}"
            return translate_text(response, lang_code)
        else:
            # Skip to additional symptoms if no diagnostic questions
            conversation_state.update_session(session_id, stage='ask_additional')
            response = "Are you experiencing any additional symptoms? (e.g., nausea, fatigue, body aches) Or say 'none' if you don't have any."
            return translate_text(response, lang_code)
    
    # Stage 4: Ask diagnostic questions
    elif session['stage'] == 'ask_diagnostic':
        # Store the answer
        diagnostic_answers = session.get('diagnostic_answers', [])
        diagnostic_answers.append(user_input)
        
        current_index = session.get('current_question_index', 0)
        diagnostic_questions = session.get('diagnostic_questions', [])
        
        # Check if there are more questions
        if current_index + 1 < len(diagnostic_questions):
            conversation_state.update_session(
                session_id,
                diagnostic_answers=diagnostic_answers,
                current_question_index=current_index + 1
            )
            response = diagnostic_questions[current_index + 1]
            return translate_text(response, lang_code)
        else:
            # All diagnostic questions answered, move to additional symptoms
            conversation_state.update_session(
                session_id,
                diagnostic_answers=diagnostic_answers,
                stage='ask_additional'
            )
            response = "Are you experiencing any additional symptoms? (e.g., nausea, fatigue, body aches) Or say 'none' if you don't have any."
            return translate_text(response, lang_code)
    
    # Stage 5: Ask about additional symptoms and provide final advice
    elif session['stage'] == 'ask_additional':
        conversation_state.update_session(
            session_id,
            additional_symptoms=user_input,
            stage='complete'
        )
        
        # Generate personalized response with disease suggestions
        symptom = session['symptom']
        duration = session['duration']
        severity = session['severity']
        additional = user_input
        diagnostic_answers = session.get('diagnostic_answers', [])
        
        base_advice = RESPONSES_EN.get(symptom, RESPONSES_EN['default'])
        
        # Suggest possible conditions based on diagnostic answers
        suggested_conditions = suggest_conditions(symptom, diagnostic_answers)
        
        # Create personalized response
        personalized_response = f"Based on your {symptom.replace('_', ' ')} for {duration} with severity {severity}"
        
        if additional.lower() not in ['none', 'no', 'नहीं', 'இல்லை', 'లేదు', 'ಇಲ್ಲ', 'না']:
            personalized_response += f" and additional symptoms ({additional})"
        
        # Add disease suggestions if available
        if suggested_conditions:
            condition_names = [cond.replace('_', ' ').title() for cond in suggested_conditions]
            if len(condition_names) == 1:
                personalized_response += f", you might be experiencing **{condition_names[0]}**."
            elif len(condition_names) == 2:
                personalized_response += f", you might be experiencing **{condition_names[0]}** or **{condition_names[1]}**."
            else:
                personalized_response += f", possible conditions include **{condition_names[0]}**, **{condition_names[1]}**, or **{condition_names[2]}**."
            
            personalized_response += "\n\n"
        else:
            personalized_response += ", here's my advice:\n\n"
        
        # Add specific advice for suggested conditions or base advice
        if suggested_conditions:
            # Provide advice for the most likely condition
            primary_condition = suggested_conditions[0]
            condition_advice = RESPONSES_EN.get(primary_condition, base_advice)
            personalized_response += f"**Recommended Action:**\n{condition_advice}"
        else:
            personalized_response += base_advice
        
        # Add urgency note based on severity
        try:
            severity_num = int(''.join(filter(str.isdigit, severity)) or '5')
            if severity_num >= 8:
                personalized_response += "\n\n⚠️ **URGENT:** Given the high severity, I strongly recommend seeking immediate medical attention."
            elif severity_num >= 6:
                personalized_response += "\n\n⚠️ Please consider consulting a doctor soon for proper diagnosis and treatment."
        except:
            pass
        
        # Add important disclaimer
        personalized_response += "\n\n📌 **Important:** This is general health information only. For accurate diagnosis and treatment, please consult a qualified healthcare professional."
        
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
