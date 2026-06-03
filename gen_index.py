# -*- coding: utf-8 -*-
from _components import head, nav, FOOTER
from _widgets import WIDGETS, SHARED_JS

COURSE_CARDS = [
    ("muaythai.html","泰拳","Muay Thai","course_muaythai.jpg","八肢的藝術，最全面的站立格鬥。"),
    ("kickboxing.html","踢拳","Kickboxing","course_kickboxing.jpg","速度與節奏的博弈，越打越上癮。"),
    ("sanda.html","散打","Sanda","course_sanda.jpg","踢打摔三合一，最接近實戰。"),
    ("strength.html","肌力體能","S&C","course_sc.jpg","不練死肌肉，練真正能用的力量。"),
]

def hcard(href,zh,en,img,desc):
    return f"""
                <a href="{href}" class="w-[420px] h-full relative group interactive-el shrink-0 border hairline overflow-hidden block">
                    <img src="{img}" class="w-full h-full object-cover filter grayscale group-hover:grayscale-0 transition-all duration-700" onerror="this.src='coach_huang_03_padwork.jpg'">
                    <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent opacity-90"></div>
                    <div class="absolute bottom-8 left-8 right-8">
                        <span class="text-brand-red text-[10px] font-mono tracking-[0.2em] border border-brand-red px-2 py-1 mb-3 inline-block">{en}</span>
                        <h3 class="text-4xl font-black tracking-widest text-white mb-2">{zh}</h3>
                        <p class="text-sm text-gray-300 leading-relaxed mb-3">{desc}</p>
                        <span class="text-[11px] tracking-widest text-white/70 group-hover:text-brand-red transition-colors">了解更多 →</span>
                    </div>
                </a>"""

def mcard(href,zh,en,img,desc):
    return f"""
            <a href="{href}" class="snap-slide w-[80vw] h-[55vh] relative shrink-0 border hairline overflow-hidden block">
                <img src="{img}" class="w-full h-full object-cover filter grayscale brightness-75" onerror="this.src='coach_huang_03_padwork.jpg'">
                <div class="absolute inset-0 bg-gradient-to-t from-[#050505] via-[#050505]/40 to-transparent"></div>
                <div class="absolute bottom-6 left-6 right-6"><span class="text-brand-red text-[10px] border border-brand-red px-2 py-1 mb-2 inline-block font-mono tracking-widest">{en}</span><h3 class="text-3xl font-black text-white mb-1 tracking-widest">{zh}</h3><p class="text-[11px] text-gray-300">{desc}</p></div>
            </a>"""

body = f"""
    <!-- HERO (zoom) -->
    <section id="hero-zoom-section" class="relative w-full h-[200vh]">
        <div class="sticky top-0 w-full h-[100dvh] overflow-hidden flex flex-col justify-center items-center bg-brand-bg">
            <div class="absolute inset-0 z-0 flex items-center justify-center">
                <img id="zoom-image" src="hero-main.jpg" alt="HCF" class="w-full h-full object-cover theme-img filter grayscale-[80%] brightness-[0.35] transform scale-100 will-change-transform">
                <div class="absolute inset-0 bg-gradient-to-t from-brand-bg via-transparent to-brand-bg/50"></div>
            </div>
            <div id="hero-text" class="relative z-10 text-center px-6 fade-up visible">
                <div class="flex items-center justify-center gap-4 mb-6"><div class="w-10 h-[1px] bg-brand-red"></div><p class="text-xs md:text-sm tracking-[0.4em] text-brand-red uppercase font-bold">Awaken Your Fighting DNA</p><div class="w-10 h-[1px] bg-brand-red"></div></div>
                <h1 class="text-5xl sm:text-7xl md:text-9xl font-serif font-light tracking-wide mb-6 leading-none text-white drop-shadow-xl">ENTER THE <span class="italic text-gray-400">CAGE</span></h1>
                <p class="text-white/80 text-sm md:text-base tracking-[0.2em]">新竹頂級格鬥基地 ・ 從零開始，重新打造自己</p>
                <p class="text-xs font-mono text-white/60 tracking-[0.3em] mt-10 animate-pulse">SCROLL TO DIVE IN ↓</p>
            </div>
        </div>
    </section>

    <!-- 戰績橫幅 -->
    <section id="champion" class="relative w-full bg-brand-bg border-y hairline overflow-hidden transition-colors duration-500">
        <div class="absolute inset-0 z-0"><img src="coach_huang_05_ring.jpg" class="w-full h-full object-cover theme-img filter grayscale brightness-[0.25]" alt="總教練" loading="lazy" onerror="this.style.display='none'"><div class="absolute inset-0 bg-gradient-to-r from-brand-bg via-brand-bg/85 to-transparent"></div></div>
        <div class="relative z-10 max-w-7xl mx-auto px-6 md:px-12 py-28 md:py-36 grid md:grid-cols-2 gap-12 items-center">
            <div class="fade-up">
                <span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">MPF07 · 2026.03.21 · KAOHSIUNG</span>
                <h2 class="text-5xl md:text-7xl font-black tracking-widest text-brand-text leading-none mb-2">復出首戰</h2>
                <h2 class="text-6xl md:text-8xl font-serif italic text-brand-red leading-none mb-8">全勝.</h2>
                <p class="text-brand-text text-lg md:text-xl tracking-wider leading-relaxed mb-4">總教練 <strong class="text-brand-red">黃謙和</strong>，斷骨重鑄、復出首戰，擊敗來台五年未嘗敗北的泰國名將。</p>
                <p class="text-brand-muted text-sm tracking-widest leading-loose">全場九場職業賽——唯一勝出的台灣選手。<br>這不是空話，是 42 場勝利累積出的真理。</p>
                <div class="mt-10 flex flex-wrap gap-4"><button onclick="openBooking('mt-trial')" class="bg-brand-red text-white px-8 py-3.5 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_20px_rgb(var(--color-red)/0.3)] interactive-el magnetic-btn">跟冠軍教練學・$400</button><a href="coaches.html" class="border hairline text-brand-muted px-8 py-3.5 text-xs tracking-[0.2em] font-bold hover:border-brand-red hover:text-brand-red transition-colors duration-300 interactive-el">認識教練團隊</a></div>
            </div>
            <div class="grid grid-cols-3 gap-px bg-brand-border/10 fade-up">
                <div class="bg-brand-bg p-6 md:p-8 text-center"><div class="text-4xl md:text-5xl font-black text-brand-red font-serif">42</div><div class="text-[10px] tracking-[0.2em] text-brand-muted mt-2">職業勝仗</div></div>
                <div class="bg-brand-bg p-6 md:p-8 text-center"><div class="text-4xl md:text-5xl font-black text-brand-text font-serif">越南</div><div class="text-[10px] tracking-[0.2em] text-brand-muted mt-2">MAX FC 站冠軍</div></div>
                <div class="bg-brand-bg p-6 md:p-8 text-center"><div class="text-4xl md:text-5xl font-black text-brand-text font-serif">C級</div><div class="text-[10px] tracking-[0.2em] text-brand-muted mt-2">國家教練認證</div></div>
            </div>
        </div>
    </section>

    <!-- 信任數據 -->
    <section class="bg-brand-panel border-b hairline py-16 transition-colors duration-500">
        <div class="max-w-6xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-10 text-center">
            <div class="fade-up"><div class="text-4xl md:text-5xl font-black text-brand-red font-serif mb-2">200<span class="text-2xl align-top">+</span></div><div class="text-[10px] md:text-xs tracking-[0.2em] text-brand-muted">共同成長的戰士</div></div>
            <div class="fade-up"><div class="text-4xl md:text-5xl font-black text-brand-text font-serif mb-2">6→60</div><div class="text-[10px] md:text-xs tracking-[0.2em] text-brand-muted">歲都能從零開始</div></div>
            <div class="fade-up"><div class="text-4xl md:text-5xl font-black text-brand-red font-serif mb-2">5.0<span class="text-2xl">★</span></div><div class="text-[10px] md:text-xs tracking-[0.2em] text-brand-muted">Google 滿分評價</div></div>
            <div class="fade-up"><div class="text-4xl md:text-5xl font-black text-brand-text font-serif mb-2">2022</div><div class="text-[10px] md:text-xs tracking-[0.2em] text-brand-muted">深耕新竹 SINCE</div></div>
        </div>
    </section>

    <!-- 痛點 -->
    <section id="painpoints" class="py-28 px-6 md:px-12 bg-brand-bg transition-colors duration-500">
        <div class="max-w-5xl mx-auto">
            <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">WHY HCF</span><h2 class="text-3xl md:text-5xl font-light tracking-[0.15em] text-brand-text leading-snug">你是不是，<br><span class="text-brand-red font-serif italic">也厭倦了這樣的自己？</span></h2></div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-px bg-brand-border/10 fade-up">
                <div class="bg-brand-bg p-8 hover:bg-brand-panel transition-colors"><div class="text-2xl mb-3">😤</div><h3 class="text-brand-text font-bold tracking-widest mb-2">減肥減了一百次，每次都失敗</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider">一堂課燃燒 800 大卡，邊學防身邊燃脂。比起對著鏡子數卡路里，這裡讓你愛上流汗。</p></div>
                <div class="bg-brand-bg p-8 hover:bg-brand-panel transition-colors"><div class="text-2xl mb-3">😰</div><h3 class="text-brand-text font-bold tracking-widest mb-2">工作壓力大到快爆炸</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider">加班、開會、被客戶刁難。你需要一個合法把壓力打出去的地方——出拳那一刻，全部歸零。</p></div>
                <div class="bg-brand-bg p-8 hover:bg-brand-panel transition-colors"><div class="text-2xl mb-3">💪</div><h3 class="text-brand-text font-bold tracking-widest mb-2">練了很久健身，但只是好看</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider">肌肉再大不會用也只是擺設。你的身體值得被真正派上用場，這才是真正的全身訓練。</p></div>
                <div class="bg-brand-bg p-8 hover:bg-brand-panel transition-colors"><div class="text-2xl mb-3">🛡️</div><h3 class="text-brand-text font-bold tracking-widest mb-2">想學防身，但怕被打、怕受傷</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider">80% 學員零基礎、無壓力環境，教練全程帶你。帶得走的，是真正的自信與底氣。</p></div>
            </div>
            <div class="text-center mt-16 fade-up"><p class="text-brand-muted text-sm tracking-widest leading-loose mb-2">真正的勇者，不是從未倒下，</p><p class="text-brand-text text-lg tracking-widest leading-loose mb-10">而是每次倒下後，都能<span class="text-brand-red font-bold">重新站起。</span></p><button onclick="openBooking('mt-trial')" class="inline-block bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">給自己一次機會・$400 開始</button></div>
        </div>
    </section>

    <!-- 課程 (橫向) -->
    <section id="horizontal-courses" class="hidden md:block relative w-full h-[400vh] bg-brand-panel transition-colors duration-500">
        <div class="sticky top-0 w-full h-[100dvh] flex flex-col justify-center overflow-hidden border-y hairline">
            <div class="absolute top-24 left-12 z-20 mix-blend-difference"><h2 class="text-5xl font-serif text-white tracking-widest">Programs.</h2><p class="text-brand-red text-sm tracking-[0.3em] mt-2 font-bold">四大專業課程 / 左右滑動探索</p></div>
            <div id="scroll-container" class="flex items-center gap-12 px-[10vw] h-[60vh] mt-10 w-[max-content] will-change-transform">
                {''.join(hcard(*c) for c in COURSE_CARDS)}
                <div class="w-[300px] h-full flex flex-col items-center justify-center shrink-0 interactive-el"><button onclick="openBooking('mt-trial')" class="w-32 h-32 rounded-full border border-brand-red text-brand-red flex flex-col items-center justify-center hover:bg-brand-red hover:text-white transition-all duration-300 magnetic-btn"><span class="text-xs tracking-widest font-bold mb-1">預約</span><i class="fa-solid fa-arrow-right"></i></button></div>
            </div>
        </div>
    </section>
    <section class="md:hidden py-20 bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="px-6 mb-10"><h2 class="text-4xl font-serif text-brand-text tracking-widest">Programs.</h2><p class="text-brand-red text-xs tracking-[0.2em] mt-2 font-bold">向左滑動探索四大課程</p></div>
        <div class="snap-container flex gap-6 px-6 pb-8 w-full after:content-[''] after:w-1 after:shrink-0">{''.join(mcard(*c) for c in COURSE_CARDS)}</div>
    </section>

    <!-- 課程方案 -->
    <section id="pricing" class="py-24 px-6 md:px-12 max-w-7xl mx-auto">
        <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">TRAINING PLANS</span><h2 class="text-4xl md:text-6xl font-black tracking-widest text-brand-text">選擇你的戰線</h2><p class="text-brand-muted mt-4 tracking-wider text-sm">燃脂塑形、防身實戰、競技精進——總有一條路是為你準備的。</p></div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="border border-brand-red/30 bg-brand-panel p-8 relative hover:border-brand-red transition-all duration-300 fade-up interactive-el flex flex-col"><div class="absolute top-0 left-0 right-0 h-[2px] bg-brand-red"></div><span class="text-brand-red text-[10px] font-mono tracking-[0.3em] border border-brand-red px-3 py-1 inline-block mb-4 self-start">TEAM BATTLE</span><h3 class="text-2xl font-black tracking-widest text-brand-text mb-3">團體戰線</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider flex-grow mb-8">和一群戰友一起流汗。60 分鐘完整訓練，從暖身到實戰，$400 就能開始。</p><a href="group-class.html" class="block w-full text-center bg-brand-red text-white py-3 tracking-widest text-xs font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 interactive-el">了解團體課程</a></div>
            <div class="border hairline bg-brand-panel p-8 relative hover:border-brand-red/50 transition-all duration-300 fade-up interactive-el flex flex-col"><span class="text-brand-muted text-[10px] font-mono tracking-[0.3em] border border-brand-muted/30 px-3 py-1 inline-block mb-4 self-start">ELITE FOCUS</span><h3 class="text-2xl font-black tracking-widest text-brand-text mb-3">菁英私人武裝</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider flex-grow mb-8">一對一專屬特訓，教練 100% 為你而戰，進步速度快三倍。</p><a href="private-class.html" class="block w-full text-center border hairline text-brand-muted py-3 tracking-widest text-xs font-bold hover:border-brand-red hover:text-brand-red transition-colors duration-300 interactive-el">了解私人課程</a></div>
            <div class="border hairline bg-brand-panel p-8 relative hover:border-brand-red/50 transition-all duration-300 fade-up interactive-el flex flex-col"><span class="text-brand-muted text-[10px] font-mono tracking-[0.3em] border border-brand-muted/30 px-3 py-1 inline-block mb-4 self-start">FULL PRICING</span><h3 class="text-2xl font-black tracking-widest text-brand-text mb-3">完整價目表</h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider flex-grow mb-8">團體、私人、雙人、打靶課，所有方案與價格一次看懂，透明無負擔。</p><a href="pricing.html" class="block w-full text-center bg-brand-red text-white py-3 tracking-widest text-xs font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 interactive-el">查看所有方案</a></div>
        </div>
    </section>

    <!-- 真實評價 -->
    <section id="reviews" class="py-24 bg-brand-panel border-y hairline transition-colors duration-500">
        <div class="max-w-7xl mx-auto px-6 md:px-12">
            <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">REAL REVIEWS</span><h2 class="text-4xl md:text-6xl font-black tracking-widest text-brand-text">鐵證如山</h2><p class="text-brand-muted mt-4 tracking-wider text-sm">不是我們說自己好。是每一個來過的人，都給了五顆星。</p></div>
            <div class="snap-container flex gap-6 pb-6 md:grid md:grid-cols-4 md:gap-6 after:content-[''] after:w-1 after:shrink-0 md:after:hidden">
                <div class="snap-slide w-[70vw] md:w-auto shrink-0 border hairline bg-brand-bg overflow-hidden hover:border-brand-red/50 transition-colors interactive-el"><img src="review_IMG_4189.jpg" class="w-full h-auto object-cover" alt="Google 評價" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                <div class="snap-slide w-[70vw] md:w-auto shrink-0 border hairline bg-brand-bg overflow-hidden hover:border-brand-red/50 transition-colors interactive-el"><img src="review_IMG_4198.jpg" class="w-full h-auto object-cover" alt="Google 評價" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                <div class="snap-slide w-[70vw] md:w-auto shrink-0 border hairline bg-brand-bg overflow-hidden hover:border-brand-red/50 transition-colors interactive-el"><img src="review_IMG_4199.jpg" class="w-full h-auto object-cover" alt="Google 評價" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                <div class="snap-slide w-[70vw] md:w-auto shrink-0 border hairline bg-brand-bg overflow-hidden hover:border-brand-red/50 transition-colors interactive-el"><img src="review_IMG_4194.jpg" class="w-full h-auto object-cover" alt="Google 評價" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
            </div>
            <div class="text-center mt-12 fade-up"><a href="https://maps.app.goo.gl/Mee8hr4Xcr53UWy37" target="_blank" rel="noopener" class="text-[11px] font-mono tracking-[0.2em] text-brand-red hover:underline interactive-el">查看全部 Google 評論 →</a></div>
        </div>
    </section>

    <!-- FAQ -->
    <section id="faq" class="py-24 px-6 md:px-12 max-w-4xl mx-auto">
        <div class="text-center mb-16 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">FAQ</span><h2 class="text-4xl md:text-6xl font-black tracking-widest text-brand-text">你想知道的</h2><p class="text-brand-muted mt-4 tracking-wider text-sm">我們都幫你問了。</p></div>
        <div class="space-y-4 fade-up">
            {''.join(f'''<details class="group border hairline bg-brand-bg hover:border-brand-red/50 transition-colors"><summary class="flex justify-between items-center px-8 py-6 cursor-pointer list-none outline-none interactive-el"><span class="text-brand-text font-bold tracking-widest">{q}</span><i class="fa-solid fa-plus text-brand-red text-sm group-open:rotate-45 transition-transform duration-300"></i></summary><div class="px-8 pb-6 text-sm text-brand-muted leading-relaxed tracking-wider border-t hairline pt-6">{a}</div></details>''' for q,a in [
              ("第一次上課要準備什麼？","穿著舒適的運動服與運動鞋就好。手綁帶、拳套等裝備館內全部免費提供，空手來都沒問題。"),
              ("完全沒有運動基礎，可以來嗎？","當然。我們 80% 的學員都是從零開始，教練最擅長帶新手。你唯一要帶的，是願意挑戰自己的心態。"),
              ("格鬥適合女生嗎？","非常適合。格鬥是高效的全身燃脂運動，還能建立防身意識與自信。HCF 超過 40% 的學員是女性。"),
              ("上課真的要對打、被打嗎？","日常訓練以打靶、打沙包為主，不會一來就對打。自由對練是進階選項，全程配戴護具並由教練監督。"),
              ("費用怎麼算？","體驗課 $400 起，另有團體、私人、無限等多種方案。完整價格請見課程方案頁，或用 LINE 直接詢問。"),
            ])}
        </div>
    </section>
"""

title = "HCF 新竹格鬥館 | 泰拳・踢拳・散打・肌力體能・覺醒你的戰鬥 DNA"
desc = "新竹頂級格鬥基地。冠軍教練親自帶你，從零開始學泰拳、踢拳、散打與肌力體能。$400 體驗，運動服來就好，裝備全免費。"
html = head(title, desc, "index.html") + nav("home") + body + FOOTER + WIDGETS + SHARED_JS

# index needs the zoom-hero + horizontal-scroll JS; inject before closing </body> of SHARED_JS
extra = """
    <script>
        const zs=document.getElementById('hero-zoom-section'),zi=document.getElementById('zoom-image'),ht=document.getElementById('hero-text');
        addEventListener('scroll',()=>{if(!zs||!zi)return;const r=zs.getBoundingClientRect();if(r.top<=0&&r.bottom>=0){let p=Math.abs(r.top)/(r.height-innerHeight);zi.style.transform=`scale(${1+p*3}) translateZ(0)`;ht.style.opacity=1-p*2;}},{passive:true});
        const hs=document.getElementById('horizontal-courses'),sc=document.getElementById('scroll-container');
        if(innerWidth>=768){addEventListener('scroll',()=>{if(!hs||!sc)return;const r=hs.getBoundingClientRect();if(r.top<=0&&r.bottom>=innerHeight){let p=Math.abs(r.top)/(r.height-innerHeight);let mx=sc.scrollWidth-innerWidth+200;sc.style.transform=`translate3d(-${p*mx}px,0,0)`;}},{passive:true});}
    </script>
"""
html = html.replace("</body>\n</html>", extra + "</body>\n</html>")
open("index.html","w",encoding="utf-8").write(html)
print("generated index.html", len(html), "bytes")
