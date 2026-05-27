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

# 3. 데이터 및 캐릭터 정의 (실제 움직이는 공식 GIF 애니메이션 주소 사용)
# 이미지 링크가 활성화되지 않을 때를 대비해 로컬 이미지 불러오기 팁도 하단에 적어둘게요!
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
        "gif": "https://media.tenor.com/Iz0VY8qjc4MAAAAC/hachiware-chiikawa.gif"
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
        "gif": "https://media.tenor.com/a_zv3hlKrEAAAAAi/mario-g.gif" # 모몬가/귀여운 댄스 대용 GIF
    }
}

# 4. 질문지 데이터 정의 (각 질문은 성향의 한쪽 축을 결정합니다)
questions = [
    {
        "axis": "EI",
        "text": "🎈 주말에 친한 친구가 예고도 없이 우리 집 앞에 찾아왔다! 나의 첫 생각은?",
        "options": [
            "우와 대박! 완전 깜짝 선물이다! 신나게 준비해서 당장 밖으로 뛰어나간다 🥳 (E 성향)",
            "앗... 정말 기쁘고 고마운데... 오늘 나만의 힐링 시간이 필요했는데 조금 당황스럽다... 🏠 (I 성향)"
        ]
    },
    {
        "axis": "SN",
        "text": "💎 길을 가다가 우연히 정말 독특하고 예쁘게 반짝이는 돌멩이를 발견했을 때 나의 행동은?",
        "options": [
            "우와 신기하게 생겼네! 혹시 비싼 보석인가 검색해 보거나 가만히 보고 둔다 🔍 (S 성향)",
            "이건 어쩌면 과거 마법사들이 떨어뜨린 기억 소환석 아닐까? 혼자 판타지 소설을 집필하기 시작한다 🪄 (N 성향)"
        ]
    },
    {
        "axis": "TF",
        "text": "😭 친구가 시험 점수를 생각보다 너무 못 받아서 우울하다며 속상하게 전화를 걸어왔다면?",
        "options": [
            "아고 속상하겠다... 어떤 과목이 아쉬웠어? 다음 시험엔 어떻게 준비할지 현실적인 조언과 전략을 세워준다 📊 (T 성향)",
            "에구ㅠㅠ 정말 고생 많았는데 너무 슬프다... 고생한 너를 위해 맛있는 거 먹으러 가자고 위로를 건넨다 🍰 (F 성향)"
        ]
    },
    {
        "axis": "JP",
        "text": "📝 방과 후에 친구들과 함께 떡볶이를 먹으러 가기로 약속했을 때 나의 모습은?",
        "options": [
            "맛집 위치, 가볼 만한 카페 정보, 걸어갈 동선을 머릿속으로 미리 싹 정해놓는다 📍 (J 성향)",
            "그냥 가기로 했으니까 이따 모여서 근처에 문 열려 있는 곳 아무 데나 가자고 생각한다 💨 (P 성향)"
        ]
    }
]

# 5. 세션 상태(Session State) 초기화 (스트림릿에서 페이지가 바뀌어도 데이터를 유지하게 해줍니다)
if "step" not in st.session_state:
    st.session_state.step = 0 # 0: 대기실, 1~4: 질문 단계, 5: 결과 페이지
if "answers" not in st.session_state:
    st.session_state.answers = []

# --- 6. 화면 구현 시작 ---

st.markdown("<div class='title'>🌸 말랑말랑 먼작귀 MBTI 테스트 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>나의 성향은 어떤 먼작귀 캐릭터와 꼭 닮아 있을까요?</div>", unsafe_allow_html=True)

# 6-1. 테스트 시작 대기실 (step 0)
if st.session_state.step == 0:
    st.image("https://media.tenor.com/98NGqBWbyrcAAAAj/%E3%81%A1%E3%81%84%E3%81%8F%E3%82%8F-chiikawa.gif", use_container_width=True) # 대문 일러스트
    st.write("")
    st.info("💡 **안내:** 단 4개의 질문으로 당신이 숨겨온 먼작귀 속 정체성을 완벽히 분석해 드립니다!")
    if st.button("✨ 테스트 시작하기! (두근두근) ✨", use_container_width=True):
        st.session_state.step = 1
        st.session_state.answers = []
        st.rerun()

# 6-2. 질문 진행 단계 (step 1 ~ 4)
elif 1 <= st.session_state.step <= 4:
    q_index = st.session_state.step - 1
    current_q = questions[q_index]
    
    # 진행 상황을 귀엽게 보여주는 프로그레스 바(ProgressBar)
    progress_val = (st.session_state.step - 1) / 4.0
    st.progress(progress_val)
    st.write(f"📝 **{st.session_state.step}번째 탐험 중... (총 4문항)**")
    
    st.markdown(f"""
        <div class="question-box">
            <h4 style="color: #4A4A4A; line-height: 1.5;">{current_q['text']}</h4>
        </div>
    """, unsafe_allow_html=True)
    
    # 두 개의 답변 라디오 버튼 구성
    choice = st.radio(
        "마음에 드는 생각을 골라보세요!",
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
            # 사용자가 선택한 답변의 맨 끝 괄호 안의 알파벳(E, I, S, N, T, F, J, P)을 추출하여 누적합니다.
            selected_letter = choice.split("(")[-1][0]
            st.session_state.answers.append(selected_letter)
            st.session_state.step += 1
            st.rerun()

# 6-3. 결과 도출 단계 (step 5)
elif st.session_state.step == 5:
    # 4글자의 MBTI 결과 생성 (예: "ENFP")
    user_mbti = "".join(st.session_state.answers)
    
    with st.spinner('☁️ 당신과 꼭 닮은 먼작귀 친구를 소환 중입니다... 몽글몽글...☁️'):
        time.sleep(1.5)
        
    st.balloons() # 축하 풍선 팡팡! 🎉
    
    # MBTI 결과에 따라 4대 대표 캐릭터 매핑
    final_char = ""
    for char_name, info in character_db.items():
        if user_mbti in info["mbtis"]:
            final_char = char_name
            break
            
    # 매핑되지 않는 외외의 성향이 생겼을 때의 예외 처리 (방어적 코드 설계 학습!)
    if not final_char:
        final_char = "치이카와 🐹" # 기본값 지정
        
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
    # 귀여운 공식 캐릭터 GIF 이미지 띄우기!
    st.image(result_info["gif"], caption=f"해맑게 움직이는 {final_char}의 모습 🌸", use_container_width=True)
    
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
