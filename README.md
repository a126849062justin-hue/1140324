# HCF 新竹格鬥館 — 官網（完整重建版 v5）

電影感紅黑沉浸式設計 × 完整課程內容 × 可後台管理。全站繁體中文。

---

## 一、網站架構

```
首頁              index.html        重寫文案・縮放 Hero・戰績橫幅・痛點・橫向課程・評價・FAQ
課程介紹（6 個獨立子頁）
  ├ 泰拳          muaythai.html
  ├ 踢拳          kickboxing.html
  ├ 散打          sanda.html
  ├ 肌力體能      strength.html
  ├ 團體課程      group-class.html
  └ 私人課程      private-class.html
教練團隊          coaches.html      重新設計：總教練大卡＋成員卡，含戰績／折扣碼
最新課表          schedule.html     2026 官方課表互動版：依類別篩選、LV.1/LV.2 分級、預約規範＋會員獎勵、點選即預約
課程方案          pricing.html      完整透明價目（團體／私人／雙人／打靶）
新手問答          faq.html          新手最常問的四大類問題（開始之前／怎麼上課／課程怎麼選／費用與預約）
後台中控台        admin.html        主題換色 ＋ 數據儀表板（不公開、已設 noindex）
```

課程子頁已帶入《團體課程課綱手冊》的「一堂課這樣跑」60 分鐘排程；課表完全對應官方 2026 海報（泰拳紅／散打金／踢拳灰／肌力綠、LV.1 綠徽 / LV.2 紅徽）。

每個課程子頁的結構一致：電影感 Hero → 一句話定位 → 為什麼練（三大理由）→ 你會學到 → 適合誰 → FAQ → 預約 CTA。

全站共用元件（導覽列、頁尾、AI 教練、預約 Modal）由 `_components.py` / `_widgets.py` 產生，確保每頁一致。要改版時，改模組再跑下方的「重新生成」即可。

---

## 二、後台系統 admin.html

### 1. 主題換色（即時套用全站）
- 6 組預設配色（烈焰紅／帝王金／電光藍／毒液綠／暗夜紫／熔岩橘）＋ 自訂色票。
- 原理：全站主色改用 CSS 變數 `--color-red`，後台選色後寫入瀏覽器 `localStorage`，每頁載入時自動套用。
- 想做成「全站永久統一」：後台同時會嘗試呼叫 `set-theme` 函式；搭配 `get-theme` 在頁面載入時讀取，即可讓所有訪客看到同一個主色（需部署 Netlify）。

### 2. 數據儀表板
- 收集事件：頁面瀏覽、開啟／使用 AI 教練、開啟預約、送出預約、課表篩選。
- 顯示：總覽數字卡、事件分佈、熱門頁面、最新事件表，並可匯出 CSV。
- 資料來源：未接後端時讀取本機 `localStorage`（DEMO，立即可用）；部署後可改接 Supabase 取得真實全站數據。

---

## 三、互動功能
- AI 智能鯊魚教練（右下浮球）— 接 `chat-claude` 函式。
- 快速預約 Modal（全站任何 CTA 都能開）— 接 `bookings` 函式。
- 明暗主題切換、自訂游標、磁吸按鈕、縮放 Hero、橫向捲動課程、進場動畫。
- PWA：可加到主畫面、離線頁 `offline.html`。

---

## 四、部署（Netlify）

1. 把整個資料夾推到 Git 或直接拖拉上傳到 Netlify。
2. 設定環境變數（Site settings → Environment variables）：
   - `ANTHROPIC_API_KEY` — AI 教練（沒設會自動導向 LINE）
   - `SUPABASE_URL`、`SUPABASE_KEY` — 預約與數據（沒設會進 DEMO 模式）
   - `ADMIN_PASSWORD` — 後台數據 API 存取密碼
3. `netlify.toml` 已設好發佈目錄、函式目錄與快取／安全標頭。
4. 資料表結構見 `supabase-init.sql`。

> 本機直接開檔（file://）時，預約／AI／數據後端不會運作，屬正常；務必在 Netlify 環境測試完整功能。

---

## 五、改版／重新生成

頁面由 Python 產生器組裝（已附在資料夾內）：

```bash
python3 gen_index.py            # 首頁
python3 gen_courses.py          # 6 個課程子頁
python3 gen_coaches_pricing.py  # 教練 + 價目
python3 gen_schedule.py         # 2026 互動課表
python3 gen_faq.py              # 新手問答
python3 gen_admin.py            # 後台

# 改完 class 後重新編譯 CSS：
npm install -D tailwindcss@3.4.17
npx tailwindcss -i tw-input.css -o tw-build.css --minify
```

- 文案：直接改各 `gen_*.py` 裡的中文字串。
- 課表時段：改 `gen_schedule.py` 裡的 `SCHEDULE.slots`。
- 教練資料：改 `gen_coaches_pricing.py` 裡的 `COACHES`。

---

## 六、設計規格
- 主色（可換）：預設 #E63946；深色底 #050505／面板 #0F0F0F。
- 字體：大標 Cormorant Garamond（英）＋ Noto Sans TC（中）。
- 課表類型色：泰拳紅・踢拳藍・散打橘・肌力綠・綜合紫。
