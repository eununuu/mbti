import streamlit as st
import random

# 1. 웹페이지 기본 설정 (타이틀, 귀여운 이모지)
st.set_page_config(
    page_title="말랑말랑 먼작귀 MBTI 추천기",
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
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        color: #8C7A6B;
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    /* 결과 박스 스타일 */
    .result-box {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #FFC2D1;
        box-shadow: 3px 3px 15px rgba(255, 194, 209, 0.3);
        margin-top: 20px;
        text-align: center;
    }
    /* 서브 타이틀 스타일 */
    .char-name {
        color: #FF5C7C;
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI별 먼작귀 캐릭터 데이터 매핑
# 캐릭터 분류: 치이카와, 하치와레, 우사기, 쿠리만쥬, 시사, 모몬가, 랏코, 포셰트 갑옷씨
mbti_db = {
    "INFP": {"char": "치이카와 🐹", "desc": "소심하지만 누구보다 따뜻하고 주변을 챙기는 마음씨를 가졌어요. 겁이 많아도 소중한 친구들을 위해 용기를 내는 당신은 진정한 내면의 영웅!", "tag": "#공감대장 #울보지만_용감해 #수줍은_엔젤"},
    "ISFP": {"char": "치이카와 🐹", "desc": "따뜻하고 온화하며 삶의 소소한 행복을 즐길 줄 알아요. 갈등을 싫어하며 주변 사람들의 마음을 말없이 편안하게 해주는 수줍은 예술가 타입!", "tag": "#평화주의자 #소소한행복 #말랑말랑"},
    
    "ENFP": {"char": "하치와레 🐱", "desc": "호기심이 많고 긍정 에너지가 넘쳐나요! 친구들에게 긍정적인 말로 힘을 북돋아 주며, 어려운 상황에서도 '어떻게든 되겠지!'라며 헤쳐 나가는 분위기 메이커입니다.", "tag": "#초긍정 #호기심천국 #어떻게든되겠지"},
    "ESFP": {"char": "하치와레 🐱", "desc": "사람들과 어울리는 것을 좋아하고 에너지가 넘쳐요! 맛있는 것을 나눠 먹고 즐거운 추억을 만드는 데 온 진심을 다하는 활기찬 성격의 소유자입니다.", "tag": "#사교성만렙 #인기쟁이 #오늘을즐겨"},
    
    "ENTP": {"char": "우사기 🐰", "desc": "어디로 튈지 모르는 독특한 매력의 소유자! 머리가 좋고 임기응변에 강해 위기 상황도 장난처럼 유쾌하게 극복해 버려요. '우라!', '야하!' 하고 외치며 세상을 탐험해 보세요!", "tag": "#자유로운영혼 #예측불가 #천재토끼"},
    "ESTP": {"char": "우사기 🐰", "desc": "말보다는 행동이 먼저! 모험과 스릴을 즐기며, 어떤 복잡한 고민도 행동력 하나로 싹 날려 버리는 파워풀하고 매력 넘치는 개척자입니다.", "tag": "#행동파 #스릴중독 #에너지만랩"},
    
    "ISTP": {"char": "쿠리만쥬 🌰", "desc": "혼자만의 여유와 미식을 즐길 줄 아는 쿨가이! 겉으로는 무심해 보이지만 슬며시 맛있는 음식을 챙겨주는 츤데레 매력을 가지고 있어요. 세상사 초연한 고수의 포스!", "tag": "#인생2회차 #안주맛집 #알고보면_따뜻함"},
    "ESTJ": {"char": "랏코 🦦", "desc": "강력한 리더십과 계획성을 가진 멋진 선배! 자신에게는 엄격하지만 타인에게는 든든한 버팀목이 되어 줍니다. 가끔 남몰래 달콤한 디저트를 먹으며 스트레스를 푸는 귀여운 면도 있어요.", "tag": "#카리스마 #정석리더 #숨겨진_초코사랑"},
    
    "ISTJ": {"char": "포셰트 갑옷씨 ⚔️", "desc": "묵묵하고 성실하게 자신의 책임을 다하는 사람! 정해진 규칙을 잘 지키고, 주변 사람들을 위해 보이지 않는 곳에서 필요한 물건을 뚝딱 만들어 주는 든든하고 다정한 어른스러운 성격입니다.", "tag": "#프로성실러 #꼼꼼함 #츤데레장인"},
    "ISFJ": {"char": "포셰트 갑옷씨 ⚔️", "desc": "주변 사람들을 지키고 보살피는 수호자! 다정한 눈길로 다른 이들의 성장을 응원하고 챙겨주며, 자신이 만든 소소한 선물로 타인을 행복하게 만드는 데 큰 보람을 느낍니다.", "tag": "#수호천사 #다정다감 #바느질달인"},
    
    "ESFJ": {"char": "시사 🦁", "desc": "친절하고 예의 바르며, 목표를 위해 엄청난 노력을 기울이는 노력파! 모두에게 사랑받는 살가운 성격이며, 자신이 속한 커뮤니티의 조화를 가장 중요하게 생각합니다.", "tag": "#눈썹열일 #정리왕 #인사성바른_아기사자"},
    "ENFJ": {"char": "시사 🦁", "desc": "타인의 성장을 돕고 긍정적인 리더십을 발휘하는 따뜻한 조력자! 주변 사람들에게 에너지를 불어넣고 더 나은 내일을 위해 다 같이 으쌰으쌰 나아가는 다정한 리더입니다.", "tag": "#다정보스 #공감요정 #인류애가득"},
    
    "INTJ": {"char": "랏코 🦦", "desc": "엄청난 집중력과 지적 호기심을 지닌 전략가! 스스로 정한 목표를 완벽하게 달성해내는 멋진 능력을 가지고 있으며, 감정에 휘둘리지 않고 늘 냉철하고 명확하게 판단합니다.", "tag": "#독고다이 #프로페셔널 #목표달성"},
    "INFJ": {"char": "치이카와 🐹", "desc": "마음속 깊이 거대하고 아름다운 세계를 품고 있는 통찰력 있는 영혼! 다른 사람들의 상처를 조용히 어루만져 주며, 작고 여린 몸집 안에 세상을 바꾸는 조용한 의지를 품고 있어요.", "tag": "#통찰력 #속깊은친구 #소리없는_응원"},
    
    "ENTJ": {"char": "모몬가 🐿️", "desc": "귀여움으로 세상을 정복하려는 야망가! 목표가 생기면 저돌적으로 직진하며, '나를 칭찬해라!'라며 당당하게 요구하는 자신감 넘치는 모습이 얄밉지만 결코 미워할 수 없는 매력덩어리입니다.", "tag": "#야망가 #세상의중심 #나를칭찬해"},
    "INTP": {"char": "우사기 🐰", "desc": "남들의 시선은 신경 쓰지 않고 오직 호기심과 지적 탐구에 집중하는 괴짜 천재! 엉뚱해 보이는 행동 속에는 사실 아무도 예측하지 못한 기발한 논리와 번뜩이는 아이디어가 숨어 있습니다.", "tag": "#천재괴짜 #마이웨이 #아이디어뱅크"}
}

# 응원의 한마디 리스트 (결과 확인 시 무작위로 한 문장씩 띄워줍니다)
cheering_messages = [
    "오늘도 열심히 살아가느라 고생 많았어요! 토닥토닥 🌸",
    "하치와레처럼 '어떻게든 될 거야!'라는 마음으로 힘내 봐요! 💪",
    "우사기처럼 신나게 '야하-!' 외치며 스트레스를 날려버려요! 🎉",
    "달콤한 초코 슈크림을 먹으며 힐링하는 하루가 되길 바라요! 🍰",
    "가장 나다운 모습이 가장 귀엽고 사랑스럽답니다! ⭐"
]

# 4. 앱 UI 구현 부분
st.markdown("<div class='title'>🌸 먼작귀 MBTI 추천기 🌸</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>나와 꼭 닮은 먼지 쌓인 귀여운 녀석들은 누구일까요?</div>", unsafe_allow_html=True)

# 재미있는 인트로 일러스트 장식 대신 이모지 조합 배치
st.write("")
st.markdown("<h3 style='text-align: center;'>🐹 🐱 🐰 🌰 🦁 🦦</h3>", unsafe_allow_html=True)
st.write("")

# MBTI 선택 박스
mbti_list = sorted(list(mbti_db.keys()))
selected_mbti = st.selectbox(
    "👉 당신의 MBTI를 선택해 주세요!",
    options=mbti_list,
    index=0
)

# 분석하기 버튼
if st.button("✨ 나랑 닮은 먼작귀 확인하기! ✨"):
    # 로딩 애니메이션 효과
    with st.spinner('정성껏 분석하는 중... 몽글몽글...☁️'):
        # 약간의 딜레이를 주어 분석하는 느낌을 살립니다.
        import time
        time.sleep(1)
        
    # 축하 풍선 날리기 효과! 🎉
    st.balloons()
    
    # 선택된 MBTI 정보 가져오기
    result = mbti_db[selected_mbti]
    
    # 결과 출력 카드 구성 (HTML 스타일링)
    st.markdown(f"""
        <div class="result-box">
            <span style="font-size: 1.2rem; color: #7F8C8D; font-weight: bold;">{selected_mbti}인 당신에게 찰떡인 캐릭터는?</span>
            <div class="char-name">{result['char']}</div>
            <p style="color: #6D214F; font-weight: bold; margin-top: 10px; font-size: 1.05rem;">{result['tag']}</p>
            <hr style="border: 0.5px solid #FFD1D1; margin: 15px 0;">
            <p style="color: #4A4A4A; line-height: 1.6; text-align: justify; word-break: keep-all;">{result['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 랜덤 응원 메시지 노출
    st.write("")
    st.info(f"💌 **먼작귀 친구들의 편지:** {random.choice(cheering_messages)}")

# 하단 푸터 (Footer)
st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #BDC3C7; font-size: 0.85rem;'>제작: 당곡고등학교 멋진 개발자 학생 💖 | Streamlit Cloud 배포용</p>", unsafe_allow_html=True)
