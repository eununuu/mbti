import streamlit as st
import os
import time

# 1. 웹페이지 기본 설정
st.set_page_config(
    page_title="말랑말랑 먼작귀 MBTI 테스트",
    page_icon="🌸",
    layout="centered"
)

# 2. 파스텔톤의 귀여운 커스텀 스타일 적용 (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF9F2;
    }
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
    .question-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #FFD1D1;
        box-shadow: 2px 2px 10px rgba(255, 194, 209, 0.2);
        margin-bottom: 20px;
    }
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
        font-size: 2rem;
        font-weight: bold;
        margin-top: 15px;
    }
    .firewall-alert {
        background-color: #FFF3CD;
        border-left: 5px solid #FFC107;
        color: #856404;
        padding: 15px;
        border-radius: 8px;
        font-size: 0.9rem;
        margin-top: 15px;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 8종 캐릭터 대가족 매핑 데이터 (모두 해맑고 활기찬 공식 GIF 주소 엄선!)
character_db = {
    "치이카와 🐹": {
        "mbtis": ["INFP", "ISFP"],
        "desc": "소심하고 걱정이 많아 눈물 흘릴 때도 많지만, 소중한 친구들을 위해 누구보다 큰 용기를 내는 따뜻한 주인공이에요. 수줍음이 많고 감수성이 풍부하며, 말없이 타인의 아픔에 깊이 공감하는 따뜻한 마음씨를 가지고 있습니다 💖",
        "tag": "#수줍은_엔젤 #울보지만_용감해 #공감대장 #선한영향력",
        "local_file": "images/chiikawa.gif",
        "web_url": "https://media.tenor.com/98NGqBWbyrcAAAAj/%E3%81%A1%E3%81%84%E3%81%8F%E3%82%8F-chiikawa.gif",
        "emoji": "🐹💖✨"
    },
    "하치와레 🐱": {
        "mbtis": ["ENFP", "ESFP"],
        "desc": "말을 유창하게 잘하고 매사에 초긍정적인 마인드를 가진 활기찬 친구예요! 어려운 처지 속에서도 '어떻게든 되겠지!'라며 해맑게 위기를 이겨내며, 주변 사람들에게 다정한 말과 에너지를 불어넣어 주는 분위기 메이커입니다 🎵",
        "tag": "#초긍정 #호기심대왕 #어떻게든되겠지 #우정의콘서트",
        "local_file": "images/hachiware.gif",
        "web_url": "https://media.tenor.com/ip-HUMGOc-oAAAAC/chiikawa-hachiware-dance.gif",
        "emoji": "🐱🎵💙"
    },
    "우사기 🐰": {
        "mbtis": ["ENTP", "ESTP"],
        "desc": "어디로 튈지 모르는 미스터리하고 강력한 개성의 소유자! 말보단 행동이 먼저이며, 두려움 없이 기발한 아이디어로 눈앞의 문제를 뚝딱 해결해요. 남의 눈치를 보지 않고 인생을 온전히 신나게 개척하는 매력 토끼예요 ⚡",
        "tag": "#천재괴짜 #행동력대왕 #야하_우라_하아 #마이웨이_최강자",
        "local_file": "images/usagi.gif",
        "web_url": "https://media.tenor.com/HVCUxmPxTvAAAAAi/chiikawa-usagi.gif",
        "emoji": "🐰⚡🍍"
    },
    "쿠리만쥬 🌰": {
        "mbtis": ["ISTP", "INTP"],
        "desc": "혼자만의 조용한 여유와 맛있는 음식을 음미할 줄 아는 시크한 매력쟁이! 겉은 살짝 시크하고 초연해 보여도, 곁에서 조용히 챙겨주는 깊고 묵직한 정을 지녔어요. 세상사 초연한 태도로 자신만의 템포를 완성하는 인생 2회차 고수의 포스! ☕",
        "tag": "#인생2회차 #시크한_츤데레 #소소한_미식가 #안주와_음료한잔",
        "local_file": "images/kurimanju.gif",
        "web_url": "https://media.tenor.com/Tskv4K9w1qUAAAAC/chiikawa-kurimanju.gif",
        "emoji": "🌰☕🍁"
    },
    "시사 🦁": {
        "mbtis": ["ESFJ", "ENFJ"],
        "desc": "친절하고 살가우며, 원하는 목표를 이루기 위해 엄청난 노력을 기울이는 대단한 성실파예요! 모두에게 예의 바른 인사성 만점 사자이며, 언제나 밝은 에너지를 전파하며 주변 환경의 조화와 화합을 가장 중요하게 생각합니다 🦁",
        "tag": "#정리달인 #인사성만점 #성실아기사자 #우정의조율사",
        "local_file": "images/shisa.gif",
        "web_url": "https://media.tenor.com/E8YI9Ie69dIAAAAC/chiikawa-shisa.gif",
        "emoji": "🦁💖🌟"
    },
    "랏코 🦦": {
        "mbtis": ["ESTJ", "ENTJ"],
        "desc": "강력한 실력과 든든한 카리스마를 장착한 멋진 영웅이자 의지할 수 있는 스승님! 자신에게는 매우 엄격하고 프로답지만, 소중한 친구들에게는 한없이 자상하고 듬직해요. 남몰래 달콤한 초코 디저트를 탐닉하며 얼굴을 붉히는 숨막히는 반전 매력의 소유자입니다 🍰",
        "tag": "#카리스마멘토 #듬직한선배 #프로페셔널 #디저트_러버",
        "local_file": "images/rakko.gif",
        "web_url": "https://media.tenor.com/HHOKLQO4VYCCqwGf/chiikawa-rakko.gif",
        "emoji": "🦦🗡️🍫"
    },
    "포셰트 갑옷씨 ⚔️": {
        "mbtis": ["ISTJ", "ISFJ"],
        "desc": "묵묵히 뒤에서 규칙을 지키며 모두를 지켜주는 과묵하고 다정한 보디가드! 성실하고 꼼꼼하며, 손재주가 매우 뛰어나 소중한 사람들에게 아기자기한 수공예품을 만들어 선물하는 데서 엄청난 보람과 따뜻함을 느끼는 든든한 수호자 타입입니다 🧵",
        "tag": "#꼼꼼장인 #성실한갑옷 #바느질달인 #다정한보디가드",
        "local_file": "images/armor.gif",
        "web_url": "https://media.tenor.com/siORfInKM7Gq0Q62/yoroi-pochette.gif",
        "emoji": "⚔️🧵💝"
    },
    "모몬가 🐿️": {
        "mbtis": ["INTJ", "INFJ"],
        "desc": "새침떼기 외모 속에 원대한 우주적 정복 야망을 품고 있는 야심 가득한 친구예요! 자신에 대한 깊은 자부심이 하늘을 찌르며, '나를 귀여워해라!'라며 당당히 외치죠. 가끔은 도통 무슨 생각을 하는지 알 수 없는 독창적인 발상으로 사람들을 깜짝 놀라게 만듭니다 👑",
        "tag": "#나만의세계 #나를칭찬해라 #귀여운야심가 #반전매력덩어리",
        "local_file": "images/momonga.gif",
        "web_url": "https://media.tenor.com/Ga9mCjhiuToAAAAC/shaking-butt-shaking-rear.gif",
        "emoji": "🐿️👑🍑"
    }
}

# 4. 방화벽 완벽 방어형 출력 함수 (로컬 파일 우선, 깨지면 이모지 대체)
def show_character_media(local_path, web_url, emoji, caption):
    if os.path.exists(local_path):
        st.image(local_path, caption=caption, use_container_width=True)
    else:
        try:
            st.image(web_url, caption=caption, use_container_width=True)
        except Exception:
            st.warning("⚠️ 이미지를 웹에서 불러올 수 없습니다. 아래 귀여운 텍스트를 감상해 주세요!")
            
        st.markdown(f"""
            <div class="firewall-alert">
                ⚠️ <b>[방화벽 안내]</b> 학교 와이파이 등으로 이미지 로딩이 원활하지 않을 수 있습니다. <br>
                깃허브 내 <b><code>images/</code></b> 폴더를 생성하고 <b><code>{local_path.split('/')[-1]}</code></b> 파일을 넣어두면 학교 컴퓨터실에서도 100% 무조건 보입니다!
            </div>
            <h1 style="text-align: center; margin-top: 15px; font-size: 5rem; letter-spacing: 10px;">{emoji}</h1>
        """, unsafe_allow_html=True)

# 5. 질문지 정의 (MBTI 지표 은닉 구조)
questions = [
    {
        "axis": "EI",
        "text": "🎈 주말에 친한 친구가 예고도 없이 우리 집 앞에 찾아왔다! 나의 진짜 속마음은?",
        "options": [
            "우와 대박! 완전 깜짝 선물이다! 신나게 준비해서 당장 밖으로 뛰어나간다 🥳",
            "앗... 정말 기쁘고 고마운데... 오늘 나만의 힐링 시간이 필요했는데 조금 당황스럽다... 🏠"
        ],
        "mapping": ["E", "I"]
    },
    {
        "axis": "SN",
        "text": "💎 길을 가다가 우연히 정말 독특하고 예쁘게 반짝이는 돌멩이를 발견했을 때 나의 생각은?",
        "options": [
            "우와 신기하게 생겼네! 혹시 비싼 보석인가 인터넷에 시세를 검색해 본다 🔍",
            "이건 어쩌면 과거 마법사가 떨어뜨린 기억 소환석 아닐까? 가상의 시나리오를 상상해 본다 🪄"
        ],
        "mapping": ["S", "N"]
    },
    {
        "axis": "TF",
        "text": "😭 시험 점수를 생각보다 너무 못 받아서 친구가 우울하다며 속상하게 전화를 걸어왔다면?",
        "options": [
            "많이 속상하겠다ㅠㅠ 혹시 어떤 과목이 아쉬웠어? 다음 시험 공부법을 같이 고민해 준다 📊",
            "에구ㅠㅠ 정말 열심히 한 거 내가 다 아는데 너무 속상하다... 오늘 맛있는 거 먹으러 가자고 위로한다 🍰"
        ],
        "mapping": ["T", "F"]
    },
    {
        "axis": "JP",
        "text": "📝 방과 후에 친구들과 함께 맛있는 떡볶이를 먹으러 가기로 약속했을 때 나의 행동은?",
        "options": [
            "맛집 위치, 영업 시간, 먹고 갈 예쁜 카페 동선까지 미리 싹 다 파악해 놓는다 📍",
            "그냥 가기로 약속했으니 이따가 먹고 싶은 곳 눈에 띄면 들어가지 뭐! 하고 생각한다 💨"
        ],
        "mapping": ["J", "P"]
    }
]

# 6. 세션 상태 관리
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- 7. 메인 렌더링 영역 ---
st.markdown("<div class='title'>🌸 말랑말랑 먼작귀 대가족 테스트 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>풍성해진 먼작귀 대가족 중 당신의 진짜 단짝을 소환해 드릴게요!</div>", unsafe_allow_html=True)

# 7-1. 대기실 (Step 0)
if st.session_state.step == 0:
    show_character_media(
        local_path="images/main.gif", 
        web_url="https://media.tenor.com/ip-HUMGOc-oAAAAC/chiikawa-hachiware-dance.gif", 
        emoji="🐹🐱🐰🐿️", 
        caption="해맑게 어깨춤을 추는 대표 커플 🌸"
    )
    st.write("")
    if st.button("✨ 업그레이드 대가족 테스트 시작! ✨", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = []
        st.rerun()

# 7-2. 질문 루프 (Step 1 ~ 4)
elif 1 <= st.session_state.step <= 4:
    q_index = st.session_state.step - 1
    current_q = questions[q_index]
    
    progress_val = (st.session_state.step - 1) / 4.0
    st.progress(progress_val)
    st.write(f"📝 **{st.session_state.step}번째 방에서 단서를 수집하는 중...**")
    
    st.markdown(f"""
        <div class="question-box">
            <h4 style="color: #4A4A4A; line-height: 1.5;">{current_q['text']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    choice = st.radio(
        "마음이 이끄는 정답을 골라주세요!",
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

# 7-3. 결과 도출 (Step 5)
elif st.session_state.step == 5:
    user_mbti = "".join(st.session_state.answers)
    
    with st.spinner('☁️ 대가족 먼작귀들이 당신을 환영하기 위해 꽃가루를 장전하고 있습니다...☁️'):
        time.sleep(1.2)
        
    st.balloons()
    
    # 16가지 MBTI에 대해 8종 캐릭터를 분배하는 로직 작동!
    final_char = ""
    for char_name, info in character_db.items():
        if user_mbti in info["mbtis"]:
            final_char = char_name
            break
            
    if not final_char:
        final_char = "치이카와 🐹"  # 예외 예방 설계
        
    result_info = character_db[final_char]
    
    # 결과 요약 박스
    st.markdown(f"""
        <div class="result-box">
            <span style="font-size: 1.3rem; color: #FF7B93; font-weight: bold;">[ {user_mbti} ] 성향을 가진 당신은!</span>
            <div class="char-name">{final_char}</div>
            <p style="color: #9C515F; font-weight: bold; margin-top: 10px; font-size: 1.1rem;">{result_info['tag']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    # 개성 넘치고 활발한 캐릭터의 GIF를 무적 함수로 렌더링!
    show_character_media(
        local_path=result_info["local_file"],
        web_url=result_info["web_url"],
        emoji=result_info["emoji"],
        caption=f"해맑게 반겨주는 {final_char} 🌸"
    )
    
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
st.markdown("<p style='text-align: center; color: #BDC3C7; font-size: 0.85rem;'>제작: 당곡고등학교 멋진 개발자 학생 💖 | Streamlit Cloud 배포용</p>", unsafe_allow_html=True)
