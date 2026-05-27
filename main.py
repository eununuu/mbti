import streamlit as st
import time

# 1. 웹페이지 기본 설정 (타이틀, 귀여운 이모지)
st.set_page_config(
    page_title="말랑말랑 먼작귀 MBTI 테스트",
    page_icon="🌸",
    layout="centered"
)

# 2. 파스텔톤의 귀여운 커스텀 스타일 적용 (CSS)
st.markdown("""
    <style>
    /* 전체 배경색 지정 */
    .stApp {
        background-color: #FFF9F2;
    }
    /* 타이틀 스타일 */
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
    /* 질문지 박스 스타일 */
    .question-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #FFD1D1;
        box-shadow: 2px 2px 10px rgba(255, 194, 209, 0.2);
        margin-bottom: 20px;
    }
    /* 결과 박스 스타일 */
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
    </style>
""", unsafe_allow_html=True)

# 3. 캐릭터 및 결과 매핑 데이터 (진짜 신나게 춤추고 해맑은 GIF 애니메이션 주소로 올킬!)
character_db = {
    "치이카와 🐹": {
        "mbtis": ["INFP", "ISFP", "INFJ", "ISFJ"],
        "desc": "소심하고 걱정이 많아 눈물 흘릴 때도 많지만, 소중한 친구들을 위해 누구보다 큰 용기를 내는 따뜻한 주인공이에요. 수줍음이 많고 감수성이 풍부하며, 말없이 타인의 아픔에 깊이 공감하는 따뜻한 마음씨를 가지고 있습니다 💖",
        "tag": "#수줍은_엔젤 #울보지만_용감해 #공감대장 #선한영향력",
        "gif": "https://media.tenor.com/98NGqBWbyrcAAAAj/%E3%81%A1%E3%81%84%E3%81%8F%E3%82%8F-chiikawa.gif"
    },
    "하치와레 🐱": {
        "mbtis": ["ENFP", "ESFP", "ENFJ", "ESFJ"],
        "desc": "말을 유창하게 잘하고 매사에 초긍정적인 마인드를 가진 활기찬 친구예요! 어려운 처지 속에서도 '어떻게든 되겠지!'라며 해맑게 위기를 이겨내며, 주변 사람들에게 다정한 말과 에너지를 불어넣어 주는 진정한 리더이자 분위기 메이커입니다 🎵",
        "tag": "#초긍정 #호기심대왕 #어떻게든되겠지 #우정의콘서트",
        # 하치와레와 치이카와가 함께 룰루랄라 무조건 신나게 어깨춤을 추는 해맑은 댄스 GIF
        "gif": "https://media.tenor.com/ip-HUMGOc-oAAAAC/chiikawa-hachiware-dance.gif"
    },
    "우사기 🐰": {
        "mbtis": ["ENTP", "ESTP", "INTP", "ISTP"],
        "desc": "어디로 튈지 모르는 미스터리하고 강력한 개성의 소유자! 말보단 행동이 먼저이며, 두려움 없이 기발한 아이디어로 눈앞의 몬스터를 해치우는 위풍당당한 해결사입니다. 남의 눈치를 보지 않고 인생을 온전히 즐기는 똑똑한 마이웨이 토끼예요 ⚡",
        "tag": "#천재괴짜 #행동력대왕 #야하_우라_하아 #마이웨이_최강자",
        "gif": "https://media.tenor.com/HVCUxmPxTvAAAAAi/chiikawa-usagi.gif"
    },
    "모몬가 🐿️": {
        "mbtis": ["ENTJ", "INTJ", "ESTJ", "ISTJ"],
        "desc": "귀여운 외모 속에 거대한 정복 야망을 품고 있는 자신감 넘치는 캐릭터예요! 자존감이 하늘을 찌르며 타인에게 끊임없이 '칭찬'과 '관심'을 당당하게 요구하지만, 그 당당함과 빈틈 가득한 반전 매력 덕분에 결코 미워할 수 없는 존재감을 자랑합니다 👑",
        "tag": "#야망가 #세상의중심은_나 #나를칭찬해라 #새침떼기공주",
        # 모몬가가 해맑게 씰룩쌜룩 치명적인 엉덩이 댄스를 추는 초귀여운 GIF
        "gif": "https://media.tenor.com/Ga9mCjhiuToAAAAC/shaking-butt-shaking-rear.gif"
    }
}

# 4. 질문지 데이터 정의 (겉으로는 MBTI 성향 단어가 전혀 보이지 않도록 분리 설계!)
questions = [
    {
        "axis": "EI",
        "text": "🎈 주말에 친한 친구가 예고도 없이 우리 집 앞에 찾아왔다! 나의 진짜 속마음은?",
        "options": [
            "우와 대박! 완전 깜짝 선물이다! 신나게 준비해서 당장 밖으로 뛰어나간다 🥳",
            "앗... 정말 기쁘고 고마운데... 오늘 나만의 힐링 시간이 필요했는데 조금 당황스럽다... 🏠"
        ],
        "mapping": ["E", "I"]  # 첫 번째 선택지는 E, 두 번째는 I로 내부 매핑
    },
    {
        "axis": "SN",
        "text": "💎 길을 가다가 우연히 정말 독특하고 예쁘게 반짝이는 돌멩이를 발견했을 때 나의 생각은?",
        "options": [
            "우와 신기하게 생겼네! 혹시 비싼 보석인가 인터넷에 시세를 검색해 본다 🔍",
            "이건 어쩌면 과거 마법사가 떨어뜨린 기억 소환석 아닐까? 가상의 시나리오를 상상해 본다 🪄"
        ],
        "mapping": ["S", "N"]  # 첫 번째 선택지는 S, 두 번째는 N으로 내부 매핑
    },
    {
        "axis": "TF",
        "text": "😭 시험 점수를 생각보다 너무 못 받아서 친구가 우울하다며 속상하게 전화를 걸어왔다면?",
        "options": [
            "많이 속상하겠다ㅠㅠ 혹시 어떤 과목이 아쉬웠어? 다음 시험 공부법을 같이 고민해 준다 📊",
            "에구ㅠㅠ 정말 열심히 한 거 내가 다 아는데 너무 속상하다... 오늘 맛있는 거 먹으러 가자고 위로한다 🍰"
        ],
        "mapping": ["T", "F"]  # 첫 번째 선택지는 T, 두 번째는 F로 내부 매핑
    },
    {
        "axis": "JP",
        "text": "📝 방과 후에 친구들과 함께 맛있는 떡볶이를 먹으러 가기로 약속했을 때 나의 행동은?",
        "options": [
            "맛집 위치, 영업 시간, 먹고 갈 예쁜 카페 동선까지 미리 싹 다 파악해 놓는다 📍",
            "그냥 가기로 약속했으니 이따가 먹고 싶은 곳 눈에 띄면 들어가지 뭐! 하고 생각한다 💨"
        ],
        "mapping": ["J", "P"]  # 첫 번째 선택지는 J, 두 번째는 P로 내부 매핑
    }
]

# 5. 세션 상태(Session State) 초기화
if "step" not in st.session_state:
    st.session_state.step = 0 # 0: 대기실, 1~4: 질문 단계, 5: 결과 페이지
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- 6. 화면 구현 시작 ---

st.markdown("<div class='title'>🌸 말랑말랑 먼작귀 MBTI 테스트 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>나의 숨겨진 성향은 어떤 먼작귀 캐릭터와 꼭 닮아 있을까요?</div>", unsafe_allow_html=True)

# 6-1. 테스트 시작 대기실 (step 0)
if st.session_state.step == 0:
    # 로고 일러스트로 귀엽게 시작
    st.image("https://media.tenor.com/ip-HUMGOc-oAAAAC/chiikawa-hachiware-dance.gif", use_container_width=True)
    st.write("")
    st.info("💡 **안내:** 단 4개의 일상 질문으로 당신의 진짜 성향을 족집게처럼 분석해 드립니다!")
    if st.button("✨ 테스트 시작하기! (두근두근) ✨", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = []
        st.rerun()

# 6-2. 질문 진행 단계 (step 1 ~ 4)
elif 1 <= st.session_state.step <= 4:
    q_index = st.session_state.step - 1
    current_q = questions[q_index]
    
    # 진행 상황 프로그레스 바
    progress_val = (st.session_state.step - 1) / 4.0
    st.progress(progress_val)
    st.write(f"📝 **{st.session_state.step}번째 질문지에 대답하는 중...**")
    
    st.markdown(f"""
        <div class="question-box">
            <h4 style="color: #4A4A4A; line-height: 1.5;">{current_q['text']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    # 두 개의 답변 라디오 버튼 (MBTI 힌트 완벽 차단!)
    choice = st.radio(
        "당신의 선택은 무엇인가요?",
        options=current_q["options"],
        key=f"q_{st.session_state.step}"
    )
    
    st.write("")
    
    # 다음으로 넘어가기 버튼
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ 처음으로", use_container_width=True):
            st.session_state.step = 0
            st.session_state.answers = []
            st.rerun()
            
    with col2:
        if st.button("다음 질문으로 ➡️", use_container_width=True):
            # 사용자가 고른 선택지의 인덱스(0 또는 1)를 찾아, 매핑 테이블의 알파벳(E, I 등)을 가져옵니다.
            selected_idx = current_q["options"].index(choice)
            selected_letter = current_q["mapping"][selected_idx]
            
            # 사용자 답변 누적
            st.session_state.answers.append(selected_letter)
            st.session_state.step += 1
            st.rerun()

# 6-3. 결과 도출 단계 (step 5)
elif st.session_state.step == 5:
    user_mbti = "".join(st.session_state.answers)  # 예: "ENFP"
    
    with st.spinner('☁️ 당신의 영혼을 쏙 빼닮은 먼작귀 친구를 소환하는 중...☁️'):
        time.sleep(1.5)
        
    st.balloons() # 축하 풍선 팡팡! 🎉
    
    # MBTI 결과 매핑
    final_char = ""
    for char_name, info in character_db.items():
        if user_mbti in info["mbtis"]:
            final_char = char_name
            break
            
    if not final_char:
        final_char = "치이카와 🐹"  # 안전 장치용 기본값
        
    result_info = character_db[final_char]
    
    # 결과 화면 출력
    st.markdown(f"""
        <div class="result-box">
            <span style="font-size: 1.3rem; color: #FF7B93; font-weight: bold;">[ {user_mbti} ] 성향을 가진 당신은!</span>
            <div class="char-name">{final_char}</div>
            <p style="color: #9C515F; font-weight: bold; margin-top: 10px; font-size: 1.1rem;">{result_info['tag']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    # 귀여운 공식 캐릭터의 진짜 '해맑고 신나는' GIF 띄우기!
    st.image(result_info["gif"], caption=f"신나게 움직이는 {final_char}의 모습 🌸", use_container_width=True)
    
    st.markdown(f"""
        <div style="background-color: #FFF; padding: 20px; border-radius: 15px; border: 1px solid #FFD1D1; margin-top: 15px; line-height: 1.6; text-align: justify; word-break: keep-all;">
            {result_info['desc']}
        </div>
    """, unsafe_allow_html=True)
    
    # 다시 하기 버튼
    st.write("")
    if st.button("🔄 테스트 다시 도전하기!", use_container_width=True):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()

# 하단 푸터 (Footer)
st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #BDC3C7; font-size: 0.85rem;'>제작: 당곡고등학교 멋진 개발자 학생 💖 | Streamlit Cloud 배포용</p>", unsafe_allow_html=True)
