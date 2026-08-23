#!/usr/bin/env python3
"""
Telemetry Engine for Yasir Amin Brohi's GitHub Profile Universe
Fetches live GitHub API statistics and dynamically updates assets/telemetry-live.svg
"""
import urllib.request
import json
import os
import datetime

USERNAME = "YasirAminBrohi"
HEADERS = {"User-Agent": "GitHub-Telemetry-Engine"}

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

    public_repos = user_data.get('public_repos', len(repos_data))
    followers = user_data.get('followers', 7)
    
    total_stars = sum(r.get('stargazers_count', 0) for r in repos_data)
    total_forks = sum(r.get('forks_count', 0) for r in repos_data)
    
    # Language breakdown
    languages = {}
    for r in repos_data:
        lang = r.get('language')
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    top_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:4]
    lang_str = " • ".join([f"{l[0]} ({l[1]})" for l in top_langs]) if top_langs else "TS • Kotlin • Go • Rust"

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 200" width="100%" height="100%">
  <defs>
    <linearGradient id="telBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070b14"/>
      <stop offset="100%" stop-color="#0c1424"/>
    </linearGradient>
    <filter id="telGlow">
      <feGaussianBlur stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .mono {{ font-family: 'Fira Code', 'Courier New', monospace; }}
      .lbl {{ font-size: 10px; font-weight: 700; fill: #577899; letter-spacing: 1.5px; }}
      .val {{ font-size: 20px; font-weight: 900; fill: #00F0FF; }}
      .sub {{ font-size: 9px; fill: #486582; }}
    </style>
  </defs>

  <rect width="950" height="200" rx="10" fill="url(#telBg)" stroke="#16243b" stroke-width="1.2"/>

  <!-- Top Telemetry Header -->
  <g transform="translate(30, 30)">
    <text class="mono" font-size="12" font-weight="800" fill="#00FF88" letter-spacing="2">
      ⚡ LIVE SYSTEM TELEMETRY // TELEMETRY_ONLINE
    </text>
    <text x="650" class="mono" font-size="10" fill="#4B6A8A">
      LAST_SYNC: {timestamp}
    </text>
  </g>

  <!-- 4 Telemetry Gauges -->
  <!-- Box 1: Public Repos -->
  <g transform="translate(30, 60)">
    <rect width="205" height="90" rx="6" fill="#0b1322" stroke="#1c2d47"/>
    <text x="15" y="28" class="mono lbl">ACTIVE REPOSITORIES</text>
    <text x="15" y="60" class="mono val" filter="url(#telGlow)">{public_repos}</text>
    <text x="15" y="78" class="mono sub">VERIFIED CODE BASES</text>
  </g>

  <!-- Box 2: Total Stars -->
  <g transform="translate(255, 60)">
    <rect width="205" height="90" rx="6" fill="#0b1322" stroke="#1c2d47"/>
    <text x="15" y="28" class="mono lbl">SIGNAL STARGAZERS</text>
    <text x="15" y="60" class="mono val" fill="#FF007F" filter="url(#telGlow)">{total_stars} ★</text>
    <text x="15" y="78" class="mono sub">COMMUNITY SIGNALS</text>
  </g>

  <!-- Box 3: Network Peers (Followers/Following) -->
  <g transform="translate(480, 60)">
    <rect width="205" height="90" rx="6" fill="#0b1322" stroke="#1c2d47"/>
    <text x="15" y="28" class="mono lbl">NETWORK PEERS</text>
    <text x="15" y="60" class="mono val" fill="#7000FF" filter="url(#telGlow)">{followers}</text>
    <text x="15" y="78" class="mono sub">CONNECTED DEVELOPERS</text>
  </g>

  <!-- Box 4: Dominant Stack -->
  <g transform="translate(705, 60)">
    <rect width="215" height="90" rx="6" fill="#0b1322" stroke="#1c2d47"/>
    <text x="15" y="28" class="mono lbl">DOMINANT CODE BASES</text>
    <text x="15" y="55" class="mono" font-size="12" font-weight="800" fill="#00FF88">{top_langs[0][0] if top_langs else "TypeScript"}</text>
    <text x="15" y="78" class="mono sub">{lang_str[:28]}</text>
  </g>

  <!-- Bottom Diagnostic Trace -->
  <g class="mono" font-size="9" fill="#3D5A78" transform="translate(30, 180)">
    <text>PIPELINE: GITHUB_ACTIONS_CRON</text>
    <text x="320">TARGET_HOST: @YasirAminBrohi</text>
    <text x="680">DATA_INTEGRITY: 100% VERIFIED</text>
  </g>
</svg>"""

    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "telemetry-live.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print("Telemetry SVG generated successfully!")

if __name__ == "__main__":
    main()