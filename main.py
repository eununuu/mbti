import streamlit as st
import time

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="말랑말랑 먼작귀 대가족 MBTI 테스트",
    page_icon="🌸",
    layout="centered"
)

# 2. 파스텔톤의 귀여운 커스텀 스타일 적용 (CSS)
st.markdown("""
    <style>
    /* 전체 배경색 */
    .stApp {
        background-color: #FFF9F2;
    }
    /* 타이틀 */
    .title {
        color: #FF7B93;
        font-size: 2.3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #8C7A6B;
        text-align: center;
        font-size: 1.05rem;
        margin-bottom: 25px;
    }
    /* 질문 박스 */
    .question-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #FFD1D1;
        box-shadow: 2px 2px 10px rgba(255, 194, 209, 0.2);
        margin-bottom: 20px;
    }
    /* 결과 박스 */
    .result-box {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 20px;
        border: 3px dashed #FFC2D1;
        box-shadow: 3px 3px 15px rgba(255, 194, 209, 0.3);
        text-align: center;
    }
    .char-name {
        color: #FF5C7C;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 15px;
    }
    /* 이미지(SVG) 래퍼 */
    .img-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)


# 3. 방화벽 철통 방어! 직접 그린 귀여운 8종 먼작귀 SVG 데이터베이스
# (코드 자체로 구현되어 이미지가 안 깨지고 100% 무적 로딩됩니다)
character_db = {
    "치이카와 🐹": {
        "mbtis": ["INFP", "ISFP"],
        "desc": "소심하고 걱정이 많아 눈물 흘릴 때도 많지만, 소중한 친구들을 위해 누구보다 큰 용기를 내는 따뜻한 주인공이에요. 수줍음이 많고 감수성이 풍부하며, 말없이 타인의 아픔에 깊이 공감하는 따뜻한 마음씨를 가지고 있습니다 💖",
        "tag": "#수줍은_엔젤 #울보지만_용감해 #공감대장 #선한영향력",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 귀 -->
            <path d="M 60 50 Q 50 20 75 35 Q 85 45 80 55 Z" fill="#FFFFFF" stroke="#FFC2D1" stroke-width="3"/>
            <path d="M 140 50 Q 150 20 125 35 Q 115 45 120 55 Z" fill="#FFFFFF" stroke="#FFC2D1" stroke-width="3"/>
            <!-- 얼굴 몸통 -->
            <circle cx="100" cy="110" r="65" fill="#FFFFFF" stroke="#FFD1D1" stroke-width="4"/>
            <!-- 볼따구 핑크 -->
            <circle cx="55" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <circle cx="145" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <!-- 눈 -->
            <circle cx="75" cy="100" r="7.5" fill="#333333"/>
            <circle cx="73" cy="98" r="2.5" fill="#FFFFFF"/>
            <circle cx="125" cy="100" r="7.5" fill="#333333"/>
            <circle cx="123" cy="98" r="2.5" fill="#FFFFFF"/>
            <!-- 슬픈/말랑 눈썹 -->
            <path d="M 67 85 Q 75 88 83 85" stroke="#333333" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 117 85 Q 125 88 133 85" stroke="#333333" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <!-- 귀여운 시무룩 입 -->
            <path d="M 95 115 Q 100 122 105 115" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
        """
    },
    "하치와레 🐱": {
        "mbtis": ["ENFP", "ESFP"],
        "desc": "말을 유창하게 잘하고 매사에 초긍정적인 마인드를 가진 활기찬 친구예요! 어려운 처지 속에서도 '어떻게든 되겠지!'라며 해맑게 위기를 이겨내며, 주변 사람들에게 다정한 말과 에너지를 불어넣어 주는 분위기 메이커입니다 🎵",
        "tag": "#초긍정 #호기심대왕 #어떻게든되겠지 #우정의콘서트",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 고양이 귀 -->
            <path d="M 50 60 L 40 20 L 75 45 Z" fill="#A4C2F4" stroke="#7AA0CD" stroke-width="3"/>
            <path d="M 150 60 L 160 20 L 125 45 Z" fill="#A4C2F4" stroke="#7AA0CD" stroke-width="3"/>
            <path d="M 52 55 L 47 30 L 70 45 Z" fill="#FFFFFF"/>
            <path d="M 148 55 L 153 30 L 130 45 Z" fill="#FFFFFF"/>
            <!-- 얼굴 몸통 -->
            <circle cx="100" cy="110" r="65" fill="#FFFFFF" stroke="#FFD1D1" stroke-width="4"/>
            <!-- 파란색 가르마 헤어 패턴 -->
            <path d="M 37 95 C 45 50 155 50 163 95 C 135 70 115 85 100 70 C 85 85 65 70 37 95 Z" fill="#A4C2F4"/>
            <!-- 볼따구 -->
            <circle cx="55" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <circle cx="145" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <!-- 눈 -->
            <circle cx="75" cy="105" r="7.5" fill="#333333"/>
            <circle cx="73" cy="103" r="2.5" fill="#FFFFFF"/>
            <circle cx="125" cy="105" r="7.5" fill="#333333"/>
            <circle cx="123" cy="103" r="2.5" fill="#FFFFFF"/>
            <!-- 눈썹 -->
            <path d="M 68 93 Q 75 90 82 93" stroke="#333333" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 118 93 Q 125 90 132 93" stroke="#333333" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <!-- 미소 띤 입 -->
            <path d="M 93 118 Q 100 125 107 118" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
        """
    },
    "우사기 🐰": {
        "mbtis": ["ENTP", "ESTP"],
        "desc": "어디로 튈지 모르는 미스터리하고 강력한 개성의 소유자! 말보단 행동이 먼저이며, 두려움 없이 기발한 아이디어로 눈앞의 문제를 뚝딱 해결해요. 남의 눈치를 보지 않고 인생을 온전히 신나게 개척하는 매력 토끼예요 ⚡",
        "tag": "#천재괴짜 #행동력대왕 #야하_우라_하아 #마이웨이_최강자",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 긴 귀 -->
            <rect x="55" y="10" width="22" height="70" rx="11" fill="#FFF2CC" stroke="#E2B25B" stroke-width="3" transform="rotate(-10 66 45)"/>
            <rect x="123" y="10" width="22" height="70" rx="11" fill="#FFF2CC" stroke="#E2B25B" stroke-width="3" transform="rotate(10 134 45)"/>
            <!-- 얼굴 몸통 -->
            <circle cx="100" cy="115" r="65" fill="#FFF2CC" stroke="#FFE599" stroke-width="4"/>
            <!-- 볼따구 -->
            <circle cx="55" cy="125" r="12" fill="#FFC2D1" opacity="0.85"/>
            <circle cx="145" cy="125" r="12" fill="#FFC2D1" opacity="0.85"/>
            <!-- 눈 -->
            <circle cx="75" cy="105" r="7.5" fill="#333333"/>
            <circle cx="73" cy="103" r="2.5" fill="#FFFFFF"/>
            <circle cx="125" cy="105" r="7.5" fill="#333333"/>
            <circle cx="123" cy="103" r="2.5" fill="#FFFFFF"/>
            <!-- 씩씩한 눈썹 -->
            <path d="M 68 92 L 82 95" stroke="#333333" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M 118 95 L 132 92" stroke="#333333" stroke-width="2.5" stroke-linecap="round"/>
            <!-- 벌린 하- 입 -->
            <path d="M 90 122 Q 100 140 110 122 Z" fill="#FF8A8A" stroke="#333333" stroke-width="2.5"/>
        </svg>
        """
    },
    "쿠리만쥬 🌰": {
        "mbtis": ["ISTP", "INTP"],
        "desc": "혼자만의 조용한 여유와 맛있는 음식을 음미할 줄 아는 시크한 매력쟁이! 겉은 살짝 시크하고 초연해 보여도, 곁에서 조용히 챙겨주는 깊고 묵직한 정을 지녔어요. 세상사 초연한 태도로 자신만의 템포를 완성하는 인생 2회차 고수의 포스! ☕",
        "tag": "#인생2회차 #시크한_츤데레 #소소한_미식가 #안주와_음료한잔",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 밤톨 머리 모양 -->
            <path d="M 35 110 C 35 50 165 50 165 110 C 165 155 130 175 100 175 C 70 175 35 155 35 110 Z" fill="#FFF2CC" stroke="#D4A373" stroke-width="4"/>
            <path d="M 35 110 C 35 50 165 50 165 110 C 140 90 115 100 100 85 C 85 100 60 90 35 110 Z" fill="#8B4513"/>
            <!-- 귀 -->
            <circle cx="38" cy="105" r="10" fill="#8B4513"/>
            <circle cx="162" cy="105" r="10" fill="#8B4513"/>
            <!-- 볼따구 -->
            <circle cx="58" cy="130" r="10" fill="#FFC2D1" opacity="0.8"/>
            <circle cx="142" cy="130" r="10" fill="#FFC2D1" opacity="0.8"/>
            <!-- 기분 좋은 눈 -->
            <path d="M 68 115 Q 78 110 84 118" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 116 118 Q 122 110 132 115" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- 만족스러운 입 -->
            <path d="M 95 128 C 95 133 105 133 105 128" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
        """
    },
    "시사 🦁": {
        "mbtis": ["ESFJ", "ENFJ"],
        "desc": "친절하고 살가우며, 원하는 목표를 이루기 위해 엄청난 노력을 기울이는 대단한 성실파예요! 모두에게 예의 바른 인사성 만점 사자이며, 언제나 밝은 에너지를 전파하며 주변 환경의 조화와 화합을 가장 중요하게 생각합니다 🦁",
        "tag": "#정리달인 #인사성만점 #성실아기사자 #우정의조율사",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 사자 갈기 장식 -->
            <path d="M 40 80 Q 20 50 50 40 Q 80 20 100 35 Q 120 20 150 40 Q 180 50 160 80 Q 185 110 160 140 Q 140 175 100 165 Q 60 175 40 140 Q 15 110 40 80 Z" fill="#FFE599" stroke="#E69138" stroke-width="3"/>
            <!-- 얼굴 -->
            <circle cx="100" cy="105" r="55" fill="#FFF2CC" stroke="#F1C232" stroke-width="3"/>
            <!-- 두꺼운 개성 눈썹 -->
            <path d="M 68 82 Q 78 72 84 82" stroke="#E69138" stroke-width="6" fill="none" stroke-linecap="round"/>
            <path d="M 116 82 Q 122 72 132 82" stroke="#E69138" stroke-width="6" fill="none" stroke-linecap="round"/>
            <!-- 볼따구 -->
            <circle cx="60" cy="115" r="10" fill="#F4CCCC" opacity="0.9"/>
            <circle cx="140" cy="115" r="10" fill="#F4CCCC" opacity="0.9"/>
            <!-- 웃는 눈 -->
            <path d="M 70 95 Q 77 88 84 95" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
            <path d="M 116 95 Q 123 88 130 95" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- 방글방글 입 -->
            <path d="M 92 115 Q 100 125 108 115" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
        """
    },
    "랏코 🦦": {
        "mbtis": ["ESTJ", "ENTJ"],
        "desc": "강력한 실력과 든든한 카리스마를 장착한 멋진 영웅이자 의지할 수 있는 스승님! 자신에게는 매우 엄격하고 프로답지만, 소중한 친구들에게는 한없이 자상하고 듬직해요. 남몰래 달콤한 초코 디저트를 먹으며 행복해하는 귀여운 반전 매력의 소유자입니다 🍰",
        "tag": "#카리스마멘토 #듬직한선배 #프로페셔널 #디저트_러버",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 후드 몸통 배경 -->
            <circle cx="100" cy="110" r="65" fill="#D5A6BD" stroke="#C27BA0" stroke-width="3"/>
            <!-- 얼굴 부분 -->
            <circle cx="100" cy="115" r="50" fill="#FFF2CC" stroke="#D4A373" stroke-width="3"/>
            <!-- 영웅의 이마 상처 -->
            <line x1="90" y1="80" x2="105" y2="92" stroke="#C27BA0" stroke-width="4" stroke-linecap="round"/>
            <!-- 귀 -->
            <circle cx="45" cy="105" r="12" fill="#D5A6BD" stroke="#C27BA0" stroke-width="2"/>
            <circle cx="155" cy="105" r="12" fill="#D5A6BD" stroke="#C27BA0" stroke-width="2"/>
            <!-- 홍조 -->
            <circle cx="62" cy="125" r="10" fill="#FFC2D1" opacity="0.8"/>
            <circle cx="138" cy="125" r="10" fill="#FFC2D1" opacity="0.8"/>
            <!-- 진지하고 귀여운 눈 -->
            <circle cx="78" cy="108" r="7.5" fill="#333333"/>
            <circle cx="76" cy="106" r="2.5" fill="#FFFFFF"/>
            <circle cx="122" cy="108" r="7.5" fill="#333333"/>
            <circle cx="120" cy="106" r="2.5" fill="#FFFFFF"/>
            <!-- 일자 입 -->
            <line x1="93" y1="125" x2="107" y2="125" stroke="#333333" stroke-width="3" stroke-linecap="round"/>
        </svg>
        """
    },
    "포셰트 갑옷씨 ⚔️": {
        "mbtis": ["ISTJ", "ISFJ"],
        "desc": "묵묵히 뒤에서 규칙을 지키며 모두를 지켜주는 과묵하고 다정한 보디가드! 성실하고 꼼꼼하며, 손재주가 매우 뛰어나 소중한 사람들에게 아기자기한 수공예품을 만들어 선물하는 데서 엄청난 보람과 따뜻함을 느끼는 든든한 수호자 타입입니다 🧵",
        "tag": "#꼼꼼장인 #성실한갑옷 #바느질달인 #다정한보디가드",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 헬멧 본체 -->
            <rect x="45" y="55" width="110" height="110" rx="35" fill="#CFD8DC" stroke="#78909C" stroke-width="4"/>
            <!-- 바이저 고글 영역 -->
            <rect x="55" y="80" width="90" height="30" rx="8" fill="#455A64"/>
            <!-- 고글 안의 하얀 눈 -->
            <circle cx="78" cy="95" r="4.5" fill="#FFFFFF"/>
            <circle cx="122" cy="95" r="4.5" fill="#FFFFFF"/>
            <!-- 헬멧의 핑크 볼 장식 -->
            <circle cx="62" cy="135" r="10" fill="#FF8A8A" opacity="0.85"/>
            <circle cx="138" cy="135" r="10" fill="#FF8A8A" opacity="0.85"/>
            <!-- 헬멧 장식용 뿔 -->
            <path d="M 65 57 L 55 35 L 80 50 Z" fill="#CFD8DC" stroke="#78909C" stroke-width="3"/>
            <path d="M 135 57 L 145 35 L 120 50 Z" fill="#CFD8DC" stroke="#78909C" stroke-width="3"/>
            <!-- 수줍은 입선 -->
            <line x1="92" y1="130" x2="108" y2="130" stroke="#78909C" stroke-width="3" stroke-linecap="round"/>
        </svg>
        """
    },
    "모몬가 🐿️": {
        "mbtis": ["INTJ", "INFJ"],
        "desc": "새침떼기 외모 속에 원대한 우주적 정복 야망을 품고 있는 야심 가득한 친구예요! 자신에 대한 깊은 자부심이 하늘을 찌르며, '나를 귀여워해라!'라며 당당히 외치죠. 가끔은 도통 무슨 생각을 하는지 알 수 없는 독특함으로 사람들을 사로잡습니다 👑",
        "tag": "#나만의세계 #나를칭찬해라 #귀여운야심가 #반전매력덩어리",
        "svg": """
        <svg width="180" height="180" viewBox="0 0 200 200">
            <!-- 다람쥐 귀 -->
            <path d="M 30 70 Q 10 20 50 35 Q 70 50 75 65 Z" fill="#E8F0FE" stroke="#A4C2F4" stroke-width="3"/>
            <path d="M 170 70 Q 190 20 150 35 Q 130 50 125 65 Z" fill="#E8F0FE" stroke="#A4C2F4" stroke-width="3"/>
            <!-- 얼굴 본체 -->
            <circle cx="100" cy="110" r="65" fill="#FFFFFF" stroke="#D1E2FF" stroke-width="4"/>
            <!-- 볼따구 -->
            <circle cx="55" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <circle cx="145" cy="120" r="12" fill="#FFC2D1" opacity="0.85"/>
            <!-- 커다랗고 초롱초롱한 눈 -->
            <circle cx="73" cy="100" r="12.5" fill="#1C3D5A"/>
            <circle cx="70" cy="96" r="4.5" fill="#FFFFFF"/>
            <circle cx="76" cy="104" r="2.5" fill="#FFFFFF"/>
            <circle cx="127" cy="100" r="12.5" fill="#1C3D5A"/>
            <circle cx="124" cy="96" r="4.5" fill="#FFFFFF"/>
            <circle cx="130" cy="104" r="2.5" fill="#FFFFFF"/>
            <!-- 깜찍한 눈썹 -->
            <path d="M 63 80 Q 73 78 80 84" stroke="#1C3D5A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <path d="M 137 80 Q 127 78 120 84" stroke="#1C3D5A" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <!-- 도도한 입 -->
            <path d="M 94 118 Q 100 124 106 118" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
        """
    }
}

# 4. 대문용 합동 일러스트 SVG (귀엽게 춤추는 삼총사)
main_banner_svg = """
<svg width="100%" height="150" viewBox="0 0 400 150">
  <!-- 좌측 치이카와 -->
  <g transform="translate(60, 25) scale(0.6)">
    <path d="M 60 50 Q 50 20 75 35 Q 85 45 80 55 Z" fill="#FFFFFF" stroke="#FFC2D1" stroke-width="3"/>
    <path d="M 140 50 Q 150 20 125 35 Q 115 45 120 55 Z" fill="#FFFFFF" stroke="#FFC2D1" stroke-width="3"/>
    <circle cx="100" cy="110" r="65" fill="#FFFFFF" stroke="#FFD1D1" stroke-width="4"/>
    <circle cx="55" cy="120" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="145" cy="120" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="75" cy="100" r="7.5" fill="#333333"/>
    <circle cx="73" cy="98" r="2.5" fill="#FFFFFF"/>
    <circle cx="125" cy="100" r="7.5" fill="#333333"/>
    <circle cx="123" cy="98" r="2.5" fill="#FFFFFF"/>
    <path d="M 95 115 Q 100 122 105 115" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>
  <!-- 중앙 하치와레 -->
  <g transform="translate(160, 15) scale(0.7)">
    <path d="M 50 60 L 40 20 L 75 45 Z" fill="#A4C2F4" stroke="#7AA0CD" stroke-width="3"/>
    <path d="M 150 60 L 160 20 L 125 45 Z" fill="#A4C2F4" stroke="#7AA0CD" stroke-width="3"/>
    <circle cx="100" cy="110" r="65" fill="#FFFFFF" stroke="#FFD1D1" stroke-width="4"/>
    <path d="M 37 95 C 45 50 155 50 163 95 C 135 70 115 85 100 70 C 85 85 65 70 37 95 Z" fill="#A4C2F4"/>
    <circle cx="55" cy="120" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="145" cy="120" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="75" cy="105" r="7.5" fill="#333333"/>
    <circle cx="73" cy="103" r="2.5" fill="#FFFFFF"/>
    <circle cx="125" cy="105" r="7.5" fill="#333333"/>
    <circle cx="123" cy="103" r="2.5" fill="#FFFFFF"/>
    <path d="M 93 118 Q 100 125 107 118" stroke="#333333" stroke-width="3" fill="none" stroke-linecap="round"/>
  </g>
  <!-- 우측 우사기 -->
  <g transform="translate(260, 25) scale(0.6)">
    <rect x="55" y="10" width="22" height="70" rx="11" fill="#FFF2CC" stroke="#E2B25B" stroke-width="3" transform="rotate(-10 66 45)"/>
    <rect x="123" y="10" width="22" height="70" rx="11" fill="#FFF2CC" stroke="#E2B25B" stroke-width="3" transform="rotate(10 134 45)"/>
    <circle cx="100" cy="115" r="65" fill="#FFF2CC" stroke="#FFE599" stroke-width="4"/>
    <circle cx="55" cy="125" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="145" cy="125" r="12" fill="#FFC2D1" opacity="0.8"/>
    <circle cx="75" cy="105" r="7.5" fill="#333333"/>
    <circle cx="73" cy="103" r="2.5" fill="#FFFFFF"/>
    <circle cx="125" cy="105" r="7.5" fill="#333333"/>
    <circle cx="123" cy="103" r="2.5" fill="#FFFFFF"/>
    <path d="M 90 122 Q 100 140 110 122 Z" fill="#FF8A8A" stroke="#333333" stroke-width="2.5"/>
  </g>
</svg>
"""

# 5. 질문지 정의 (MBTI 지표는 외부에 일절 드러나지 않음!)
questions = [
    {
        "axis": "EI",
        "text": "🎈 주말에 친한 친구가 예고도 없이 우리 집 앞에 깜짝 찾아왔다! 나의 진짜 속마음은?",
        "options": [
            "우와 대박! 완전 기분 좋은 서프라이즈다! 신나게 씻고 옷 입고 바로 문 열고 나간다 🥳",
            "정말 고맙고 좋은 친구인 건 맞는데... 오늘은 조용히 쉴 생각이었어서 살짝 마음이 복잡해진다... 🏠"
        ],
        "mapping": ["E", "I"]
    },
    {
        "axis": "SN",
        "text": "💎 하굣길에 우연히 햇빛을 받아 아주 신기하고 이쁘게 반짝거리는 돌멩이를 길바닥에서 주웠다면?",
        "options": [
            "우와 이쁘다! 신기하게 생긴 기념품으로 가방 구석에 쏙 넣어두거나 만져보고 제자리에 둔다 🔍",
            "이건 전설 속 요정이 잃어버린 보물이 아닐까? 밤에 막 빛나는 상상을 하며 혼자 판타지 소설을 상상해 본다 🪄"
        ],
        "mapping": ["S", "N"]
    },
    {
        "axis": "TF",
        "text": "😭 평소 정말 열심히 시험을 준비했던 짝꿍이 시험 결과가 안 좋아 울상으로 말을 걸어온다면?",
        "options": [
            "정말 속상하겠다... 무슨 과목이 유독 아쉬웠어? 오답 정리부터 같이 해보자며 전략적인 공부법을 같이 찾아준다 📊",
            "에고ㅠㅠ 고생한 거 내가 다 아는데 마음 아프다... 고생 많았으니 오늘 같이 진짜 맛있는 떡볶이 먹으러 가자고 달래준다 🍰"
        ],
        "mapping": ["T", "F"]
    },
    {
        "axis": "JP",
        "text": "📝 방과 후에 친구들과 당곡역 근처 유명한 맛집에 다 같이 가서 저녁 식사를 하기로 약속했을 때 나의 행동은?",
        "options": [
            "미리 메뉴를 공부하고 영업시간과 동선, 혹시 사람 많으면 대신 갈 대피 맛집까지 정해놓는다 📍",
            "그냥 가기로 했으니까 시간 맞춰 간다! 문이 닫혀 있으면 옆집이나 앞집 아무 데나 쓱 들어간다 💨"
        ],
        "mapping": ["J", "P"]
    }
]

# 6. 세션 상태 관리
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- 7. 메인 렌더링 ---
st.markdown("<div class='title'>🌸 말랑말랑 먼작귀 대가족 테스트 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>방화벽 걱정 제로! 나랑 똑같이 생긴 먼작귀는 과연 누구일까요?</div>", unsafe_allow_html=True)

# 7-1. 인트로 대기실 (Step 0)
if st.session_state.step == 0:
    # 100% 안 깨지고 바로 로딩되는 대형 SVG 장식
    st.markdown(f"<div class='img-container'>{main_banner_svg}</div>", unsafe_allow_html=True)
    st.write("")
    st.success("🚨 **안내:** 이 앱은 학교 컴퓨터실의 강력한 방화벽 차단을 완벽히 통과하는 **무적 자체 일러스트 렌더링**을 제공합니다. 마음 편히 테스트해 보세요!")
    if st.button("✨ 8종 대가족 테스트 시작하기! ✨", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = []
        st.rerun()

# 7-2. 질문 진행 (Step 1 ~ 4)
elif 1 <= st.session_state.step <= 4:
    q_index = st.session_state.step - 1
    current_q = questions[q_index]
    
    # 귀여운 게이지 바
    progress_val = (st.session_state.step - 1) / 4.0
    st.progress(progress_val)
    st.write(f"📝 **{st.session_state.step}번째 방에서 정밀 스캔 중...**")
    
    st.markdown(f"""
        <div class="question-box">
            <h4 style="color: #4A4A4A; line-height: 1.5;">{current_q['text']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    choice = st.radio(
        "마음이 더 끌리는 대답은?",
        options=current_q["options"],
        key=f"q_{st.session_state.step}"
    )
    
    st.write("")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ 처음으로", use_container_width=True):
            st.session_state.step = 0
            st.session_state.answers = []
            st.rerun()
            
    with col2:
        if st.button("다음 질문으로 ➡️", use_container_width=True):
            selected_idx = current_q["options"].index(choice)
            selected_letter = current_q["mapping"][selected_idx]
            
            st.session_state.answers.append(selected_letter)
            st.session_state.step += 1
            st.rerun()

# 7-3. 결과 출력 (Step 5)
elif st.session_state.step == 5:
    user_mbti = "".join(st.session_state.answers)
    
    with st.spinner('☁️ 당곡고의 스마트한 기운으로 당신의 소울 캐릭터를 그리는 중...☁️'):
        time.sleep(1.2)
        
    st.balloons() # 파티 타임! 🎉
    
    # 결과 캐릭터 매칭
    final_char = ""
    for char_name, info in character_db.items():
        if user_mbti in info["mbtis"]:
            final_char = char_name
            break
            
    if not final_char:
        final_char = "치이카와 🐹"  # 예외 예방 기본값
        
    result_info = character_db[final_char]
    
    # 결과 요약 카드
    st.markdown(f"""
        <div class="result-box">
            <span style="font-size: 1.3rem; color: #FF7B93; font-weight: bold;">[ {user_mbti} ] 인 당신의 소울 패밀리는?</span>
            <div class="char-name">{final_char}</div>
            <p style="color: #9C515F; font-weight: bold; margin-top: 10px; font-size: 1.1rem;">{result_info['tag']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 100% 무적 로딩되는 귀여운 캐릭터 SVG 출력!
    st.markdown(f"<div class='img-container'>{result_info['svg']}</div>", unsafe_allow_html=True)
    
    # 상세 성향 묘사
    st.markdown(f"""
        <div style="background-color: #FFF; padding: 20px; border-radius: 15px; border: 1px solid #FFD1D1; margin-top: 15px; line-height: 1.6; text-align: justify; word-break: keep-all;">
            {result_info['desc']}
        </div>
    """, unsafe_allow_html=True)
    
    # 다시 하기
    st.write("")
    if st.button("🔄 테스트 다시 도전하기!", use_container_width=True):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()

st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #BDC3C7; font-size: 0.85rem;'>제작: 당곡고등학교 멋진 개발자 학생 💖 | 100% 오프라인/방화벽 통과형 무적 SVG 기술 적용</p>", unsafe_allow_html=True)
