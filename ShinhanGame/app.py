# -*- coding: utf-8 -*-
"""
💕 두근두근 신한 : 첫번째 고객님
신한금융그룹 세일즈 트레이닝 게임 (미연시 컨셉)

pip install streamlit streamlit-lottie requests google-generativeai
streamlit run app.py
"""

import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import requests
import random
import json
import io
import base64
from datetime import datetime

# ============================================================
# 🎨 LOTTIE
# ============================================================
LOTTIE_URLS = {
    "dancing": "https://assets3.lottiefiles.com/packages/lf20_UJNc2t.json",
    "success": "https://assets1.lottiefiles.com/packages/lf20_s2lryxtd.json",
    "heart": "https://assets2.lottiefiles.com/packages/lf20_qh5z2fdq.json",
}

# ============================================================
# 📐 페이지 설정
# ============================================================
st.set_page_config(
    page_title="💕 두근두근 신한 : 첫번째 고객님",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 🎨 CSS (미연시 컨셉 - 핑크빛 은행 지점)
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
    
    :root {
        --pink-light: #FFB6C1;
        --pink-main: #FF69B4;
        --pink-deep: #DB7093;
        --heart-red: #FF6B6B;
        --cream: #FFF5EE;
        --shinhan-blue: #0046FF;
        --gold: #FFD700;
    }
    
    /* ============ 귀여운 하트 커서 ============ */
    
    /* 기본 커서 - 핑크 하트 */
    .stApp, .stApp * {
        cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' fill='%23FF69B4' stroke='%23FF1493' stroke-width='1'/%3E%3C/svg%3E") 12 12, auto !important;
    }
    
    /* 클릭 가능한 요소 - 빨간 하트 */
    .stButton > button,
    a, [role="button"],
    .stSelectbox, .stRadio,
    [data-testid="stExpanderToggleIcon"] {
        cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' fill='%23FF1493' stroke='%23C71585' stroke-width='1'/%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' fill='%23FF1493'/%3E%3Cellipse cx='8' cy='9' rx='2' ry='1.5' fill='%23FFB6C1' opacity='0.6'/%3E%3C/svg%3E") 12 12, pointer !important;
    }
    
    /* 텍스트 입력 - 작은 하트 */
    input, textarea, .stChatInput {
        cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20' viewBox='0 0 24 24'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z' fill='%23FFB6C1' stroke='%23FF69B4' stroke-width='1'/%3E%3C/svg%3E") 10 10, text !important;
    }
    
    /* ============ 화려한 애니메이션 효과 ============ */
    
    /* 배경 그라데이션 애니메이션 */
    @keyframes bgShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 부드러운 떠다니는 효과 */
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
    }
    
    /* 하트 펄스 효과 */
    @keyframes heartPulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    /* 반짝이는 효과 */
    @keyframes sparkle {
        0%, 100% { opacity: 1; filter: brightness(1); }
        50% { opacity: 0.8; filter: brightness(1.3); }
    }
    
    /* 슬라이드 인 (왼쪽에서) */
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* 슬라이드 인 (오른쪽에서) */
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    /* 페이드 인 업 */
    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* 게이지 채우기 애니메이션 */
    @keyframes fillGauge {
        from { width: 0%; }
    }
    
    /* 빛나는 테두리 */
    @keyframes glowBorder {
        0%, 100% { box-shadow: 0 0 5px rgba(255,105,180,0.5), 0 0 10px rgba(255,105,180,0.3); }
        50% { box-shadow: 0 0 15px rgba(255,105,180,0.8), 0 0 25px rgba(255,105,180,0.5); }
    }
    
    /* 숫자 팝 효과 */
    @keyframes numPop {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); color: #FF1493; }
        100% { transform: scale(1); }
    }
    
    /* 무지개 빛 효과 */
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    /* 하트 떨어지는 효과 */
    @keyframes heartFall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
    }
    
    @keyframes heartFall2 {
        0% { transform: translateY(-100vh) rotate(0deg) scale(0.8); opacity: 0.8; }
        100% { transform: translateY(100vh) rotate(-540deg) scale(1.2); opacity: 0; }
    }
    
    @keyframes heartFall3 {
        0% { transform: translateY(-100vh) rotate(45deg); opacity: 0.9; }
        50% { transform: translateY(50vh) rotate(180deg); opacity: 0.7; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    
    /* 하트 파티클 컨테이너 */
    .heart-particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    
    .heart-particle {
        position: absolute;
        top: -50px;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }
    
    .heart-particle:nth-child(1) { left: 5%; font-size: 18px; animation: heartFall 10s infinite 0s; opacity: 0.7; }
    .heart-particle:nth-child(2) { left: 15%; font-size: 14px; animation: heartFall2 12s infinite 1s; opacity: 0.5; }
    .heart-particle:nth-child(3) { left: 25%; font-size: 20px; animation: heartFall3 8s infinite 2s; opacity: 0.6; }
    .heart-particle:nth-child(4) { left: 35%; font-size: 16px; animation: heartFall 14s infinite 0.5s; opacity: 0.4; }
    .heart-particle:nth-child(5) { left: 45%; font-size: 12px; animation: heartFall2 11s infinite 3s; opacity: 0.5; }
    .heart-particle:nth-child(6) { left: 55%; font-size: 22px; animation: heartFall3 9s infinite 1.5s; opacity: 0.6; }
    .heart-particle:nth-child(7) { left: 65%; font-size: 15px; animation: heartFall 13s infinite 2.5s; opacity: 0.5; }
    .heart-particle:nth-child(8) { left: 75%; font-size: 18px; animation: heartFall2 10s infinite 0.8s; opacity: 0.7; }
    .heart-particle:nth-child(9) { left: 85%; font-size: 14px; animation: heartFall3 12s infinite 3.5s; opacity: 0.4; }
    .heart-particle:nth-child(10) { left: 95%; font-size: 16px; animation: heartFall 11s infinite 1.2s; opacity: 0.6; }
    .heart-particle:nth-child(11) { left: 10%; font-size: 13px; animation: heartFall2 15s infinite 4s; opacity: 0.5; }
    .heart-particle:nth-child(12) { left: 30%; font-size: 19px; animation: heartFall3 9s infinite 0.3s; opacity: 0.6; }
    .heart-particle:nth-child(13) { left: 50%; font-size: 11px; animation: heartFall 16s infinite 2.2s; opacity: 0.4; }
    .heart-particle:nth-child(14) { left: 70%; font-size: 17px; animation: heartFall2 10s infinite 1.8s; opacity: 0.5; }
    .heart-particle:nth-child(15) { left: 90%; font-size: 15px; animation: heartFall3 13s infinite 3.2s; opacity: 0.6; }
    
    /* 별 반짝임 */
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    #MainMenu, footer, header, .stDeployButton {visibility: hidden; display: none;}
    
    /* 사이드바 - 모바일에서 숨김/펼침 가능 */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF0F5, #FFE4EC) !important;
    }
    
    /* ============ 사이드바 토글 버튼 (귀여운 스타일) ============ */
    [data-testid="collapsedControl"] {
        position: fixed !important;
        top: 10px !important;
        left: 10px !important;
        z-index: 999999 !important;
    }
    
    [data-testid="collapsedControl"] button {
        background: linear-gradient(135deg, #FF69B4, #FF1493) !important;
        border: 2px solid white !important;
        border-radius: 15px !important;
        padding: 8px 14px !important;
        box-shadow: 0 4px 15px rgba(255,105,180,0.5) !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="collapsedControl"] button:hover {
        transform: scale(1.1) !important;
        box-shadow: 0 6px 20px rgba(255,105,180,0.6) !important;
        background: linear-gradient(135deg, #FF1493, #C71585) !important;
    }
    
    [data-testid="collapsedControl"] button svg {
        stroke: white !important;
        fill: white !important;
    }
    
    /* 사이드바 기본 닫기 버튼 숨김 (커스텀 버튼 사용) */
    button[kind="headerNoPadding"],
    [data-testid="stSidebarCollapseButton"],
    .stSidebarCollapseButton {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* 모바일에서 메인 콘텐츠 전체 너비 사용 */
    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            width: 280px !important;
            min-width: 280px !important;
        }
        
        .main .block-container {
            padding: 1rem !important;
            max-width: 100% !important;
        }
        
        [data-testid="collapsedControl"] {
            top: 8px !important;
            left: 8px !important;
        }
        
        [data-testid="collapsedControl"] button {
            padding: 6px 10px !important;
        }
    }
    
    /* 사이드바 내부 스타일 */
    section[data-testid="stSidebar"] > div {
        padding-top: 1rem;
    }
    
    /* 은행 지점 배경 (핑크빛) - 애니메이션 적용 */
    .stApp {
        background: linear-gradient(-45deg, #FFE4EC, #FFD1DC, #FFC0CB, #FFB6C1, #FFE4EC);
        background-size: 400% 400%;
        background-attachment: fixed;
        font-family: 'Noto Sans KR', sans-serif;
        animation: bgShift 15s ease infinite;
    }
    
    
    /* 은행 창구 느낌의 오버레이 - 미세한 움직임 */
    .main::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            linear-gradient(90deg, rgba(255,255,255,0.08) 1px, transparent 1px),
            linear-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
        background-size: 50px 50px;
        pointer-events: none;
        animation: bgShift 30s linear infinite;
        z-index: 0;
    }
    
    .main .block-container {
        padding: 0.3rem 1rem !important;
        padding-top: 0.2rem !important;
        max-width: 1100px !important;
        position: relative;
        z-index: 1;
    }
    
    /* 메인 영역 간격 강제 제거 */
    .main .block-container > div {
        gap: 0 !important;
    }
    
    .main .block-container > div > div {
        margin-bottom: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* 요소 간 간격 최소화 */
    .stColumn > div {
        padding: 0 !important;
    }
    
    .element-container {
        margin-bottom: 0.1rem !important;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        gap: 0.1rem !important;
    }
    
    /* expander 간격 줄이기 */
    .streamlit-expanderHeader {
        padding: 0.2rem 0.5rem !important;
        font-size: 12px !important;
    }
    
    div[data-testid="stExpander"] {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* 모든 요소 마진 제거 */
    .stMarkdown, .stAlert, .stInfo, .stWarning {
        margin: 0 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* 블록 간격 최소화 */
    section[data-testid="stMain"] > div {
        gap: 0 !important;
    }
    
    .block-container > div > div {
        gap: 0.1rem !important;
    }
    
    /* 타이틀 (두근두근) - 화려하고 반짝이는 스타일 */
    .game-title {
        text-align: center;
        padding: 25px 20px;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        margin-bottom: 15px;
        border: 3px solid #FF69B4;
        box-shadow: 0 0 30px rgba(255,105,180,0.5), 0 0 60px rgba(255,105,180,0.3), inset 0 0 30px rgba(255,105,180,0.1);
        position: relative;
        overflow: hidden;
    }
    
    .game-title::before {
        content: "✨";
        position: absolute;
        top: 10px;
        left: 20px;
        font-size: 20px;
        animation: twinkle 1.5s ease-in-out infinite;
    }
    
    .game-title::after {
        content: "✨";
        position: absolute;
        top: 10px;
        right: 20px;
        font-size: 20px;
        animation: twinkle 1.5s ease-in-out infinite 0.5s;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    .game-title h1 {
        font-size: 42px;
        font-weight: 900;
        background: linear-gradient(90deg, #FF69B4, #FFB6C1, #FF1493, #FFB6C1, #FF69B4);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        animation: shimmer 3s linear infinite;
        text-shadow: 0 0 20px rgba(255,105,180,0.8);
        letter-spacing: 3px;
    }
    
    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    .game-title .subtitle {
        color: #FFB6C1;
        font-size: 14px;
        margin-top: 8px;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(255,182,193,0.8);
    }
    
    /* 호감도 게이지 (하트 스타일) - 애니메이션 */
    .gauge-section {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,240,245,0.9));
        border-radius: 12px;
        padding: 8px 12px;
        margin-bottom: 5px;
        border: 2px solid var(--pink-main);
        box-shadow: 0 2px 8px rgba(255,105,180,0.15);
        animation: fadeInUp 0.4s ease;
    }
    
    .gauge-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 4px;
        color: var(--pink-deep);
        font-weight: 700;
        font-size: 12px;
    }
    
    .gauge-bar-bg {
        background: rgba(255,182,193,0.4);
        border-radius: 10px;
        height: 18px;
        overflow: hidden;
        border: 1px solid var(--pink-light);
        position: relative;
    }
    
    /* 게이지 배경 빛나는 효과 */
    .gauge-bar-bg::after {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        animation: shine 2s ease-in-out infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        50%, 100% { left: 100%; }
    }
    
    .gauge-bar-fill {
        height: 100%;
        background: linear-gradient(90deg, #FF69B4, #FF1493, #FF6B6B, #FF69B4);
        background-size: 200% 100%;
        border-radius: 10px;
        transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 11px;
        animation: fillGauge 1s ease-out, bgShift 3s ease infinite;
        text-shadow: 0 0 5px rgba(0,0,0,0.3);
        font-weight: 700;
        font-size: 13px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* 고객 카드 (캐릭터 프로필) - 애니메이션 */
    .customer-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,240,245,0.95));
        border: 2px solid var(--pink-main);
        border-radius: 15px;
        padding: 10px;
        text-align: center;
        margin-bottom: 4px;
        box-shadow: 0 3px 12px rgba(255,105,180,0.2);
        animation: fadeInUp 0.5s ease, glowBorder 3s ease-in-out infinite;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .customer-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 25px rgba(255,105,180,0.4);
    }
    
    .customer-emoji { 
        font-size: 60px; 
        margin-bottom: 8px; 
        filter: drop-shadow(2px 2px 4px rgba(255,105,180,0.4));
    }
    .customer-name { 
        color: var(--pink-deep); 
        font-size: 18px; 
        font-weight: 700; 
    }
    .customer-info { 
        color: #888; 
        font-size: 12px; 
        margin-top: 4px; 
    }
    
    /* 대화 영역 (비주얼 노벨 스타일) - 스크롤 */
    .dialogue-area {
        background: transparent;
        padding: 5px;
        min-height: 20px;
        max-height: 200px;
        margin: 0 !important;
        margin-top: -10px !important;
        overflow-y: auto;
        scroll-behavior: smooth;
    }
    
    /* 게임 화면 전체 레이아웃 */
    .game-container {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 100px);
    }
    
    .game-top-fixed {
        flex-shrink: 0;
        background: linear-gradient(135deg, rgba(255,228,236,0.95), rgba(255,209,220,0.95));
        border-radius: 12px;
        padding: 8px;
        margin-bottom: 3px;
        box-shadow: 0 2px 8px rgba(255,105,180,0.15);
    }
    
    .game-dialogue-scroll {
        flex-grow: 1;
        overflow-y: auto;
        min-height: 0;
        margin-top: 0;
    }
    
    /* 메시지 박스 (비주얼 노벨 대화창) - 슬라이드 애니메이션 */
    .msg-box {
        background: linear-gradient(180deg, rgba(30,20,50,0.92) 0%, rgba(50,30,70,0.95) 100%);
        border: 2px solid rgba(255,105,180,0.6);
        border-radius: 8px;
        padding: 0;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .msg-box:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 25px rgba(255,105,180,0.3), inset 0 1px 0 rgba(255,255,255,0.15);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* 캐릭터 이름 영역 */
    .msg-speaker {
        background: linear-gradient(90deg, rgba(255,105,180,0.9), rgba(255,105,180,0.3), transparent);
        padding: 8px 20px;
        font-size: 16px;
        font-weight: 800;
        color: white;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        border-bottom: 1px solid rgba(255,105,180,0.3);
    }
    
    /* 대화 내용 */
    .msg-text {
        color: white;
        font-size: 17px;
        line-height: 1.9;
        padding: 15px 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* 고객 메시지 - 왼쪽에서 슬라이드 인 */
    .msg-customer {
        border-color: rgba(255,105,180,0.7);
        animation: slideInLeft 0.5s ease;
    }
    
    .msg-customer .msg-speaker {
        background: linear-gradient(90deg, rgba(255,105,180,0.9), rgba(255,105,180,0.3), transparent);
        animation: heartPulse 3s ease-in-out infinite;
    }
    
    /* 내 메시지 - 오른쪽에서 슬라이드 인 */
    .msg-user {
        border-color: rgba(100,181,246,0.7);
        animation: slideInRight 0.5s ease;
    }
    
    .msg-user .msg-speaker {
        background: linear-gradient(90deg, rgba(100,181,246,0.9), rgba(100,181,246,0.3), transparent);
    }
    
    /* 점수 팝업 (하트) - 화려한 효과 */
    .score-popup {
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        margin: 8px 0;
        animation: heartBeat 0.6s ease, sparkle 1s ease infinite;
        text-shadow: 0 0 10px currentColor, 0 0 20px currentColor;
    }
    
    @keyframes heartBeat {
        0% { transform: scale(0) rotate(-10deg); opacity: 0; }
        50% { transform: scale(1.4) rotate(5deg); }
        70% { transform: scale(0.9); }
        100% { transform: scale(1); }
    }
    
    .score-great { color: var(--heart-red); }
    .score-good { color: var(--pink-main); }
    .score-ok { color: var(--pink-light); }
    
    /* 상품 팁 */
    .tips-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,250,240,0.9));
        border: 2px solid var(--gold);
        border-radius: 15px;
        padding: 12px;
        margin-bottom: 12px;
        box-shadow: 0 3px 10px rgba(255,215,0,0.2);
    }
    
    .tips-box h4 {
        color: #B8860B;
        font-size: 13px;
        margin: 0 0 8px 0;
    }
    
    .tips-box ul {
        margin: 0;
        padding-left: 18px;
        color: #555;
        font-size: 12px;
        line-height: 1.5;
    }
    
    .keyword-tag {
        display: inline-block;
        background: linear-gradient(135deg, var(--pink-main), var(--heart-red));
        color: white;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 11px;
        font-weight: 700;
        margin: 2px;
    }
    
    /* 스탯 - 애니메이션 */
    .stat-box {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,240,245,0.9));
        border-radius: 10px;
        padding: 6px 8px;
        text-align: center;
        border: 1px solid var(--pink-light);
        animation: fadeInUp 0.5s ease;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 5px 15px rgba(255,105,180,0.3);
    }
    
    .stat-label { color: #888; font-size: 9px; text-transform: uppercase; letter-spacing: 1px; }
    .stat-value { 
        color: var(--pink-deep); 
        font-size: 16px; 
        font-weight: 900;
        animation: sparkle 2s ease-in-out infinite;
    }
    
    /* 버튼 (하트 테마) - 화려한 애니메이션 */
    .stButton > button {
        background: linear-gradient(135deg, var(--pink-main), #FF1493, var(--pink-main)) !important;
        background-size: 200% 200% !important;
        color: white !important;
        border: 3px solid var(--heart-red) !important;
        border-radius: 25px !important;
        padding: 12px 30px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(255,105,180,0.4) !important;
        animation: bgShift 3s ease infinite, float 3s ease-in-out infinite !important;
        transition: all 0.3s ease !important;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: "💕";
        position: absolute;
        left: 10px;
        animation: heartPulse 1s ease-in-out infinite;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.05) !important;
        box-shadow: 0 10px 30px rgba(255,105,180,0.6), 0 0 20px rgba(255,105,180,0.4) !important;
        animation: none !important;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98) !important;
    }
    
    /* 채팅 입력 - 빛나는 효과 */
    .stChatInput > div {
        background: white !important;
        border: 3px solid var(--pink-main) !important;
        border-radius: 25px !important;
        animation: glowBorder 2s ease-in-out infinite !important;
        transition: all 0.3s ease !important;
    }
    
    .stChatInput > div:focus-within {
        box-shadow: 0 0 20px rgba(255,105,180,0.5), 0 0 40px rgba(255,105,180,0.3) !important;
        border-color: #FF1493 !important;
    }
    
    /* 사이드바 (연한 핑크) */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF0F5, #FFE4EC) !important;
    }
    
    [data-testid="stSidebar"] * { color: #333 !important; }
    [data-testid="stSidebar"] h2 { color: var(--pink-deep) !important; }
    
    /* 리포트 카드 */
    .report-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(255,240,245,0.95));
        border: 3px solid var(--pink-main);
        border-radius: 25px;
        padding: 25px;
        margin: 12px 0;
        box-shadow: 0 8px 30px rgba(255,105,180,0.3);
    }
    
    .report-title {
        color: var(--pink-deep);
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 15px;
    }
    
    .grade-box {
        text-align: center;
        margin: 15px 0;
    }
    
    .grade-letter {
        font-size: 60px;
        font-weight: 900;
        padding: 8px 25px;
        border-radius: 15px;
        display: inline-block;
    }
    
    .grade-s { background: linear-gradient(135deg, #FF69B4, #FF1493); color: white; }
    .grade-a { background: linear-gradient(135deg, #FFB6C1, #FF69B4); color: white; }
    .grade-b { background: linear-gradient(135deg, #87CEEB, #4682B4); color: white; }
    .grade-c { background: linear-gradient(135deg, #DDA0DD, #BA55D3); color: white; }
    
    /* 대화 기록 */
    .history-item {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,245,250,0.9));
        border-radius: 15px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid var(--pink-main);
        box-shadow: 0 2px 8px rgba(255,105,180,0.15);
    }
    
    .history-turn { color: #888; font-size: 11px; margin-bottom: 6px; }
    .history-user { color: var(--shinhan-blue); margin-bottom: 6px; font-size: 13px; }
    .history-customer { color: var(--pink-deep); font-size: 13px; }
    .history-feedback { color: #555; font-size: 12px; margin-top: 10px; padding-top: 10px; border-top: 1px solid rgba(255,105,180,0.2); }
    
    /* 승리/실패 */
    .victory-box {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border: 4px solid white;
        border-radius: 25px;
        padding: 35px;
        text-align: center;
        animation: pop 0.5s ease;
    }
    
    @keyframes pop {
        0% { transform: scale(0); }
        70% { transform: scale(1.08); }
        100% { transform: scale(1); }
    }
    
    .victory-title { font-size: 36px; font-weight: 900; color: #000; margin-bottom: 8px; }
    .victory-sub { font-size: 16px; color: #333; margin-bottom: 12px; }
    .victory-score { font-size: 28px; font-weight: 900; color: var(--shinhan-navy); }
    
    .defeat-box {
        background: linear-gradient(135deg, #ff6b6b, #ee5a5a);
        border: 4px solid white;
        border-radius: 25px;
        padding: 35px;
        text-align: center;
    }
    
    .defeat-title { font-size: 36px; font-weight: 900; color: white; }
    
    /* 입력창/선택창 스타일 - 흰색 배경 + 검정색 글씨 */
    .stTextInput input, .stTextArea textarea {
        background-color: white !important;
        color: #333 !important;
        border: 2px solid #FFB6C1 !important;
        border-radius: 10px !important;
    }
    
    .stSelectbox > div > div,
    .stSelectbox [data-baseweb="select"] > div,
    .stRadio > div {
        background-color: white !important;
        color: #333 !important;
    }
    
    .stSelectbox [data-baseweb="select"] span,
    .stSelectbox div[data-baseweb] * {
        color: #333 !important;
        background-color: white !important;
    }
    
    /* 드롭다운 메뉴 */
    [data-baseweb="popover"] {
        background-color: white !important;
    }
    
    [data-baseweb="menu"] {
        background-color: white !important;
    }
    
    [data-baseweb="menu"] li {
        color: #333 !important;
        background-color: white !important;
    }
    
    [data-baseweb="menu"] li:hover {
        background-color: #FFE4EC !important;
    }
    
    /* 채팅 입력창 */
    .stChatInput input {
        background-color: white !important;
        color: #333 !important;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: white !important;
        color: #333 !important;
    }
    
    /* 고객 이미지 - 박스에 꽉 차게 + 애니메이션 */
    .customer-image-large {
        display: block;
        width: 100%;
        max-width: 280px;
        height: 200px;
        border-radius: 12px;
        object-fit: cover;
        object-position: center top;
        border: 3px solid #FF69B4;
        margin: 0 auto 12px auto;
        box-shadow: 0 4px 15px rgba(255,105,180,0.4), 0 0 20px rgba(255,105,180,0.3);
        animation: float 3s ease-in-out infinite, glowBorder 2s ease-in-out infinite;
        transition: transform 0.3s ease;
    }
    
    .customer-image-large:hover {
        transform: scale(1.02);
        animation-play-state: paused;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# 🔧 유틸리티
# ============================================================

@st.cache_data(ttl=3600)
def load_lottie(url):
    try:
        r = requests.get(url, timeout=10)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def get_persona_image(image_name):
    """페르소나 이미지를 base64로 인코딩해서 반환"""
    import os
    
    # 확장자에 따른 MIME 타입
    ext = image_name.split('.')[-1].lower()
    mime_type = "image/jpeg" if ext in ['jpg', 'jpeg'] else "image/png"
    
    # 가능한 경로들
    possible_paths = [
        image_name,
        os.path.join(os.path.dirname(__file__), image_name),
        os.path.join(".", image_name),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            try:
                with open(path, "rb") as f:
                    data = base64.b64encode(f.read()).decode()
                    return f"data:{mime_type};base64,{data}"
            except:
                continue
    
    # 이미지를 찾지 못하면 빈 문자열 반환
    return ""

# ============================================================
# 📊 데이터 (상세 혜택 포함)
# ============================================================

COMPANY_PRODUCTS = {
    "🏦 신한은행": {
        "SOL트래블 체크카드": {
            "points": ["해외 결제 수수료 0원", "환전 우대 90%", "공항 라운지 무료 이용"],
            "keywords": ["수수료", "환전", "해외", "여행", "무료", "라운지", "0원", "90"],
            "details": {
                "주요혜택": "해외 결제 시 수수료 0원, 환전 우대 90%",
                "연회비": "없음 (체크카드)",
                "대상고객": "해외여행/출장이 잦은 고객",
                "절약효과": "연간 약 10~15만원 절약 가능",
                "가입조건": "신한은행 계좌 보유자",
                "추천멘트": "해외여행 자주 가시면 연간 10만원 이상 절약하실 수 있어요!"
            }
        },
        "쏠편한 정기예금": {
            "points": ["연 4.5% 고금리", "중도해지 이자 보장", "모바일 간편 가입"],
            "keywords": ["금리", "이자", "4.5", "예금", "안전", "보장", "높"],
            "details": {
                "주요혜택": "연 4.5% 고금리 (1년 기준)",
                "최소가입금액": "100만원",
                "대상고객": "안정적인 목돈 운용 원하는 고객",
                "특이사항": "중도해지 시에도 기본 이자 보장",
                "가입방법": "SOL 앱에서 5분 만에 가입",
                "추천멘트": "1000만원 예치 시 연 45만원 이자 받으실 수 있어요!"
            }
        },
    },
    "💳 신한카드": {
        "신한카드 Deep Dream": {
            "points": ["넷플릭스/유튜브 10% 할인", "배달앱 5% 적립", "통신비 할인"],
            "keywords": ["넷플릭스", "유튜브", "배달", "스트리밍", "할인", "적립", "10"],
            "details": {
                "주요혜택": "OTT 10% 할인, 배달앱 5% 적립",
                "연회비": "국내전용 15,000원 / 해외겸용 18,000원",
                "대상고객": "디지털 콘텐츠 소비가 많은 MZ세대",
                "절약효과": "월 2~3만원 절약 (연 24~36만원)",
                "전월실적": "30만원 이상 사용 시 혜택 적용",
                "추천멘트": "넷플릭스, 유튜브 프리미엄 쓰시면 매달 2만원 이상 아끼실 수 있어요!"
            }
        },
        "신한카드 Mr.Life": {
            "points": ["주유 리터당 60원 할인", "마트 5% 할인", "공과금 할인"],
            "keywords": ["주유", "마트", "생활", "할인", "60원", "공과금"],
            "details": {
                "주요혜택": "주유 L당 60원, 대형마트 5% 할인",
                "연회비": "국내전용 15,000원",
                "대상고객": "자가용 이용, 대형마트 쇼핑하는 가정",
                "절약효과": "월 3~5만원 절약 가능",
                "전월실적": "40만원 이상",
                "추천멘트": "주유비만 한 달에 3만원 이상 아끼실 수 있어요!"
            }
        },
    },
    "📈 신한투자증권": {
        "연금저축펀드": {
            "points": ["세액공제 최대 16.5%", "노후 준비 필수", "다양한 펀드 선택"],
            "keywords": ["세액공제", "연금", "노후", "절세", "16.5", "공제"],
            "details": {
                "주요혜택": "연 400만원 납입 시 최대 66만원 세액공제",
                "가입한도": "연 1,800만원",
                "대상고객": "절세와 노후 준비를 동시에 원하는 직장인",
                "세제혜택": "총급여 5,500만원 이하 16.5%, 초과 13.2%",
                "수령조건": "만 55세 이후 연금 수령",
                "추천멘트": "연말정산 때 최대 66만원 돌려받으실 수 있어요!"
            }
        },
    },
    "🛡️ 신한라이프": {
        "통합건강보험": {
            "points": ["암/뇌/심장 3대 질병 보장", "갱신 없이 평생 보장", "납입면제 특약"],
            "keywords": ["암", "건강", "보장", "평생", "질병", "납입면제", "3대"],
            "details": {
                "주요혜택": "3대 질병 진단비 최대 5천만원",
                "보험료": "30대 기준 월 3~5만원",
                "대상고객": "건강 보장이 필요한 모든 연령",
                "특이사항": "비갱신형으로 보험료 인상 없음",
                "납입면제": "암/뇌졸중/급성심근경색 진단 시 이후 보험료 면제",
                "추천멘트": "비갱신형이라 20년 후에도 보험료가 똑같아요!"
            }
        },
    },
}

# 고객 페르소나 (이미지 포함)
PERSONAS = {
    "20대 사회초년생 김신한": {
        "emoji": "👨‍💼", 
        "age": "26세", 
        "job": "IT기업 개발자", 
        "style": "가성비 중시, 디지털 친화",
        "image": "20.jpg",
        "concerns": ["해외여행", "구독서비스", "재테크 시작"],
        "speech_style": "친근하고 캐주얼한 MZ 말투"
    },
    "30대 맞벌이 이행복": {
        "emoji": "👩‍💼", 
        "age": "35세", 
        "job": "대기업 과장", 
        "style": "안정 추구, 시간 부족",
        "image": "30.jpg",
        "concerns": ["육아비용", "내집마련", "시간절약"],
        "speech_style": "정중하지만 핵심을 원함"
    },
    "40대 자영업 박사장": {
        "emoji": "👨‍🍳", 
        "age": "45세", 
        "job": "음식점 사장", 
        "style": "실용적, 절세 관심",
        "image": "40.jpg",
        "concerns": ["사업자금", "절세", "수수료절감"],
        "speech_style": "직설적이고 실용적"
    },
    "50대 은퇴준비 최부장": {
        "emoji": "👴", 
        "age": "55세", 
        "job": "제조업 부장", 
        "style": "원금 보장 선호",
        "image": "50.jpg",
        "concerns": ["노후준비", "안전한 투자", "건강보험"],
        "speech_style": "신중하고 꼼꼼함"
    },
}

# ============================================================
# 📜 체험 모드 시나리오 (설득도 상승형)
# ============================================================

def get_scenarios(company, product, persona, difficulty):
    pd = COMPANY_PRODUCTS.get(company, {}).get(product, {})
    points = pd.get("points", ["좋은 혜택"])
    keywords = pd.get("keywords", ["혜택"])
    details = pd.get("details", {})
    
    # 난이도별 설득도 상승량 (5턴 기준: 좋은 답변 / 보통 답변)
    gain_map = {"🌱 Easy": (25, 15), "🔥 Normal": (22, 12), "💀 Hard": (15, 5)}
    gains = gain_map.get(difficulty.split()[0] + " " + difficulty.split()[1], (22, 12))
    
    is_hard = "Hard" in difficulty or "매운맛" in difficulty
    is_easy = "Easy" in difficulty or "순한맛" in difficulty
    
    # 난이도별 시나리오
    if is_hard:
        # 💀 매운맛: 까다롭고 의심 많은 고객
        return [
            {
                "turn": 1,
                "customer": f"아 저기요. {product}? 인터넷에서 별로라던데 뭐가 좋다는 거예요? 솔직히 말해봐요.",
                "emotion": "😒",
                "keywords": keywords[:4],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 진상 고객의 날카로운 질문에 잘 대응했어요!",
                "feedback_ok": "💡 까다로운 고객일수록 구체적인 수치로 설득해야 해요.",
            },
            {
                "turn": 2,
                "customer": f"아니 근데 다른 은행에선 더 좋은 조건 준다던데요? 여기만 이래요? 제가 바보로 보여요?",
                "emotion": "😤",
                "keywords": keywords[:4] + ["최고", "1위", "특별", "차별", "독점"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 타사 비교 공격을 잘 방어했어요!",
                "feedback_ok": "💡 타사 대비 우위점을 객관적 수치로 제시하세요.",
            },
            {
                "turn": 3,
                "customer": f"수수료 숨겨놓은 거 아니에요? 나중에 이상한 비용 청구하면 본사에 컴플레인 넣을 거예요. 확실해요?",
                "emotion": "😠",
                "keywords": ["수수료", "무료", "0원", "면제", "연회비", "비용", "숨겨진"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 비용 투명성 질문에 신뢰를 줬어요!",
                "feedback_ok": "💡 컴플레인 언급 시 당황하지 말고 정확한 정보를 제공하세요.",
            },
            {
                "turn": 4,
                "customer": f"그래서 실제로 얼마나 이득이라는 거예요? 뜬구름 잡는 소리 말고 숫자로 딱 말해봐요. 시간 없어요.",
                "emotion": "😤",
                "keywords": ["절약", "연간", "월", "만원", "원", "이득", "혜택", "숫자"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 구체적 숫자로 설득력을 높였어요!",
                "feedback_ok": "💡 진상 고객에겐 정확한 숫자가 필수예요.",
            },
            {
                "turn": 5,
                "customer": f"...알겠어요. 근데 나중에 문제 생기면 담당자 이름 뭐예요? 기억해둘게요. 가입은 해볼게요.",
                "emotion": "😐",
                "keywords": ["지금", "오늘", "바로", "간편", "쉽", "가입", "신청", "책임"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 끝까지 프로답게 대응했어요! 진상도 결국 설득!",
                "feedback_ok": "💡 마지막까지 신뢰를 주는 클로징이 중요해요.",
            },
        ]
    elif is_easy:
        # 🌱 순한맛: 친절하고 수용적인 고객
        return [
            {
                "turn": 1,
                "customer": f"안녕하세요~ {product} 추천받아서 왔어요! 좋은 점 좀 알려주실 수 있을까요? ☺️",
                "emotion": "😊",
                "keywords": keywords[:4],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 친절한 고객에게 잘 설명했어요!",
                "feedback_ok": "💡 기본적인 혜택만 언급해도 좋은 반응을 얻을 수 있어요.",
            },
            {
                "turn": 2,
                "customer": f"와~ 그렇군요! 정말 좋네요. 혹시 다른 좋은 점도 더 있나요?",
                "emotion": "😄",
                "keywords": keywords[:4] + ["최고", "1위", "특별", "차별", "독점"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 추가 혜택 설명을 잘했어요!",
                "feedback_ok": "💡 고객이 관심 보일 때 더 많은 혜택을 소개하세요.",
            },
            {
                "turn": 3,
                "customer": f"비용은 어떻게 되나요? 부담되면 좀 고민해볼게요~",
                "emotion": "🤔",
                "keywords": ["수수료", "무료", "0원", "면제", "연회비", "비용"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 비용 설명으로 안심시켰어요!",
                "feedback_ok": "💡 부담없는 비용이라는 걸 강조하면 좋아요.",
            },
            {
                "turn": 4,
                "customer": f"실제로 어느 정도 혜택인지 궁금해요! 대충이라도 괜찮아요~",
                "emotion": "😊",
                "keywords": ["절약", "연간", "월", "만원", "원", "이득", "혜택"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 구체적인 혜택을 잘 설명했어요!",
                "feedback_ok": "💡 대략적인 숫자만 말해도 충분해요.",
            },
            {
                "turn": 5,
                "customer": f"좋아요! 설명 너무 잘해주셨어요. 가입할게요! 감사합니다 💕",
                "emotion": "😍",
                "keywords": ["지금", "오늘", "바로", "간편", "쉽", "가입", "신청"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 완벽한 상담이었어요! 고객 만족!",
                "feedback_ok": "💡 클로징까지 잘 마무리했어요.",
            },
        ]
    else:
        # 🔥 보통: 일반 고객
        return [
            {
                "turn": 1,
                "customer": f"안녕하세요~ {product}에 대해 들어봤는데, 구체적으로 어떤 혜택이 있나요?",
                "emotion": "🤔",
                "keywords": keywords[:4],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 핵심 혜택을 잘 설명했어요!",
                "feedback_ok": "💡 상품의 구체적인 혜택을 언급하면 더 좋아요.",
            },
            {
                "turn": 2,
                "customer": f"오~ 그렇군요! 근데 비슷한 상품들이 많잖아요. 이게 특별히 좋은 이유가 뭐예요?",
                "emotion": "🤔",
                "keywords": keywords[:4] + ["최고", "1위", "특별", "차별", "독점"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 차별화 포인트를 잘 전달했어요!",
                "feedback_ok": "💡 경쟁 상품 대비 장점을 강조해보세요.",
            },
            {
                "turn": 3,
                "customer": f"그런데 수수료나 비용은 어떻게 되나요? 숨겨진 비용은 없겠죠?",
                "emotion": "🤔",
                "keywords": ["수수료", "무료", "0원", "면제", "연회비", "비용"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 비용 관련 설명을 투명하게 잘했어요!",
                "feedback_ok": "💡 수수료/비용에 대해 명확하게 설명해주세요.",
            },
            {
                "turn": 4,
                "customer": f"실제로 얼마나 절약되는 건가요? 구체적인 금액이 궁금해요.",
                "emotion": "😊",
                "keywords": ["절약", "연간", "월", "만원", "원", "이득", "혜택"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 구체적인 절약 금액을 잘 제시했어요!",
                "feedback_ok": "💡 '연간 ~원 절약' 같이 숫자로 말하면 효과적이에요.",
            },
            {
                "turn": 5,
                "customer": f"좋아요! 그럼 오늘 바로 가입하면 되나요?",
                "emotion": "😊",
                "keywords": ["지금", "오늘", "바로", "간편", "쉽", "가입", "신청"],
                "gain_good": gains[0],
                "gain_ok": gains[1],
                "feedback_good": "✅ 클로징 멘트를 잘 했어요!",
                "feedback_ok": "💡 '지금 가입하시면...' 식의 클로징 멘트가 효과적이에요.",
            },
        ]

# ============================================================
# 🤖 Gemini AI (정교한 평가 시스템)
# ============================================================

import re

def parse_json_response(text):
    """Gemini 응답에서 JSON 추출"""
    # 코드 블록 제거
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]
    
    text = text.strip()
    
    # JSON 파싱 시도
    try:
        return json.loads(text)
    except:
        pass
    
    # { } 사이 추출 시도
    match = re.search(r'\{[^{}]*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass
    
    # 필드별 추출 시도
    result = {}
    
    # evaluation 추출
    eval_match = re.search(r'"?evaluation"?\s*[:=]\s*"?(EXCELLENT|GOOD|AVERAGE|POOR)"?', text, re.IGNORECASE)
    if eval_match:
        result["evaluation"] = eval_match.group(1).upper()
    
    # persuasion_gain 추출
    gain_match = re.search(r'"?persuasion_gain"?\s*[:=]\s*(-?\d+)', text)
    if gain_match:
        result["persuasion_gain"] = int(gain_match.group(1))
    
    # customer_response 추출
    resp_match = re.search(r'"?customer_response"?\s*[:=]\s*"([^"]+)"', text)
    if resp_match:
        result["customer_response"] = resp_match.group(1)
    
    # feedback 추출
    pos_match = re.search(r'"?feedback_positive"?\s*[:=]\s*"([^"]*)"', text)
    if pos_match:
        result["feedback_positive"] = pos_match.group(1)
    
    imp_match = re.search(r'"?feedback_improve"?\s*[:=]\s*"([^"]*)"', text)
    if imp_match:
        result["feedback_improve"] = imp_match.group(1)
    
    tip_match = re.search(r'"?tip"?\s*[:=]\s*"([^"]*)"', text)
    if tip_match:
        result["tip"] = tip_match.group(1)
    
    return result if result else None


def evaluate_answer_locally(user_input, keywords, product, product_data=None):
    """로컬 평가 (백업용) - 정확한 정보 체크 포함"""
    user_lower = user_input.lower()
    
    # 무의미한 답변 체크
    nonsense = ["ㅋ", "ㅎ", "ㄷ", "...", "몰라", "모르", "글쎄", "음...", "그냥", "아무거나", "뭐", "일걸", "같아요", "아마"]
    if any(ns in user_lower for ns in nonsense) or len(user_input.strip()) < 8:
        return "POOR", 0
    
    # 불확실한 표현 체크 (추측성 답변)
    uncertain = ["것 같", "일걸", "아마", "글쎄", "잘 모르", "확실하지"]
    if any(u in user_input for u in uncertain):
        return "AVERAGE", 5
    
    # 틀린 정보 체크 (정확한 수치 확인)
    if product_data:
        points = product_data.get("points", [])
        # "환전 우대 90%"인데 "50%"라고 하면 틀림
        if "90" in str(points) and ("50%" in user_input or "50퍼" in user_input or "오십" in user_input):
            return "POOR", 0
        if "0원" in str(points) and ("100원" in user_input or "천원" in user_input or "유료" in user_input):
            return "POOR", 0
    
    # 키워드 매칭
    matched = sum(1 for k in keywords if k.lower() in user_lower)
    
    # 구체적 수치 체크 (정확한 수치만)
    has_correct_number = False
    if product_data:
        points_str = str(product_data.get("points", []))
        # 정확한 수치가 있는지 체크
        if "90" in points_str and "90" in user_input:
            has_correct_number = True
        if "0원" in points_str and "0원" in user_input:
            has_correct_number = True
    
    has_number = bool(re.search(r'\d+[%원만억]|\d+\s*퍼센트', user_input))
    
    if matched >= 2 and has_correct_number:
        return "EXCELLENT", 35
    elif matched >= 2 and has_number:
        return "GOOD", 18
    elif matched >= 1 and has_number:
        return "AVERAGE", 10
    elif matched >= 1 and len(user_input) > 20:
        return "AVERAGE", 8
    elif len(user_input) > 30:
        return "AVERAGE", 5
    else:
        return "POOR", 0


def get_gemini_response(api_key, user_input, context):
    """Gemini가 실제 고객처럼 자연스럽게 반응하고, 상담사를 코칭"""
    
    persona_name = context.get('persona', '30대 직장인')
    persona_data = PERSONAS.get(persona_name, {})
    product = context.get('product', '금융상품')
    product_data = COMPANY_PRODUCTS.get(context.get('company', ''), {}).get(product, {})
    persuasion = context.get('persuasion', 0)
    turn = context.get('turn', 1)
    prev_customer_msg = context.get('prev_msg', '')
    history = context.get('history', [])
    difficulty = context.get('difficulty', '💀 Hard (매운맛)')
    
    points = product_data.get("points", [])
    keywords = product_data.get("keywords", [])
    
    # 로컬 평가 (백업용) - 정확한 정보 체크 포함
    local_eval, local_gain = evaluate_answer_locally(user_input, keywords, product, product_data)
    
    # 대화 히스토리 구성
    conv_history = ""
    for h in history[-3:]:  # 최근 3개만
        conv_history += f"고객: {h.get('customer', '')}\n상담사: {h.get('user', '')}\n"
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        # 모델 목록 (우선순위대로 - 다양한 버전)
        model_names = [
            'gemini-2.5-flash-preview-05-20',
            'gemini-2.5-pro-preview-05-06',
            'gemini-2.5-flash-lite',
            'gemini-2.5-flash',
            'gemini-2.0-flash',
            'gemini-2.0-flash-exp',
            'gemini-2.0-flash-lite',
            'gemini-1.5-flash',
            'gemini-1.5-flash-latest',
            'gemini-1.5-flash-001',
            'gemini-1.5-flash-002',
            'gemini-1.5-pro',
            'gemini-1.5-pro-latest',
            'gemini-1.0-pro',
            'gemini-pro',
            'models/gemini-pro',
            'models/gemini-1.5-flash',
        ]
        st.session_state.last_model_used = None
        
        # 호감도 상태
        if persuasion < 25:
            mood = "경계하며 의심함, 설득이 필요함"
            mood_emoji = "😒"
        elif persuasion < 50:
            mood = "조금 관심을 보이지만 아직 확신이 없음"
            mood_emoji = "🤔"
        elif persuasion < 75:
            mood = "꽤 긍정적, 거의 설득됨"
            mood_emoji = "😊"
        else:
            mood = "매우 긍정적, 가입 직전"
            mood_emoji = "😍"
        
        # 난이도별 고객 성격 설정
        if "Hard" in difficulty or "매운맛" in difficulty:
            difficulty_mode = "hard"
            difficulty_personality = """
⚠️ **[매운맛 진상 고객 모드]**
- 당신은 극도로 까다롭고 의심 많은 진상 고객입니다
- 말투: 반말 섞어가며, 짜증 내며, 따지듯이 말함
- 예시: "아니 그게 말이 돼요?", "다른 은행에선 더 해준다던데", "솔직히 사기 아니에요?"
- 조금이라도 애매하면 바로 지적함
- 화가 나면 "본사에 컴플레인 넣겠습니다", "책임자 불러주세요" 등 강하게 압박
- 설득하기 매우 어려움 (점수 획득 기준 엄격)
- 담당자 바꿔달라, 지점장 나오라 등 압박 가능"""
        elif "Easy" in difficulty or "순한맛" in difficulty:
            difficulty_mode = "easy"
            difficulty_personality = """
🌱 **[순한맛 친절 고객 모드]**
- 당신은 친절하고 수용적인 고객입니다
- 말투: 공손하고 부드럽게, 존댓말 사용
- 상담사 말에 긍정적 반응을 보임
- 조금만 괜찮아도 관심을 표현함
- 설득하기 쉬움 (점수 획득 기준 관대)"""
        else:
            difficulty_mode = "normal"
            difficulty_personality = """
🔥 **[보통 난이도 일반 고객 모드]**
- 당신은 평범한 일반 고객입니다
- 말투: 보통의 존댓말, 중립적
- 합리적인 질문과 반응
- 좋은 설명에는 관심, 부족한 설명에는 의문 표현"""
        
        # 상품 상세 정보
        details = product_data.get("details", {})
        recommend_phrase = details.get("추천멘트", "")
        saving_effect = details.get("절약효과", details.get("세제혜택", ""))
        target_customer = details.get("대상고객", "")
        
        # 페르소나 상세 정보
        concerns = persona_data.get("concerns", [])
        speech_style = persona_data.get("speech_style", "")
        
        # 난이도별 평가 기준 (f-string 중첩 문제 방지를 위해 미리 생성)
        example_point = points[0] if points else '핵심혜택'
        
        if difficulty_mode == 'hard':
            eval_criteria = f"""[!] **[매운맛 엄격 평가 모드]**
**EXCELLENT (+20~25)**: 
- 완벽한 수치 + 실질적 효과 + 고객 맞춤 제안까지 필요
- 정확한 혜택 언급 + 구체적 금액 절약 효과 + 타 상품 비교 우위
- 예: "{example_point}" + 실제 절약 금액 + 왜 이게 최선인지

**GOOD (+10~15)**:
- 정확한 수치는 있지만 실질적 설득력 부족
- 일반적인 설명만으로는 부족

**AVERAGE (+3~8)**:
- 대부분의 답변이 여기 해당
- 수치 없이 장점만 나열

**POOR (0 또는 -10)**:
- 틀린 정보 -> 강하게 항의하고 본사 컴플레인 언급
- 애매한 답변 -> "제대로 모르시는 것 같은데요?"
- 상품과 무관한 답변 -> "시간 낭비시키지 마세요\""""
            reaction_style = "매우 까다롭게"
            speech_examples = """- 좋은 답변에도: "그래서 결론이 뭐예요?", "다른 은행은 더 해주던데?"
- 애매한 답변에: "아니 제대로 좀 설명해봐요", "이거 별로인 거 아니에요?"
- 나쁜 답변에: "본사에 얘기해야겠네요", "담당자 바꿔주세요", "책임자 불러요"
- 항상 뭔가 불만족스러운 표정, 의심하는 톤 유지"""
        elif difficulty_mode == 'easy':
            eval_criteria = """[순한맛 관대 평가 모드]
**EXCELLENT (+30~40)**: 
- 혜택을 언급하면 OK
- 정확한 수치가 아니어도 방향이 맞으면 인정

**GOOD (+20~30)**:
- 상품 관련 내용이면 대부분 인정
- 노력하는 모습 보이면 가산점

**AVERAGE (+10~15)**:
- 짧아도 관련 내용이면 OK
- 모호해도 시도한 것에 점수

**POOR (+5)**:
- 완전히 틀리거나 무관해도 격려
- 다음에 더 잘하면 된다는 분위기"""
            reaction_style = "관대하게"
            speech_examples = """- 좋은 답변에: 크게 기뻐하며 관심 표현 + 후속 질문
- 애매한 답변에도: 긍정적으로 반응하며 부드럽게 추가 정보 요청
- 나쁜 답변에: 조금 아쉬워하며 친절하게 다시 설명 요청"""
        else:
            eval_criteria = f"""[보통 난이도 표준 평가]
**EXCELLENT (+30~40)**: 
- 정확한 수치 포함 (예: "{example_point}" 정확히 언급)
- 고객 질문에 직접적으로 답변
- 혜택의 실질적 효과 설명 (예: "연간 10만원 절약")

**GOOD (+15~25)**:
- 상품 관련 맞는 내용이지만 수치가 부족함
- 일반적인 설명

**AVERAGE (+5~12)**:
- 너무 짧거나 애매함
- "좋아요", "괜찮아요" 같은 모호한 답변
- "~인 것 같아요", "아마" 같은 추측성 표현

**POOR (0 또는 -5)**:
- 틀린 정보 (예: 90%인데 50%라고 함)
- 질문과 무관한 답변
- "모르겠어요", "잘..." 같은 답변
- 상품 설명 안 하고 딴소리"""
            reaction_style = "평범하게"
            speech_examples = """- 좋은 답변에: 관심 표현 + 후속 질문
- 애매한 답변에: 아쉬움 + 더 구체적인 정보 요청
- 나쁜 답변에: 당황/짜증 + 제대로 된 설명 요구"""
        
        prompt = f'''당신은 은행에 방문한 실제 고객입니다. 배우처럼 캐릭터에 완전히 몰입해서 연기하세요.

## 당신의 캐릭터

**{persona_name}**
- 나이/직업: {persona_data.get('age', '30대')}, {persona_data.get('job', '직장인')}
- 성격/특징: {persona_data.get('style', '일반적')}
- 말투 스타일: {speech_style}
- 주요 관심사: {', '.join(concerns)}
- 현재 호감도: {persuasion}% {mood_emoji} ({mood})

{difficulty_personality}

## 상품 정보 (정확한 내용!)

**{product}**
- 핵심 혜택: {', '.join(points)}
- 절약 효과: {saving_effect}
- 추천 대상: {target_customer}
- 모범 답변 예시: "{recommend_phrase}"

중요: 위 정보가 정확한 내용입니다. 상담사가 다른 숫자나 틀린 정보를 말하면 지적해야 합니다!

## 대화 상황

{conv_history}
[고객(당신)]: {prev_customer_msg}
[상담사]: {user_input}

---

## 상담사 답변 평가

"{user_input}"

### 평가 기준 (난이도: {difficulty}):

{eval_criteria}

## 고객 반응 연기

당신은 {persona_name}입니다. 이 캐릭터답게 자연스럽게 반응하세요:

**반응 가이드:**
- 호감도 {persuasion}%인 상태에서의 반응
- {mood}
- 상담사의 답변 퀄리티에 따라 감정적으로 반응
- 난이도: {difficulty} ({reaction_style})

**말투 예시:**
{speech_examples}

**다음 질문 (이전과 다른 새로운 주제):**
- 가격/비용 관련
- 가입 절차/조건
- 다른 혜택
- 타사 비교
- 숨겨진 조건/단점
- 실제 사용 후기

## 📝 피드백 작성 (매우 구체적으로!)

**feedback_positive**: 
- 상담사가 "{user_input}"에서 구체적으로 뭘 잘했는지
- 예: "'환전 우대 90%'라고 정확한 수치를 언급해서 신뢰감을 줬어요"
- 잘한 게 없으면 빈 문자열

**feedback_improve**:
- 부족한 점 + 구체적 개선 예시
- 예: "수치만 말하지 말고 실질적 혜택을 설명하세요. '환전 우대 90%라서 10만원 환전 시 9천원 절약됩니다' 처럼요"

**tip**:
- 이 상황에서 효과적인 멘트 예시
- 예: "{recommend_phrase}"

---

JSON 형식으로만 응답:
{{"evaluation":"EXCELLENT/GOOD/AVERAGE/POOR","persuasion_gain":숫자,"customer_response":"캐릭터 말투로 자연스럽게 (이모지 1개)","feedback_positive":"구체적으로","feedback_improve":"개선점 + 예시","tip":"효과적인 멘트"}}'''

        # API 호출 설정
        generation_config = {
            "temperature": 0.9,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 1024,
        }
        
        # Safety 설정 (필터링 완화)
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        # 여러 모델 순차적으로 시도
        response = None
        last_model_error = None
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    prompt, 
                    generation_config=generation_config,
                    safety_settings=safety_settings
                )
                # 성공하면 모델 이름 저장하고 루프 탈출
                if response and response.text:
                    st.session_state.last_model_used = model_name
                    st.session_state.last_api_error = None
                    break
            except Exception as model_error:
                last_model_error = f"{model_name}: {str(model_error)[:50]}"
                continue
        
        # 모든 모델 실패 시
        if response is None:
            st.session_state.last_api_error = f"모든 모델 실패 - {last_model_error}"
            raise Exception(f"모든 모델 실패: {last_model_error}")
        
        # 응답 검증
        if not response:
            raise Exception("응답 없음")
        
        # Safety 필터로 차단된 경우 -> 다음 모델 시도 안하고 로컬로
        if response.candidates and len(response.candidates) > 0:
            finish_reason = response.candidates[0].finish_reason
            if finish_reason != 1:  # 1=STOP(정상), 2=SAFETY, 3=RECITATION 등
                st.session_state.last_api_error = f"Safety 필터 ({finish_reason})"
                raise Exception(f"Safety 필터: {finish_reason}")
        
        if not response.text:
            return {
                "evaluation": local_eval,
                "persuasion_gain": local_gain,
                "customer_response": "네, 계속요. 🤔",
                "feedback_positive": "",
                "feedback_improve": "",
                "tip": "",
                "api_fallback": True
            }
        
        text = response.text.strip()
        
        result = parse_json_response(text)
        
        if result and "evaluation" in result:
            eval_result = result.get("evaluation", "AVERAGE").upper()
            if eval_result not in ["EXCELLENT", "GOOD", "AVERAGE", "POOR"]:
                eval_result = local_eval
            
            gain = result.get("persuasion_gain", local_gain)
            if not isinstance(gain, (int, float)):
                gain = local_gain
            
            # 로컬 평가로 보정
            if local_eval == "POOR" and eval_result in ["EXCELLENT", "GOOD"]:
                eval_result = "AVERAGE"
                gain = min(gain, 5)
            
            gain = max(-5, min(40, int(gain)))
            
            # 등급별 점수 범위
            if eval_result == "POOR":
                gain = min(gain, 0)
            elif eval_result == "AVERAGE":
                gain = max(5, min(gain, 12))
            elif eval_result == "GOOD":
                gain = max(15, min(gain, 25))
            
            # 평가에 맞는 점수 범위 강제
            if eval_result == "POOR":
                gain = min(gain, 0)
            elif eval_result == "AVERAGE":
                gain = max(5, min(gain, 10))
            elif eval_result == "GOOD":
                gain = max(15, min(gain, 25))
            elif eval_result == "EXCELLENT":
                gain = max(30, min(gain, 40))
            
            return {
                "evaluation": eval_result,
                "persuasion_gain": gain,
                "customer_response": result.get("customer_response", "네, 좀 더 자세히 설명해주세요. 🤔"),
                "feedback_positive": result.get("feedback_positive", ""),
                "feedback_improve": result.get("feedback_improve", "상품의 핵심 혜택을 언급해보세요."),
                "tip": result.get("tip", f"'{keywords[0] if keywords else '혜택'}' 키워드를 활용해보세요.")
            }
        
        raise ValueError("JSON 파싱 실패")
        
    except Exception as e:
        # API 에러 로깅 및 저장 (디버깅용)
        error_msg = str(e)
        if "404" in error_msg:
            st.session_state.last_api_error = "404 - 모델을 찾을 수 없습니다."
        elif "403" in error_msg:
            st.session_state.last_api_error = "403 - API 키 권한 오류"
        elif "429" in error_msg:
            st.session_state.last_api_error = "429 - API 호출 한도 초과"
        else:
            st.session_state.last_api_error = error_msg[:100]
        print(f"[Gemini API Error] {error_msg}")
        
        # 로컬 평가 사용 (백업) - 페르소나별 응답
        import random
        
        # 페르소나별 응답
        persona_responses = {
            "20대 사회초년생 김신한": {
                "poor": ["에?? 그게 뭔 말이에요? 😅", "아 잘 모르겠는데요... 다시 설명해주실래요?", "네? 상품 얘기 해주세요 ㅋㅋ"],
                "avg": ["음~ 그렇구나... 근데 정확히 어떤 혜택이에요?", "아 그런가요? 좀 더 자세히요!", "오 근데 구체적으로 얼마나 좋은 건데요?"],
                "good": ["오 진짜요?? 완전 좋은데요! 😆", "헐 그거 대박이에요! 다른 건요?", "와 그거 진짜 괜찮네요!"],
            },
            "30대 맞벌이 이행복": {
                "poor": ["죄송한데 무슨 말씀이신지... 핵심만 말씀해주세요.", "시간이 없어서요, 상품 설명 부탁드려요.", "네? 그게 상품이랑 무슨 관련이죠?"],
                "avg": ["네, 알겠어요. 구체적으로 어떤 혜택이 있나요?", "그래서 정확히 얼마나 절약되는 건가요?", "음, 좀 더 자세히 알 수 있을까요?"],
                "good": ["아 그 정도면 괜찮네요! 다른 혜택도 있나요?", "오 실용적이네요. 가입은 어떻게 해요?", "좋네요, 더 설명해주세요."],
            },
            "40대 자영업 박사장": {
                "poor": ["야 그게 무슨 말이야? 상품 설명을 해봐.", "뭐? 다시 말해봐.", "아니 장난해? 제대로 설명해."],
                "avg": ["그래서 내가 얼마나 이득인 건데?", "음, 정확한 숫자로 말해봐.", "다른 데랑 비교하면 어때?"],
                "good": ["오 그거 괜찮은데? 더 있어?", "그거 쓸만하겠네. 수수료는?", "좋아, 계속 말해봐."],
            },
            "50대 은퇴준비 최부장": {
                "poor": ["잘 모르겠는데요... 다시 설명해주시겠습니까?", "그게 무슨 말씀이신지... 🤔", "죄송한데 이해가 안 되네요."],
                "avg": ["그렇습니까... 좀 더 자세히 알 수 있을까요?", "흠, 정확한 내용이 궁금합니다.", "원금은 보장되는 거죠?"],
                "good": ["아, 그건 괜찮아 보이는군요. 😊", "흠, 안전하다면 고려해볼게요.", "좋네요, 더 설명해주세요."],
            },
        }
        
        p_resp = persona_responses.get(persona_name, persona_responses["30대 맞벌이 이행복"])
        
        if local_eval == "POOR":
            resp = random.choice(p_resp["poor"])
            fb_imp = f"상품과 관련된 내용으로 대답하세요. 예: '{points[0] if points else '핵심 혜택'}' 언급"
        elif local_eval == "AVERAGE":
            resp = random.choice(p_resp["avg"])
            fb_imp = f"구체적인 수치를 언급하세요. 예: '{points[0] if points else '정확한 혜택'}'"
        else:
            resp = random.choice(p_resp["good"])
            fb_imp = "좋아요! 이 흐름을 유지하면서 다른 혜택도 언급해보세요."
        
        return {
            "evaluation": local_eval,
            "persuasion_gain": local_gain,
            "customer_response": resp,
            "feedback_positive": "" if local_eval == "POOR" else "상품 관련 내용을 언급했어요.",
            "feedback_improve": fb_imp,
            "tip": f"'{keywords[0] if keywords else '혜택'}' 같은 키워드를 사용해보세요.",
            "api_fallback": True  # API 호출 실패 플래그
        }

# ============================================================
# 🎮 세션
# ============================================================

# Gemini API Key (고정)
# 환경 변수에서 API 키 가져오기 (배포 환경용)
# 하드코딩된 API 키는 보안상 제거됨 - 유출 시 비활성화됨
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", st.secrets["GEMINI_API_KEY"])

def init_session():
    defaults = {
        "game_state": "intro",
        "game_mode": "ai",  # 기본 AI 모드
        "api_key": GEMINI_API_KEY,  # Gemini API Key
        "last_evaluation": "AVERAGE",
        "api_error": False,  # API 에러 플래그
        "company": "🏦 신한은행",
        "product": "SOL트래블 체크카드",
        "difficulty": "💀 Hard (매운맛)",
        "persona": "20대 사회초년생 김신한",
        "persuasion": 0,  # 설득도 (0~100)
        "score": 0,
        "turn": 0,
        "scenarios": [],
        "scenario_idx": 0,
        "history": [],
        "current_msg": "",
        "last_gain": 0,
        "show_gain": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
    
    # API 키가 비어있으면 강제로 다시 설정
    if not st.session_state.api_key:
        st.session_state.api_key = GEMINI_API_KEY

init_session()

# ============================================================
# 🎨 렌더링
# ============================================================

def render_persuasion_gauge():
    """호감도 게이지 (상승형)"""
    p = min(100, st.session_state.persuasion)
    
    # 호감도에 따른 하트 이모지
    if p < 30:
        heart = "🤍"
        status = "아직 관심이 없어요..."
    elif p < 60:
        heart = "💗"
        status = "조금씩 관심이 생기고 있어요!"
    elif p < 85:
        heart = "💕"
        status = "많이 마음에 드시는 것 같아요!"
    else:
        heart = "💝"
        status = "거의 마음을 얻었어요!"
    
    st.markdown(f"""
    <div class="gauge-section">
        <div class="gauge-header">
            <span>{heart} 호감도 - {status}</span>
            <span style="color:#FF1493;font-size:18px;">{p}%</span>
        </div>
        <div class="gauge-bar-bg">
            <div class="gauge-bar-fill" style="width: {p}%;">{"💕 " if p > 50 else ""}{p}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_customer():
    p = PERSONAS.get(st.session_state.persona, {})
    image_name = p.get('image', '')
    image_url = get_persona_image(image_name) if image_name else ''
    
    # 이미지와 정보 표시 (이미지 크게)
    st.markdown(f"""
    <div class="customer-card" style="text-align:center;padding:10px;">
        <img src="{image_url}" class="customer-image-large" onerror="this.style.display='none'">
        <div style="font-size:16px;font-weight:700;color:#FF1493;margin-bottom:4px;">{st.session_state.persona.split()[-1]}</div>
        <div style="color:#666;font-size:11px;">{p.get('age', '')} | {p.get('job', '')}</div>
            </div>
    """, unsafe_allow_html=True)

def render_tips():
    pd = COMPANY_PRODUCTS.get(st.session_state.company, {}).get(st.session_state.product, {})
    points = pd.get("points", [])
    keywords = pd.get("keywords", [])[:6]
    details = pd.get("details", {})
    recommend = details.get("추천멘트", "")
    
    # 접힌 상태의 힌트 박스
    with st.expander("💡 힌트 보기 (상품 정보)", expanded=False):
        st.markdown(f"**📌 {st.session_state.product}**")
        for p in points:
            st.markdown(f"- {p}")
        st.markdown("**🔑 키워드:**")
        st.markdown(" | ".join([f"`{k}`" for k in keywords]))
        if recommend:
            st.info(f"💬 **추천 멘트:** {recommend}")

def render_stats():
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="stat-box"><div class="stat-label">SCORE</div><div class="stat-value">{st.session_state.score:,}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="stat-box"><div class="stat-label">TURN</div><div class="stat-value">{st.session_state.turn}</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="stat-box"><div class="stat-label">설득도</div><div class="stat-value">{min(100, st.session_state.persuasion)}%</div></div>', unsafe_allow_html=True)

def render_stats_inline():
    """스탯을 한 줄에 표시"""
    st.markdown(f"""
    <div style="display:flex;justify-content:center;gap:15px;margin:5px 0;">
        <div class="stat-box" style="min-width:70px;">
            <div class="stat-label">SCORE</div>
            <div class="stat-value">{st.session_state.score:,}</div>
        </div>
        <div class="stat-box" style="min-width:70px;">
            <div class="stat-label">TURN</div>
            <div class="stat-value">{st.session_state.turn}</div>
        </div>
        <div class="stat-box" style="min-width:70px;">
            <div class="stat-label">설득도</div>
            <div class="stat-value">{min(100, st.session_state.persuasion)}%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_dialogue():
    # 고객 이름 가져오기
    customer_name = st.session_state.persona.split()[-1] if st.session_state.persona else "고객님"
    
    st.markdown('<div class="dialogue-area">', unsafe_allow_html=True)
    
    for item in st.session_state.history:
        # 고객 메시지 (비주얼 노벨 스타일)
        st.markdown(f"""
        <div class="msg-box msg-customer">
            <div class="msg-speaker">{customer_name}</div>
            <div class="msg-text">{item['customer']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # 내 메시지 + 평가
        eval_badge = item.get('evaluation', '')
        eval_colors = {"EXCELLENT": "#FFD700", "GOOD": "#00C851", "AVERAGE": "#87CEEB", "POOR": "#ff4444"}
        eval_color = eval_colors.get(eval_badge, "#87CEEB")
        badge_html = f'<span style="background:{eval_color};color:#000;padding:3px 10px;border-radius:4px;font-size:12px;font-weight:700;margin-left:10px;">{eval_badge}</span>' if eval_badge else ''
        
        st.markdown(f"""
        <div class="msg-box msg-user">
            <div class="msg-speaker">나 (상담사){badge_html}</div>
            <div class="msg-text">{item['user']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 현재 고객 메시지
    if st.session_state.current_msg:
        st.markdown(f"""
        <div class="msg-box msg-customer">
            <div class="msg-speaker">{customer_name}</div>
            <div class="msg-text">{st.session_state.current_msg}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 점수 팝업 (평가 등급 기반)
    if st.session_state.show_gain:
        gain = st.session_state.last_gain
        evaluation = st.session_state.get('last_evaluation', 'AVERAGE')
        
        popup_colors = {"EXCELLENT": "#FFD700", "GOOD": "#00C851", "AVERAGE": "#87CEEB", "POOR": "#ff4444"}
        popup_color = popup_colors.get(evaluation, "#87CEEB")
        
        display_gain = f"+{gain}%" if gain >= 0 else f"{gain}%"
        st.markdown(f'<div class="score-popup" style="color:{popup_color};">{evaluation} {display_gain}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 상담 종료 버튼
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🏁 상담 종료하기", key="end_consultation", use_container_width=True):
            # 설득도 70% 이상이면 성공, 아니면 실패
            if st.session_state.persuasion >= 70:
                st.session_state.game_state = "victory"
            else:
                st.session_state.game_state = "defeat"
            st.rerun()

def generate_text_report(history, coaching, is_victory, grade, eval_counts):
    """텍스트 형식의 보고서 생성 (PDF 생성 실패 시 대안)"""
    report = []
    report.append("=" * 50)
    report.append("💕 두근두근 신한 - 상담 결과 리포트")
    report.append("=" * 50)
    report.append(f"생성일: {datetime.now().strftime('%Y년 %m월 %d일 %H:%M')}")
    report.append("")
    report.append(f"종합 등급: {grade}")
    report.append(f"상담 결과: {'계약 성사!' if is_victory else '계약 미성사'}")
    report.append(f"총 대화 횟수: {len(history)}턴")
    report.append("")
    report.append("[ 평가 통계 ]")
    report.append(f"  EXCELLENT: {eval_counts.get('EXCELLENT', 0)}회")
    report.append(f"  GOOD: {eval_counts.get('GOOD', 0)}회")
    report.append(f"  AVERAGE: {eval_counts.get('AVERAGE', 0)}회")
    report.append(f"  POOR: {eval_counts.get('POOR', 0)}회")
    report.append("")
    
    if coaching:
        overall = coaching.get('overall_assessment', '')
        if overall:
            report.append("[ 종합 평가 ]")
            report.append(overall)
            report.append("")
        
        strengths = coaching.get('strength_analysis', [])
        if strengths:
            report.append("[ 강점 ]")
            for item in strengths:
                if isinstance(item, dict):
                    report.append(f"• {item.get('point', '')}")
                else:
                    report.append(f"• {item}")
            report.append("")
        
        improvements = coaching.get('improvement_analysis', [])
        if improvements:
            report.append("[ 보완점 ]")
            for item in improvements:
                if isinstance(item, dict):
                    report.append(f"• {item.get('point', '')}")
                    if item.get('better_response'):
                        report.append(f"  → 개선 답변: {item.get('better_response', '')}")
                else:
                    report.append(f"• {item}")
            report.append("")
    
    report.append("=" * 50)
    report.append("[ 대화 내역 및 피드백 ]")
    report.append("=" * 50)
    
    for i, item in enumerate(history):
        ev = item.get('evaluation', 'AVERAGE')
        gain = item.get('gain', 0)
        report.append("")
        report.append(f"--- Turn {i+1} [{ev}] {('+' if gain >= 0 else '')}{gain}% ---")
        report.append(f"고객: {item.get('customer', '')}")
        report.append(f"나: {item.get('user', '')}")
        
        feedback_pos = item.get('feedback_positive', '')
        feedback_imp = item.get('feedback_improve', '')
        if feedback_pos:
            report.append(f"  ✓ {feedback_pos}")
        if feedback_imp:
            report.append(f"  → {feedback_imp}")
    
    return "\n".join(report).encode('utf-8')

def get_ai_coaching(history, product, persona, is_victory, api_key, company):
    """AI를 활용한 상세 코칭 피드백 생성"""
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        # 모델 선택 (여러 모델 시도)
        model = None
        model_names = [
            'gemini-2.5-flash-preview-05-20',
            'gemini-2.5-pro-preview-05-06', 
            'gemini-2.5-flash-lite',
            'gemini-2.5-flash',
            'gemini-2.0-flash',
            'gemini-1.5-flash',
            'gemini-1.5-pro',
            'gemini-pro',
        ]
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                break
            except:
                continue
        if model is None:
            model = genai.GenerativeModel('gemini-pro')
        
        # 상품 정보 가져오기
        product_data = COMPANY_PRODUCTS.get(company, {}).get(product, {})
        points = product_data.get("points", [])
        keywords = product_data.get("keywords", [])
        
        # 대화 내용 상세 정리
        conversation = ""
        for i, item in enumerate(history):
            ev = item.get('evaluation', 'AVERAGE')
            gain = item.get('gain', 0)
            conversation += f"[Turn {i+1}] 평가: {ev}, +{gain}%\n"
            conversation += f"고객: \"{item['customer']}\"\n"
            conversation += f"상담사: \"{item['user']}\"\n\n"
        
        prompt = f'''신한금융 세일즈 코치로서 상담을 분석해줘.

[상담 정보]
- 상품: {product}
- 상품 혜택: {', '.join(points[:3]) if points else '없음'}
- 고객: {persona}
- 결과: {'성공' if is_victory else '실패'}

[대화 내용]
{conversation}

아래 JSON 형식으로만 답변해. 다른 텍스트 없이 JSON만:

{{
  "flow_analysis": "대화 흐름 분석 (상담이 어떻게 진행되었는지 3문장)",
  "overall_assessment": "종합 평가 (잘한점, 아쉬운점 포함 3문장)",
  "communication_score": "A~D",
  "product_knowledge_score": "A~D",
  "customer_handling_score": "A~D",
  "strength_analysis": [
    {{"point": "강점1 제목", "detail": "구체적 설명과 실제 대화 인용"}},
    {{"point": "강점2 제목", "detail": "구체적 설명과 실제 대화 인용"}}
  ],
  "improvement_analysis": [
    {{"point": "보완점1 제목", "detail": "문제점 설명", "suggestion": "이렇게 말했으면 좋았을 답변"}},
    {{"point": "보완점2 제목", "detail": "문제점 설명", "suggestion": "이렇게 말했으면 좋았을 답변"}}
  ],
  "key_tips": ["실천 팁1", "실천 팁2", "실천 팁3"]
}}'''

        generation_config = {
            "temperature": 0.8,
            "top_p": 0.95,
            "max_output_tokens": 2048,
        }
        
        # Safety 설정 (필터링 완화)
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
        
        response = model.generate_content(
            prompt, 
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        if not response:
            return None
        
        # Safety 필터로 차단된 경우
        if response.candidates and response.candidates[0].finish_reason != 1:
            return None
        
        if not response.text:
            return None
        
        text = response.text.strip()
        
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            text = text.split("```")[1].split("```")[0]
        
        return json.loads(text.strip())
    except Exception as e:
        return None


def render_report(is_victory):
    """종합 리포트 (페이지 네비게이션 포함)"""
    turns = st.session_state.turn
    history = st.session_state.history
    
    # 리포트 페이지 상태 초기화
    if 'report_page' not in st.session_state:
        st.session_state.report_page = 1
    
    # 평가 통계
    eval_counts = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "POOR": 0}
    for item in history:
        ev = item.get('evaluation', 'AVERAGE')
        if ev in eval_counts:
            eval_counts[ev] += 1
    
    # 등급 계산
    excellent_ratio = eval_counts["EXCELLENT"] / max(1, turns)
    good_ratio = (eval_counts["EXCELLENT"] + eval_counts["GOOD"]) / max(1, turns)
    
    if is_victory:
        if excellent_ratio >= 0.5:
            grade = "S"
        elif good_ratio >= 0.6:
            grade = "A"
        else:
            grade = "B"
    else:
        if good_ratio >= 0.4:
            grade = "C"
        else:
            grade = "D"
    
    # AI 코칭 데이터 (한 번만 로드)
    coaching = None
    ai_coaching_success = False
    
    if st.session_state.game_mode == "ai" and st.session_state.api_key:
        if 'last_coaching' not in st.session_state or st.session_state.last_coaching is None:
            with st.spinner("🤖 AI 코치가 분석 중..."):
                coaching = get_ai_coaching(
                    history, 
                    st.session_state.product, 
                    st.session_state.persona,
                    is_victory, 
                    st.session_state.api_key,
                    st.session_state.company
                )
                st.session_state.last_coaching = coaching
        else:
            coaching = st.session_state.last_coaching
        
        if coaching:
            ai_coaching_success = True
    
    # 페이지 제목
    st.markdown(f"""
    <div style="text-align:center;margin-bottom:20px;">
        <span style="background:linear-gradient(135deg,#FF69B4,#FF1493);color:white;padding:8px 20px;border-radius:20px;font-size:14px;">
            📄 페이지 {st.session_state.report_page} / 3
        </span>
            </div>
    """, unsafe_allow_html=True)
    
    # ========== 페이지 1: 결과 요약 ==========
    if st.session_state.report_page == 1:
        result_msg = f'💕 {turns}턴 만에 고객의 마음을 얻었어요!' if is_victory else f'💔 호감도 {st.session_state.persuasion}%에서 아쉽게 마무리...'
        
        st.markdown(f"""
        <div class="report-card">
            <div class="report-title">💝 상담 결과 리포트</div>
            <div class="grade-box">
                <span class="grade-letter grade-{grade.lower() if grade != 'D' else 'c'}">{grade}</span>
        </div>
        <div style="text-align:center;color:#555;font-size:16px;margin:10px 0;">
            {result_msg}
    </div>
        <div style="display:flex;justify-content:center;gap:20px;margin-top:15px;">
            <div style="text-align:center;background:#FFF0F5;padding:10px 15px;border-radius:12px;">
                <div style="color:#FF1493;font-size:22px;font-weight:700;">{eval_counts['EXCELLENT']}</div>
                <div style="color:#FF1493;font-size:11px;">EXCELLENT</div>
            </div>
            <div style="text-align:center;background:#FFF0F5;padding:10px 15px;border-radius:12px;">
                <div style="color:#FF69B4;font-size:22px;font-weight:700;">{eval_counts['GOOD']}</div>
                <div style="color:#FF69B4;font-size:11px;">GOOD</div>
            </div>
            <div style="text-align:center;background:#F0F8FF;padding:10px 15px;border-radius:12px;">
                <div style="color:#4682B4;font-size:22px;font-weight:700;">{eval_counts['AVERAGE']}</div>
                <div style="color:#4682B4;font-size:11px;">AVERAGE</div>
            </div>
            <div style="text-align:center;background:#FFF5EE;padding:10px 15px;border-radius:12px;">
                <div style="color:#CD853F;font-size:22px;font-weight:700;">{eval_counts['POOR']}</div>
                <div style="color:#CD853F;font-size:11px;">POOR</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        # AI 코칭 대화 흐름 (있으면)
        if ai_coaching_success and coaching:
            flow = coaching.get('flow_analysis', '')
            overall = coaching.get('overall_assessment', '')
            if flow:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,#E8F4FD,#D1E8FF);border-radius:15px;padding:20px;margin:20px 0;border:2px solid #4A90D9;">
                    <h4 style="color:#2E6BA6;margin:0 0 10px 0;">📊 대화 흐름 분석</h4>
                    <p style="color:#333;margin:0;line-height:1.8;font-size:15px;">{flow}</p>
                </div>
                """, unsafe_allow_html=True)
            if overall:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,#FFF0F5,#FFE4EC);border-radius:15px;padding:20px;border:2px solid #FF69B4;">
                    <h4 style="color:#FF69B4;margin:0 0 10px 0;">📋 종합 평가</h4>
                    <p style="color:#333;margin:0;line-height:1.8;font-size:15px;">{overall}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # ========== 페이지 2: 강점 & 보완점 ==========
    elif st.session_state.report_page == 2:
        st.markdown("### 🎓 상세 분석 리포트")
        
        if ai_coaching_success and coaching:
            # AI 기반 강점
            st.markdown("### ✅ 직원의 강점")
            strength_list = coaching.get('strength_analysis', [])
            for item in strength_list:
                if isinstance(item, dict):
                    point = item.get('point', '')
                    detail = item.get('detail', '') or item.get('quote', '') or item.get('why_good', '')
                    st.markdown(f"""
                    <div style="background:#F0FFF0;border-radius:12px;padding:15px;margin-bottom:12px;border-left:4px solid #228B22;">
                        <div style="color:#228B22;font-weight:700;margin-bottom:8px;font-size:16px;">💚 {point}</div>
                        <div style="color:#333;font-size:14px;line-height:1.7;">{detail}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background:#F0FFF0;border-radius:12px;padding:12px;margin-bottom:8px;border-left:4px solid #228B22;">
                        <span style="color:#228B22;">💚 {item}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            # AI 기반 보완점
            st.markdown("### 💡 개선이 필요한 부분")
            improve_list = coaching.get('improvement_analysis', [])
            for item in improve_list:
                if isinstance(item, dict):
                    point = item.get('point', '')
                    detail = item.get('detail', '') or item.get('original', '')
                    suggestion = item.get('suggestion', '') or item.get('better_response', '')
                    st.markdown(f"""
                    <div style="background:#FFF5EE;border-radius:12px;padding:15px;margin-bottom:12px;border-left:4px solid #FF6347;">
                        <div style="color:#FF6347;font-weight:700;margin-bottom:8px;font-size:16px;">⚠️ {point}</div>
                        <div style="color:#555;font-size:14px;margin-bottom:10px;">{detail}</div>
                        {f'<div style="background:#E8FFE8;padding:12px;border-radius:8px;"><div style="font-size:12px;color:#228B22;margin-bottom:5px;">✨ 이렇게 말해보세요:</div><div style="color:#228B22;font-weight:500;font-size:14px;">"{suggestion}"</div></div>' if suggestion else ''}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background:#FFF5EE;border-radius:12px;padding:12px;margin-bottom:8px;border-left:4px solid #FF6347;">
                        <span style="color:#FF6347;">⚠️ {item}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            # 실천 팁
            tips = coaching.get('key_tips', []) or coaching.get('action_items', [])
            if tips:
                st.markdown("### 🚀 실천 팁")
                for i, tip in enumerate(tips):
                    st.markdown(f"""
                    <div style="background:linear-gradient(135deg,#FFF0F5,#FFE4EC);border-radius:12px;padding:15px;margin-bottom:10px;border-left:4px solid #FF69B4;">
                        <span style="background:#FF69B4;color:white;padding:3px 10px;border-radius:10px;font-size:12px;font-weight:700;">TIP {i+1}</span>
                        <p style="color:#333;margin:10px 0 0 0;font-size:14px;">{tip}</p>
                    </div>
    """, unsafe_allow_html=True)
        else:
            # 기본 강점/보완점
            excellent_count = eval_counts.get("EXCELLENT", 0)
            good_count = eval_counts.get("GOOD", 0)
            poor_count = eval_counts.get("POOR", 0)
            average_count = eval_counts.get("AVERAGE", 0)
            
            st.markdown("### ✅ 직원의 강점")
            strengths = []
            good_turns = [item for item in history if item.get('evaluation') in ['EXCELLENT', 'GOOD']]
            if good_turns:
                strengths.append(f"효과적인 응대 - '{good_turns[0].get('user', '')[:40]}...' 같은 답변이 좋았습니다.")
            if excellent_count > 0:
                strengths.append(f"핵심 혜택 전달 ({excellent_count}회 EXCELLENT)")
            if good_count > 0:
                strengths.append(f"적절한 대응력 ({good_count}회 GOOD)")
            if is_victory:
                strengths.append("끈기 있게 상담하여 설득 성공!")
            if not strengths:
                strengths.append("상담 경험을 쌓고 있습니다.")
            
            for s in strengths[:3]:
                st.markdown(f"""
                <div style="background:#F0FFF0;border-radius:12px;padding:12px;margin-bottom:8px;border-left:4px solid #228B22;">
                    <span style="color:#228B22;">💚 {s}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("### 💡 개선이 필요한 부분")
            improvements = []
            if poor_count > 0:
                improvements.append(f"답변 품질 개선 필요 ({poor_count}회 POOR)")
            if average_count > 0:
                improvements.append(f"차별화된 어필 필요 ({average_count}회 AVERAGE)")
            if not is_victory:
                improvements.append("고객 거절 시 다른 각도로 접근해보세요")
            if not improvements:
                improvements.append("다양한 멘트를 연습해보세요")
            
            for imp in improvements[:3]:
                st.markdown(f"""
                <div style="background:#FFF5EE;border-radius:12px;padding:12px;margin-bottom:8px;border-left:4px solid #FF6347;">
                    <span style="color:#FF6347;">⚠️ {imp}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # ========== 페이지 3: 대화 복기 & 다운로드 ==========
    elif st.session_state.report_page == 3:
        st.markdown("### 📝 대화 복기")
        
        for i, item in enumerate(history):
            ev = item.get('evaluation', 'AVERAGE')
            gain = item.get('gain', 0)
            ev_colors = {"EXCELLENT": "#FF1493", "GOOD": "#FF69B4", "AVERAGE": "#4682B4", "POOR": "#CD853F"}
            ev_color = ev_colors.get(ev, "#4682B4")
            
            feedback_pos = item.get('feedback_positive', '')
            feedback_imp = item.get('feedback_improve', '')
            tip = item.get('tip', '')
            
            feedback_html = ""
            if feedback_pos:
                feedback_html += f'<div style="color:#228B22;">✅ {feedback_pos}</div>'
            if feedback_imp:
                feedback_html += f'<div style="color:#FF6347;">💡 {feedback_imp}</div>'
            if tip:
                feedback_html += f'<div style="color:#4682B4;">📌 {tip}</div>'
            
            st.markdown(f"""
            <div class="history-item" style="border-left-color:{ev_color};">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                    <span class="history-turn">Turn {i+1}</span>
                    <span style="background:{ev_color};color:white;padding:4px 12px;border-radius:12px;font-size:12px;font-weight:700;">
                        {ev} {'+' if gain >= 0 else ''}{gain}%
                    </span>
                </div>
                <div class="history-customer">💬 고객: {item['customer']}</div>
                <div class="history-user">💼 나: {item['user']}</div>
                {f'<div style="margin-top:12px;padding-top:12px;border-top:1px solid #FFB6C1;font-size:13px;">{feedback_html}</div>' if feedback_html else ''}
            </div>
            """, unsafe_allow_html=True)
        
        # 텍스트 리포트 다운로드 버튼
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📥 리포트 다운로드")
        
        coaching_data = st.session_state.get('last_coaching', None)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                report_data = generate_text_report(history, coaching_data, is_victory, grade, eval_counts)
                filename = f"상담리포트_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
                
                st.download_button(
                    label="📄 레포트를 텍스트 파일로 다운받기",
                    data=report_data,
                    file_name=filename,
                    mime="text/plain",
                    use_container_width=True,
                    key="download_report"
                )
            except Exception as e:
                st.error(f"리포트 생성 오류: {e}")
    
    # ========== 하단 네비게이션 버튼 ==========
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.session_state.report_page > 1:
            if st.button("⬅️ 이전", key="prev_page", use_container_width=True):
                st.session_state.report_page -= 1
                st.rerun()
    
    with col2:
        # 페이지 표시
        st.markdown(f"""
        <div style="text-align:center;padding:10px;">
            <span style="color:#FF69B4;font-size:14px;">
                {'●' if st.session_state.report_page == 1 else '○'} 
                {'●' if st.session_state.report_page == 2 else '○'} 
                {'●' if st.session_state.report_page == 3 else '○'}
            </span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        if st.session_state.report_page < 3:
            if st.button("다음 ➡️", key="next_page", use_container_width=True):
                st.session_state.report_page += 1
                st.rerun()

# ============================================================
# 🎮 로직
# ============================================================

def process_input(user_input):
    pd = COMPANY_PRODUCTS.get(st.session_state.company, {}).get(st.session_state.product, {})
    keywords = pd.get("keywords", [])
    
    if st.session_state.game_mode == "demo":
        # 체험 모드 (기존 로직)
        scenarios = st.session_state.scenarios
        idx = st.session_state.scenario_idx
        
        if idx < len(scenarios):
            sc = scenarios[idx]
            sc_keywords = sc.get("keywords", keywords)
            
            user_lower = user_input.lower()
            matched = sum(1 for k in sc_keywords if k in user_lower)
            
            if matched >= 1:
                gain = sc["gain_good"]
                feedback = sc["feedback_good"]
            else:
                gain = sc["gain_ok"]
                feedback = sc["feedback_ok"]
            
            st.session_state.persuasion += gain
            st.session_state.score += gain * 10
            st.session_state.last_gain = gain
            st.session_state.show_gain = True
            
            st.session_state.history.append({
                "customer": sc["customer"],
                "user": user_input,
                "gain": gain,
                "feedback": feedback,
                "evaluation": "GOOD" if matched >= 1 else "AVERAGE",
            })
            
            st.session_state.turn += 1
            st.session_state.scenario_idx += 1
            
            if st.session_state.persuasion >= 100:
                st.session_state.current_msg = "좋아요! 말씀하신 혜택들이 정말 좋네요. 가입할게요! 😊"
                st.session_state.game_state = "victory"
            elif st.session_state.scenario_idx < len(scenarios):
                st.session_state.current_msg = scenarios[st.session_state.scenario_idx]["customer"]
            else:
                if st.session_state.persuasion >= 100:
                    st.session_state.game_state = "victory"
                else:
                    st.session_state.game_state = "defeat"
    else:
        # AI 모드 (Gemini 정교한 평가)
        context = {
            "persona": st.session_state.persona,
            "company": st.session_state.company,
            "product": st.session_state.product,
            "persuasion": st.session_state.persuasion,
            "turn": st.session_state.turn + 1,
            "keywords": keywords,
            "prev_msg": st.session_state.current_msg,
            "history": st.session_state.history,  # 대화 맥락 전달
            "difficulty": st.session_state.difficulty,  # 난이도 전달
        }
        
        result = get_gemini_response(st.session_state.api_key, user_input, context)
        
        # API 폴백 사용 여부 확인 (evaluation이 로컬 평가와 동일하면 API 실패 가능성)
        if result.get("api_fallback"):
            st.session_state.api_error = True
        else:
            st.session_state.api_error = False
        
        # 결과 추출
        evaluation = result.get("evaluation", "AVERAGE")
        gain = result.get("persuasion_gain", 0)
        customer_response = result.get("customer_response", "네, 계속 설명해주세요. 🤔")
        feedback_pos = result.get("feedback_positive", "")
        feedback_imp = result.get("feedback_improve", "")
        tip = result.get("tip", "")
        
        # 점수 계산 (POOR면 0점)
        if evaluation == "POOR":
            gain = max(-5, gain)  # POOR는 마이너스 가능
            score_add = 0
        else:
            gain = max(0, gain)
            score_add = gain * 10
        
        st.session_state.persuasion = max(0, st.session_state.persuasion + gain)
        st.session_state.score += score_add
        st.session_state.last_gain = gain
        st.session_state.last_evaluation = evaluation
        st.session_state.show_gain = True
        
        # 피드백 조합
        feedback_parts = []
        if feedback_pos:
            feedback_parts.append(f"✅ {feedback_pos}")
        if feedback_imp:
            feedback_parts.append(f"💡 {feedback_imp}")
        if tip:
            feedback_parts.append(f"📌 {tip}")
        feedback = " | ".join(feedback_parts) if feedback_parts else "다음 답변에서 더 구체적으로 설명해보세요."
        
        st.session_state.history.append({
            "customer": st.session_state.current_msg,
            "user": user_input,
            "gain": gain,
            "evaluation": evaluation,
            "feedback": feedback,
            "feedback_positive": feedback_pos,
            "feedback_improve": feedback_imp,
            "tip": tip,
        })
        
        st.session_state.current_msg = customer_response
        
        st.session_state.turn += 1
        
        # 승리 체크
        if st.session_state.persuasion >= 100:
            st.session_state.game_state = "victory"
    
    # 턴 제한 없음 - 상담 종료 버튼으로 종료

def start_game():
    st.session_state.game_state = "playing"
    st.session_state.persuasion = 0
    st.session_state.score = 0
    st.session_state.turn = 0
    st.session_state.scenario_idx = 0
    st.session_state.history = []
    st.session_state.show_gain = False
    st.session_state.last_evaluation = "AVERAGE"
    
    st.session_state.scenarios = get_scenarios(
        st.session_state.company,
        st.session_state.product,
        st.session_state.persona,
        st.session_state.difficulty
    )
    
    # 첫 메시지 (페르소나별)
    persona = st.session_state.persona
    product = st.session_state.product
    
    first_messages = {
        "20대 사회초년생 김신한": f"아 저기요~ 친구가 {product} 좋다고 해서 왔는데요, 근데 솔직히 이런 거 잘 몰라서... 뭐가 좋은 건지 쉽게 설명해주실 수 있어요? 😅",
        "30대 맞벌이 이행복": f"안녕하세요. {product} 문의드리려고요. 애들 학원 데려다줘야 해서 시간이 좀 촉박한데, 핵심만 빠르게 설명해주실 수 있을까요?",
        "40대 자영업 박사장": f"아 예, {product} 있다고 해서 왔는데... 요즘 장사가 안 돼서 돈 아끼려고 알아보는 건데, 진짜 혜택 있는 거 맞아요? 솔직히 말해봐요.",
        "50대 은퇴준비 최부장": f"실례합니다. {product}에 대해서 좀 여쭤보려고 하는데요... 요즘 뉴스 보면 금융사기가 너무 많아서요. 이거 안전한 거 맞죠? 🤔",
    }
    
    if st.session_state.game_mode == "demo" and st.session_state.scenarios:
        st.session_state.current_msg = st.session_state.scenarios[0]["customer"]
    else:
        st.session_state.current_msg = first_messages.get(persona, f"안녕하세요! {product}에 대해 설명해주세요. 🤔")

def reset_game():
    keys = ["game_state", "persuasion", "score", "turn", "scenario_idx", "history", "current_msg", "show_gain", "last_gain"]
    for k in keys:
        if k in st.session_state:
            del st.session_state[k]
    init_session()

# ============================================================
# 📺 화면
# ============================================================

def render_sidebar():
    with st.sidebar:
        # 사이드바 최상단 닫기 버튼
        close_col1, close_col2, close_col3 = st.columns([1, 3, 1])
        with close_col3:
            if st.button("✖️", key="sidebar_close_btn", help="메뉴 닫기"):
                st.session_state.sidebar_visible = False
                st.rerun()
        
        # 타이틀
        st.markdown("## 💕 두근두근 신한")
        st.caption("첫번째 고객님")
        
        # API 상태 표시 (디버그)
        with st.expander("🔧 API 상태", expanded=False):
            st.write(f"**모드:** {st.session_state.game_mode}")
            st.write(f"**API Key:** {'설정됨 ✅' if st.session_state.api_key else '없음 ❌'}")
            if st.session_state.get("api_error"):
                st.error(f"❌ 마지막 에러: {st.session_state.get('last_api_error', '알 수 없음')}")
            else:
                st.success("✅ API 정상")
            if st.session_state.get("last_model_used"):
                st.info(f"📡 사용 모델: {st.session_state.last_model_used}")
        
        # 게임 중일 때 코치 피드백을 맨 위에 표시
        if st.session_state.game_state == "playing" and st.session_state.history:
            last = st.session_state.history[-1]
            feedback_pos = last.get('feedback_positive', '')
            feedback_imp = last.get('feedback_improve', '')
            tip = last.get('tip', '')
            
            if feedback_pos or feedback_imp or tip:
                st.markdown("""
                <div style="background:linear-gradient(135deg,#FFF5EE,#FFE4EC);border-radius:12px;padding:12px;margin-bottom:15px;border-left:4px solid #FF69B4;">
                    <div style="color:#FF69B4;font-weight:700;margin-bottom:8px;font-size:14px;">💝 코치 피드백</div>
                </div>
                """, unsafe_allow_html=True)
                
                if feedback_pos:
                    st.success(f"✅ {feedback_pos}")
                if feedback_imp:
                    st.warning(f"💡 {feedback_imp}")
                if tip:
                    st.info(f"📌 Tip: {tip}")
                
                st.divider()
        
        # 탭 구성
        tab1, tab2 = st.tabs(["⚙️ 설정", "📋 상품정보"])
        
        with tab1:
            # 상담 설정을 먼저 배치
            st.markdown("### 💼 상담 설정")
            
            st.session_state.company = st.selectbox("🏢 계열사", list(COMPANY_PRODUCTS.keys()))
            products = list(COMPANY_PRODUCTS.get(st.session_state.company, {}).keys())
            st.session_state.product = st.selectbox("📦 추천 상품", products)
            st.session_state.persona = st.selectbox("👤 고객 타입", list(PERSONAS.keys()))
            st.session_state.difficulty = st.selectbox("💪 난이도", ["🌱 Easy (순한맛)", "🔥 Normal (보통)", "💀 Hard (매운맛)"], index=2)
            
            st.divider()
            
            # 모드 선택과 API Key는 아래로
            mode = st.radio("🎮 모드 선택", ["💝 AI 모드 (Gemini)", "🎮 체험 모드"], index=0)
            st.session_state.game_mode = "ai" if "AI" in mode else "demo"
            
        
        with tab2:
            # 계열사별 상품 혜택 보기
            st.markdown("### 📦 계열사별 상품 혜택")
            
            for company, products in COMPANY_PRODUCTS.items():
                with st.expander(company, expanded=False):
                    for prod_name, prod_data in products.items():
                        st.markdown(f"**{prod_name}**")
                        
                        # 주요 혜택
                        for point in prod_data.get("points", []):
                            st.markdown(f"- {point}")
                        
                        # 상세 정보
                        details = prod_data.get("details", {})
                        if details:
                            st.caption(f"💰 {details.get('절약효과', details.get('세제혜택', ''))}")
                            st.caption(f"👤 {details.get('대상고객', '')}")
                            st.info(f"💬 {details.get('추천멘트', '')}")
                        st.divider()

def render_intro():
    # 메인 배너 이미지
    import base64
    import os
    
    banner_path = os.path.join(os.path.dirname(__file__), "main_banner.png")
    if os.path.exists(banner_path):
        with open(banner_path, "rb") as f:
            banner_data = base64.b64encode(f.read()).decode()
        
        st.markdown(f"""
        <div style="text-align:center;margin-bottom:12px;">
            <img src="data:image/png;base64,{banner_data}" style="width:100%;max-width:500px;border-radius:15px;box-shadow:0 5px 20px rgba(255,105,180,0.3);border:2px solid #FF69B4;">
        </div>
        """, unsafe_allow_html=True)
    else:
        # 이미지가 없으면 기존 타이틀 표시
        st.markdown("""
        <div class="game-title" style="padding:10px 0;">
            <h1 style="font-size:24px;">💕 두근두근 신한</h1>
            <div class="subtitle">첫번째 고객님</div>
        </div>
        """, unsafe_allow_html=True)
    
    # 게임 시작 버튼 (이미지 바로 아래)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("💕 게임 시작!", use_container_width=True, key="start_btn"):
            start_game()
            st.rerun()

    # 고객 프로필 + 상품 정보 (컴팩트)
    col1, col2 = st.columns(2)
    
    with col1:
        p = PERSONAS.get(st.session_state.persona, {})
        persona_img = get_persona_image(p.get('image', ''))
        st.markdown(f"""
        <div class="customer-card" style="padding:10px;">
            <div style="font-size:11px;color:#888;margin-bottom:5px;">💝 오늘의 고객님</div>
            <img src="{persona_img}" style="width:60px;height:60px;border-radius:50%;object-fit:cover;border:2px solid #FF69B4;margin:5px 0;" onerror="this.style.display='none'">
            <div style="font-size:14px;font-weight:700;color:#FF1493;">{st.session_state.persona}</div>
            <div style="font-size:11px;color:#666;">{p.get('age', '')} · {p.get('job', '')}</div>
            <div style="margin-top:5px;font-size:10px;color:#888;">{p.get('style', '')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="customer-card" style="padding:10px;">
            <div style="font-size:11px;color:#888;margin-bottom:5px;">🎁 추천 상품</div>
            <div style="font-size:14px;font-weight:700;color:#FF1493;margin:8px 0;">{st.session_state.product}</div>
        </div>
        """, unsafe_allow_html=True)
        render_tips()
    
    # 게임 가이드 (컴팩트 - 기본 숨김)
    with st.expander("📖 게임 가이드", expanded=False):
        st.markdown("""
        <div style="font-size:12px;color:#555;">
            <b>🎯 목표:</b> 5턴 안에 호감도 100% 달성<br>
            <b>💡 팁:</b> 정확한 수치와 혜택을 언급하세요<br>
            <b>📊 평가:</b> EXCELLENT (+30~40) · GOOD (+15~25) · AVERAGE (+5~10) · POOR (0)
        </div>
        """, unsafe_allow_html=True)

def render_game():
    # API 에러 알림 (상세)
    if st.session_state.get("api_error"):
        error_detail = st.session_state.get("last_api_error", "알 수 없는 오류")
        st.error(f"⚠️ AI 연결 실패: {error_detail} (로컬 평가 사용 중)")
    
    # ===== 상단: 고객 프로필 (중앙 크게) =====
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        render_customer()
    
    # ===== 중단: 스탯 바 (호감도 + 점수/턴/설득도) =====
    render_persuasion_gauge()
    render_stats_inline()
    
    # 힌트 (접이식)
    render_tips()
    
    # ===== 하단: 대화창 =====
    render_dialogue()
    
    user_input = st.chat_input("💕 고객님에게 어떻게 말씀하시겠어요?")
    
    if user_input:
        st.session_state.show_gain = False
        process_input(user_input)
        st.rerun()

def render_victory():
    st.balloons()
    
    # 타이틀
    st.markdown("""
    <div class="game-title" style="padding:15px 0;">
        <h1 style="font-size:32px;">💕 축하해요!</h1>
        <div class="subtitle">고객의 마음을 사로잡았어요!</div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        lottie = load_lottie(LOTTIE_URLS["success"])
        if lottie:
            st_lottie(lottie, height=130)
    
    st.markdown(f"""
        <div style="background:linear-gradient(135deg,#FFE4EC,#FFF0F5);border-radius:25px;padding:25px;text-align:center;border:3px solid #FF69B4;box-shadow:0 8px 30px rgba(255,105,180,0.3);">
            <div style="font-size:40px;margin-bottom:10px;">💕</div>
            <div style="color:#FF1493;font-size:24px;font-weight:900;">계약 성공!</div>
            <div style="color:#555;font-size:14px;margin-top:8px;">"{st.session_state.product}"</div>
            <div style="color:#FF69B4;font-size:28px;font-weight:700;margin-top:15px;">🏆 {st.session_state.score:,} Point</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    render_report(True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("💕 다시 도전!", use_container_width=True):
            reset_game()
            st.rerun()
    
def render_defeat():
    # 타이틀
    st.markdown("""
    <div class="game-title" style="padding:15px 0;">
        <h1 style="font-size:32px;">💔 아쉬워요...</h1>
        <div class="subtitle">다음에는 꼭 성공할 거예요!</div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#F5F5F5,#FFE4EC);border-radius:25px;padding:25px;text-align:center;border:3px solid #DDA0DD;box-shadow:0 8px 30px rgba(221,160,221,0.3);">
            <div style="font-size:40px;margin-bottom:10px;">😢</div>
            <div style="color:#BA55D3;font-size:22px;font-weight:900;">아쉽게도 설득에 실패했어요</div>
            <div style="color:#555;font-size:14px;margin-top:8px;">호감도 {st.session_state.persuasion}%에서 종료</div>
            <div style="color:#9370DB;font-size:24px;font-weight:700;margin-top:15px;">📊 {st.session_state.score:,} Point</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    render_report(False)
    
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("💪 다시 도전!", use_container_width=True):
            reset_game()
            st.rerun()

# ============================================================
# 🚀 메인
# ============================================================

def main():
    # 떨어지는 하트 파티클 (15개)
    st.markdown("""
    <div class="heart-particles">
        <div class="heart-particle">💕</div>
        <div class="heart-particle">💗</div>
        <div class="heart-particle">💖</div>
        <div class="heart-particle">💝</div>
        <div class="heart-particle">💕</div>
        <div class="heart-particle">💗</div>
        <div class="heart-particle">💖</div>
        <div class="heart-particle">💝</div>
        <div class="heart-particle">💕</div>
        <div class="heart-particle">💗</div>
        <div class="heart-particle">💖</div>
        <div class="heart-particle">💝</div>
        <div class="heart-particle">💕</div>
        <div class="heart-particle">💗</div>
        <div class="heart-particle">💖</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 사이드바 상태 관리 (최초 실행 시 접힌 상태)
    if 'sidebar_visible' not in st.session_state:
        st.session_state.sidebar_visible = False
    
    # 사이드바 표시/숨김 CSS (동적) - 더 강력한 선택자
    if st.session_state.sidebar_visible:
        sidebar_css = """
        <style>
        /* 사이드바 강제 표시 */
        [data-testid="stSidebar"],
        section[data-testid="stSidebar"],
        .st-emotion-cache-1cypcdb,
        .st-emotion-cache-16txtl3,
        div[data-testid="stSidebar"] {
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            transform: none !important;
            margin-left: 0 !important;
            left: 0 !important;
            width: 300px !important;
            min-width: 300px !important;
            position: relative !important;
        }
        
        [data-testid="stSidebar"] > div {
            display: block !important;
            visibility: visible !important;
        }
        
        [data-testid="stSidebarContent"],
        .stSidebarContent {
            display: block !important;
            visibility: visible !important;
        }
        </style>
        """
    else:
        sidebar_css = """
        <style>
        /* 사이드바 강제 숨김 */
        [data-testid="stSidebar"],
        section[data-testid="stSidebar"],
        .st-emotion-cache-1cypcdb,
        .st-emotion-cache-16txtl3,
        div[data-testid="stSidebar"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            transform: translateX(-100%) !important;
            margin-left: -300px !important;
            width: 0 !important;
            min-width: 0 !important;
        }
        </style>
        """
    st.markdown(sidebar_css, unsafe_allow_html=True)
    
    # 플로팅 버튼 영역 (항상 왼쪽 상단에 표시)
    toggle_col = st.container()
    with toggle_col:
        col1, col2, col3 = st.columns([1, 10, 1])
        with col1:
            btn_label = "💕 옵션" if not st.session_state.sidebar_visible else "✖️ 닫기"
            if st.button(btn_label, key="sidebar_toggle_btn", help="설정 메뉴 열기/닫기"):
                st.session_state.sidebar_visible = not st.session_state.sidebar_visible
                st.rerun()
    
    # 사이드바는 항상 렌더링 (CSS로 표시/숨김 제어)
    render_sidebar()
    
    state = st.session_state.game_state
    if state == "intro":
        render_intro()
    elif state == "playing":
        render_game()
    elif state == "victory":
        render_victory()
    elif state == "defeat":
        render_defeat()

if __name__ == "__main__":
    main()
