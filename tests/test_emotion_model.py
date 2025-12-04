import pytest
from emotion_model import EmotionDetector

def test_emotion_detector_initialization():
    detector = EmotionDetector()
    assert detector is not None

def test_detect_emotion_keywords():
    detector = EmotionDetector()
    
    # Test anxiety
    result = detector.detect_emotion("أنا قلقان جدا")
    assert result['emotion'] == 'anxiety'
    
    # Test happiness
    result = detector.detect_emotion("أنا سعيد اليوم")
    assert result['emotion'] == 'happiness'
    
    # Test depression
    result = detector.detect_emotion("أنا حزين ومكتئب")
    assert result['emotion'] == 'depression'
    
    # Test stress
    result = detector.detect_emotion("عندي ضغط شغل كتير")
    assert result['emotion'] == 'stress'

def test_detect_emotion_neutral():
    detector = EmotionDetector()
    result = detector.detect_emotion("الجو جميل")
    # Depending on implementation, might be neutral or happiness, but let's assume neutral for simple statement
    # Adjust expectation based on actual logic if needed, but "الجو جميل" might trigger happiness in some models.
    # Let's try a very neutral statement
    result = detector.detect_emotion("ذهب أحمد إلى المدرسة")
    assert result['emotion'] == 'neutral'

def test_short_text():
    detector = EmotionDetector()
    result = detector.detect_emotion("لا")
    assert result['emotion'] == 'neutral'
    assert result['description_ar'] == 'نص قصير جداً'
