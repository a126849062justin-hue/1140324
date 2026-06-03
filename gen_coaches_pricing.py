# -*- coding: utf-8 -*-
from _components import head, nav, FOOTER
from _widgets import WIDGETS, SHARED_JS

# ---------------- COACHES ----------------
COACHES = [
 {"name":"黃謙和","title":"總教練 / HEAD COACH","alias":"格鬥鋼鐵人","img":"coach_huang_01_portrait.jpg","disc":"HUANG90",
  "quote":"我的教學沒有空話，只有 42 場勝利累積出的真理。",
  "tags":["泰拳 Muay Thai","散打 Sanda"],
  "honors":["職業戰績 42 勝","MAX FC 越南站冠軍","WOTD 雙料優勝","國家 C 級教練認證"]},
 {"name":"Allen","title":"踢拳教練 / KICKBOXING","alias":"竹科戰神","img":"coach_allen_01_portrait.jpg","disc":"ALLEN90",
  "quote":"把複雜的動作拆到最簡單，你就學得會。",
  "tags":["踢拳 Kickboxing"],
  "honors":["動作精密拆解專家","戰術邏輯思維建立","零基礎高速建立肌肉記憶"]},
 {"name":"鄭豫","title":"散打教練 / SANDA","alias":"重型坦克","img":"coach_cheng_01_portrait.jpg","disc":"CHENG90",
  "quote":"距離對了，體型就不是問題。",
  "tags":["散打 Sanda","摔技"],
  "honors":["80kg+ 量級絕對霸主","遠踢近打貼身摔","世界南少林詠春大賽 85kg 冠軍","T1 踢拳之王"]},
 {"name":"高大可","title":"泰拳教練 / MUAY THAI","alias":"逆襲狂人","img":"coach_kao_01_portrait.jpg","disc":"KAO90",
  "quote":"秩序，源於能保護自己與在乎的人的實力。",
  "tags":["泰拳 Muay Thai"],
  "honors":["一年內狂減 30KG（104→74）","立青泰拳精英挑戰賽優勝","新手蛻變最佳見證"]},
 {"name":"胡脩誠","title":"助教 / 鐵血戰神","alias":"臨火無懼","img":"coach_hu_01_portrait.jpg","disc":"HU90",
  "quote":"想學會怎麼破壞，先學會怎麼保護。",
  "tags":["踢拳 Kickboxing","實戰"],
  "honors":["75 公斤級絕對統治力","WOTD-09 鐵籠搏擊優勝","Rise Nova 冠軍","T1 積分賽常勝軍"]},
 {"name":"小米","title":"助教 / 女子格鬥","alias":"柔中帶剛","img":"coach_mimi_01_portrait.jpg","disc":"MIMI90",
  "quote":"力量不分性別，技巧才是真正的武器。",
  "tags":["女子防身","體能"],
  "honors":["女子格鬥專項教練","新手與女性學員的最佳引路人","防身實戰課程設計"]},
]

def coach_card(c, big=False):
    tags = "".join(f'<span class="text-[10px] font-mono tracking-widest border border-brand-red/40 text-brand-red px-2 py-1">{t}</span>' for t in c["tags"])
    honors = "".join(f'<li class="flex items-start gap-2 text-sm text-brand-muted tracking-wider"><i class="fa-solid fa-trophy text-brand-red text-[10px] mt-1.5"></i><span>{h}</span></li>' for h in c["honors"])
    span = "lg:col-span-2" if big else ""
    h_img = "h-[460px]" if big else "h-[360px]"
    return f"""
        <div class="group border hairline bg-brand-panel overflow-hidden fade-up hover:border-brand-red/50 transition-colors {span}">
            <div class="grid {'md:grid-cols-2' if big else 'grid-cols-1'}">
                <div class="relative {h_img} overflow-hidden">
                    <img src="{c['img']}" class="w-full h-full object-cover object-top filter grayscale group-hover:grayscale-0 transition-all duration-700" alt="{c['name']}" loading="lazy" onerror="this.style.opacity=0.2">
                    <div class="absolute inset-0 bg-gradient-to-t from-brand-panel via-transparent to-transparent"></div>
                    <span class="absolute top-4 left-4 text-[10px] font-mono tracking-[0.2em] text-brand-red border border-brand-red px-2 py-1 bg-brand-bg/60">「{c['alias']}」</span>
                </div>
                <div class="p-8 flex flex-col justify-center">
                    <p class="text-[10px] font-mono tracking-[0.3em] text-brand-red mb-2">{c['title']}</p>
                    <h3 class="text-3xl font-black tracking-widest text-brand-text mb-3">{c['name']}</h3>
                    <p class="text-brand-muted text-sm italic leading-relaxed tracking-wider border-l-2 border-brand-red pl-4 mb-5">{c['quote']}</p>
                    <div class="flex flex-wrap gap-2 mb-5">{tags}</div>
                    <ul class="space-y-2 mb-6">{honors}</ul>
                    <div class="flex items-center justify-between border-t hairline pt-4">
                        <div class="text-xs tracking-widest"><span class="text-brand-muted">專屬折扣碼 </span><span class="text-brand-red font-mono font-bold">{c['disc']}</span><span class="text-brand-muted"> · 9折</span></div>
                        <button onclick="openBooking('private-1')" class="text-[11px] tracking-widest text-brand-red hover:underline interactive-el">預約他的課 →</button>
                    </div>
                </div>
            </div>
        </div>"""

cards = coach_card(COACHES[0], big=True) + "".join(coach_card(c) for c in COACHES[1:])

coaches_body = f"""
    <section class="relative w-full h-[70dvh] flex flex-col justify-center items-center overflow-hidden border-b hairline">
        <div class="absolute inset-0 z-0"><img src="coach_huang_04_strike.jpg" class="w-full h-full object-cover theme-img filter grayscale brightness-[0.25]" alt="教練團隊" loading="eager" onerror="this.style.display='none'"><div class="absolute inset-0 bg-gradient-to-t from-brand-bg via-brand-bg/50 to-brand-bg/70"></div></div>
        <div class="relative z-10 text-center px-6 fade-up visible">
            <div class="flex items-center justify-center gap-4 mb-6"><div class="w-10 h-[1px] bg-brand-red"></div><p class="text-xs md:text-sm tracking-[0.4em] text-brand-red uppercase font-bold">Select Your Commander</p><div class="w-10 h-[1px] bg-brand-red"></div></div>
            <h1 class="text-5xl md:text-8xl font-black tracking-widest text-white drop-shadow-xl mb-6">教練團隊</h1>
            <p class="text-white/80 text-base md:text-lg tracking-wider font-light max-w-2xl mx-auto leading-relaxed">把身體交給連擂台都沒上過的人，是對自己的不負責。<br>在這裡，每一位教練都是從鮮血與勝利中走出來的現役戰士。</p>
        </div>
        <p class="absolute bottom-8 text-[10px] font-mono text-white/50 tracking-[0.3em] animate-pulse">SCROLL ↓</p>
    </section>

    <section class="py-24 px-6 md:px-12 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">{cards}</div>
    </section>

    <section class="py-20 px-6 md:px-12 bg-brand-panel border-y hairline">
        <div class="max-w-4xl mx-auto text-center fade-up">
            <i class="fa-solid fa-ticket text-brand-red text-3xl mb-6"></i>
            <h2 class="text-2xl md:text-3xl font-black tracking-widest text-brand-text mb-4">教練專屬折扣碼</h2>
            <p class="text-brand-muted text-sm tracking-wider leading-loose mb-8">每位教練都有自己的專屬折扣碼。購課時於 FitBook 輸入，即可享 <strong class="text-brand-red">9 折</strong> 優惠。喜歡哪位教練的風格，就用他的代碼支持他。</p>
            <button onclick="openBooking('mt-trial')" class="bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">預約體驗・指定教練</button>
        </div>
    </section>
"""

open("coaches.html","w",encoding="utf-8").write(
    head("HCF 教練團隊 | 冠軍級現役戰士陣容 | 新竹格鬥館","HCF 教練團隊由現役職業選手與冠軍教練組成，泰拳、踢拳、散打、女子防身專項，從零開始帶你變強。","coaches.html")
    + nav("coaches") + coaches_body + FOOTER + WIDGETS + SHARED_JS)
print("generated coaches.html")

# ---------------- PRICING ----------------
pricing_body = """
    <section class="relative w-full h-[55dvh] md:h-[60dvh] flex flex-col justify-center items-center overflow-hidden border-b hairline">
        <div class="absolute inset-0 z-0"><img src="course_kickboxing.jpg" class="w-full h-full object-cover theme-img filter grayscale brightness-[0.3]" alt="課程方案" loading="eager" onerror="this.style.display='none'"><div class="absolute inset-0 bg-gradient-to-t from-brand-bg via-brand-bg/60 to-brand-bg/80"></div></div>
        <div class="relative z-10 text-center px-6 fade-up visible">
            <div class="flex items-center justify-center gap-4 mb-6"><div class="w-10 h-[1px] bg-brand-red"></div><p class="text-xs md:text-sm tracking-[0.4em] text-brand-red uppercase font-bold">Training Plans</p><div class="w-10 h-[1px] bg-brand-red"></div></div>
            <h1 class="text-5xl md:text-8xl font-serif font-light tracking-wide text-white drop-shadow-xl mb-4">課程<span class="italic text-brand-red">方案</span></h1>
            <p class="text-brand-muted text-sm tracking-[0.2em]">投資自己，是報酬率最高的選擇。</p>
        </div>
    </section>

    <section class="py-20 px-6 md:px-12 max-w-5xl mx-auto">
        <div class="border border-brand-red bg-brand-red/5 p-10 md:p-14 text-center fade-up relative overflow-hidden"><div class="absolute top-0 left-0 right-0 h-[3px] bg-brand-red"></div>
            <span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">NEWBIE TRIAL / 新手首選</span>
            <h2 class="text-3xl md:text-5xl font-black tracking-widest text-brand-text mb-4">首次體驗只要 <span class="text-brand-red font-serif">$400</span></h2>
            <p class="text-brand-muted text-sm tracking-wider leading-loose max-w-2xl mx-auto mb-8">零基礎也能上 ・ 運動服來就好 ・ 拳套等裝備全免費 ・ 教練全程帶你。80% 的學員都是從零開始，在無壓力的環境感受格鬥的魅力。</p>
            <button onclick="openBooking('mt-trial')" class="bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">立即預約 $400 體驗</button>
        </div>
    </section>

    <section class="py-12 px-6 md:px-12 max-w-7xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="border hairline bg-brand-panel p-8 md:p-10 fade-up">
                <div class="flex items-center justify-between mb-8 pb-5 border-b hairline"><h3 class="text-2xl font-black tracking-widest text-brand-text"><i class="fa-solid fa-users text-brand-red mr-3"></i>團體課程</h3><span class="text-brand-red text-[10px] font-mono tracking-widest border border-brand-red px-3 py-1.5">GROUP</span></div>
                <ul class="space-y-4 text-sm">
                    <li class="flex justify-between items-baseline"><span class="text-brand-text font-bold">體驗價 · 單堂</span><span class="font-mono text-brand-red font-bold text-xl">$400</span></li>
                    <li class="flex justify-between items-baseline border-t hairline pt-4"><span class="text-brand-muted">單堂</span><span class="font-mono text-brand-text text-lg">$600</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-muted">10 堂 <span class="text-[11px] text-brand-muted/70">/ 60 天</span></span><span class="font-mono text-brand-text text-lg">$4,500</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-muted">30 堂 <span class="text-[11px] text-brand-muted/70">/ 150 天</span></span><span class="font-mono text-brand-text text-lg">$10,500</span></li>
                    <li class="flex justify-between items-baseline border-t hairline pt-4"><span class="text-brand-text font-bold">無限方案 <span class="text-[11px] text-brand-muted/70 block mt-1 font-normal">當月團課無限次數</span></span><span class="font-mono text-brand-red font-bold text-lg">$5,500<span class="text-[11px] text-brand-muted">/月</span></span></li>
                </ul>
                <div class="mt-8 flex gap-3"><button onclick="openBooking('mt-trial')" class="flex-1 text-center bg-brand-red text-white py-3.5 tracking-widest text-xs font-bold hover:bg-brand-text hover:text-brand-bg transition-colors interactive-el">預約體驗</button><a href="group-class.html" class="flex-1 text-center border hairline text-brand-muted py-3.5 tracking-widest text-xs font-bold hover:border-brand-red hover:text-brand-red transition-colors interactive-el">課程內容</a></div>
            </div>
            <div class="border hairline bg-brand-panel p-8 md:p-10 fade-up">
                <div class="flex items-center justify-between mb-8 pb-5 border-b hairline"><h3 class="text-2xl font-black tracking-widest text-brand-text"><i class="fa-solid fa-user-shield text-brand-red mr-3"></i>私人課程</h3><span class="text-brand-red text-[10px] font-mono tracking-widest border border-brand-red px-3 py-1.5">1-ON-1</span></div>
                <ul class="space-y-4 text-sm">
                    <li class="flex justify-between items-baseline"><span class="text-brand-text font-bold">體驗價 · 1 堂</span><span class="font-mono text-brand-red font-bold text-xl">$1,400</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-text font-bold">體驗價 · 2 堂</span><span class="font-mono text-brand-red font-bold text-lg">$2,400</span></li>
                    <li class="flex justify-between items-baseline border-t hairline pt-4"><span class="text-brand-muted">單堂</span><span class="font-mono text-brand-text text-lg">$2,200</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-muted">10 堂 <span class="text-[11px] text-brand-muted/70">/ 90 天</span></span><span class="font-mono text-brand-text text-lg">$18,000</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-muted">20 堂 <span class="text-[11px] text-brand-muted/70">/ 120 天</span></span><span class="font-mono text-brand-text text-lg">$34,000</span></li>
                    <li class="flex justify-between items-baseline"><span class="text-brand-muted">30 堂 <span class="text-[11px] text-brand-muted/70">/ 180 天</span></span><span class="font-mono text-brand-text text-lg">$48,000</span></li>
                </ul>
                <div class="mt-8 flex gap-3"><button onclick="openBooking('private-1')" class="flex-1 text-center bg-brand-red text-white py-3.5 tracking-widest text-xs font-bold hover:bg-brand-text hover:text-brand-bg transition-colors interactive-el">預約體驗</button><a href="private-class.html" class="flex-1 text-center border hairline text-brand-muted py-3.5 tracking-widest text-xs font-bold hover:border-brand-red hover:text-brand-red transition-colors interactive-el">課程內容</a></div>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
            <div class="border hairline bg-brand-bg p-8 fade-up"><h3 class="text-lg font-black tracking-widest text-brand-text mb-5 border-l-2 border-brand-red pl-3">1 對 2 雙人包班</h3><ul class="space-y-3 text-sm"><li class="flex justify-between"><span class="text-brand-muted">體驗價 (1堂)</span><span class="font-mono text-brand-text">$2,400</span></li><li class="flex justify-between"><span class="text-brand-muted">10 堂 / 90 天</span><span class="font-mono text-brand-text">$23,000</span></li><li class="flex justify-between"><span class="text-brand-muted">20 堂 / 150 天</span><span class="font-mono text-brand-text">$44,000</span></li></ul></div>
            <div class="border hairline bg-brand-bg p-8 fade-up"><h3 class="text-lg font-black tracking-widest text-brand-text mb-5 border-l-2 border-brand-red pl-3">私人打靶課 <span class="text-[11px] text-brand-muted font-normal">/ 40 MINS</span></h3><ul class="space-y-3 text-sm"><li class="flex justify-between"><span class="text-brand-muted">單堂</span><span class="font-mono text-brand-text">$1,000</span></li><li class="flex justify-between"><span class="text-brand-muted">10 堂 / 60 天</span><span class="font-mono text-brand-text">$9,000</span></li></ul></div>
        </div>
        <div class="mt-8 border border-brand-red/30 bg-brand-red/5 p-6 flex flex-col md:flex-row items-center gap-4 fade-up"><i class="fa-solid fa-ticket text-brand-red text-2xl"></i><p class="text-sm text-brand-text tracking-wider text-center md:text-left flex-1">每位教練都有 <strong class="text-brand-red">專屬折扣碼</strong>，於 FitBook 購課時輸入即享 <strong>9 折</strong>。</p><a href="coaches.html" class="shrink-0 border border-brand-red text-brand-red px-6 py-2.5 text-xs tracking-widest font-bold hover:bg-brand-red hover:text-white transition-colors interactive-el">取得折扣碼 →</a></div>
        <p class="text-center text-xs text-brand-muted tracking-widest mt-6 fade-up">付款方式：街口支付 ・ 現金 ・ 轉帳</p>
    </section>

    <section class="py-28 px-6 text-center bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="max-w-3xl mx-auto fade-up"><h2 class="text-3xl md:text-5xl font-light tracking-[0.15em] text-brand-text mb-6">還在猶豫？<span class="text-brand-red font-serif italic block mt-3">先來流一場汗再說。</span></h2><p class="text-brand-muted text-sm tracking-wider leading-loose mb-10">每個強者，都是從踏進門的那一刻開始的。$400，給自己一次機會。</p><button onclick="openBooking('mt-trial')" class="bg-brand-red text-white px-12 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">立即預約體驗</button></div>
    </section>
"""
open("pricing.html","w",encoding="utf-8").write(
    head("HCF 課程方案 | 價格・團體・私人課程 | 新竹格鬥館","HCF 新竹格鬥館完整課程方案與價格：團體課 $400 體驗、私人 1對1、雙人包班、打靶課，透明價目一次看懂。","pricing.html")
    + nav("pricing") + pricing_body + FOOTER + WIDGETS + SHARED_JS)
print("generated pricing.html")
