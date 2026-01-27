# 💕 두근두근 신한 : 첫번째 고객님

신한금융그룹 임직원을 위한 **세일즈 트레이닝 게임**입니다.

미연시(비주얼 노벨) 컨셉으로 고객 설득 스킬을 재미있게 연습할 수 있습니다.

## 🎮 주요 기능

- **AI 모드**: Google Gemini API를 활용한 실시간 고객 응대 시뮬레이션
- **체험 모드**: API 없이도 체험 가능한 데모 모드
- **4개 계열사**: 신한은행 / 신한카드 / 신한투자증권 / 신한라이프
- **다양한 상품**: 계열사별 실제 상품 기반 시나리오
- **AI 코칭**: 상담 후 강점/보완점 분석 리포트
- **난이도 선택**: Easy / Normal / Hard (매운맛 고객)

## 🚀 실행 방법

### 온라인 (Streamlit Cloud)
[여기를 클릭하여 바로 실행](https://your-app.streamlit.app)

### 로컬 실행
```bash
# 1. 패키지 설치
pip install -r requirements.txt

# 2. 실행
streamlit run app.py
```

## 📦 필요 패키지

- streamlit >= 1.28.0
- streamlit-lottie >= 0.0.5
- google-generativeai >= 0.3.0
- requests >= 2.28.0

## 🔑 API 키 설정

AI 모드 사용 시 Google Gemini API 키가 필요합니다.
1. [Google AI Studio](https://makersuite.google.com/app/apikey)에서 API 키 발급
2. 게임 사이드바에서 API 키 입력

## 📸 스크린샷

![메인 화면](main_banner.png)

## 🏢 제작

신한금융그룹 세일즈 트레이닝 프로젝트
