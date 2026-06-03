# -*- coding: utf-8 -*-
import sys
from _components import head, nav, FOOTER
from _widgets import WIDGETS, SHARED_JS

# 60 分鐘排程（取自 HCF 團體課程課綱手冊）；key 對應 COURSES 的 slug
CURRICULUM = {
 "muaythai": ("LV.1 新手泰拳 ・ 60 分鐘排程", [
    ("0–12 分","集體暖身","關節活動、跳繩／原地步法、動態伸展，喚醒身體"),
    ("12–20 分","體能心肺","高強度間歇（HIIT）：開合跳、波比、核心，啟動代謝"),
    ("20–38 分","技術指導","當日主題拆解：站架、直拳、掃踢、肘膝其一，教練示範"),
    ("38–60 分","分組打靶","兩兩持靶互打，教練巡場修正動作、放大每個進步"),
 ]),
 "kickboxing": ("LV.1 踢拳腿連擊 ・ 60 分鐘排程", [
    ("0–12 分","集體暖身","關節活動、步法移動、動態伸展"),
    ("12–20 分","體能心肺","間歇心肺，重點在下肢與核心"),
    ("20–38 分","技術指導","拳腿連擊組合：手法接腿法的流暢轉換，刪去纏抱"),
    ("38–60 分","分組打靶","連擊組合上靶，追求速度與節奏感"),
 ]),
 "sanda": ("LV.1 散打 ・ 60 分鐘排程", [
    ("0–12 分","集體暖身","關節活動、跌撲保護、動態伸展"),
    ("12–20 分","體能心肺","核心與下肢爆發，建立摔技所需穩定度"),
    ("20–38 分","技術指導","遠踢控距、近身入摔，抱摔過肩摔拆解"),
    ("38–60 分","分組演練","餵招與條件對練，距離轉換與重心爭奪"),
 ]),
 "strength": ("LV.1 肌力體能 ・ 60 分鐘排程", [
    ("0–10 分","動態暖身","關節活動度、神經喚醒、徒手熱身"),
    ("10–34 分","肌力主訓","壺鈴、啞鈴、自體重量：深蹲／硬舉／推／拉／核心，循環式"),
    ("34–52 分","功能性與爆發","跳躍、投擲、敏捷——練協調、爆發、活動度"),
    ("52–60 分","收操伸展","靜態伸展、呼吸放鬆、降心率"),
 ]),
}

# Each course: slug, names, hero media, tagline, intro, why(list of dict), learn(list), forwho(list), faq(list of (q,a)), bookId
COURSES = {
"muaythai": {
  "active":"courses","zh":"泰拳","en":"Muay Thai","tag":"八肢的藝術","book":"mt-trial",
  "img":"course_muaythai.jpg","video":"course_muaythai.mp4",
  "hero_sub":"拳、肘、膝、腿，全身都是武器。",
  "lead":"泰拳被稱為「八肢的藝術」——雙拳、雙肘、雙膝、雙腿，八個攻擊點，是站立格鬥技裡最全面、最兇悍的一門。但它教你的，從來不只是怎麼打人。",
  "why":[
    ("fa-fire","最高效的燃脂引擎","一堂泰拳課平均消耗 600–800 大卡。大量的核心旋轉與節奏性打擊，讓你在不知不覺中雕塑出緊實的腰腹與線條。"),
    ("fa-shield-halved","真正帶得走的防身","泰拳的距離控制與膝肘技，是近身自衛最實用的工具。你練的每一拳，都是真正能保護自己的底氣。"),
    ("fa-brain","把壓力一拳打散","當你全力踢中沙包的那一刻，工作、人際、煩惱全部歸零。這是最誠實、也最痛快的紓壓方式。"),
  ],
  "learn":["基本站架、步法與重心轉移","直拳、勾拳、上勾拳的發力鏈","掃踢、推蹬與膝撞的距離感","格擋、閃避與反擊節奏","靶位實戰與組合技串接"],
  "forwho":[
    ("零基礎新手","從沒運動過也沒關係，80% 的學員和你一樣從零開始。"),
    ("想減脂塑形","比起跑步機，你會更期待每一堂課。"),
    ("壓力大的上班族","下班後最好的解壓出口。"),
    ("想學防身的女性","距離與節奏，比力氣更重要。"),
  ],
  "faq":[
    ("完全沒基礎可以練泰拳嗎？","可以。教練會從最基本的站架開始帶，循序漸進，不會讓你一開始就對打。"),
    ("會不會很容易受傷？","日常訓練以打靶、打沙包為主，全程在教練監督下進行，安全是第一順位。"),
    ("女生練泰拳會變很壯嗎？","不會。泰拳訓練主要是雕塑線條與提升心肺，會讓你更緊實、更有力量感，而不是變壯。"),
  ],
},
"kickboxing": {
  "active":"courses","zh":"踢拳","en":"Kickboxing","tag":"速度與節奏的博弈","book":"kb-trial",
  "img":"course_kickboxing.jpg","video":"course_kickboxing.mp4",
  "hero_sub":"快、準、狠，攻防之間只在一瞬。",
  "lead":"踢拳講究的是流暢的攻防轉換與爆發節奏。它比泰拳更強調速度與步法，是一門讓你越打越上癮、越打越靈活的格鬥技。",
  "why":[
    ("fa-bolt","爆發力與反應速度","踢拳的快節奏組合，能有效訓練你的協調性、反應與爆發力，讓身體變得更靈活。"),
    ("fa-person-running","修長下半身線條","大量的踢擊與步法移動，精準刺激臀腿肌群，是打造修長腿部線條的高效途徑。"),
    ("fa-heart-pulse","心肺爆表的暢快","回合制的高強度間歇，讓你的心肺在每一堂課都被推到新的高度。"),
  ],
  "learn":["拳法與踢法的快速切換","前手刺拳與後手重拳的時機","邊腿、前踢與膝擊的組合","步法移動與出入距離","回合制的攻防節奏訓練"],
  "forwho":[
    ("想要靈活敏捷","踢拳讓你的身體反應更快、更協調。"),
    ("覺得重訓太單調","用節奏和組合技取代數槓片的無聊。"),
    ("想雕塑腿臀線條","踢擊就是最好的下半身訓練。"),
    ("喜歡有節奏的運動","像在打一場流動的舞，停不下來。"),
  ],
  "faq":[
    ("踢拳和泰拳有什麼不同？","踢拳更強調速度、步法與拳腿的快速切換；泰拳則多了肘、膝與纏鬥。新手兩者都很適合入門。"),
    ("柔軟度不好可以踢高嗎？","可以從低位踢擊開始，柔軟度會隨著訓練自然進步，不需要一開始就踢過頭。"),
    ("需要很好的體力嗎？","教練會依你的程度調整強度，跟著上幾堂課，體力會明顯提升。"),
  ],
},
"sanda": {
  "active":"courses","zh":"散打","en":"Sanda","tag":"踢打摔的全面對抗","book":"sd-trial",
  "img":"course_sanda.jpg","video":"course_sanda.mp4",
  "hero_sub":"能踢、能打、能摔，最接近實戰的搏擊。",
  "lead":"散打融合了踢、打、摔三大元素，是中華武術裡最接近真實對抗的搏擊系統。它不只練攻擊，更練如何在混亂中保持平衡、控制對手。",
  "why":[
    ("fa-hand-fist","最完整的實戰技術","踢打結合貼身摔，讓你面對各種距離都有應對方式，是防身的全能解。"),
    ("fa-dumbbell","打造鋼鐵核心","摔技與防摔需要強大的核心與全身協調，散打會把你的身體重新整合。"),
    ("fa-chess","格鬥中的策略思維","散打是一場物理博弈，你會學會預判、控制與創造機會。"),
  ],
  "learn":["踢打基礎與距離管理","抱摔、過肩摔與防摔技術","貼身纏鬥的重心爭奪","接腿摔與反擊時機","實戰情境下的攻防判斷"],
  "forwho":[
    ("追求實戰能力","散打是踢打摔三合一的全面搏擊。"),
    ("想強化核心與爆發","摔技訓練會徹底喚醒你的核心。"),
    ("有其他格鬥基礎","想補足貼身與摔法的最佳選擇。"),
    ("喜歡對抗與策略","這是一場身體與頭腦的雙重博弈。"),
  ],
  "faq":[
    ("散打是不是很危險？","訓練循序漸進，從技術拆解到護具對練，全程教練在場把關，新手也能安全入門。"),
    ("體型瘦小適合練散打嗎？","非常適合。散打強調技巧、時機與槓桿，而不是單純比力氣，體型不是限制。"),
    ("沒有任何武術基礎可以練嗎？","可以。教練會從最基礎的踢打與重心開始帶起。"),
  ],
},
"strength": {
  "active":"courses","zh":"肌力體能","en":"Strength & Conditioning","tag":"格鬥者的身體工程","book":"sc-trial",
  "img":"course_sc.jpg","video":"course_sc.mp4",
  "hero_sub":"不練死肌肉，練真正能用的力量。",
  "lead":"肌力體能不是健美式的「練好看」，而是為了讓你的身體在格鬥與生活中真正派得上用場。我們訓練的是功能性力量、關節穩定與代謝效率。",
  "why":[
    ("fa-gauge-high","打造易瘦體質","透過高強度間歇與複合動作，提升基礎代謝，讓你連睡覺都在燃脂。"),
    ("fa-bone","強化關節與穩定度","正確的肌力訓練能保護你的關節，降低運動與日常的受傷風險。"),
    ("fa-bolt-lightning","支撐你的格鬥表現","更強的核心與爆發力，會直接反映在你的拳、踢、摔的品質上。"),
  ],
  "learn":["深蹲、硬舉、推拉的正確動作模式","核心抗旋轉與穩定訓練","高強度間歇 (HIIT) 心肺強化","爆發力與協調性訓練","訓練後的恢復與伸展"],
  "forwho":[
    ("想提升代謝減脂","功能性訓練是燃脂的高效引擎。"),
    ("格鬥表現遇到瓶頸","力量是技術的地基。"),
    ("久坐、體態不佳","重新建立正確的身體動作模式。"),
    ("想要不易受傷的身體","穩定的關節，是長久運動的本錢。"),
  ],
  "faq":[
    ("我只想學格鬥，需要練肌力嗎？","強烈建議。肌力體能是所有格鬥技的地基，能讓你打得更重、更久、更不容易受傷。"),
    ("會不會練得很壯很笨重？","不會。我們的訓練目標是功能性與線條，而非健美式的肌肉肥大。"),
    ("沒有重訓經驗可以參加嗎？","可以。教練會先教你正確的動作模式，再循序漸進增加強度。"),
  ],
},
"group-class": {
  "active":"courses","zh":"團體課程","en":"Group Class","tag":"和戰友一起變強","book":"mt-trial",
  "img":"course_muaythai.jpg","video":"course_muaythai.mp4",
  "hero_sub":"一個人練得久，一群人練得遠。",
  "lead":"團體課是 HCF 的核心。在這裡，你不會孤單地對著鏡子流汗——一群目標一致的戰友會推著你前進。每堂 60 分鐘，從暖身到實戰，完整而扎實。",
  "why":[
    ("fa-people-group","團隊氛圍推著你前進","有人一起流汗、一起喊聲，你會發現自己能撐得比想像中更久。"),
    ("fa-clock","結構完整的 60 分鐘","集體暖身、體能心肺、技術指導、分組靶修，一堂課把該練的都練到。"),
    ("fa-coins","最划算的入門選擇","體驗只要 $400，無限方案每月暢練，是最沒有負擔的開始方式。"),
  ],
  "learn":["動態暖身與關節活動","體能與心肺強化","當日主題技術教學（泰拳/踢拳/散打輪替）","分組靶位對練","收操伸展與恢復"],
  "forwho":[
    ("喜歡熱血氛圍","一群人一起練，動力完全不一樣。"),
    ("預算有限的新手","$400 體驗，無痛開始。"),
    ("想規律運動","固定課表，幫你養成習慣。"),
    ("想認識同好","在這裡，戰友就是朋友。"),
  ],
  "faq":[
    ("團體課一班大概多少人？","採小班制，教練能照顧到每一位學員，不用擔心被忽略。"),
    ("跟不上大家怎麼辦？","教練會依個人狀況調整，每個人都有自己的節奏，不需要勉強。"),
    ("團體課有分程度嗎？","課程設計讓新手與老手都能各取所需，新手練基礎，老手練細節與強度。"),
  ],
},
"private-class": {
  "active":"courses","zh":"私人課程","en":"Private Coaching","tag":"100% 為你打造","book":"private-1",
  "img":"course_sc.jpg","video":"course_sc.mp4",
  "hero_sub":"教練的全部注意力，只在你身上。",
  "lead":"如果你想用最快的速度進步，私人課是答案。一對一的專屬特訓，教練 100% 針對你的體能、目標與弱點，量身打造每一堂課。進步速度，是團體課的三倍。",
  "why":[
    ("fa-bullseye","精準突破你的弱點","教練看著你的每一個動作，即時修正，不讓壞習慣定型。"),
    ("fa-rocket","三倍速的進步曲線","沒有等待、沒有分心，整堂課都是你的有效訓練時間。"),
    ("fa-calendar-check","彈性的專屬時段","依你的時間安排課程，忙碌的你也能穩定訓練。"),
  ],
  "learn":["個人體能與動作評估","針對目標的客製化課表","一對一動作精修與即時回饋","長時間高品質靶修","階段性進度追蹤"],
  "forwho":[
    ("想快速進步","一對一是最高效的學習方式。"),
    ("有特定目標","減重、比賽、防身，量身規劃。"),
    ("時間不固定","彈性約課，配合你的行程。"),
    ("想被完整看見","教練的注意力，全程都在你身上。"),
  ],
  "faq":[
    ("私人課比團體課好嗎？","各有優勢。私人課進步最快、最客製；團體課氛圍好、最划算。很多學員會兩者搭配。"),
    ("可以指定教練嗎？","可以。你可以依專長與風格選擇適合你的教練，詳見教練團隊頁面。"),
    ("一堂私人課多長時間？","標準一對一為完整課程時間；另有 40 分鐘的私人打靶課可選。"),
  ],
},
}

def render_course(slug, c):
    why = "".join(f"""
                <div class="border hairline bg-brand-bg p-8 hover:border-brand-red/50 transition-colors fade-up">
                    <div class="w-12 h-12 border border-brand-red/40 text-brand-red flex items-center justify-center mb-5 text-xl"><i class="fa-solid {ic}"></i></div>
                    <h3 class="text-lg font-black tracking-widest text-brand-text mb-3">{t}</h3>
                    <p class="text-sm text-brand-muted leading-relaxed tracking-wider">{d}</p>
                </div>""" for ic,t,d in c["why"])
    learn = "".join(f"""
                    <li class="flex items-start gap-4 fade-up"><span class="text-brand-red font-mono text-sm mt-0.5">{i:02d}</span><span class="text-brand-text tracking-wider">{x}</span></li>""" for i,x in enumerate(c["learn"],1))
    forwho = "".join(f"""
                <div class="border hairline bg-brand-panel p-6 hover:border-brand-red/50 transition-colors fade-up">
                    <h4 class="text-brand-text font-bold tracking-widest mb-2 flex items-center gap-2"><i class="fa-solid fa-check text-brand-red text-xs"></i>{t}</h4>
                    <p class="text-sm text-brand-muted leading-relaxed tracking-wider">{d}</p>
                </div>""" for t,d in c["forwho"])
    faq = "".join(f"""
                <details class="group border hairline bg-brand-bg hover:border-brand-red/50 transition-colors">
                    <summary class="flex justify-between items-center px-8 py-6 cursor-pointer list-none outline-none interactive-el"><span class="text-brand-text font-bold tracking-widest">{q}</span><i class="fa-solid fa-plus text-brand-red text-sm group-open:rotate-45 transition-transform duration-300"></i></summary>
                    <div class="px-8 pb-6 text-sm text-brand-muted leading-relaxed tracking-wider border-t hairline pt-6">{a}</div>
                </details>""" for q,a in c["faq"])

    # 60 分鐘排程（若該課程有課綱資料）
    curriculum_section = ""
    if slug in CURRICULUM:
        ctitle, rows = CURRICULUM[slug]
        trows = "".join(f"""
                <div class="grid grid-cols-[92px_1fr] md:grid-cols-[120px_160px_1fr] gap-x-4 gap-y-1 py-5 border-b hairline items-baseline fade-up">
                    <div class="text-brand-red font-mono font-bold text-sm">{time}</div>
                    <div class="text-brand-text font-bold tracking-widest col-start-2 md:col-start-2">{seg}</div>
                    <div class="text-sm text-brand-muted leading-relaxed tracking-wider col-span-2 md:col-span-1 md:col-start-3">{desc}</div>
                </div>""" for time, seg, desc in rows)
        curriculum_section = f"""
    <!-- 課綱排程 -->
    <section class="py-24 px-6 md:px-12 bg-brand-bg dot-grid border-y hairline">
        <div class="max-w-4xl mx-auto">
            <div class="flex items-center gap-2 mb-4 fade-up"><span class="sys-dot"></span><span class="sys-label text-brand-red">CLASS BREAKDOWN</span></div>
            <h2 class="text-3xl md:text-4xl font-black tracking-widest text-brand-text mb-2 fade-up">一堂課，這樣跑</h2>
            <p class="text-brand-muted text-sm tracking-wider mb-10 fade-up">{ctitle}　·　教練照表上課，你清楚知道每段在練什麼</p>
            <div class="border hairline bg-brand-panel/40 px-6 md:px-10 py-2">{trows}</div>
        </div>
    </section>"""


    body = f"""
    <!-- HERO -->
    <section class="relative w-full h-[85dvh] flex flex-col justify-center items-center overflow-hidden border-b hairline">
        <div class="absolute inset-0 z-0">
            <video autoplay muted loop playsinline class="w-full h-full object-cover theme-img filter grayscale brightness-[0.3]" poster="{c['img']}" onerror="this.style.display='none'"><source src="{c['video']}" type="video/mp4"></video>
            <img src="{c['img']}" class="absolute inset-0 w-full h-full object-cover theme-img filter grayscale brightness-[0.3] -z-10" alt="{c['zh']}" loading="eager">
            <div class="absolute inset-0 bg-gradient-to-t from-brand-bg via-brand-bg/40 to-brand-bg/70"></div>
        </div>
        <div class="relative z-10 text-center px-6 fade-up visible">
            <div class="flex items-center justify-center gap-4 mb-6"><div class="w-10 h-[1px] bg-brand-red"></div><p class="text-xs md:text-sm tracking-[0.4em] text-brand-red uppercase font-bold">{c['en']}</p><div class="w-10 h-[1px] bg-brand-red"></div></div>
            <h1 class="text-6xl sm:text-8xl md:text-9xl font-black tracking-widest text-white drop-shadow-xl mb-4">{c['zh']}</h1>
            <p class="text-brand-muted text-sm md:text-base tracking-[0.3em] mb-2">{c['tag']}</p>
            <p class="text-white/80 text-base md:text-lg tracking-wider font-light">{c['hero_sub']}</p>
            <button onclick="openBooking('{c['book']}')" class="mt-10 bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-white hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">預約 $400 體驗</button>
        </div>
        <p class="absolute bottom-8 text-[10px] font-mono text-white/50 tracking-[0.3em] animate-pulse">SCROLL ↓</p>
    </section>

    <!-- LEAD -->
    <section class="py-28 px-6 md:px-12 max-w-4xl mx-auto text-center">
        <p class="text-xl md:text-2xl text-brand-text font-light leading-loose tracking-wider fade-up">{c['lead']}</p>
    </section>

    <!-- WHY -->
    <section class="py-24 px-6 md:px-12 bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="max-w-7xl mx-auto">
            <div class="mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">WHY {c['en'].split()[0].upper()}</span><h2 class="text-4xl md:text-5xl font-black tracking-widest text-brand-text">為什麼練{c['zh']}</h2></div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">{why}</div>
        </div>
    </section>

    <!-- LEARN -->
    <section class="py-24 px-6 md:px-12 max-w-5xl mx-auto">
        <div class="grid md:grid-cols-2 gap-12 items-center">
            <div class="fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">CURRICULUM</span><h2 class="text-4xl md:text-5xl font-black tracking-widest text-brand-text mb-4">你會學到</h2><p class="text-brand-muted text-sm tracking-wider leading-loose">從零到能實戰，我們把每一步都拆解清楚，讓你的進步看得見。</p></div>
            <ul class="space-y-5">{learn}</ul>
        </div>
    </section>
{curriculum_section}

    <!-- FOR WHO -->
    <section class="py-24 px-6 md:px-12 bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">WHO IS IT FOR</span><h2 class="text-4xl md:text-5xl font-black tracking-widest text-brand-text">這堂課適合你嗎？</h2></div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">{forwho}</div>
        </div>
    </section>

    <!-- FAQ -->
    <section class="py-24 px-6 md:px-12 max-w-4xl mx-auto">
        <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">FAQ</span><h2 class="text-4xl md:text-5xl font-black tracking-widest text-brand-text">關於{c['zh']}，你想問的</h2></div>
        <div class="space-y-4 fade-up">{faq}</div>
    </section>

    <!-- CTA -->
    <section class="py-32 px-6 text-center bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="max-w-3xl mx-auto fade-up">
            <h2 class="text-3xl md:text-5xl font-light tracking-[0.15em] text-brand-text mb-6">準備好了嗎？<span class="text-brand-red font-serif italic block mt-3">第一拳，從 $400 開始。</span></h2>
            <p class="text-brand-muted text-sm tracking-wider leading-loose mb-10">運動服來就好，裝備全免費，教練全程帶你。今天，就給自己一個開始的理由。</p>
            <button onclick="openBooking('{c['book']}')" class="bg-brand-red text-white px-12 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">立即預約體驗</button>
        </div>
    </section>
"""
    title = f"HCF {c['zh']}課程 | {c['en']} | 新竹格鬥館"
    desc = c['lead'][:70]
    return head(title, desc, slug+".html") + nav(c["active"]) + body + FOOTER + WIDGETS + SHARED_JS

if __name__ == "__main__":
    for slug, c in COURSES.items():
        open(f"{slug}.html","w",encoding="utf-8").write(render_course(slug,c))
        print("generated", slug+".html")
