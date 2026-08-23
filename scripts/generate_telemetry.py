#!/usr/bin/env python3
"""
Telemetry Engine for Yasir Amin Brohi's GitHub Profile Operating System
Fetches live GitHub metrics and generates assets/telemetry-live.svg
"""
import urllib.request
import json
import os
import datetime

USERNAME = "YasirAminBrohi"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def main():
    user_data = fetch_json(f"https://api.github.com/users/{USERNAME}") or {}
    repos_data = fetch_json(f"https://api.github.com/users/{USERNAME}/repos?per_page=100") or []

    public_repos = user_data.get('public_repos', 22)
    followers = user_data.get('followers', 7)
    
    total_stars = sum(r.get('stargazers_count', 0) for r in repos_data) if repos_data else 2
    total_forks = sum(r.get('forks_count', 0) for r in repos_data) if repos_data else 1
    
    languages = {}
    for r in repos_data:
        lang = r.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    top_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:4]
    dominant_lang = top_langs[0][0] if top_langs else "TypeScript"
    lang_pills = " • ".join([f"{l[0]} ({l[1]})" for l in top_langs]) if top_langs else "TypeScript • Kotlin • Go • Rust"

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    svg_content = f"""<svg width="950" height="220" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 220">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#0F1D30" stroke-width="1" opacity="0.8"/>
    </pattern>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <style>
    text {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .blinkDot {{ animation: blink 1.5s ease-in-out infinite alternate; }}
    @keyframes blink {{ 0% {{ opacity: 0.2; }} 100% {{ opacity: 1; }} }}
  </style>

  <rect width="950" height="220" fill="#0A1628" rx="8" stroke="#152238" stroke-width="2"/>
  <rect width="950" height="220" fill="url(#grid)" rx="8" opacity="0.7"/>

  <!-- Corner Brackets -->
  <path d="M 15 35 L 15 15 L 35 15" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
  <path d="M 915 15 L 935 15 L 935 35" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
  <path d="M 15 185 L 15 205 L 35 205" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>
  <path d="M 915 205 L 935 205 L 935 185" fill="none" stroke="#00F0FF" stroke-width="2" filter="url(#glow)"/>

  <!-- Top Status -->
  <text x="45" y="38" fill="#00FF88" font-size="13" font-weight="bold">⚡ SYSTEM TELEMETRY // REAL-TIME MONITOR</text>
  <circle class="blinkDot" cx="420" cy="34" r="4" fill="#00FF88" filter="url(#glow)"/>
  <text x="905" y="38" fill="#4B6A8A" font-size="10" text-anchor="end">SYNC_TIME: {timestamp}</text>

  <!-- 4 Telemetry Instrumentation Boxes -->
  <!-- Box 1 -->
  <g transform="translate(45, 60)">
    <rect width="195" height="95" rx="6" fill="#050A12" stroke="#1c2d47" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="95" fill="#00F0FF" rx="2"/>
    <text x="18" y="26" fill="#577899" font-size="10" font-weight="bold">ACTIVE REPOSITORIES</text>
    <text x="18" y="60" fill="#00F0FF" font-size="24" font-weight="bold" filter="url(#glow)">{public_repos}</text>
    <text x="18" y="80" fill="#3D5675" font-size="9">VERIFIED CODE BASES</text>
  </g>

  <!-- Box 2 -->
  <g transform="translate(265, 60)">
    <rect width="195" height="95" rx="6" fill="#050A12" stroke="#1c2d47" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="95" fill="#FF007F" rx="2"/>
    <text x="18" y="26" fill="#577899" font-size="10" font-weight="bold">SIGNAL STARGAZERS</text>
    <text x="18" y="60" fill="#FF007F" font-size="24" font-weight="bold" filter="url(#glow)">{total_stars} ★</text>
    <text x="18" y="80" fill="#3D5675" font-size="9">COMMUNITY SIGNALS</text>
  </g>

  <!-- Box 3 -->
  <g transform="translate(485, 60)">
    <rect width="195" height="95" rx="6" fill="#050A12" stroke="#1c2d47" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="95" fill="#7B2FFF" rx="2"/>
    <text x="18" y="26" fill="#577899" font-size="10" font-weight="bold">NETWORK PEERS</text>
    <text x="18" y="60" fill="#7B2FFF" font-size="24" font-weight="bold" filter="url(#glow)">{followers}</text>
    <text x="18" y="80" fill="#3D5675" font-size="9">CONNECTED DEVELOPERS</text>
  </g>

  <!-- Box 4 -->
  <g transform="translate(705, 60)">
    <rect width="200" height="95" rx="6" fill="#050A12" stroke="#1c2d47" stroke-width="1.2"/>
    <rect x="0" y="0" width="4" height="95" fill="#00FF88" rx="2"/>
    <text x="18" y="26" fill="#577899" font-size="10" font-weight="bold">DOMINANT CODE BASE</text>
    <text x="18" y="55" fill="#00FF88" font-size="14" font-weight="bold">{dominant_lang}</text>
    <text x="18" y="78" fill="#3D5675" font-size="8.5">{lang_pills[:28]}</text>
  </g>

  <!-- Bottom Diagnostics -->
  <text x="45" y="195" fill="#3D5675" font-size="9">ENGINE: GITHUB_ACTIONS_CRON</text>
  <text x="475" y="195" fill="#3D5675" font-size="9" text-anchor="middle">TARGET: @YasirAminBrohi // PRODUCTION</text>
  <text x="905" y="195" fill="#3D5675" font-size="9" text-anchor="end">INTEGRITY: 100% OPERATIONAL</text>
</svg>"""

    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    out_path = os.path.join(assets_dir, "telemetry-live.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print("Telemetry SVG generated successfully!")

if __name__ == "__main__":
    main()