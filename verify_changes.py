
import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

def test_emotion_model():
    print("\n--- Testing Emotion Model (MARBERT) ---")
    try:
        from emotion_model import EmotionDetector
        detector = EmotionDetector()
        text = "أنا حزين جدا اليوم"
        result = detector.detect_emotion(text)
        print(f"Text: {text}")
        print(f"Result: {result}")
        
        if result.get('source') == 'MARBERT AI':
            print("✅ MARBERT model is ACTIVE and working")
        else:
            print(f"⚠️ MARBERT not active, using: {result.get('source')}")
            
        if result['emotion'] == 'depression':
            print("✅ Emotion detection passed (detected depression)")
        else:
            print(f"⚠️ Emotion detection result unexpected: {result['emotion']}")
    except Exception as e:
        print(f"❌ Emotion model test failed: {e}")

def test_gemini_integration():
    print("\n--- Testing Gemini Integration ---")
    try:
        from response_generator import GeminiResponseGenerator
        generator = GeminiResponseGenerator()
        response = generator.generate_ai_response(
            user_text="أنا حزين",
            emotion="depression",
            history=""
        )
        print(f"Response: {response}")
        if response and len(response) > 10:
            print("✅ Gemini response generation passed")
        else:
            print("⚠️ Gemini response empty or too short")
    except Exception as e:
        print(f"❌ Gemini integration test failed: {e}")

if __name__ == "__main__":
    test_emotion_model()
    test_gemini_integration()
