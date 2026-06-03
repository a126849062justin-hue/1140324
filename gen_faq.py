# -*- coding: utf-8 -*-
from _components import head, nav, FOOTER
from _widgets import WIDGETS, SHARED_JS

# 新手問答：分類 Q&A（取自課綱與常見疑問）
FAQ = [
 ("開始之前", "fa-flag-checkered", [
   ("完全沒運動基礎，可以來嗎？","可以，這正是我們最擅長的。新客一律從 LV.1 入門班開始，動作慢拆、循序漸進，不對打、不比較。我們 80% 的學員都是零基礎起步。"),
   ("第一次上課要帶什麼？","穿舒適的運動服與運動鞋、帶水壺和毛巾就好。拳套、手綁帶等裝備館內全部免費提供，空手來也沒問題。"),
   ("女生適合嗎？會不會練得很壯？","非常適合，館內超過四成是女性學員。格鬥訓練主要是雕塑線條、提升心肺與建立防身意識，會讓你更緊實有力，而不是變壯。"),
   ("年齡有限制嗎？","6 歲到 60 歲都有學員在練。教練會依每個人的狀況調整強度，重點是循序漸進，而不是逞強。"),
 ]),
 ("怎麼上課", "fa-dumbbell", [
   ("一堂課大概怎麼進行？","LV.1 入門班 60 分鐘：集體暖身 12 分 → 體能心肺 8 分 → 技術指導 18 分 → 分組打靶 22 分。一堂課把該練的都練到，流汗但不操爆。"),
   ("我會不會一上場就要跟人對打？","不會。初學者只打沙袋與教練手靶，全程在教練監督下進行。對打是進階（LV.2）的選項，且必須雙方同意、全程戴護具才會模擬實戰。"),
   ("LV.1 和 LV.2 差在哪？","LV.1 是入門班，所有人都能上；LV.2 是進階實戰班，著重距離、時機與護具下的條件對練。建議 LV.1 上滿 20 堂、教練認可後再挑戰 LV.2。"),
   ("Fighter Squad 選手班是什麼？","週末 14:00–16:00 的兩小時完整訓練，採教練邀請制，給勤練、有基礎的進階與備賽學員。它是一種榮譽肯定，也是往上爬的目標。"),
 ]),
 ("課程怎麼選", "fa-list-check", [
   ("我想減脂，該上哪一堂？","「泰拳燃脂（Cardio）」最適合——心肺與打靶比重加重、技術門檻放低，一堂約 600–800 大卡。搭配飲食，效果最明顯。"),
   ("我想學實用防身？","泰拳與散打都很適合。泰拳是八肢全距離的全面打擊；散打多了摔法與貼身控制。兩者都從 LV.1 入門即可。"),
   ("泰拳和踢拳怎麼選？","泰拳含拳肘膝腿與纏鬥、全距離；踢拳節奏更快、偏中遠距、不纏抱，線條導向。喜歡快節奏、想雕塑腿臀線條，選踢拳；想要最全面，選泰拳。"),
   ("只想練體能、增肌呢？","上「肌力體能（S&C）」。練的是功能性力量、爆發與基礎代謝，打造易瘦體質，也是所有格鬥技的地基。"),
 ]),
 ("費用與預約", "fa-ticket", [
   ("費用怎麼算？","首次體驗 $400（含裝備、教練全程帶）。之後有單堂、10／30 堂方案，以及包月無限 $5,500。完整價格見課程方案頁。"),
   ("怎麼預約？要先預約嗎？","全預約制。可透過官網預約鈕、官方 LINE 或電話預約。最晚取消時間為上課前 2 小時。"),
   ("課程會不會開不成？","全部課程滿 3 人（含以上）即可開課；若前一日 22:00 確認未達標，會以系統簡訊通知停課，不會讓你白跑。"),
   ("有沒有推薦或回饋獎勵？","有。舊生帶新生、體驗當天購課，可享 10% 回饋金，新生再獲 $500；教練或學員引薦，當天購課體驗免收費。"),
 ]),
]

def block(title, icon, qas):
    items="".join(f"""
            <details class="group border hairline bg-brand-bg hover:border-brand-red/50 transition-colors">
                <summary class="flex justify-between items-center px-6 md:px-8 py-5 cursor-pointer list-none outline-none interactive-el"><span class="text-brand-text font-bold tracking-wider pr-4">{q}</span><i class="fa-solid fa-plus text-brand-red text-sm group-open:rotate-45 transition-transform duration-300 shrink-0"></i></summary>
                <div class="px-6 md:px-8 pb-6 text-sm text-brand-muted leading-loose tracking-wider border-t hairline pt-5">{a}</div>
            </details>""" for q,a in qas)
    return f"""
        <div class="mb-12 fade-up">
            <div class="flex items-center gap-3 mb-6"><div class="w-10 h-10 border border-brand-red/40 text-brand-red flex items-center justify-center"><i class="fa-solid {icon}"></i></div><h2 class="text-2xl font-black tracking-widest text-brand-text">{title}</h2></div>
            <div class="space-y-3">{items}</div>
        </div>"""

blocks="".join(block(t,i,q) for t,i,q in FAQ)

body=f"""
    <section class="pt-32 pb-12 px-6 md:px-12 dot-grid">
        <div class="max-w-4xl mx-auto text-center">
            <div class="flex items-center justify-center gap-2 mb-5 fade-up visible"><span class="sys-dot"></span><span class="sys-label text-brand-red">ROOKIE BRIEFING</span></div>
            <h1 class="text-5xl md:text-7xl font-black tracking-widest text-brand-text mb-5 fade-up visible">新手問答</h1>
            <p class="text-brand-muted text-sm md:text-base tracking-wider leading-loose fade-up visible">第一次踏進格鬥館，難免緊張。<br>把你會想問的都整理好了——看完，你就知道該怎麼開始。</p>
        </div>
    </section>

    <section class="pb-20 px-6 md:px-12 max-w-4xl mx-auto">{blocks}</section>

    <section class="py-24 px-6 text-center bg-brand-panel border-y hairline dot-grid">
        <div class="max-w-3xl mx-auto fade-up">
            <h2 class="text-3xl md:text-5xl font-light tracking-[0.15em] text-brand-text mb-6">還有問題？<span class="text-brand-red font-serif italic block mt-3">直接問，最快。</span></h2>
            <p class="text-brand-muted text-sm tracking-wider leading-loose mb-10">點右下角的智能教練即時發問，或用官方 LINE 找真人客服。當然，最好的答案是——直接來體驗一堂。</p>
            <div class="flex flex-wrap justify-center gap-4">
                <button onclick="openBooking('mt-trial')" class="bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">預約 $400 體驗</button>
                <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="border hairline text-brand-muted px-10 py-4 text-xs tracking-[0.2em] font-bold hover:border-brand-red hover:text-brand-red transition-colors duration-300 interactive-el"><i class="fa-brands fa-line mr-2"></i>LINE 諮詢</a>
            </div>
        </div>
    </section>
"""

open("faq.html","w",encoding="utf-8").write(
    head("HCF 新手問答 | 第一次來該知道的事 | 新竹格鬥館","HCF 新竹格鬥館新手問答：零基礎能不能練、第一次帶什麼、課程怎麼選、費用與預約規範，一次解答。","faq.html")
    + nav("faq") + body + FOOTER + WIDGETS + SHARED_JS)
print("generated faq.html")
