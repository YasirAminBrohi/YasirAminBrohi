import os
import shutil

base_dir = r'c:\Users\Adi\Documents\Yasir\Github'
assets_dir = os.path.join(base_dir, 'assets')
scripts_dir = os.path.join(base_dir, 'scripts')
workflows_dir = os.path.join(base_dir, '.github', 'workflows')

print("Cleaning up old directories...")
for d in [assets_dir, scripts_dir, workflows_dir]:
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d, exist_ok=True)

print("Directories recreated.")

def write_svg(filename, content):
    path = os.path.join(assets_dir, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated {filename}")

# Shared CSS and Definitions
SHARED_DEFS = """
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#0F1D30" stroke-width="1" opacity="0.8"/>
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <linearGradient id="grad-title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#7B2FFF" />
    </linearGradient>
    <linearGradient id="grad-end" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF007F" />
      <stop offset="50%" stop-color="#00F0FF" />
      <stop offset="100%" stop-color="#00FF88" />
    </linearGradient>
  </defs>
  <style>
    text { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .scanline { animation: scan 6s linear infinite; }
    @keyframes scan {
      0% { transform: translateY(-50px); opacity: 0; }
      10% { opacity: 0.5; }
      90% { opacity: 0.5; }
      100% { transform: translateY(600px); opacity: 0; }
    }
    .pulseBeam { stroke-dasharray: 100 900; animation: dash 4s linear infinite; }
    @keyframes dash {
      from { stroke-dashoffset: 1000; }
      to { stroke-dashoffset: 0; }
    }
    .blinkDot { animation: blink 1.5s ease-in-out infinite alternate; }
    @keyframes blink { 0% { opacity: 0.2; } 100% { opacity: 1; } }
    .pulseNode { animation: pulseRadius 2s ease-in-out infinite alternate; }
    @keyframes pulseRadius { 0% { r: 16; } 100% { r: 20; } }
    .titleGlow { animation: drop 3s infinite alternate; }
    @keyframes drop {
      0% { filter: drop-shadow(0px 0px 5px rgba(0,240,255,0.4)); }
      100% { filter: drop-shadow(0px 0px 10px rgba(123,47,255,0.6)); }
    }
  </style>
"""

def make_corners(width, height):
    return f"""
    <!-- Corner Brackets -->
    <path d="M 15 35 L 15 15 L 35 15" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
    <path d="M {width-35} 15 L {width-15} 15 L {width-15} 35" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
    <path d="M 15 {height-35} L 15 {height-15} L 35 {height-15}" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
    <path d="M {width-35} {height-15} L {width-15} {height-15} L {width-15} {height-35}" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
    """

# ----------------- SVG 1: header-core.svg -----------------
svg_header = f"""<svg width="950" height="260" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 260">
  {SHARED_DEFS}
  <rect width="950" height="260" fill="#050A12" rx="8"/>
  <rect width="950" height="260" fill="url(#grid)" rx="8" opacity="0.8"/>
  {make_corners(950, 260)}
  
  <!-- Animated Scanline -->
  <line class="scanline" x1="0" y1="0" x2="950" y2="0" stroke="#00F0FF" stroke-width="2" opacity="0.2"/>

  <!-- Top Metadata -->
  <text x="45" y="30" fill="#7E9EB8" font-size="12">SYS_ID: YASIR_CORE-0x7F</text>
  <text x="475" y="30" fill="#7E9EB8" font-size="12" text-anchor="middle">NODE: FAST-NUCES.KHI</text>
  <text x="905" y="30" fill="#7E9EB8" font-size="12" text-anchor="end">KERNEL: v3.0_INTERCEPTOR</text>

  <!-- LIVE Beacon -->
  <circle class="blinkDot" cx="925" cy="26" r="4" fill="#00FF88" filter="url(#glow)"/>

  <!-- Circuit Trace -->
  <path class="pulseBeam" d="M 45 45 L 200 45 L 220 65 L 730 65 L 750 45 L 905 45" fill="none" stroke="#00F0FF" stroke-width="1.5" filter="url(#glow)"/>

  <!-- Title -->
  <text x="475" y="140" fill="url(#grad-title)" font-size="48" font-weight="bold" text-anchor="middle" class="titleGlow">YASIR AMIN BROHI</text>
  
  <!-- Subtitle -->
  <text x="475" y="175" fill="#7E9EB8" font-size="14" text-anchor="middle" letter-spacing="1">[ PROTOCOL ENGINEERING · BROWSER INTERNALS · SYSTEMS · ANDROID ]</text>

  <!-- Waveform -->
  <path d="M 275 220 Q 300 190 325 220 T 375 220 T 425 220 T 475 220 T 525 220 T 575 220 T 625 220 T 675 220" fill="none" stroke="#FF007F" stroke-width="1.5" filter="url(#glow)" stroke-dasharray="250 500" class="pulseBeam"/>

  <!-- Bottom Metadata -->
  <text x="45" y="240" fill="#3D5675" font-size="10">COORD: 24.8607° N, 67.0011° E</text>
  <text x="905" y="240" fill="#3D5675" font-size="10" text-anchor="end">RUNTIME: DISTRIBUTED_V3</text>
</svg>"""

# ----------------- SVG 2: operator-core.svg -----------------
svg_operator = f"""<svg width="950" height="200" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 200">
  {SHARED_DEFS}
  <rect width="950" height="200" fill="#0A1628" rx="8" stroke="#152238" stroke-width="2"/>
  <rect width="950" height="200" fill="url(#grid)" rx="8" opacity="0.8"/>
  {make_corners(950, 200)}

  <!-- Left Section (60%) -->
  <text x="45" y="45" fill="#00F0FF" font-size="16" font-weight="bold">OPERATOR // IDENTITY MANIFEST</text>
  <path d="M 45 55 L 350 55" fill="none" stroke="#152238" stroke-width="1"/>
  
  <text x="45" y="85" fill="#3D5675" font-size="12">HANDLE:</text>
  <text x="120" y="85" fill="#E2E8F0" font-size="13">YasirAminBrohi</text>
  
  <text x="45" y="115" fill="#3D5675" font-size="12">BASE:</text>
  <text x="120" y="115" fill="#E2E8F0" font-size="13">FAST-NUCES Karachi Campus (BSCS)</text>

  <text x="45" y="145" fill="#3D5675" font-size="12">REGION:</text>
  <text x="120" y="145" fill="#E2E8F0" font-size="13">Sindh, Pakistan</text>
  
  <text x="45" y="175" fill="#3D5675" font-size="12">MODE:</text>
  <text x="120" y="175" fill="#00FF88" font-size="13">Systems &amp; Browser Protocol Engineering</text>

  <!-- Right Section (40%) -->
  <path d="M 550 20 L 550 180" fill="none" stroke="#152238" stroke-width="1"/>
  <text x="580" y="45" fill="#00F0FF" font-size="14" font-weight="bold">PRIMARY DOMAINS</text>
  
  <!-- Bars -->
  <!-- Cyan -->
  <text x="580" y="75" fill="#7E9EB8" font-size="11">BROWSER INTERCEPTION</text>
  <rect x="750" y="67" width="120" height="8" fill="#00F0FF" rx="2"/><rect x="872" y="67" width="30" height="8" fill="#152238" rx="2"/>
  
  <!-- Green -->
  <text x="580" y="100" fill="#7E9EB8" font-size="11">ANDROID SYSTEMS</text>
  <rect x="750" y="92" width="90" height="8" fill="#00FF88" rx="2"/><rect x="842" y="92" width="60" height="8" fill="#152238" rx="2"/>
  
  <!-- Violet -->
  <text x="580" y="125" fill="#7E9EB8" font-size="11">FULL STACK WEB</text>
  <rect x="750" y="117" width="105" height="8" fill="#7B2FFF" rx="2"/><rect x="857" y="117" width="45" height="8" fill="#152238" rx="2"/>
  
  <!-- Amber -->
  <text x="580" y="150" fill="#7E9EB8" font-size="11">SYSTEMS / CLI</text>
  <rect x="750" y="142" width="75" height="8" fill="#FFB800" rx="2"/><rect x="827" y="142" width="75" height="8" fill="#152238" rx="2"/>
  
  <!-- Magenta -->
  <text x="580" y="175" fill="#7E9EB8" font-size="11">ALGORITHMS / C</text>
  <rect x="750" y="167" width="60" height="8" fill="#FF007F" rx="2"/><rect x="812" y="167" width="90" height="8" fill="#152238" rx="2"/>
</svg>"""

# ----------------- SVG 3: sector-constellation.svg -----------------
svg_constellation = f"""<svg width="950" height="500" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 500">
  {SHARED_DEFS}
  <rect width="950" height="500" fill="#050A12" rx="8"/>
  <rect width="950" height="500" fill="url(#grid)" rx="8" opacity="0.4"/>
  {make_corners(950, 500)}

  <!-- Animated Bus Lines -->
  <path class="pulseBeam" d="M 475 250 L 175 100" fill="none" stroke="#00F0FF" stroke-width="2" stroke-dasharray="30 100" opacity="0.6"/>
  <path class="pulseBeam" d="M 475 250 L 175 400" fill="none" stroke="#00FF88" stroke-width="2" stroke-dasharray="30 100" opacity="0.6"/>
  <path class="pulseBeam" d="M 475 250 L 775 100" fill="none" stroke="#FF007F" stroke-width="2" stroke-dasharray="30 100" opacity="0.6"/>
  <path class="pulseBeam" d="M 475 250 L 775 400" fill="none" stroke="#FFB800" stroke-width="2" stroke-dasharray="30 100" opacity="0.6"/>

  <!-- Thin project connection lines -->
  <path d="M 175 100 L 90 60 M 175 100 L 160 155 M 175 100 L 250 55 M 175 100 L 80 155" fill="none" stroke="#00F0FF" stroke-width="0.5" opacity="0.4"/>
  <path d="M 175 400 L 90 350 M 175 400 L 170 430 M 175 400 L 260 380 M 175 400 L 90 440" fill="none" stroke="#00FF88" stroke-width="0.5" opacity="0.4"/>
  <path d="M 775 100 L 690 55 M 775 100 L 780 155 M 775 100 L 870 60 M 775 100 L 850 155 M 775 100 L 700 155" fill="none" stroke="#FF007F" stroke-width="0.5" opacity="0.4"/>
  <path d="M 775 400 L 700 380 M 775 400 L 780 430 M 775 400 L 870 370" fill="none" stroke="#FFB800" stroke-width="0.5" opacity="0.4"/>

  <!-- Core Node -->
  <circle class="pulseNode" cx="475" cy="250" r="18" fill="none" stroke="#7B2FFF" stroke-width="2" filter="url(#glow)"/>
  <circle cx="475" cy="250" r="6" fill="#7B2FFF"/>
  <text x="475" y="285" fill="#E2E8F0" font-size="12" font-weight="bold" text-anchor="middle">YASIR_NEXUS</text>

  <!-- Sector Nodes -->
  <!-- ALPHA -->
  <circle cx="175" cy="100" r="14" fill="#00F0FF" filter="url(#glow)" opacity="0.8"/>
  <text x="175" y="130" fill="#00F0FF" font-size="10" text-anchor="middle">BROWSER &amp; MV3</text>
  
  <!-- BETA -->
  <circle cx="175" cy="400" r="14" fill="#00FF88" filter="url(#glow)" opacity="0.8"/>
  <text x="175" y="380" fill="#00FF88" font-size="10" text-anchor="middle">MOBILE &amp; ANDROID</text>

  <!-- GAMMA -->
  <circle cx="775" cy="100" r="14" fill="#FF007F" filter="url(#glow)" opacity="0.8"/>
  <text x="775" y="130" fill="#FF007F" font-size="10" text-anchor="middle">PLATFORMS &amp; WEB</text>

  <!-- DELTA -->
  <circle cx="775" cy="400" r="14" fill="#FFB800" filter="url(#glow)" opacity="0.8"/>
  <text x="775" y="380" fill="#FFB800" font-size="10" text-anchor="middle">SYSTEMS &amp; CLI</text>

  <!-- ALPHA Projects -->
  <circle cx="90" cy="60" r="4" fill="#00F0FF"/><text x="90" y="52" fill="#7E9EB8" font-size="9" text-anchor="middle">WhatsappSpam</text>
  <circle cx="160" cy="155" r="4" fill="#00F0FF"/><text x="160" y="170" fill="#7E9EB8" font-size="9" text-anchor="middle">WhatsappForward</text>
  <circle cx="250" cy="55" r="4" fill="#00F0FF"/><text x="250" y="47" fill="#7E9EB8" font-size="9" text-anchor="middle">Jadu</text>
  <circle cx="80" cy="155" r="4" fill="#00F0FF"/><text x="80" y="170" fill="#7E9EB8" font-size="9" text-anchor="middle">GmailAutoMailMerge</text>

  <!-- BETA Projects -->
  <circle cx="90" cy="350" r="4" fill="#00FF88"/><text x="90" y="342" fill="#7E9EB8" font-size="9" text-anchor="middle">ChupChap</text>
  <circle cx="170" cy="430" r="4" fill="#00FF88"/><text x="170" y="445" fill="#7E9EB8" font-size="9" text-anchor="middle">Woof-App</text>
  <circle cx="260" cy="380" r="4" fill="#00FF88"/><text x="260" y="372" fill="#7E9EB8" font-size="9" text-anchor="middle">Dice-App</text>
  <circle cx="90" cy="440" r="4" fill="#00FF88"/><text x="90" y="455" fill="#7E9EB8" font-size="9" text-anchor="middle">Tip-Calculator</text>

  <!-- GAMMA Projects -->
  <circle cx="690" cy="55" r="4" fill="#FF007F"/><text x="690" y="47" fill="#7E9EB8" font-size="9" text-anchor="middle">Jagha</text>
  <circle cx="780" cy="155" r="4" fill="#FF007F"/><text x="780" y="170" fill="#7E9EB8" font-size="9" text-anchor="middle">Volia</text>
  <circle cx="870" cy="60" r="4" fill="#FF007F"/><text x="870" y="52" fill="#7E9EB8" font-size="9" text-anchor="middle">Volia-Backend</text>
  <circle cx="850" cy="155" r="4" fill="#FF007F"/><text x="850" y="170" fill="#7E9EB8" font-size="9" text-anchor="middle">iNotebook</text>
  <circle cx="700" cy="155" r="4" fill="#FF007F"/><text x="700" y="170" fill="#7E9EB8" font-size="9" text-anchor="middle">portfolio</text>

  <!-- DELTA Projects -->
  <circle cx="700" cy="380" r="4" fill="#FFB800"/><text x="700" y="372" fill="#7E9EB8" font-size="9" text-anchor="middle">wacli_window</text>
  <circle cx="780" cy="430" r="4" fill="#FFB800"/><text x="780" y="445" fill="#7E9EB8" font-size="9" text-anchor="middle">Soundboard</text>
  <circle cx="870" cy="370" r="4" fill="#FFB800"/><text x="870" y="362" fill="#7E9EB8" font-size="9" text-anchor="middle">Games_2D_C</text>
</svg>"""

# ----------------- Banners Generation -----------------
def generate_banner(name, desc, color):
    return f"""<svg width="950" height="42" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 42">
  {SHARED_DEFS}
  <rect width="950" height="42" fill="#0A1628" rx="4"/>
  <rect width="950" height="42" fill="url(#grid)" rx="4" opacity="0.6"/>
  <polygon points="15,21 21,15 27,21 21,27" fill="{color}" filter="url(#glow)"/>
  <text x="40" y="25" fill="{color}" font-size="12" font-weight="bold">── ◆ SECTOR // {name.upper()} ── {desc.upper()}</text>
  <line x1="450" y1="21" x2="930" y2="21" stroke="{color}" stroke-width="1" opacity="0.4"/>
  <text x="930" y="35" fill="#3D5675" font-size="8" text-anchor="end">SYS_{name.upper()}_0x88</text>
</svg>"""

svg_alpha = generate_banner("ALPHA", "BROWSER & MV3 INTERCEPTION", "#00F0FF")
svg_beta = generate_banner("BETA", "MOBILE & ANDROID EXPERIMENTS", "#00FF88")
svg_gamma = generate_banner("GAMMA", "PLATFORMS & WEB INFRASTRUCTURE", "#FF007F")
svg_delta = generate_banner("DELTA", "SYSTEMS & CLI TOOLS", "#FFB800")

# ----------------- SVG 8: dossier-browser.svg -----------------
svg_dossier_browser = f"""<svg width="950" height="160" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 160">
  {SHARED_DEFS}
  <rect width="950" height="160" fill="#0A1628" rx="8" stroke="#152238" stroke-width="1"/>
  <rect width="950" height="160" fill="url(#grid)" rx="8" opacity="0.5"/>
  {make_corners(950, 160)}
  
  <!-- Pipelines -->
  <g transform="translate(45, 30)">
    <!-- Stage 1 -->
    <rect width="240" height="100" fill="#050A12" rx="6" stroke="#00F0FF" stroke-width="1"/>
    <text x="120" y="25" fill="#00F0FF" font-size="12" font-weight="bold" text-anchor="middle">CONTENT SCRIPT ENGINE</text>
    <circle cx="15" cy="50" r="3" fill="#7E9EB8"/><text x="25" y="54" fill="#E2E8F0" font-size="10">State Sync &amp; Dispatch</text>
    <circle cx="15" cy="70" r="3" fill="#7E9EB8"/><text x="25" y="74" fill="#E2E8F0" font-size="10">Background Comm (MV3)</text>
    <circle cx="15" cy="90" r="3" fill="#7E9EB8"/><text x="25" y="94" fill="#E2E8F0" font-size="10">Target App Context</text>

    <!-- Arrow 1 -->
    <path class="pulseBeam" d="M 250 50 L 310 50" fill="none" stroke="#7B2FFF" stroke-width="2" stroke-dasharray="10 5"/>
    <polygon points="310,47 316,50 310,53" fill="#7B2FFF"/>

    <!-- Stage 2 -->
    <rect x="320" y="0" width="240" height="100" fill="#050A12" rx="6" stroke="#7B2FFF" stroke-width="1"/>
    <text x="440" y="25" fill="#7B2FFF" font-size="12" font-weight="bold" text-anchor="middle">HOOK INJECTOR / DOM</text>
    <circle cx="335" cy="50" r="3" fill="#7E9EB8"/><text x="345" y="54" fill="#E2E8F0" font-size="10">Mutation Observers</text>
    <circle cx="335" cy="70" r="3" fill="#7E9EB8"/><text x="345" y="74" fill="#E2E8F0" font-size="10">Event Interception</text>
    <circle cx="335" cy="90" r="3" fill="#7E9EB8"/><text x="345" y="94" fill="#E2E8F0" font-size="10">UI Node Injection</text>

    <!-- Arrow 2 -->
    <path class="pulseBeam" d="M 570 50 L 630 50" fill="none" stroke="#00F0FF" stroke-width="2" stroke-dasharray="10 5"/>
    <polygon points="630,47 636,50 630,53" fill="#00F0FF"/>

    <!-- Stage 3 -->
    <rect x="640" y="0" width="220" height="100" fill="#050A12" rx="6" stroke="#00F0FF" stroke-width="1"/>
    <text x="750" y="25" fill="#00F0FF" font-size="12" font-weight="bold" text-anchor="middle">TARGET PROTOCOL STACK</text>
    <circle cx="655" cy="50" r="3" fill="#7E9EB8"/><text x="665" y="54" fill="#E2E8F0" font-size="10">WebSocket Override</text>
    <circle cx="655" cy="70" r="3" fill="#7E9EB8"/><text x="665" y="74" fill="#E2E8F0" font-size="10">XHR / Fetch Hooking</text>
  </g>
</svg>"""

# ----------------- SVG 9: dossier-mobile.svg -----------------
svg_dossier_mobile = f"""<svg width="950" height="160" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 160">
  {SHARED_DEFS}
  <rect width="950" height="160" fill="#0A1628" rx="8" stroke="#152238" stroke-width="1"/>
  <rect width="950" height="160" fill="url(#grid)" rx="8" opacity="0.5"/>
  {make_corners(950, 160)}
  
  <g transform="translate(45, 30)">
    <!-- Stage 1 -->
    <rect width="240" height="100" fill="#050A12" rx="6" stroke="#00FF88" stroke-width="1"/>
    <text x="120" y="25" fill="#00FF88" font-size="12" font-weight="bold" text-anchor="middle">HARDWARE KEY EVENTS</text>
    <circle cx="15" cy="50" r="3" fill="#7E9EB8"/><text x="25" y="54" fill="#E2E8F0" font-size="10">Volume Rocker Hooks</text>
    <circle cx="15" cy="70" r="3" fill="#7E9EB8"/><text x="25" y="74" fill="#E2E8F0" font-size="10">Broadcast Receivers</text>

    <!-- Arrow 1 -->
    <path class="pulseBeam" d="M 250 50 L 310 50" fill="none" stroke="#FFB800" stroke-width="2" stroke-dasharray="10 5"/>
    <polygon points="310,47 316,50 310,53" fill="#FFB800"/>

    <!-- Stage 2 -->
    <rect x="320" y="0" width="240" height="100" fill="#050A12" rx="6" stroke="#FFB800" stroke-width="1"/>
    <text x="440" y="25" fill="#FFB800" font-size="12" font-weight="bold" text-anchor="middle">FOREGROUND SERVICE</text>
    <circle cx="335" cy="50" r="3" fill="#7E9EB8"/><text x="345" y="54" fill="#E2E8F0" font-size="10">Persistent Execution</text>
    <circle cx="335" cy="70" r="3" fill="#7E9EB8"/><text x="345" y="74" fill="#E2E8F0" font-size="10">WakeLocks &amp; State</text>
    <circle cx="335" cy="90" r="3" fill="#7E9EB8"/><text x="345" y="94" fill="#E2E8F0" font-size="10">Notification Bypass</text>

    <!-- Arrow 2 -->
    <path class="pulseBeam" d="M 570 50 L 630 50" fill="none" stroke="#00FF88" stroke-width="2" stroke-dasharray="10 5"/>
    <polygon points="630,47 636,50 630,53" fill="#00FF88"/>

    <!-- Stage 3 -->
    <rect x="640" y="0" width="220" height="100" fill="#050A12" rx="6" stroke="#00FF88" stroke-width="1"/>
    <text x="750" y="25" fill="#00FF88" font-size="12" font-weight="bold" text-anchor="middle">CAMERAX HEADLESS WORKER</text>
    <circle cx="655" cy="50" r="3" fill="#7E9EB8"/><text x="665" y="54" fill="#E2E8F0" font-size="10">Stealth Capture Matrix</text>
    <circle cx="655" cy="70" r="3" fill="#7E9EB8"/><text x="665" y="74" fill="#E2E8F0" font-size="10">Image Analysis Core</text>
  </g>
</svg>"""

# ----------------- SVG 10: tech-matrix.svg -----------------
def make_pill(x, y, text, color):
    return f"""<rect x="{x}" y="{y}" width="{len(text)*8 + 20}" height="24" fill="#050A12" rx="12" stroke="{color}" stroke-width="1"/>
               <text x="{x + (len(text)*8 + 20)/2}" y="{y+16}" fill="{color}" font-size="11" text-anchor="middle">{text}</text>"""

svg_matrix = f"""<svg width="950" height="260" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 260">
  {SHARED_DEFS}
  <rect width="950" height="260" fill="#050A12" rx="8"/>
  <rect width="950" height="260" fill="url(#grid)" rx="8" opacity="0.6"/>
  {make_corners(950, 260)}

  <!-- L4 -->
  <g transform="translate(45, 30)">
    <rect width="860" height="40" fill="#0A1628" rx="4"/>
    <rect width="4" height="40" fill="#00F0FF" rx="2"/>
    <text x="20" y="25" fill="#00F0FF" font-size="12" font-weight="bold">L4 // INTERFACE</text>
    {make_pill(160, 8, 'React.js', '#E2E8F0')}
    {make_pill(250, 8, 'Next.js', '#E2E8F0')}
    {make_pill(330, 8, 'Vite', '#E2E8F0')}
    {make_pill(390, 8, 'Tailwind CSS', '#E2E8F0')}
    {make_pill(510, 8, 'Jetpack Compose', '#E2E8F0')}
  </g>

  <!-- L3 -->
  <g transform="translate(45, 80)">
    <rect width="860" height="40" fill="#0A1628" rx="4"/>
    <rect width="4" height="40" fill="#7B2FFF" rx="2"/>
    <text x="20" y="25" fill="#7B2FFF" font-size="12" font-weight="bold">L3 // INTERCEPTION</text>
    {make_pill(180, 8, 'Chrome MV3', '#E2E8F0')}
    {make_pill(280, 8, 'DOM Mutation', '#E2E8F0')}
    {make_pill(390, 8, 'Protocol Hooks', '#E2E8F0')}
    {make_pill(510, 8, 'CameraX API', '#E2E8F0')}
  </g>

  <!-- L2 -->
  <g transform="translate(45, 130)">
    <rect width="860" height="40" fill="#0A1628" rx="4"/>
    <rect width="4" height="40" fill="#00FF88" rx="2"/>
    <text x="20" y="25" fill="#00FF88" font-size="12" font-weight="bold">L2 // SERVICES</text>
    {make_pill(150, 8, 'TypeScript', '#E2E8F0')}
    {make_pill(250, 8, 'Node.js', '#E2E8F0')}
    {make_pill(330, 8, 'Express', '#E2E8F0')}
    {make_pill(410, 8, 'MongoDB', '#E2E8F0')}
    {make_pill(490, 8, 'REST / JWT', '#E2E8F0')}
  </g>

  <!-- L1 -->
  <g transform="translate(45, 180)">
    <rect width="860" height="40" fill="#0A1628" rx="4"/>
    <rect width="4" height="40" fill="#FF007F" rx="2"/>
    <text x="20" y="25" fill="#FF007F" font-size="12" font-weight="bold">L1 // RUNTIME</text>
    {make_pill(150, 8, 'Go', '#E2E8F0')}
    {make_pill(190, 8, 'Rust / Tauri', '#E2E8F0')}
    {make_pill(300, 8, 'C/C++', '#E2E8F0')}
    {make_pill(370, 8, 'Kotlin', '#E2E8F0')}
    {make_pill(440, 8, 'Win32 API', '#E2E8F0')}
  </g>
</svg>"""

# ----------------- SVG 11: footer-uplink.svg -----------------
svg_footer = f"""<svg width="950" height="130" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 130">
  {SHARED_DEFS}
  <rect width="950" height="130" fill="#0A1628" rx="8"/>
  <rect width="950" height="130" fill="url(#grid)" rx="8" opacity="0.6"/>
  {make_corners(950, 130)}
  
  <rect x="0" y="0" width="950" height="2" fill="url(#grad-end)"/>
  
  <text x="475" y="60" fill="#00F0FF" font-size="16" font-weight="bold" text-anchor="middle" filter="url(#glow)">// END_TRANSMISSION: UPLINK CHANNELS STANDBY</text>
  
  <g transform="translate(475, 85)">
    <text x="-15" y="0" fill="#7E9EB8" font-size="12" text-anchor="middle">STATUS: LISTENING ON PORT 443</text>
    <rect x="110" y="-10" width="10" height="12" fill="#00FF88" class="blinkDot"/>
  </g>
  
  <text x="45" y="115" fill="#3D5675" font-size="10">HASH: 0x9F4B2C_VALIDATED</text>
  <text x="905" y="115" fill="#3D5675" font-size="10" text-anchor="end">ATTRIBUTION: SYS_CORE_MAINFRAME</text>
</svg>"""


# Write all files
write_svg('header-core.svg', svg_header)
write_svg('operator-core.svg', svg_operator)
write_svg('sector-constellation.svg', svg_constellation)
write_svg('sector-alpha.svg', svg_alpha)
write_svg('sector-beta.svg', svg_beta)
write_svg('sector-gamma.svg', svg_gamma)
write_svg('sector-delta.svg', svg_delta)
write_svg('dossier-browser.svg', svg_dossier_browser)
write_svg('dossier-mobile.svg', svg_dossier_mobile)
write_svg('tech-matrix.svg', svg_matrix)
write_svg('footer-uplink.svg', svg_footer)

print("ALL ASSETS GENERATED")
