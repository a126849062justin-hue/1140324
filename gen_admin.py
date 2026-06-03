# -*- coding: utf-8 -*-
from _components import head, BASE_STYLE
# Admin is standalone (no public nav/widgets) but shares the design system.

ADMIN_BODY = """
    <div class="min-h-screen">
    <header class="border-b hairline bg-brand-panel/60 backdrop-blur-md sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-5 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-brand-red/15 border border-brand-red/40 flex items-center justify-center text-brand-red rounded-sm"><i class="fa-solid fa-gauge-high"></i></div>
                <div><h1 class="text-lg font-black tracking-widest text-brand-text">HCF 中控台</h1><p class="text-[10px] text-brand-muted tracking-[0.2em] font-mono">ADMIN CONTROL PANEL</p></div>
            </div>
            <div class="flex items-center gap-3">
                <span id="conn-status" class="text-[10px] tracking-widest font-mono text-brand-muted flex items-center gap-1.5"><span class="w-2 h-2 rounded-full bg-yellow-500"></span>DEMO 模式</span>
                <a href="index.html" class="text-xs tracking-widest text-brand-muted hover:text-brand-red transition-colors">← 回官網</a>
            </div>
        </div>
    </header>

    <main class="max-w-6xl mx-auto px-6 py-10 space-y-10">

        <!-- 主題顏色控制 -->
        <section class="border hairline bg-brand-panel">
            <div class="px-6 py-4 border-b hairline flex items-center gap-3"><i class="fa-solid fa-palette text-brand-red"></i><h2 class="font-black tracking-widest text-brand-text">主題色彩</h2><span class="text-[10px] text-brand-muted tracking-widest ml-auto">即時套用到全站</span></div>
            <div class="p-6 grid md:grid-cols-2 gap-8">
                <div>
                    <p class="text-xs text-brand-muted tracking-widest mb-4">快速套用配色</p>
                    <div class="grid grid-cols-3 gap-3" id="preset-grid"></div>
                </div>
                <div>
                    <p class="text-xs text-brand-muted tracking-widest mb-4">自訂主色</p>
                    <div class="flex items-center gap-4 mb-6">
                        <input type="color" id="accent-picker" value="#E63946" class="w-16 h-16 rounded-sm border hairline bg-transparent cursor-pointer">
                        <div><div class="text-2xl font-black text-brand-text" id="accent-hex">#E63946</div><div class="text-[10px] text-brand-muted tracking-widest font-mono">PRIMARY ACCENT</div></div>
                    </div>
                    <div class="flex gap-3">
                        <button onclick="saveTheme()" class="flex-1 bg-brand-red text-white py-3 text-xs tracking-widest font-bold hover:opacity-90 transition-opacity">儲存並套用</button>
                        <button onclick="resetTheme()" class="border hairline text-brand-muted px-5 py-3 text-xs tracking-widest font-bold hover:border-brand-red hover:text-brand-red transition-colors">重設</button>
                    </div>
                    <p id="theme-msg" class="text-[11px] tracking-widest mt-3 min-h-[1rem]"></p>
                </div>
            </div>
            <div class="px-6 py-4 border-t hairline">
                <p class="text-[10px] text-brand-muted tracking-widest mb-3">即時預覽</p>
                <div class="flex flex-wrap items-center gap-3">
                    <button class="bg-brand-red text-white px-5 py-2 text-xs tracking-widest font-bold">主要按鈕</button>
                    <button class="border border-brand-red text-brand-red px-5 py-2 text-xs tracking-widest font-bold">外框按鈕</button>
                    <span class="text-brand-red font-bold tracking-widest">重點文字</span>
                    <span class="text-[10px] font-mono tracking-widest border border-brand-red text-brand-red px-3 py-1.5">標籤</span>
                </div>
            </div>
        </section>

        <!-- 數據總覽 -->
        <section>
            <div class="flex items-center gap-3 mb-5"><i class="fa-solid fa-chart-line text-brand-red"></i><h2 class="font-black tracking-widest text-brand-text">數據總覽</h2><button onclick="loadData()" class="ml-auto text-[11px] tracking-widest text-brand-muted hover:text-brand-red transition-colors"><i class="fa-solid fa-rotate mr-1"></i>重新整理</button></div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4" id="stat-cards"></div>
        </section>

        <!-- 事件分佈 + 熱門頁面 -->
        <section class="grid md:grid-cols-2 gap-6">
            <div class="border hairline bg-brand-panel p-6">
                <h3 class="font-bold tracking-widest text-brand-text mb-5">事件分佈</h3>
                <div id="event-bars" class="space-y-3"></div>
            </div>
            <div class="border hairline bg-brand-panel p-6">
                <h3 class="font-bold tracking-widest text-brand-text mb-5">熱門頁面</h3>
                <div id="page-bars" class="space-y-3"></div>
            </div>
        </section>

        <!-- 最新事件 -->
        <section class="border hairline bg-brand-panel">
            <div class="px-6 py-4 border-b hairline flex items-center gap-3"><i class="fa-solid fa-list text-brand-red"></i><h3 class="font-bold tracking-widest text-brand-text">最新事件</h3><button onclick="exportData()" class="ml-auto text-[11px] tracking-widest text-brand-red hover:underline"><i class="fa-solid fa-download mr-1"></i>匯出 CSV</button></div>
            <div class="overflow-x-auto"><table class="w-full text-sm"><thead><tr class="text-[10px] tracking-widest text-brand-muted border-b hairline"><th class="text-left px-6 py-3 font-mono">時間</th><th class="text-left px-6 py-3 font-mono">事件</th><th class="text-left px-6 py-3 font-mono">頁面</th><th class="text-left px-6 py-3 font-mono">備註</th></tr></thead><tbody id="event-table"></tbody></table></div>
        </section>

        <p class="text-center text-[10px] text-brand-muted tracking-widest font-mono pb-6">未連接後端時顯示本機 DEMO 數據 ・ 部署 Netlify + Supabase 後將顯示真實全站數據</p>
    </main>
    </div>

    <script>
        // ===== 主題色彩 =====
        const PRESETS = [
            {name:'烈焰紅',hex:'#E63946'},{name:'帝王金',hex:'#D4A017'},{name:'電光藍',hex:'#2563EB'},
            {name:'毒液綠',hex:'#16A34A'},{name:'暗夜紫',hex:'#7C3AED'},{name:'熔岩橘',hex:'#EA580C'},
        ];
        function hexToRgbTriplet(hex){const h=hex.replace('#','');return [parseInt(h.slice(0,2),16),parseInt(h.slice(2,4),16),parseInt(h.slice(4,6),16)];}
        function darken(rgb,f){return rgb.map(v=>Math.round(v*f));}
        function applyAccent(hex){const rgb=hexToRgbTriplet(hex);const dk=darken(rgb,0.7);document.documentElement.style.setProperty('--color-red',rgb.join(' '));document.documentElement.style.setProperty('--color-red-dark',dk.join(' '));document.getElementById('accent-hex').textContent=hex.toUpperCase();document.getElementById('accent-picker').value=hex;}
        function saveTheme(){const hex=document.getElementById('accent-picker').value;const rgb=hexToRgbTriplet(hex);const dk=darken(rgb,0.7);localStorage.setItem('hcf_accent',rgb.join(' '));localStorage.setItem('hcf_accent_dark',dk.join(' '));applyAccent(hex);
            const m=document.getElementById('theme-msg');m.textContent='✅ 已儲存，全站將套用此主色（重新整理任一頁面即可看到）。';m.className='text-[11px] tracking-widest mt-3 text-green-500';
            // try persist to backend (optional)
            fetch('/.netlify/functions/set-theme',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({accent:rgb.join(' '),accentDark:dk.join(' ')})}).catch(()=>{});
        }
        function resetTheme(){localStorage.removeItem('hcf_accent');localStorage.removeItem('hcf_accent_dark');applyAccent('#E63946');document.getElementById('theme-msg').textContent='已重設為預設烈焰紅。';document.getElementById('theme-msg').className='text-[11px] tracking-widest mt-3 text-brand-muted';}
        document.getElementById('accent-picker').addEventListener('input',e=>applyAccent(e.target.value));
        // build presets
        document.getElementById('preset-grid').innerHTML = PRESETS.map(p=>`<button onclick="applyAccent('${p.hex}')" class="border hairline p-3 hover:border-brand-red transition-colors text-left"><span class="block w-full h-8 mb-2 rounded-sm" style="background:${p.hex}"></span><span class="text-[10px] tracking-widest text-brand-text">${p.name}</span></button>`).join('');
        // load saved on entry
        (function(){const c=localStorage.getItem('hcf_accent');if(c){const hex='#'+c.split(' ').map(n=>(+n).toString(16).padStart(2,'0')).join('');applyAccent(hex);}})();

        // ===== 數據 =====
        const EVENT_LABELS={pageview:'頁面瀏覽',ai_open:'開啟AI教練',ai_message:'AI對話',booking_open:'開啟預約',booking_submit:'送出預約',schedule_filter:'課表篩選'};
        async function fetchEvents(){
            // try backend; fall back to localStorage demo
            try{const r=await fetch('/.netlify/functions/admin-events');if(r.ok){const d=await r.json();if(Array.isArray(d.data)){document.getElementById('conn-status').innerHTML='<span class="w-2 h-2 rounded-full bg-green-500"></span>已連線';return d.data;}}}catch(e){}
            try{return JSON.parse(localStorage.getItem('hcf_events')||'[]');}catch(e){return [];}
        }
        function bar(label,val,max,color){const pct=max?Math.round(val/max*100):0;return `<div><div class="flex justify-between text-xs mb-1"><span class="text-brand-text tracking-wider">${label}</span><span class="text-brand-muted font-mono">${val}</span></div><div class="h-2 bg-brand-bg border hairline"><div class="h-full" style="width:${pct}%;background:${color||'rgb(var(--color-red))'}"></div></div></div>`;}
        let CACHE=[];
        async function loadData(){
            const ev=await fetchEvents();CACHE=ev;
            const total=ev.length;
            const pv=ev.filter(e=>e.type==='pageview').length;
            const bk=ev.filter(e=>e.type==='booking_submit').length;
            const ai=ev.filter(e=>e.type==='ai_open'||e.type==='ai_message').length;
            const cards=[['總事件',total,'fa-bolt'],['頁面瀏覽',pv,'fa-eye'],['AI 互動',ai,'fa-robot'],['預約送出',bk,'fa-calendar-check']];
            document.getElementById('stat-cards').innerHTML=cards.map(([l,v,i])=>`<div class="border hairline bg-brand-panel p-5"><div class="flex items-center justify-between mb-3"><i class="fa-solid ${i} text-brand-red"></i></div><div class="text-3xl font-black text-brand-text font-serif">${v}</div><div class="text-[10px] tracking-[0.2em] text-brand-muted mt-1">${l}</div></div>`).join('');
            // event distribution
            const byType={};ev.forEach(e=>byType[e.type]=(byType[e.type]||0)+1);
            const maxT=Math.max(1,...Object.values(byType));
            document.getElementById('event-bars').innerHTML=Object.entries(byType).sort((a,b)=>b[1]-a[1]).map(([t,v])=>bar(EVENT_LABELS[t]||t,v,maxT)).join('')||'<p class="text-xs text-brand-muted">尚無數據，瀏覽官網後再回來查看。</p>';
            // pages
            const byPage={};ev.filter(e=>e.type==='pageview').forEach(e=>{const p=e.path||'/';byPage[p]=(byPage[p]||0)+1;});
            const maxP=Math.max(1,...Object.values(byPage));
            document.getElementById('page-bars').innerHTML=Object.entries(byPage).sort((a,b)=>b[1]-a[1]).slice(0,8).map(([p,v])=>bar(p,v,maxP,'rgb(var(--color-text))')).join('')||'<p class="text-xs text-brand-muted">尚無數據。</p>';
            // table
            const rows=ev.slice(-30).reverse();
            document.getElementById('event-table').innerHTML=rows.map(e=>{const t=new Date(e.ts||Date.now());const ts=t.toLocaleString('zh-TW',{hour12:false});const meta=e.meta?JSON.stringify(e.meta):'—';return `<tr class="border-b hairline hover:bg-brand-bg/40"><td class="px-6 py-3 text-[11px] font-mono text-brand-muted">${ts}</td><td class="px-6 py-3 text-brand-text tracking-wider">${EVENT_LABELS[e.type]||e.type}</td><td class="px-6 py-3 text-[11px] font-mono text-brand-muted">${e.path||'—'}</td><td class="px-6 py-3 text-[11px] text-brand-muted">${meta}</td></tr>`;}).join('')||'<tr><td colspan="4" class="px-6 py-8 text-center text-brand-muted text-xs">尚無事件記錄</td></tr>';
        }
        function exportData(){const ev=CACHE;if(!ev.length){alert('尚無資料可匯出');return;}const head=['time','type','path','meta'];const lines=[head.join(',')].concat(ev.map(e=>[new Date(e.ts||Date.now()).toISOString(),e.type,e.path||'',JSON.stringify(e.meta||'')].map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(',')));const blob=new Blob([lines.join('\\n')],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='hcf-events.csv';a.click();}
        loadData();
    </script>
</body>
</html>
"""

admin_head = head("HCF 中控台 | 後台管理系統","HCF 官網後台：主題色彩控制與數據儀表板。","admin.html")
# admin: add a meta noindex
admin_head = admin_head.replace('<meta name="theme-color" content="#E63946">','<meta name="theme-color" content="#E63946">\n    <meta name="robots" content="noindex, nofollow">')
open("admin.html","w",encoding="utf-8").write(admin_head + ADMIN_BODY)
print("generated admin.html")
