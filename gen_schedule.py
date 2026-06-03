# -*- coding: utf-8 -*-
from _components import head, nav, FOOTER
from _widgets import WIDGETS, SHARED_JS

# Real 2026 schedule data (from official poster + curriculum handbook).
SCHEDULE_JS = """
    const CATS = {
      mt:    {label:'泰拳',  en:'MUAY THAI',    rgb:'var(--mt)'},
      sanda: {label:'散打',  en:'SANDA',        rgb:'var(--sanda)'},
      kb:    {label:'踢拳',  en:'KICKBOXING',   rgb:'var(--kb)'},
      sc:    {label:'肌力體能',en:'S&C / CARDIO',rgb:'var(--sc)'},
    };
    const WEEKDAYS=['MON','TUE','WED','THU','FRI'], WEEKDAY_ZH=['週一','週二','週三','週四','週五'];
    const WEEKEND=['SAT','SUN'], WEEKEND_ZH=['週六','週日'];
    const WD_TIMES=[{s:'11:00',e:'12:00'},{s:'15:00',e:'15:50'},{s:'19:30',e:'20:30'},{s:'20:40',e:'21:30'}];
    const WE_TIMES=[{s:'11:00',e:'12:00'},{s:'12:10',e:'13:00'}];
    const C=(cat,lv,zh,en,note,book)=>({cat,lv,zh,en,note,book});
    const WEEKDAY=[
      [ null, null, C('sc',1,'肌力體能','S&C','壺鈴啞鈴循環，打造易瘦體質與功能性力量','sc-trial'),
              C('sanda',1,'散打摔法','TAKEDOWNS','抱摔、過肩摔與防摔，貼身重心爭奪','sd-trial'),
              C('sc',1,'肌力體能','S&C','深蹲硬舉推拉＋爆發，格鬥技術的地基','sc-trial') ],
      [ null, null, C('mt',1,'泰拳燃脂','CARDIO','高密度打靶循環，一堂約 600–800 大卡','mt-trial'), null, null ],
      [ C('mt',1,'新手泰拳','MUAY THAI','站架步法×直拳掃踢，零基礎友善、不對打','mt-trial'),
        C('kb',1,'踢拳腿連擊','KICKBOXING','拳腿連擊組合，快節奏雕塑下半身線條','kb-trial'),
        C('mt',1,'新手泰拳','MUAY THAI','站架步法×直拳掃踢，零基礎友善、不對打','mt-trial'),
        C('mt',1,'新手泰拳','MUAY THAI','站架步法×直拳掃踢，零基礎友善、不對打','mt-trial'),
        C('mt',1,'新手泰拳','MUAY THAI','站架步法×直拳掃踢，零基礎友善、不對打','mt-trial') ],
      [ C('mt',2,'泰拳腿肘膝實戰','SPARRING','護具下條件對練，距離・時機・攻防轉換','mt-trial'),
        C('kb',2,'踢拳遠距阻擊','RANGE DRILL','前手控距、阻擊反擊的時機與反射','kb-trial'),
        C('mt',2,'泰拳實戰技術','TECH SPAR','組合技假動作×自由對練複盤','mt-trial'),
        C('mt',1,'泰拳燃脂','CARDIO','高密度打靶循環，下班來紓壓兼燃脂','mt-trial'),
        C('mt',2,'泰拳腿肘膝實戰','SPARRING','護具下條件對練，距離・時機・攻防轉換','mt-trial') ],
    ];
    const WEEKENDM=[
      [ C('mt',1,'新手泰拳','MUAY THAI','站架步法×直拳掃踢，零基礎友善、不對打','mt-trial'),
        C('sanda',1,'散打遠踢近摔','SANDA','遠踢控距、近身入摔的距離轉換','sd-trial') ],
      [ null, C('sanda',1,'散打拳腿運用','STRIKING','拳腿組合與時機，散打打擊核心','sd-trial') ],
    ];
"""

SCHEDULE_RENDER = """
    <script>
      let fCat='all';
      function cell(c){
        if(!c) return '<div class="min-h-[92px] flex items-center justify-center text-brand-muted/30 font-mono text-sm border border-dashed border-brand-border/10">—</div>';
        const cat=CATS[c.cat], dim=(fCat!=='all'&&fCat!==c.cat)?' dimmed':'', lvCls=c.lv===1?'lv1':'lv2';
        return `<button onclick="openBooking('${c.book}')" class="class-card cat-${c.cat}${dim} w-full text-left p-3 md:p-4 group interactive-el">
          <div class="flex items-center justify-between mb-2"><span class="lv-badge ${lvCls}">LV.${c.lv}</span><span class="w-2.5 h-2.5 rounded-sm" style="background:rgb(${cat.rgb})"></span></div>
          <div class="text-sm md:text-base font-black tracking-wider text-brand-text leading-tight">${c.zh}</div>
          <div class="text-[9px] md:text-[10px] font-mono tracking-[0.15em] text-brand-muted mt-1">${c.en}</div>
          <div class="text-[10px] text-brand-muted/80 leading-snug mt-2 tracking-wide group-hover:text-brand-muted transition-colors">${c.note}</div>
        </button>`;
      }
      function timeCol(t){return `<div class="flex flex-col justify-center"><div class="text-brand-red font-black text-lg md:text-xl font-mono leading-none">${t.s}</div><div class="text-brand-muted/60 text-[10px] md:text-xs font-mono mt-1">${t.e}</div></div>`;}
      function buildGrid(){
        let wd='<div class="hidden md:block"><div class="grid grid-cols-[80px_repeat(5,1fr)] gap-2 mb-3 px-1"><div class="sys-label text-brand-red flex items-end pb-1">TIME</div>';
        WEEKDAYS.forEach((d,i)=>{wd+=`<div class="text-center"><div class="font-black tracking-widest text-brand-text">${d}</div><div class="text-[10px] text-brand-muted tracking-widest">${WEEKDAY_ZH[i]}</div></div>`;});
        wd+='</div>';
        WD_TIMES.forEach((t,ti)=>{wd+='<div class="grid grid-cols-[80px_repeat(5,1fr)] gap-2 mb-2">'+timeCol(t);WEEKDAY[ti].forEach(c=>wd+=cell(c));wd+='</div>';});
        wd+='</div>';
        let we='<div class="hidden md:block mt-10"><div class="flex items-center gap-3 mb-5"><span class="sys-dot"></span><h3 class="sys-label text-brand-text">WEEKEND OPS // 週末特訓</h3></div><div class="grid grid-cols-[80px_repeat(2,1fr)] gap-2 mb-3 px-1 max-w-2xl"><div class="sys-label text-brand-red flex items-end pb-1">TIME</div>';
        WEEKEND.forEach((d,i)=>{we+=`<div class="text-center"><div class="font-black tracking-widest text-brand-text">${d}</div><div class="text-[10px] text-brand-muted tracking-widest">${WEEKEND_ZH[i]}</div></div>`;});
        we+='</div>';
        WE_TIMES.forEach((t,ti)=>{we+='<div class="grid grid-cols-[80px_repeat(2,1fr)] gap-2 mb-2 max-w-2xl">'+timeCol(t);WEEKENDM[ti].forEach(c=>we+=cell(c));we+='</div>';});
        we+='</div>';
        let mb='<div class="md:hidden space-y-7">';
        const days=[...WEEKDAY_ZH.map((z,i)=>({z,en:WEEKDAYS[i],times:WD_TIMES,col:i,src:WEEKDAY})),...WEEKEND_ZH.map((z,i)=>({z,en:WEEKEND[i],times:WE_TIMES,col:i,src:WEEKENDM}))];
        days.forEach(d=>{const items=[];d.times.forEach((t,ti)=>{const c=d.src[ti][d.col];if(c&&(fCat==='all'||fCat===c.cat))items.push({t,c});});if(!items.length)return;
          mb+=`<div><div class="flex items-baseline gap-2 mb-3 pb-2 border-b hairline"><span class="font-black tracking-widest text-brand-text">${d.z}</span><span class="text-[10px] font-mono text-brand-muted tracking-widest">${d.en}</span></div><div class="space-y-2">`;
          items.forEach(({t,c})=>{const lvCls=c.lv===1?'lv1':'lv2';mb+=`<button onclick="openBooking('${c.book}')" class="class-card cat-${c.cat} w-full text-left p-3 flex items-center gap-3"><div class="shrink-0 text-center w-14"><div class="text-brand-red font-black font-mono text-sm">${t.s}</div><div class="text-brand-muted/60 text-[9px] font-mono">${t.e}</div></div><div class="flex-1"><div class="flex items-center gap-2 mb-1"><span class="lv-badge ${lvCls}">LV.${c.lv}</span><span class="text-sm font-black tracking-wider text-brand-text">${c.zh}</span></div><div class="text-[10px] text-brand-muted/80 leading-snug">${c.note}</div></div></button>`;});
          mb+='</div></div>';});
        mb+='</div>';
        document.getElementById('sched-grid').innerHTML=wd+we+mb;
      }
      function setCat(f,el){fCat=f;document.querySelectorAll('.sched-filter').forEach(b=>{b.classList.remove('bg-brand-red','text-white','border-brand-red');b.classList.add('text-brand-muted');});el.classList.add('bg-brand-red','text-white','border-brand-red');el.classList.remove('text-brand-muted');buildGrid();hcfTrack('schedule_filter',{f});}
      buildGrid();
    </script>
"""

filters=[('all','全部'),('mt','泰拳'),('sanda','散打'),('kb','踢拳'),('sc','肌力體能')]
filter_btns="".join(f'<button onclick="setCat(\'{k}\',this)" class="sched-filter border hairline {"bg-brand-red text-white border-brand-red" if k=="all" else "text-brand-muted"} px-5 py-2 text-xs tracking-widest font-bold hover:border-brand-red transition-colors interactive-el">{lbl}</button>' for k,lbl in filters)
legend="".join(f'<span class="flex items-center gap-2 text-[11px] text-brand-muted tracking-wider"><span class="w-3 h-3 rounded-sm" style="background:rgb({c})"></span>{l}</span>' for l,c in [('泰拳 MUAY THAI','var(--mt)'),('散打 SANDA','var(--sanda)'),('踢拳 KICKBOXING','var(--kb)'),('肌力體能 S&C / CARDIO','var(--sc)')])

RULES=[("全預約制","最晚取消時間為上課前 2 小時"),("開課標準","全部課程滿 3 人（含以上）即可開課"),("進階課程 LV.2","建議上滿 20 堂基礎班（LV.1）後挑戰"),("停課通知","前一日 22:00 確認狀態，系統簡訊通知")]
MEMBERSHIP=[("包月無限方案 $5,500","天天練最划算"),("推薦獎勵","舊生帶新生，體驗當天購課"),("10% 回饋金","舊生拿獎勵金，新生獲 $500"),("新生體驗","教練／學員引薦，當天購課體驗免收費")]
rules_html="".join(f'<li class="flex items-start gap-3"><span class="w-1.5 h-1.5 rounded-full bg-brand-red mt-2 shrink-0"></span><span class="text-sm text-brand-muted tracking-wider leading-relaxed"><strong class="text-brand-text">{t}：</strong>{d}</span></li>' for t,d in RULES)
mem_html="".join(f'<li class="flex items-start gap-3"><span class="font-black mt-0.5 shrink-0" style="color:rgb(var(--sanda))">+</span><span class="text-sm text-brand-muted tracking-wider leading-relaxed"><strong class="text-brand-text">{t}：</strong>{d}</span></li>' for t,d in MEMBERSHIP)

body = f"""
    <section class="pt-28 pb-12 dot-grid">
        <div class="max-w-7xl mx-auto px-6 md:px-12">
            <div class="flex items-center gap-2 mb-4 fade-up visible"><span class="sys-dot"></span><span class="sys-label text-brand-red">SYSTEM ONLINE</span></div>
            <div class="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-10 fade-up visible">
                <div><h1 class="text-5xl md:text-7xl font-black tracking-tight text-brand-text leading-none">HSINCHU <span class="text-brand-red">COMBAT</span></h1><p class="text-brand-muted text-sm tracking-[0.2em] mt-3 border-l-2 border-brand-red pl-3">專業技擊系統 ｜ 團體課表 2026 EDITION</p></div>
                <button onclick="openBooking('mt-trial')" class="self-start md:self-auto bg-brand-red text-white px-8 py-3.5 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_20px_rgb(var(--color-red)/0.3)] interactive-el magnetic-btn">預約 $400 體驗</button>
            </div>
            <div class="flex flex-wrap gap-x-6 gap-y-3 mb-8 pb-6 border-b hairline">{legend}</div>
            <div class="flex flex-wrap gap-3 mb-10">{filter_btns}</div>
            <div id="sched-grid"></div>
        </div>
    </section>

    <section class="px-6 md:px-12 max-w-7xl mx-auto -mt-2 mb-16">
        <div class="relative overflow-hidden bg-brand-red flex flex-col md:flex-row items-center justify-between gap-4 px-8 py-7 fade-up">
            <div class="absolute inset-0 dot-grid-dense opacity-20"></div>
            <div class="relative flex items-center gap-4"><h3 class="text-3xl md:text-4xl font-black italic tracking-wide text-white">FIGHTER SQUAD</h3><span class="bg-white text-brand-red text-[10px] font-black tracking-widest px-3 py-1.5 rounded-full">INVITATION ONLY</span></div>
            <div class="relative text-white font-mono font-black text-2xl md:text-3xl tracking-widest">14:00 – 16:00</div>
        </div>
        <p class="text-center text-xs text-brand-muted tracking-wider mt-4">選手班 ｜ 週六・週日 ｜ 邀請制進階／備賽學員，總教練親自帶（職業賽冠軍底子）</p>
    </section>

    <section class="py-16 px-6 md:px-12 bg-brand-panel border-y hairline dot-grid">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-12">
            <div class="fade-up"><div class="flex items-center gap-3 mb-6"><span class="w-1 h-6 bg-brand-red"></span><h2 class="sys-label text-brand-text text-sm">SYSTEM RULES // 預約規範</h2></div><ul class="space-y-4">{rules_html}</ul></div>
            <div class="fade-up"><div class="flex items-center gap-3 mb-6"><span class="w-1 h-6" style="background:rgb(var(--sanda))"></span><h2 class="sys-label text-brand-text text-sm">MEMBERSHIP // 招募獎勵</h2></div><ul class="space-y-4">{mem_html}</ul></div>
        </div>
    </section>

    <section class="py-20 px-6 md:px-12 max-w-7xl mx-auto">
        <div class="text-center mb-12 fade-up"><span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-4 py-2 inline-block mb-6">LEVEL SYSTEM</span><h2 class="text-3xl md:text-5xl font-black tracking-widest text-brand-text">課程分級</h2></div>
        <div class="grid md:grid-cols-3 gap-6">
            <div class="border hairline bg-brand-bg p-8 fade-up"><span class="lv-badge lv1 inline-block mb-4">LV.1</span><h3 class="text-xl font-black tracking-widest text-brand-text mb-2">入門團課 <span class="text-sm text-brand-muted font-normal">60 分</span></h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider mb-4">新手泰拳・踢拳腿連擊・泰拳燃脂・肌力體能・散打。所有人都能上，新客主力。</p><p class="text-[11px] text-brand-muted/70 font-mono tracking-wider">暖身 12｜心肺 8｜技術 18｜分組打靶 22</p></div>
            <div class="border hairline bg-brand-bg p-8 fade-up"><span class="lv-badge lv2 inline-block mb-4">LV.2</span><h3 class="text-xl font-black tracking-widest text-brand-text mb-2">進階實戰 <span class="text-sm text-brand-muted font-normal">50 分</span></h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider mb-4">泰拳實戰・踢拳遠距阻擊。建議 LV.1 上滿 20 堂、教練認可後挑戰。</p><p class="text-[11px] text-brand-muted/70 font-mono tracking-wider">暖身 8｜技術精修 12｜條件對練 18｜自由對練＋複盤 12</p></div>
            <div class="border border-brand-red/30 bg-brand-red/5 p-8 fade-up"><span class="text-[10px] font-mono font-black tracking-widest text-brand-red border border-brand-red px-2 py-0.5 inline-block mb-4">SQUAD</span><h3 class="text-xl font-black tracking-widest text-brand-text mb-2">選手班 <span class="text-sm text-brand-muted font-normal">120 分</span></h3><p class="text-sm text-brand-muted leading-relaxed tracking-wider mb-4">Fighter Squad，邀請制。給進階與備賽選手的完整訓練週期。</p><p class="text-[11px] text-brand-muted/70 font-mono tracking-wider">技術深化・多回合對練・體能巔峰・逐人複盤</p></div>
        </div>
        <div class="mt-12 text-center fade-up"><p class="text-brand-muted text-sm tracking-wider mb-6">想找私人課時段？我們依你的時間彈性安排。</p><button onclick="openBooking('private-1')" class="bg-brand-red text-white px-10 py-4 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_25px_rgb(var(--color-red)/0.4)] interactive-el magnetic-btn">預約私人課程</button></div>
    </section>

    <section class="py-16 px-6 md:px-12 bg-brand-panel border-t hairline">
        <div class="max-w-4xl mx-auto grid md:grid-cols-3 gap-8 text-center">
            <div class="fade-up"><i class="fa-solid fa-clock text-brand-red text-2xl mb-4"></i><h3 class="text-brand-text font-bold tracking-widest mb-2">營業時間</h3><p class="text-sm text-brand-muted leading-relaxed">平日 11:00–22:00<br>週末 11:00–16:00</p></div>
            <div class="fade-up"><i class="fa-solid fa-person-walking text-brand-red text-2xl mb-4"></i><h3 class="text-brand-text font-bold tracking-widest mb-2">第一次來</h3><p class="text-sm text-brand-muted leading-relaxed">穿運動服、帶水壺毛巾<br>裝備館內免費提供</p></div>
            <div class="fade-up"><i class="fa-solid fa-location-dot text-brand-red text-2xl mb-4"></i><h3 class="text-brand-text font-bold tracking-widest mb-2">基地位置</h3><p class="text-sm text-brand-muted leading-relaxed">新竹市北區<br>林森路301號2樓</p></div>
        </div>
    </section>
"""

html=(head("HCF 最新課表 2026 | 互動課表・團體課程時段 | 新竹格鬥館","HCF 新竹格鬥館 2026 團體課表：泰拳、散打、踢拳、肌力體能團課時段一覽，含 LV.1/LV.2 分級、預約規範與會員獎勵，可線上快速預約。","schedule.html")
      + nav("schedule") + body + FOOTER + WIDGETS + SHARED_JS)
html=html.replace("</body>\n</html>","<script>"+SCHEDULE_JS+"</script>"+SCHEDULE_RENDER+"</body>\n</html>")
open("schedule.html","w",encoding="utf-8").write(html)
print("generated schedule.html",len(html),"bytes")
