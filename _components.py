# -*- coding: utf-8 -*-
"""Shared building blocks for the HCF site. Every page is assembled from these
so navigation, theming, footer and the AI/booking/analytics widgets stay identical."""

# ---- Theme + base CSS (themeable accent via --color-red) ----
BASE_STYLE = """
    <style>
        :root {
            --color-bg: 5 5 5;
            --color-panel: 15 15 15;
            --color-text: 245 245 247;
            --color-border: 255 255 255;
            --color-muted: 156 163 175;
            --color-red: 230 57 70;        /* accent — controlled by admin */
            --color-red-dark: 166 28 46;
            --img-brightness: 0.35;
        }
        html.light-mode {
            --color-bg: 245 245 247;
            --color-panel: 255 255 255;
            --color-text: 20 20 20;
            --color-border: 0 0 0;
            --color-muted: 107 114 128;
            --img-brightness: 0.7;
        }
        body { background-color: rgb(var(--color-bg)); color: rgb(var(--color-text)); overflow-x: hidden; transition: background-color .5s ease, color .5s ease; }
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: rgb(var(--color-bg)); }
        ::-webkit-scrollbar-thumb { background: rgb(var(--color-muted) / .5); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: rgb(var(--color-red)); }
        .hairline { border-color: rgb(var(--color-border) / .1); transition: border-color .5s ease; }
        .glass-panel { background: rgb(var(--color-panel) / .85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-right: 1px solid rgb(var(--color-border) / .05); transition: background-color .5s ease, border-color .5s ease; }
        .theme-img { transition: filter .5s ease, transform 1.5s cubic-bezier(.16,1,.3,1); }
        html.light-mode .theme-img { filter: grayscale(50%) brightness(.8); }
        @media (min-width:1024px) and (hover:hover) and (pointer:fine) {
            body,a,button,.cursor-pointer { cursor:none !important; }
            .custom-cursor-dot { position:fixed; top:0; left:0; width:6px; height:6px; background:rgb(var(--color-red)); border-radius:50%; z-index:10000; pointer-events:none; transition:width .2s,height .2s; will-change:transform; }
            .custom-cursor-ring { position:fixed; top:0; left:0; width:36px; height:36px; border:1px solid rgb(var(--color-red) / .5); border-radius:50%; z-index:9999; pointer-events:none; transition:width .2s,height .2s,border-color .2s,background-color .2s; will-change:transform; }
            body.hovering .custom-cursor-dot { width:0; height:0; }
            body.hovering .custom-cursor-ring { width:50px; height:50px; border-color:rgb(var(--color-red)); background:rgb(var(--color-red) / .1); backdrop-filter:blur(2px); }
        }
        .dropdown-menu { visibility:hidden; opacity:0; transform:translateY(10px); transition:all .3s ease; }
        .group:hover .dropdown-menu { visibility:visible; opacity:1; transform:translateY(0); }
        .snap-container { scroll-snap-type:x mandatory; overflow-x:auto; -webkit-overflow-scrolling:touch; scrollbar-width:none; }
        .snap-container::-webkit-scrollbar { display:none; }
        .snap-slide { scroll-snap-align:center; }
        .fade-up { opacity:0; transform:translateY(30px); transition:all 1s cubic-bezier(.16,1,.3,1); }
        .fade-up.visible { opacity:1; transform:translateY(0); }
        /* ===== 戰術系統視覺 (對應 2026 課表海報) ===== */
        :root { --mt:230 57 70; --sanda:234 179 8; --kb:148 163 184; --sc:34 197 94; }
        .dot-grid { background-image: radial-gradient(rgb(var(--color-border) / .07) 1px, transparent 1px); background-size: 22px 22px; }
        .dot-grid-dense { background-image: radial-gradient(rgb(var(--color-border) / .08) 1px, transparent 1px); background-size: 16px 16px; }
        .sys-label { font-family:'Noto Sans TC',monospace; letter-spacing:.3em; font-size:10px; font-weight:700; }
        .sys-dot { display:inline-block; width:7px; height:7px; border-radius:50%; background:rgb(var(--color-red)); box-shadow:0 0 8px rgb(var(--color-red)); animation:syspulse 2s infinite; }
        @keyframes syspulse { 0%,100%{opacity:1} 50%{opacity:.3} }
        .lv-badge { font-family:monospace; font-size:10px; font-weight:800; letter-spacing:.1em; padding:2px 8px; border-radius:2px; }
        .lv1 { background:rgb(var(--sc)); color:#04210f; }
        .lv2 { background:rgb(var(--color-red)); color:#fff; }
        .cat-mt{--cat:var(--mt)} .cat-sanda{--cat:var(--sanda)} .cat-kb{--cat:var(--kb)} .cat-sc{--cat:var(--sc)}
        .class-card { position:relative; border:1px solid rgb(var(--color-border)/.08); background:rgb(var(--color-panel)/.6); transition:all .3s ease; overflow:hidden; }
        .class-card::before { content:''; position:absolute; top:0; left:0; right:0; height:3px; background:rgb(var(--cat,var(--color-red))); }
        .class-card:hover { border-color:rgb(var(--cat,var(--color-red))/.6); transform:translateY(-2px); box-shadow:0 8px 24px rgb(0 0 0 / .3); }
        .class-card.dimmed { opacity:.2; filter:grayscale(1); }
        @media (max-width:767px){ .glass-panel,[class*="backdrop-blur"]{ backdrop-filter:blur(8px)!important; -webkit-backdrop-filter:blur(8px)!important; } }
        @supports not (backdrop-filter: blur(1px)){ .glass-panel{ background:rgb(var(--color-panel))!important; } }
        @media (prefers-reduced-motion: reduce){ *,*::before,*::after{ animation-duration:.01ms!important; animation-iteration-count:1!important; transition-duration:.01ms!important; scroll-behavior:auto!important; } .custom-cursor-dot,.custom-cursor-ring{ display:none!important; } }
    </style>
"""

# ---- Theme loader: applies saved accent colour + theme before paint ----
THEME_LOADER = """
    <script>
      (function(){
        try {
          if (localStorage.getItem('theme') === 'light') document.documentElement.classList.add('light-mode');
          var c = localStorage.getItem('hcf_accent');           // "230 57 70"
          var d = localStorage.getItem('hcf_accent_dark');
          if (c) document.documentElement.style.setProperty('--color-red', c);
          if (d) document.documentElement.style.setProperty('--color-red-dark', d);
        } catch(e){}
      })();
    </script>
"""

def head(title, desc, og_path="index.html"):
    return f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:image" content="hcf_logo_main.png">
    <meta property="og:site_name" content="HCF 新竹格鬥館">
    <meta property="og:locale" content="zh_TW">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#E63946">
    <link rel="icon" type="image/png" href="hcf_logo_main.png">
    <link rel="apple-touch-icon" href="hcf_logo_main.png">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="HCF">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="tw-build.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap" rel="stylesheet">
{THEME_LOADER}{BASE_STYLE}
</head>
<body class="antialiased selection:bg-brand-red selection:text-white">
    <div class="custom-cursor-dot hidden md:block" id="cursor-dot"></div>
    <div class="custom-cursor-ring hidden md:block" id="cursor-ring"></div>
"""

# nav: active = one of home/courses/coaches/schedule/pricing
def nav(active=""):
    def cls(key):
        return "text-brand-red" if active == key else "text-brand-muted hover:text-brand-red"
    return f"""
    <nav class="fixed w-full z-[80] transition-all duration-500 backdrop-blur-md bg-brand-bg/80 border-b hairline py-4 px-6 md:px-10 flex justify-between items-center" id="navbar">
        <a href="index.html" class="flex items-center gap-3 hover:opacity-80 transition-opacity interactive-el group" aria-label="HCF 首頁">
            <img src="hcf_logo_main.png" alt="HCF Logo" class="h-8 md:h-10 w-auto object-contain filter drop-shadow-md group-hover:scale-105 transition-transform" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
            <div class="hidden flex-col items-start justify-center"><span class="text-2xl md:text-3xl font-black tracking-[0.2em] uppercase leading-none text-brand-text flex items-baseline">HCF<span class="text-brand-red text-4xl leading-[0.5]">.</span></span></div>
            <div class="flex flex-col items-start justify-center border-l border-brand-text/20 pl-3">
                <span class="text-sm md:text-base font-black tracking-widest text-brand-text leading-tight">HCF</span>
                <span class="text-[10px] md:text-xs font-bold tracking-[0.1em] text-brand-muted leading-tight">新竹格鬥館</span>
            </div>
        </a>
        <div class="hidden lg:flex items-center gap-7 text-xs tracking-[0.2em] font-medium">
            <a href="index.html" class="{cls('home')} transition-colors interactive-el">首頁</a>
            <div class="relative group py-4">
                <a href="#" class="{cls('courses')} transition-colors flex items-center gap-1 interactive-el">課程介紹 <i class="fa-solid fa-angle-down text-[10px]"></i></a>
                <div class="dropdown-menu absolute top-full left-1/2 -translate-x-1/2 w-52 bg-brand-panel/95 backdrop-blur-xl border hairline shadow-2xl py-3 flex flex-col gap-1 z-50 rounded-sm">
                    <a href="muaythai.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">泰拳 Muay Thai</a>
                    <a href="kickboxing.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">踢拳 Kickboxing</a>
                    <a href="sanda.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">散打 Sanda</a>
                    <a href="strength.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">肌力體能 S&amp;C</a>
                    <div class="border-t hairline my-1"></div>
                    <a href="group-class.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">團體課程</a>
                    <a href="private-class.html" class="px-6 py-2 hover:text-brand-red hover:bg-brand-border/5 transition-colors interactive-el text-brand-text">私人課程</a>
                </div>
            </div>
            <a href="coaches.html" class="{cls('coaches')} transition-colors interactive-el">教練團隊</a>
            <a href="schedule.html" class="{cls('schedule')} transition-colors interactive-el">最新課表</a>
            <a href="pricing.html" class="{cls('pricing')} transition-colors interactive-el">課程方案</a>
            <a href="faq.html" class="{cls('faq')} transition-colors interactive-el">新手問答</a>
        </div>
        <div class="flex items-center gap-4">
            <button onclick="toggleTheme()" class="text-brand-muted hover:text-brand-red transition-colors interactive-el w-11 h-11 flex items-center justify-center text-lg" aria-label="切換明暗主題"><i class="fa-solid fa-circle-half-stroke theme-icon"></i></button>
            <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="hidden md:flex items-center gap-2 text-xs tracking-[0.1em] text-brand-muted hover:text-brand-text transition-colors interactive-el"><i class="fa-brands fa-line text-lg"></i> 專屬顧問</a>
            <button onclick="openBooking()" class="hidden md:block text-xs tracking-[0.2em] bg-brand-red text-white px-6 py-2.5 font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_15px_rgb(var(--color-red)/0.3)] interactive-el magnetic-btn">預約體驗</button>
            <button onclick="toggleNavDrawer()" class="lg:hidden text-brand-text text-xl interactive-el w-11 h-11 flex items-center justify-center" aria-label="選單"><i class="fa-solid fa-bars-staggered"></i></button>
        </div>
    </nav>

    <div id="drawer-backdrop" class="fixed inset-0 bg-black/60 backdrop-blur-sm z-[90] opacity-0 pointer-events-none transition-opacity duration-500" onclick="closeAllDrawers()"></div>
    <aside id="nav-drawer" class="fixed top-0 right-0 w-[85%] md:w-[350px] h-[100dvh] glass-panel border-l border-r-0 hairline z-[100] transform translate-x-full transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] flex flex-col p-8 pt-20 overflow-y-auto lg:hidden text-brand-text">
        <button onclick="closeAllDrawers()" class="absolute top-6 right-6 text-brand-muted hover:text-brand-red text-xl interactive-el"><i class="fa-solid fa-xmark"></i></button>
        <nav class="flex flex-col gap-1 text-sm tracking-widest">
            <a href="index.html" class="py-3 border-b hairline hover:text-brand-red transition-colors interactive-el">首頁</a>
            <span class="pt-4 pb-1 text-[10px] text-brand-muted tracking-[0.3em]">課程介紹</span>
            <a href="muaythai.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">泰拳</a>
            <a href="kickboxing.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">踢拳</a>
            <a href="sanda.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">散打</a>
            <a href="strength.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">肌力體能</a>
            <a href="group-class.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">團體課程</a>
            <a href="private-class.html" class="py-2.5 pl-3 border-l hairline hover:text-brand-red transition-colors interactive-el">私人課程</a>
            <a href="coaches.html" class="py-3 mt-2 border-b border-t hairline hover:text-brand-red transition-colors interactive-el">教練團隊</a>
            <a href="schedule.html" class="py-3 border-b hairline hover:text-brand-red transition-colors interactive-el">最新課表</a>
            <a href="pricing.html" class="py-3 border-b hairline hover:text-brand-red transition-colors interactive-el">課程方案</a>
            <a href="faq.html" class="py-3 border-b hairline hover:text-brand-red transition-colors interactive-el">新手問答</a>
        </nav>
        <button onclick="closeAllDrawers();openBooking()" class="mt-8 block w-full text-center bg-brand-red text-white py-4 tracking-widest text-sm interactive-el shadow-[0_5px_15px_rgb(var(--color-red)/0.3)]">預約 $400 體驗</button>
        <div class="flex gap-3 mt-6 justify-center">
            <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="w-10 h-10 border hairline flex items-center justify-center hover:text-[#06C755] hover:border-[#06C755] transition-colors interactive-el"><i class="fa-brands fa-line"></i></a>
            <a href="https://www.instagram.com/hc.combat2022/" target="_blank" rel="noopener" class="w-10 h-10 border hairline flex items-center justify-center hover:text-[#E1306C] hover:border-[#E1306C] transition-colors interactive-el"><i class="fa-brands fa-instagram"></i></a>
            <a href="https://m.facebook.com/hsinchucombat/" target="_blank" rel="noopener" class="w-10 h-10 border hairline flex items-center justify-center hover:text-[#1877F2] hover:border-[#1877F2] transition-colors interactive-el"><i class="fa-brands fa-facebook-f"></i></a>
        </div>
    </aside>
"""

FOOTER = """
    <footer class="bg-brand-bg pt-24 pb-24 md:pb-12 border-t hairline relative z-10 transition-colors duration-500">
        <div class="max-w-7xl mx-auto px-6 md:px-12">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 mb-16">
                <div class="lg:col-span-5 fade-up">
                    <div class="flex items-end gap-4 mb-6 opacity-90">
                        <img src="hcf_logo_main.png" alt="HCF Logo" class="h-14 w-auto object-contain" loading="lazy" onerror="this.style.display='none'">
                        <h2 class="text-xl font-black tracking-widest text-brand-text pb-1">HCF 新竹格鬥館</h2>
                    </div>
                    <div class="space-y-4 text-sm text-brand-muted leading-loose tracking-wider text-justify">
                        <p>我們相信格鬥不是暴力，而是一種<strong class="text-brand-text">面對自己的方式</strong>。人生像一場拳賽，會被擊倒，但真正重要的是——你能不能再站起來。</p>
                        <p>在 HCF，你練的不只是拳，是把自己重新打造一遍的勇氣。</p>
                    </div>
                </div>
                <div class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-10 lg:pl-10 fade-up">
                    <div class="md:col-span-2 space-y-8">
                        <div>
                            <h4 class="text-brand-text font-bold tracking-widest mb-4 border-l-2 border-brand-red pl-2">營業時間</h4>
                            <ul class="text-sm text-brand-muted space-y-2 font-mono">
                                <li>週一～週五 <span class="text-brand-text ml-2">11:00 - 22:00</span></li>
                                <li>週六＆週日 <span class="text-brand-text ml-2">11:00 - 16:00</span></li>
                            </ul>
                        </div>
                        <div>
                            <h4 class="text-brand-text font-bold tracking-widest mb-4 border-l-2 border-brand-red pl-2">基地座標</h4>
                            <ul class="text-sm text-brand-muted space-y-3">
                                <li class="flex items-start gap-3"><i class="fa-solid fa-location-dot mt-1 text-brand-red w-4"></i><a href="https://maps.app.goo.gl/Mee8hr4Xcr53UWy37" target="_blank" rel="noopener" class="hover:text-brand-text transition-colors interactive-el border-b border-transparent hover:border-brand-text pb-0.5">新竹市北區林森路301號2樓</a></li>
                                <li class="flex items-center gap-3"><i class="fa-solid fa-phone text-brand-red w-4"></i><span class="font-mono">0925-571-225</span></li>
                                <li class="flex items-center gap-3"><i class="fa-solid fa-envelope text-brand-red w-4"></i><span class="font-mono text-xs">hsinchucombat2022@gmail.com</span></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-brand-text font-bold tracking-widest mb-4 border-l-2 border-brand-red pl-2">快速連結</h4>
                        <ul class="text-sm text-brand-muted space-y-3">
                            <li><a href="muaythai.html" class="hover:text-brand-red transition-colors interactive-el">泰拳</a></li>
                            <li><a href="kickboxing.html" class="hover:text-brand-red transition-colors interactive-el">踢拳</a></li>
                            <li><a href="sanda.html" class="hover:text-brand-red transition-colors interactive-el">散打</a></li>
                            <li><a href="strength.html" class="hover:text-brand-red transition-colors interactive-el">肌力體能</a></li>
                            <li><a href="coaches.html" class="hover:text-brand-red transition-colors interactive-el">教練團隊</a></li>
                            <li><a href="schedule.html" class="hover:text-brand-red transition-colors interactive-el">最新課表</a></li>
                            <li><a href="pricing.html" class="hover:text-brand-red transition-colors interactive-el">課程方案</a></li>
                            <li><a href="faq.html" class="hover:text-brand-red transition-colors interactive-el">新手問答</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="flex flex-col md:flex-row justify-between items-center pt-8 border-t hairline gap-6">
                <div class="flex flex-wrap justify-center gap-3">
                    <button onclick="openBooking()" class="w-10 h-10 bg-brand-red text-white flex items-center justify-center hover:bg-brand-text hover:text-brand-bg transition-colors interactive-el shadow-lg" title="預約體驗"><i class="fa-solid fa-bolt"></i></button>
                    <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="w-10 h-10 border hairline text-brand-muted flex items-center justify-center hover:border-[#06C755] hover:text-[#06C755] transition-colors interactive-el magnetic-btn" title="官方 LINE"><i class="fa-brands fa-line text-lg"></i></a>
                    <a href="https://www.instagram.com/hc.combat2022/" target="_blank" rel="noopener" class="w-10 h-10 border hairline text-brand-muted flex items-center justify-center hover:border-[#E1306C] hover:text-[#E1306C] transition-colors interactive-el magnetic-btn" title="Instagram"><i class="fa-brands fa-instagram text-lg"></i></a>
                    <a href="https://m.facebook.com/hsinchucombat/" target="_blank" rel="noopener" class="w-10 h-10 border hairline text-brand-muted flex items-center justify-center hover:border-[#1877F2] hover:text-[#1877F2] transition-colors interactive-el magnetic-btn" title="Facebook"><i class="fa-brands fa-facebook-f text-lg"></i></a>
                    <a href="https://youtube.com/playlist?list=PLFtibVDr-YTBsPUoEfClpei2ttq1mGtKN" target="_blank" rel="noopener" class="w-10 h-10 border hairline text-brand-muted flex items-center justify-center hover:border-[#FF0000] hover:text-[#FF0000] transition-colors interactive-el magnetic-btn" title="YouTube"><i class="fa-brands fa-youtube text-lg"></i></a>
                </div>
                <div class="text-[10px] text-brand-muted font-mono tracking-widest text-center md:text-right"><p>© 2026 HCF COMBAT SYSTEM. ALL RIGHTS RESERVED.</p></div>
            </div>
        </div>
    </footer>

    <div class="fixed bottom-0 left-0 right-0 z-[60] md:hidden bg-brand-bg/95 backdrop-blur-md border-t hairline p-3 flex gap-3">
        <button onclick="openBooking()" class="flex-1 text-center bg-brand-red text-white py-3 text-xs font-bold tracking-widest">預約體驗</button>
        <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="flex-1 text-center border hairline text-brand-muted py-3 text-xs font-bold tracking-widest"><i class="fa-brands fa-line mr-1"></i>LINE 諮詢</a>
    </div>
"""

if __name__ == "__main__":
    print("components module OK")
