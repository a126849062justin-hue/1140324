# -*- coding: utf-8 -*-
"""AI coach widget, booking modal, analytics beacon and the shared interaction JS."""

WIDGETS = """
    <!-- AI 智能鯊魚教練 -->
    <button id="ai-fab" onclick="toggleAIChat()" class="fixed bottom-36 md:bottom-24 right-6 z-[75] bg-brand-bg border border-brand-red text-brand-red w-14 h-14 rounded-full flex items-center justify-center shadow-[0_5px_20px_rgb(var(--color-red)/0.4)] hover:bg-brand-red hover:text-white transition-all duration-300 interactive-el group" aria-label="開啟 AI 智能教練">
        <i class="fa-solid fa-robot text-xl"></i>
        <span class="absolute -top-1 -right-1 w-3 h-3 bg-brand-red rounded-full animate-ping"></span>
    </button>
    <div id="ai-chat-panel" class="fixed bottom-0 right-0 md:bottom-24 md:right-6 z-[120] w-full md:w-[380px] h-[80dvh] md:h-[520px] glass-panel border hairline flex flex-col translate-y-full md:translate-y-4 opacity-0 pointer-events-none transition-all duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] md:rounded-sm overflow-hidden">
        <div class="flex items-center justify-between px-5 py-4 border-b hairline bg-brand-bg/60">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-full bg-brand-red/15 border border-brand-red/40 flex items-center justify-center text-brand-red"><i class="fa-solid fa-robot"></i></div>
                <div><div class="text-sm font-bold tracking-widest text-brand-text">智能鯊魚教練</div><div class="text-[10px] text-brand-muted tracking-wider flex items-center gap-1.5"><span class="w-1.5 h-1.5 bg-green-500 rounded-full"></span> 24小時待命</div></div>
            </div>
            <button onclick="toggleAIChat()" class="text-brand-muted hover:text-brand-red text-lg interactive-el w-9 h-9 flex items-center justify-center"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div id="ai-chat-history" class="flex-1 overflow-y-auto p-5 space-y-4 text-sm">
            <div class="bg-brand-bg/70 border hairline p-3.5 rounded-sm rounded-tl-none max-w-[90%] text-brand-text leading-relaxed">嘿，未來的戰士！🦈 我是 HCF 智能鯊魚教練。<br>費用、新手、地點、裝備…任何問題都可以直接問我，或直接領取 $400 體驗！</div>
        </div>
        <div class="px-5 py-3 border-t hairline bg-brand-bg/60">
            <div class="flex flex-wrap gap-2 mb-3">
                <button onclick="aiAsk('費用怎麼算？')" class="text-[11px] tracking-wider border hairline text-brand-muted px-3 py-1.5 hover:border-brand-red hover:text-brand-red transition-colors interactive-el">💰 費用</button>
                <button onclick="aiAsk('新手適合嗎？')" class="text-[11px] tracking-wider border hairline text-brand-muted px-3 py-1.5 hover:border-brand-red hover:text-brand-red transition-colors interactive-el">🔰 新手</button>
                <button onclick="aiAsk('地點在哪？')" class="text-[11px] tracking-wider border hairline text-brand-muted px-3 py-1.5 hover:border-brand-red hover:text-brand-red transition-colors interactive-el">📍 地點</button>
                <button onclick="aiAsk('需要帶裝備嗎？')" class="text-[11px] tracking-wider border hairline text-brand-muted px-3 py-1.5 hover:border-brand-red hover:text-brand-red transition-colors interactive-el">🥊 裝備</button>
            </div>
            <div class="flex gap-2">
                <input id="ai-input" type="text" placeholder="輸入你的問題…" onkeydown="if(event.key==='Enter')aiSend()" class="flex-1 bg-brand-bg border hairline px-4 py-2.5 text-sm text-brand-text placeholder:text-brand-muted/60 focus:border-brand-red outline-none transition-colors">
                <button onclick="aiSend()" class="bg-brand-red text-white w-11 flex items-center justify-center hover:bg-brand-text hover:text-brand-bg transition-colors interactive-el"><i class="fa-solid fa-paper-plane"></i></button>
            </div>
        </div>
    </div>

    <!-- 預約 Modal -->
    <div id="booking-modal" class="fixed inset-0 z-[130] flex items-center justify-center px-4 opacity-0 pointer-events-none transition-opacity duration-400">
        <div class="absolute inset-0 bg-black/70 backdrop-blur-sm" onclick="closeBooking()"></div>
        <div class="relative glass-panel border hairline w-full max-w-md p-8 md:rounded-sm transform scale-95 transition-transform duration-400" id="booking-card">
            <button onclick="closeBooking()" class="absolute top-5 right-5 text-brand-muted hover:text-brand-red text-lg interactive-el"><i class="fa-solid fa-xmark"></i></button>
            <span class="text-brand-red text-[10px] font-mono tracking-[0.4em] border border-brand-red px-3 py-1.5 inline-block mb-5">QUICK BOOKING / 快速預約</span>
            <h3 class="text-2xl font-black tracking-widest text-brand-text mb-1">啟動你的第一戰</h3>
            <p class="text-xs text-brand-muted tracking-wider mb-6">填寫後我們將透過 LINE 與你確認時段。</p>
            <div class="space-y-4">
                <div><label class="text-[11px] tracking-widest text-brand-muted block mb-2">選擇方案</label>
                    <select id="bk-course" class="w-full bg-brand-bg border hairline px-4 py-3 text-sm text-brand-text focus:border-brand-red outline-none">
                        <option value="mt-trial" data-price="400">泰拳團課體驗 — $400</option>
                        <option value="kb-trial" data-price="400">踢拳團課體驗 — $400</option>
                        <option value="sd-trial" data-price="400">散打團課體驗 — $400</option>
                        <option value="sc-trial" data-price="400">肌力體能體驗 — $400</option>
                        <option value="private-1" data-price="1400">私教體驗 1 堂 — $1,400</option>
                        <option value="private-2" data-price="2400">私教體驗 2 堂 — $2,400</option>
                    </select></div>
                <div><label class="text-[11px] tracking-widest text-brand-muted block mb-2">你的稱呼</label><input id="bk-name" type="text" placeholder="戰士名" class="w-full bg-brand-bg border hairline px-4 py-3 text-sm text-brand-text placeholder:text-brand-muted/60 focus:border-brand-red outline-none"></div>
                <div><label class="text-[11px] tracking-widest text-brand-muted block mb-2">聯絡電話</label><input id="bk-phone" type="tel" placeholder="09xx-xxx-xxx" class="w-full bg-brand-bg border hairline px-4 py-3 text-sm text-brand-text placeholder:text-brand-muted/60 focus:border-brand-red outline-none"></div>
                <button onclick="submitBooking()" id="bk-submit" class="w-full bg-brand-red text-white py-3.5 text-xs tracking-[0.2em] font-bold hover:bg-brand-text hover:text-brand-bg transition-colors duration-300 shadow-[0_0_20px_rgb(var(--color-red)/0.3)] interactive-el">送出預約 →</button>
                <p id="bk-status" class="text-center text-xs tracking-wider text-brand-muted min-h-[1rem]"></p>
                <p class="text-center text-[11px] text-brand-muted tracking-wider">或直接 <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="text-brand-red hover:underline interactive-el">LINE 真人客服</a></p>
            </div>
        </div>
    </div>
"""

SHARED_JS = """
    <script>
        // ===== 主題切換 =====
        function toggleTheme(){const h=document.documentElement;h.classList.toggle('light-mode');const l=h.classList.contains('light-mode');localStorage.setItem('theme',l?'light':'dark');const i=document.querySelector('.theme-icon');if(i){i.classList.toggle('fa-circle-half-stroke',!l);i.classList.toggle('fa-moon',l);}}
        if(document.documentElement.classList.contains('light-mode')){const i=document.querySelector('.theme-icon');if(i)i.classList.replace('fa-circle-half-stroke','fa-moon');}

        // ===== 抽屜 =====
        const navDrawer=document.getElementById('nav-drawer');const backdrop=document.getElementById('drawer-backdrop');
        function toggleNavDrawer(){if(navDrawer.classList.contains('translate-x-full')){navDrawer.classList.remove('translate-x-full');showBackdrop();}else{closeAllDrawers();}}
        function showBackdrop(){backdrop.classList.remove('pointer-events-none','opacity-0');backdrop.classList.add('opacity-100');document.body.style.overflow='hidden';}
        function closeAllDrawers(){if(navDrawer)navDrawer.classList.add('translate-x-full');backdrop.classList.remove('opacity-100');backdrop.classList.add('opacity-0','pointer-events-none');document.body.style.overflow='';}

        // ===== 自訂游標 + 磁吸按鈕 =====
        if(window.matchMedia("(pointer: fine)").matches){
            const d=document.getElementById('cursor-dot'),r=document.getElementById('cursor-ring');
            let mx=innerWidth/2,my=innerHeight/2,dx=mx,dy=my,rx=mx,ry=my;
            addEventListener('mousemove',e=>{mx=e.clientX;my=e.clientY;});
            (function loop(){dx+=(mx-dx)*.4;dy+=(my-dy)*.4;rx+=(mx-rx)*.15;ry+=(my-ry)*.15;if(d)d.style.transform=`translate3d(calc(${dx}px - 50%),calc(${dy}px - 50%),0)`;if(r)r.style.transform=`translate3d(calc(${rx}px - 50%),calc(${ry}px - 50%),0)`;requestAnimationFrame(loop);})();
            document.querySelectorAll('.interactive-el').forEach(e=>{e.addEventListener('mouseenter',()=>document.body.classList.add('hovering'));e.addEventListener('mouseleave',()=>document.body.classList.remove('hovering'));});
            document.querySelectorAll('.magnetic-btn').forEach(b=>{b.addEventListener('mousemove',function(e){const t=this.getBoundingClientRect();this.style.transform=`translate3d(${(e.clientX-t.left-t.width/2)*.3}px,${(e.clientY-t.top-t.height/2)*.3}px,0)`;});b.addEventListener('mouseleave',function(){this.style.transform='translate3d(0,0,0)';});});
        }

        // ===== 導覽列縮放 =====
        const nav=document.getElementById('navbar');addEventListener('scroll',()=>{if(scrollY>50){nav.classList.add('py-3');nav.classList.remove('py-4');}else{nav.classList.remove('py-3');nav.classList.add('py-4');}},{passive:true});

        // ===== 進場動畫 =====
        const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});},{threshold:0.15,rootMargin:"0px 0px -50px 0px"});
        document.querySelectorAll('.fade-up').forEach(e=>io.observe(e));

        // ===== 數據收集 (analytics beacon) =====
        function hcfTrack(type, meta){
            try{
                const body=JSON.stringify({type,path:location.pathname,ts:Date.now(),meta:meta||null});
                fetch('/.netlify/functions/track-event',{method:'POST',headers:{'Content-Type':'application/json'},body,keepalive:true}).catch(()=>{});
                // local mirror so the admin demo dashboard works without a backend
                const k='hcf_events';const arr=JSON.parse(localStorage.getItem(k)||'[]');arr.push({type,path:location.pathname,ts:Date.now(),meta:meta||null});localStorage.setItem(k,JSON.stringify(arr.slice(-500)));
            }catch(e){}
        }
        hcfTrack('pageview');

        // ===== AI 智能教練 =====
        const aiPanel=document.getElementById('ai-chat-panel');let aiOpen=false;
        function toggleAIChat(){aiOpen=!aiOpen;if(aiOpen){aiPanel.classList.remove('translate-y-full','md:translate-y-4','opacity-0','pointer-events-none');aiPanel.classList.add('opacity-100');hcfTrack('ai_open');setTimeout(()=>document.getElementById('ai-input')?.focus(),300);}else{aiPanel.classList.add('opacity-0','pointer-events-none','md:translate-y-4','translate-y-full');aiPanel.classList.remove('opacity-100');}}
        function aiAppend(html,who){const box=document.getElementById('ai-chat-history');const w=document.createElement('div');if(who==='user'){w.className='flex justify-end';w.innerHTML='<div class="bg-brand-red text-white p-3 rounded-sm rounded-tr-none max-w-[85%] leading-relaxed">'+html+'</div>';}else{w.innerHTML='<div class="bg-brand-bg/70 border hairline p-3.5 rounded-sm rounded-tl-none max-w-[90%] text-brand-text leading-relaxed">'+html+'</div>';}box.appendChild(w);box.scrollTop=box.scrollHeight;return w;}
        function aiAsk(q){document.getElementById('ai-input').value=q;aiSend();}
        async function aiSend(){const inp=document.getElementById('ai-input');const q=inp.value.trim();if(!q)return;inp.value='';aiAppend(q,'user');hcfTrack('ai_message',{q});const l=aiAppend('<span class="text-brand-muted">🦈 鯊魚教練思考中…</span>','bot');try{const res=await fetch('/.netlify/functions/chat-claude',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:q})});const data=await res.json();const reply=(data.reply||'我不太確定，建議直接問真人客服！').replace(/\\n/g,'<br>');l.querySelector('div').innerHTML=reply+'<div class="mt-3 pt-3 border-t hairline"><a href="javascript:void(0)" onclick="closeAndBook()" class="text-brand-red text-[11px] font-bold tracking-widest hover:underline">⚡ 直接預約 $400 體驗 →</a></div>';}catch(e){l.querySelector('div').innerHTML='🦈 教練去打沙包了！直接找真人客服更快：<br><a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="text-brand-red hover:underline">LINE 官方帳號</a> ・ 0925-571-225';}}
        function closeAndBook(){toggleAIChat();openBooking('mt-trial');}

        // ===== 預約 Modal =====
        const bkModal=document.getElementById('booking-modal'),bkCard=document.getElementById('booking-card');
        function openBooking(c){if(c){const s=document.getElementById('bk-course');if([...s.options].some(o=>o.value===c))s.value=c;}bkModal.classList.remove('opacity-0','pointer-events-none');bkModal.classList.add('opacity-100');bkCard.classList.remove('scale-95');bkCard.classList.add('scale-100');document.body.style.overflow='hidden';hcfTrack('booking_open',{course:c||'default'});}
        function closeBooking(){bkModal.classList.add('opacity-0','pointer-events-none');bkModal.classList.remove('opacity-100');bkCard.classList.add('scale-95');bkCard.classList.remove('scale-100');document.body.style.overflow='';}
        async function submitBooking(){const sel=document.getElementById('bk-course');const course=sel.options[sel.selectedIndex].text;const slotId=sel.value;const price=parseInt(sel.options[sel.selectedIndex].dataset.price||'0',10);const name=document.getElementById('bk-name').value.trim();const phone=document.getElementById('bk-phone').value.trim();const st=document.getElementById('bk-status');const btn=document.getElementById('bk-submit');if(!name||!phone){st.textContent='請填寫稱呼與電話 🥊';st.className='text-center text-xs tracking-wider text-brand-red';return;}btn.disabled=true;btn.textContent='送出中…';st.textContent='';try{const res=await fetch('/.netlify/functions/bookings',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({slotId,course,name,phone,price,source:'website'})});if(!res.ok)throw new Error();st.innerHTML='✅ 預約已送出！我們會盡快用 LINE 與你確認。';st.className='text-center text-xs tracking-wider text-green-500';hcfTrack('booking_submit',{course,price});setTimeout(()=>{closeBooking();btn.disabled=false;btn.textContent='送出預約 →';document.getElementById('bk-name').value='';document.getElementById('bk-phone').value='';st.textContent='';},2500);}catch(e){st.innerHTML='⚠️ 系統忙線，請直接 <a href="https://lin.ee/7lidUv0" target="_blank" rel="noopener" class="text-brand-red underline">LINE 預約</a>';st.className='text-center text-xs tracking-wider text-brand-red';btn.disabled=false;btn.textContent='送出預約 →';}}
        document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeBooking();if(aiOpen)toggleAIChat();}});
    </script>
    <script>if('serviceWorker' in navigator){addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}</script>
</body>
</html>
"""

if __name__ == "__main__":
    print("widgets module OK")
