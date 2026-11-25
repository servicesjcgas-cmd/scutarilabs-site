import os

os.makedirs('css', exist_ok=True)
os.makedirs('js', exist_ok=True)
os.makedirs('sdk/scutaricore', exist_ok=True)
os.makedirs('blog', exist_ok=True)

NAV = '''<nav class="site-nav">
  <div class="container nav-wrapper">
    <a href="/" class="brand-link">
      <svg class="brand-logo-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
      </svg>
      SCUTARILABS
    </a>
    <div class="nav-desktop">
      <ul class="nav-links-list">
        <li class="nav-item"><a href="/#apps">Apps</a></li>
        <li class="nav-item"><a href="/sdk/">SDKs</a></li>
        <li class="nav-item"><a href="/#architecture">Architecture</a></li>
        <li class="nav-item"><a href="/blog.html">Blog</a></li>
      </ul>
      <div class="nav-actions">
        <a href="mailto:support@scutarilabs.com?subject=Commercial%20Licensing%20Inquiry" class="btn btn-primary btn-sm">Commercial Licensing</a>
      </div>
    </div>
  </div>
</nav>'''

FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <h4>SCUTARILABS LTD</h4>
        <p>Zero-cloud, strictly on-device mobile security and counter-surveillance tools for high-risk operators and enterprise teams.</p>
        <p style="font-family: var(--font-mono); font-size: 0.78rem; color: var(--accent);">
          Registered in England & Wales <!-- TODO: Insert Companies House Number -->
        </p>
      </div>
      <div class="footer-col">
        <h5>Consumer Apps</h5>
        <ul class="footer-links-list">
          <li><a href="/travelsafe.html">Travel Safe AI</a></li>
          <li><a href="/roomclear.html">RoomClear</a></li>
          <li><a href="/stillnet.html">Stillnet</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Developer SDKs</h5>
        <ul class="footer-links-list">
          <li><a href="/sdk/">SDK Directory</a></li>
          <li><a href="/sdk/scutaricore/">ScutariCore SDK</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Company & Legal</h5>
        <ul class="footer-links-list">
          <li><a href="/blog.html">Blog</a></li>
          <li><a href="/contact.html">Contact & Support</a></li>
          <li><a href="/travelsafe-privacy.html">Privacy Policy</a></li>
          <li><a href="/travelsafe-terms.html">Terms & Compliance</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; 2026 ScutariLabs Ltd. All rights reserved. Zero external tracking scripts.</div>
      <div>Direct Contact: <a href="mailto:support@scutarilabs.com" style="color: var(--accent);">support@scutarilabs.com</a></div>
    </div>
  </div>
</footer>'''

def get_hero():
    return '''
  <header class="hero">
    <div class="container hero-inner">
      <div class="hero-pill">
        <span class="pill-dot"></span>
        Zero Outbound Telemetry &bull; 100% On-Device Engine
      </div>
      <h1>Strictly On-Device Security for <span class="highlight">Uncompromising Privacy.</span></h1>
      <p class="lead">
        Zero-cloud, air-gapped protection for solo travelers, field engineers, and enterprise lone workers operating in critical dead zones.
      </p>
      <div class="hero-ctas">
        <a href="/sdk/" class="btn btn-primary btn-lg">License Our SDKs (B2B) &rarr;</a>
        <a href="#apps" class="btn btn-outline btn-lg">Explore Consumer Apps</a>
      </div>
      <div class="hero-specs">
        <div class="spec-item"><svg class="spec-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Air-Gapped Local Inference</div>
        <div class="spec-item"><svg class="spec-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Volatile RAM Processing</div>
        <div class="spec-item"><svg class="spec-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> UK Private Limited Company</div>
      </div>
    </div>
  </header>'''

def get_apps():
    return '''
  <section id="apps">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">CONSUMER & OPERATOR APPLICATIONS</span>
        <h2>Tactical Security. Zero Cloud Dependencies.</h2>
        <p>Purpose-built applications engineered to run 100% offline using native smartphone sensor arrays.</p>
      </div>

      <div class="grid-3">
        <div class="app-card">
          <div class="card-top">
            <div>
              <h3 class="app-card-title">Travel Safe AI</h3>
              <div class="app-card-sub">Acoustic Guard & Stealth Alert</div>
            </div>
            <span class="badge badge-live"><span class="badge-pulse"></span> Live on Android</span>
          </div>
          <p class="app-card-body">
            Offline acoustic threat detection and earbud translation for solo travelers. Continuous local audio classification without streaming to external cloud servers.
          </p>
          <div class="device-mockup">
            <div class="mockup-header">
              <span>TRAVEL SAFE AI</span>
              <span style="color: var(--accent);">MONITORING ACTIVE</span>
            </div>
            <div class="mockup-visual">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
              <!-- TODO: Insert screenshot -->
              <span class="mockup-label">On-Device Edge ML Audio Classifier</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="/travelsafe.html" class="btn btn-secondary">View App &rarr;</a>
            <a href="<!-- TODO: Insert Google Play Store URL -->" class="btn btn-playstore">
              <svg class="btn-playstore-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M3 20.5v-17c0-.55.45-1 1-1 .2 0 .38.07.53.18l12.43 8.32a.98.98 0 0 1 0 1.64L4.53 20.97c-.15.11-.33.18-.53.18-.55 0-1-.45-1-1z"/></svg>
              <div>
                <span class="btn-playstore-text-sub">GET IT ON</span>
                <span class="btn-playstore-text-main">Google Play</span>
              </div>
            </a>
          </div>
        </div>

        <div class="app-card">
          <div class="card-top">
            <div>
              <h3 class="app-card-title">RoomClear</h3>
              <div class="app-card-sub">Tactical Bug-Sweeping</div>
            </div>
            <span class="badge badge-beta"><span class="badge-pulse"></span> Closed Beta</span>
          </div>
          <p class="app-card-body">
            Find hidden cameras and concealed surveillance devices in hotels and Airbnbs. Combines magnetometer sweeps, retro-reflective LED strobes, and BLE bloom filters.
          </p>
          <div class="device-mockup">
            <div class="mockup-header">
              <span>ROOMCLEAR SWEEP</span>
              <span style="color: var(--cyan);">TRI-SENSOR ACTIVE</span>
            </div>
            <div class="mockup-visual">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/></svg>
              <!-- TODO: Insert screenshot -->
              <span class="mockup-label">Optical Strobe & RF Lens Detector</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="/roomclear.html" class="btn btn-secondary">View App &rarr;</a>
          </div>
        </div>

        <div class="app-card">
          <div class="card-top">
            <div>
              <h3 class="app-card-title">Stillnet</h3>
              <div class="app-card-sub">LAN Vulnerability Scanner</div>
            </div>
            <span class="badge badge-dev"><span class="badge-pulse"></span> In Development</span>
          </div>
          <p class="app-card-body">
            100% offline local network vulnerability scanner and countermeasure utility. Map connected nodes and audit rogue access points with an air-gapped threat engine.
          </p>
          <div class="device-mockup">
            <div class="mockup-header">
              <span>STILLNET ARCH</span>
              <span style="color: var(--amber);">AIR-GAPPED ENGINE</span>
            </div>
            <div class="mockup-visual">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
              <!-- TODO: Insert screenshot -->
              <span class="mockup-label">Local Subnet Topology & Vulnerability Mapper</span>
            </div>
          </div>
          <div class="card-actions">
            <a href="/stillnet.html" class="btn btn-secondary">View App &rarr;</a>
          </div>
        </div>
      </div>
    </div>
  </section>'''

def get_arch_svg():
    return '''<div class="arch-svg-container">
  <svg viewBox="0 0 1000 320" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="10" width="620" height="300" rx="12" fill="#0b1018" stroke="#1a2638" stroke-width="2"/>
    <text x="30" y="40" fill="#00ea8d" font-family="monospace" font-size="12" font-weight="bold" letter-spacing="1">INSIDE PHYSICAL DEVICE (TRUST BOUNDARY)</text>

    <rect x="40" y="80" width="160" height="180" rx="8" fill="#0f1622" stroke="#233248" stroke-width="1.5"/>
    <text x="55" y="110" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">1. Hardware Sensors</text>
    <text x="55" y="140" fill="#8896a6" font-family="monospace" font-size="11">&bull; Microphone</text>
    <text x="55" y="165" fill="#8896a6" font-family="monospace" font-size="11">&bull; Magnetometer</text>
    <text x="55" y="190" fill="#8896a6" font-family="monospace" font-size="11">&bull; BLE / Wi-Fi Subnet</text>
    <text x="55" y="215" fill="#8896a6" font-family="monospace" font-size="11">&bull; Optical IR Lens</text>

    <path d="M200 170 L240 170" stroke="#00ea8d" stroke-width="2" stroke-dasharray="4 4"/>
    <polygon points="240,165 250,170 240,175" fill="#00ea8d"/>

    <rect x="250" y="80" width="170" height="180" rx="8" fill="#0f1622" stroke="#00ea8d" stroke-width="2"/>
    <text x="265" y="110" fill="#00ea8d" font-family="sans-serif" font-size="13" font-weight="bold">2. On-Device Engine</text>
    <text x="265" y="140" fill="#cbd5e1" font-family="monospace" font-size="11">&bull; ScutariCore RASP</text>
    <text x="265" y="165" fill="#cbd5e1" font-family="monospace" font-size="11">&bull; Edge AI / TFLite</text>
    <text x="265" y="190" fill="#cbd5e1" font-family="monospace" font-size="11">&bull; ADPF Thermal Gov.</text>
    <text x="265" y="215" fill="#cbd5e1" font-family="monospace" font-size="11">&bull; Local FFT Scoring</text>

    <path d="M420 170 L460 170" stroke="#00ea8d" stroke-width="2" stroke-dasharray="4 4"/>
    <polygon points="460,165 470,170 460,175" fill="#00ea8d"/>

    <rect x="470" y="80" width="140" height="180" rx="8" fill="#0f1622" stroke="#233248" stroke-width="1.5"/>
    <text x="485" y="110" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">3. Local Storage</text>
    <text x="485" y="140" fill="#8896a6" font-family="monospace" font-size="11">&bull; Ephemeral RAM</text>
    <text x="485" y="165" fill="#8896a6" font-family="monospace" font-size="11">&bull; AES-256 SQLite</text>
    <text x="485" y="190" fill="#8896a6" font-family="monospace" font-size="11">&bull; Ed25519 .lic</text>
    <text x="485" y="215" fill="#8896a6" font-family="monospace" font-size="11">&bull; PDF Audit Kit</text>

    <rect x="660" y="10" width="40" height="300" rx="6" fill="#1f0a10" stroke="#f43f5e" stroke-width="2"/>
    <text x="685" y="40" fill="#f43f5e" font-family="monospace" font-size="11" font-weight="bold" writing-mode="vertical-rl" letter-spacing="2">AIR-GAP BARRIER &bull; ZERO OUTBOUND TRAFFIC</text>

    <rect x="730" y="10" width="260" height="300" rx="12" fill="#080a0e" stroke="#1c2432" stroke-width="1.5" stroke-dasharray="6 6"/>
    <text x="750" y="40" fill="#4b5869" font-family="monospace" font-size="11" font-weight="bold">EXTERNAL INTERNET / SERVERS</text>
    <rect x="760" y="90" width="200" height="150" rx="8" fill="#0d1117" stroke="#1f2937"/>
    <text x="780" y="130" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold">NO Cloud APIs</text>
    <text x="780" y="160" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold">NO External Telemetry</text>
    <text x="780" y="190" fill="#f43f5e" font-family="sans-serif" font-size="13" font-weight="bold">NO Remote Logging</text>
  </svg>
</div>'''

def get_arch():
    svg = get_arch_svg()
    tmpl = '''
  <section id="architecture" class="arch-section">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">VERIFIABLE HARDWARE ARCHITECTURE</span>
        <h2>Zero-Cloud Privacy & Air-Gap Proof</h2>
        <p>Sensory data and security threat scores never leave your physical handset. Here is how our on-device trust boundary operates.</p>
      </div>

      <div class="arch-diagram-card">
        {{SVG}}
      </div>

      <div class="audit-strip">
        <div class="audit-card">
          <div class="audit-card-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.2c.3.4.8.5 1.3.3l.5-.3c.4-.2.6-.6.5-1.1z"/></svg>
          </div>
          <h3>1. Airplane Mode Test</h3>
          <p>Every feature&mdash;acoustic classification, bug sweeping, and network diagnostics&mdash;works identically in 100% offline airplane mode.</p>
        </div>

        <div class="audit-card">
          <div class="audit-card-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2"/><rect x="2" y="14" width="20" height="8" rx="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>
          </div>
          <h3>2. Volatile RAM Processing</h3>
          <p>Sensitive sensor buffers live ephemerally in RAM. Audio feeds and camera frames are instantly scrubbed without writing to storage.</p>
        </div>

        <div class="audit-card">
          <div class="audit-card-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h3>3. Zero-Cloud Architecture</h3>
          <p>Eliminates server data breaches, API latency, third-party analytics leaks, and recurring monthly cloud operational costs.</p>
        </div>
      </div>
    </div>
  </section>'''
    return tmpl.replace('{{SVG}}', svg)

def get_b2b():
    return '''
  <section class="b2b-section">
    <div class="container">
      <div class="b2b-box">
        <div class="b2b-copy">
          <span class="section-eyebrow">ENTERPRISE & FIELD SERVICE SOLUTIONS</span>
          <h2>Built for Duty of Care in Zero-Signal Zones.</h2>
          <p>
            Field service crews, utility engineers, housing inspectors, and high-risk travelers frequently operate in plant rooms, remote sites, and cellular dead zones where cloud-based safety platforms fail completely.
          </p>
          <ul class="b2b-points">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>100% Local Reliability:</strong> Emergency detection algorithms execute locally even when network access drops to 0 bars.</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Zero Corporate Data Leakage:</strong> Eliminate liability under UK GDPR & EU regulations by keeping employee audio and location off third-party servers.</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Custom Enterprise Licensing:</strong> Flexible deployment for private corporate fleets, defense teams, and white-label applications.</span>
            </li>
          </ul>
          <a href="mailto:support@scutarilabs.com?subject=Enterprise%20Lone-Worker%20Licensing" class="btn btn-primary btn-lg">Discuss Enterprise & White-Label Licensing &rarr;</a>
        </div>

        <div class="b2b-card-aside">
          <h3>Enterprise Resilience Metrics</h3>
          <p style="font-size: 0.88rem;">Designed to meet employer Duty of Care standards across regulated sectors.</p>
          <div class="duty-stat-grid">
            <div class="duty-stat">
              <span class="duty-stat-num">0 ms</span>
              <span class="duty-stat-label">Cloud Latency</span>
            </div>
            <div class="duty-stat">
              <span class="duty-stat-num">100%</span>
              <span class="duty-stat-label">Offline Capability</span>
            </div>
            <div class="duty-stat">
              <span class="duty-stat-num">Zero</span>
              <span class="duty-stat-label">External Telemetry</span>
            </div>
            <div class="duty-stat">
              <span class="duty-stat-num">Ed25519</span>
              <span class="duty-stat-label">Offline Licensing</span>
            </div>
          </div>
          <div style="font-family: var(--font-mono); font-size: 0.76rem; color: var(--text-dim); margin-top: 16px;">
            // SCUTARILABS ENTERPRISE COMPLIANCE KIT
          </div>
        </div>
      </div>
    </div>
  </section>'''

def build_index():
    hero = get_hero()
    apps = get_apps()
    arch = get_arch()
    b2b = get_b2b()
    tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ScutariLabs | Zero-Cloud Mobile Security & Counter-Surveillance</title>
  <meta name="description" content="Zero-cloud, strictly on-device mobile security, counter-surveillance tools, and Flutter SDKs for solo travelers and enterprise field teams.">
  <meta property="og:title" content="ScutariLabs | Zero-Cloud Mobile Security">
  <meta property="og:description" content="Building zero-cloud, strictly on-device safety and counter-surveillance tools for travelers and lone workers.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}
  {{HERO}}
  {{APPS}}
  {{ARCH}}
  {{B2B}}
  {{FOOTER}}
</body>
</html>'''
    page = tmpl.replace('{{NAV}}', NAV).replace('{{HERO}}', hero).replace('{{APPS}}', apps).replace('{{ARCH}}', arch).replace('{{B2B}}', b2b).replace('{{FOOTER}}', FOOTER)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(page)
    print("index.html written.")

def build_sdk_index():
    card_scutaricore = '''
      <a href="/sdk/scutaricore/" class="app-card" style="display: flex; flex-direction: column;">
        <div class="card-top">
          <div>
            <h3 class="app-card-title">ScutariCore SDK</h3>
            <div class="app-card-sub">Flutter / Dart &bull; Android ADPF &bull; RASP</div>
          </div>
          <span class="badge badge-live"><span class="badge-pulse"></span> Available</span>
        </div>
        <p class="app-card-body">
          Hardware profiling, Android ADPF thermal governor telemetry, volatile RAM scrubbing, and zero-telemetry audit primitives for Flutter applications. Dual-licensed for open-source and commercial teams.
        </p>
        <div style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--text-muted);">v1.0 Production-Ready</span>
          <span style="color: var(--accent); font-weight: 600;">View Technical Specs & Pricing &rarr;</span>
        </div>
      </a>'''

    card_upcoming = '''
      <div class="app-card" style="opacity: 0.65;">
        <div class="card-top">
          <div>
            <h3 class="app-card-title">Upcoming Security Modules</h3>
            <div class="app-card-sub">Local Audio AI & LAN Inspection</div>
          </div>
          <span class="badge badge-dev">In Development</span>
        </div>
        <p class="app-card-body">
          Additional on-device acoustic classification engines, ultrasonic sweep helpers, and offline network scanner primitives currently undergoing internal security audits.
        </p>
        <div style="margin-top: auto; padding-top: 16px; border-top: 1px solid var(--border);">
          <span style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--amber);">Coming Q1 2027</span>
        </div>
      </div>'''

    tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ScutariLabs | SDK Directory</title>
  <meta name="description" content="Zero-cloud, on-device Flutter & mobile SDKs by ScutariLabs." />
  <meta property="og:title" content="ScutariLabs | SDK Directory">
  <meta property="og:description" content="Drop-in, offline-first mobile SDKs built for hardware telemetry, security, and local AI execution.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="/css/main.css" />
</head>
<body>
  {{NAV}}

  <main class="container" style="padding-top: 60px; padding-bottom: 80px;">
    <header style="margin-bottom: 48px;">
      <span class="section-eyebrow">DEVELOPER LIBRARIES // ZERO-CLOUD ARCHITECTURE</span>
      <h1 style="margin-bottom: 12px;">ScutariLabs SDK Directory</h1>
      <p style="max-width: 680px; font-size: 1.1rem; color: var(--text-muted);">
        Drop-in, offline-first mobile SDKs built for hardware telemetry, security, and local AI execution&mdash;zero external API calls, zero recurring server dependencies.
      </p>
    </header>

    <div class="grid-2">
      {{CARD1}}
      {{CARD2}}
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''

def get_scutaricore_body():
    code_text = '''// pubspec.yaml: scutari_core: ^1.0.0
import 'package:scutari_core/scutari_core.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // 1. Hardware Profiling & Adaptive Model Router
  final profile = await ScutariProfiler.inspectDevice();
  final modelPath = ScutariProfiler.routeModel(
    profile: profile,
    lowTierModelPath: 'assets/model_int8.tflite',
    highTierModelPath: 'assets/model_fp16.tflite',
  );

  // 2. Hardware RASP & Screen Shielding
  await ScutariVault.setScreenShield(true);
  await ScutariVault.verifyDeviceIntegrity();

  // 3. Android ADPF Thermal Headroom Stream
  ScutariThermalGovernor.policyStream.listen((policy) {
    engine.setInferenceThreads(policy.maxInferenceThreads);
  });
}'''

    hero_sec = '''
    <section>
      <div class="container grid-2" style="align-items: center;">
        <div>
          <a href="/sdk/" style="font-family: var(--font-mono); font-size: 0.8rem; color: var(--accent); margin-bottom: 12px; display: inline-block;">&larr; ALL SDKS</a>
          <div class="badge badge-live" style="margin-bottom: 16px;"><span class="badge-pulse"></span> v1.0 PRODUCTION-READY</div>
          <h1>Zero-Cloud Edge AI & RASP Infrastructure for Flutter.</h1>
          <p style="font-size: 1.1rem; margin-bottom: 24px;">
            Prevent OOM crashes, govern thermal throttling, and enforce strictly on-device security. Zero telemetry, zero external servers, and offline cryptographic licensing.
          </p>
          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="mailto:support@scutarilabs.com?subject=Commercial%20SDK%20Licensing%20Inquiry" class="btn btn-primary">Request Commercial License &rarr;</a>
            <a href="#dual-licensing" class="btn btn-outline">View Transparent Licensing</a>
          </div>
        </div>

        <div class="terminal-block">
          <div class="terminal-header">
            <div class="terminal-dots">
              <span class="dot dot-red"></span>
              <span class="dot dot-yellow"></span>
              <span class="dot dot-green"></span>
            </div>
            <span>scutari_core.dart // 100% Local Execution</span>
            <button class="copy-btn" id="copyBtn">COPY</button>
          </div>
          <pre class="code-pre" id="codeBlock"><code>{{CODE}}</code></pre>
        </div>
      </div>
    </section>'''.replace('{{CODE}}', code_text)

    bench_sec = '''
    <section style="padding: 40px 0; background: var(--bg-secondary);">
      <div class="container">
        <div class="benchmarks-bar">
          <div class="benchmark-col">
            <span class="benchmark-val">&lt; 18ms</span>
            <div class="benchmark-name">Local Inference Latency</div>
            <div class="benchmark-desc">On-device acoustic classification on mid-range ARM NPU</div>
          </div>
          <div class="benchmark-col">
            <span class="benchmark-val">&lt; 1ms</span>
            <div class="benchmark-name">Offline Key Verification</div>
            <div class="benchmark-desc">Ed25519 local cryptographic license verification</div>
          </div>
        </div>
      </div>
    </section>'''

    return hero_sec + bench_sec

def build_scutaricore():
    body = get_scutaricore_body()
    license_sec = '''
    <section id="dual-licensing">
      <div class="container">
        <div class="section-header">
          <span class="section-eyebrow">TRANSPARENT LICENSING</span>
          <h2>Open Source Evaluation vs. Commercial License</h2>
          <p>Predictable pricing with zero license server phone-home calls verified 100% offline.</p>
        </div>

        <div class="licensing-table-card">
          <div class="licensing-grid">
            <div class="licensing-col">
              <span class="badge badge-dev">OPEN SOURCE / EVALUATION</span>
              <h3>GPLv3 License</h3>
              <div class="licensing-price">&pound;0 <span>/ forever</span></div>
              <p style="font-size: 0.88rem;">Free for non-commercial open-source applications, internal testing, and academic research.</p>
              <ul class="licensing-list">
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Full access to open-core Dart/Flutter source</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Device Hardware Profiler & Model Router</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Community GitHub issue tracker support</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Copyleft GPLv3 compliance required</li>
              </ul>
              <a href="mailto:support@scutarilabs.com?subject=GPLv3%20Evaluation%20Inquiry" class="btn btn-outline">Evaluate Open-Core</a>
            </div>

            <div class="licensing-col featured">
              <span class="badge badge-live">COMMERCIAL ENTERPRISE</span>
              <h3>Commercial Royalty-Free</h3>
              <div class="licensing-price">&pound;349 <span>/ month (or &pound;3,500 / year)</span></div>
              <p style="font-size: 0.88rem;">Flat fee for proprietary, closed-source commercial Flutter & Android applications.</p>
              <ul class="licensing-list">
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Android ADPF Thermal & Battery Headroom Governor</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Zero-Telemetry Vault, RASP & Offline PDF Audit Kit</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Zero Copyleft Obligations (Closed-source clean)</li>
                <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Priority Next-Business-Day Engineering Support SLA</li>
              </ul>
              <a href="mailto:support@scutarilabs.com?subject=Commercial%20SDK%20License" class="btn btn-primary">Request Commercial License &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>'''

    tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ScutariCore SDK | Zero-Cloud Edge AI & RASP Infrastructure</title>
  <meta name="description" content="Zero-cloud edge AI and RASP infrastructure for Flutter. Hardware profiling, Android ADPF thermal governing, and zero-telemetry security primitives." />
  <meta property="og:title" content="ScutariCore SDK | ScutariLabs">
  <meta property="og:description" content="Hardware profiling, thermal governor telemetry, and offline sensor security primitives for Flutter and Android.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="/css/main.css" />
</head>
<body>
  {{NAV}}

  <main>
    {{BODY}}
    {{LICENSE}}
  </main>

  {{FOOTER}}

  <script>
    document.getElementById('copyBtn').addEventListener('click', function() {
      const code = document.getElementById('codeBlock').innerText;
      navigator.clipboard.writeText(code).then(() => {
        this.textContent = 'COPIED!';
        setTimeout(() => this.textContent = 'COPY', 2000);
      });
    });
  </script>
</body>
</html>'''

    page = tmpl.replace('{{NAV}}', NAV).replace('{{BODY}}', body).replace('{{LICENSE}}', license_sec).replace('{{FOOTER}}', FOOTER)
    with open('sdk/scutaricore/index.html', 'w', encoding='utf-8') as f:
        f.write(page)
    print("sdk/scutaricore/index.html generated.")

def build_travelsafe():
    ts_tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Travel Safe AI | ScutariLabs</title>
  <meta name="description" content="Offline acoustic threat detection and earbud translation for solo travelers by ScutariLabs.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 860px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 24px;">
      <div>
        <span class="section-eyebrow">PERSONAL SAFETY NET // OFFLINE GUARDIAN</span>
        <h1>Travel Safe AI</h1>
      </div>
      <span class="badge badge-live"><span class="badge-pulse"></span> Live on Android</span>
    </div>

    <p class="lead" style="margin-bottom: 24px;"><strong>Your Personal Safety Net. Offline. Private. Always On.</strong></p>
    <p style="margin-bottom: 32px;">
      Most safety apps trade your privacy for protection, constantly streaming your location and ambient audio to corporate cloud servers. Travel Safe AI flips the script. Using advanced on-device audio classification, your phone acts as an independent guardian.
    </p>

    <div class="card-actions" style="margin-bottom: 40px; flex-direction: row;">
      <a href="<!-- TODO: Insert Google Play Store URL -->" class="btn btn-playstore">
        <svg class="btn-playstore-icon" viewBox="0 0 24 24" fill="currentColor"><path d="M3 20.5v-17c0-.55.45-1 1-1 .2 0 .38.07.53.18l12.43 8.32a.98.98 0 0 1 0 1.64L4.53 20.97c-.15.11-.33.18-.53.18-.55 0-1-.45-1-1z"/></svg>
        <div>
          <span class="btn-playstore-text-sub">GET IT ON</span>
          <span class="btn-playstore-text-main">Google Play</span>
        </div>
      </a>
    </div>

    <h2 style="margin-bottom: 16px;">Core Architecture</h2>
    <ul class="licensing-list" style="margin-bottom: 40px;">
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Zero Cloud Tracking:</strong> Your location and audio data never touch an external server. Everything stays securely sandboxed on your physical device.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>100% Offline Capable:</strong> No signal? No problem. Core safety triggers and acoustic monitoring run entirely via Edge AI without needing cellular data.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Stealth Routing:</strong> Dynamic audio-to-haptic switching whispers alerts into your Bluetooth earbuds, or uses silent vibration patterns if none are connected.</span></li>
    </ul>

    <div style="padding-top: 24px; border-top: 1px solid var(--border); display: flex; gap: 16px;">
      <a href="/travelsafe-privacy.html" class="btn btn-outline btn-sm">TSAI Privacy Policy</a>
      <a href="/travelsafe-terms.html" class="btn btn-outline btn-sm">TSAI Terms & Conditions</a>
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''

    page_ts = ts_tmpl.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('travelsafe.html', 'w', encoding='utf-8') as f:
        f.write(page_ts)
    print("travelsafe.html generated.")

def build_roomclear():
    rc_tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>RoomClear | ScutariLabs</title>
  <meta name="description" content="Tactical bug-sweeping and hidden camera detection using local hardware sensors by ScutariLabs.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 860px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 24px;">
      <div>
        <span class="section-eyebrow">COUNTER-SURVEILLANCE // TACTICAL SWEEP</span>
        <h1>RoomClear</h1>
      </div>
      <span class="badge badge-beta"><span class="badge-pulse"></span> Closed Beta</span>
    </div>

    <p class="lead" style="margin-bottom: 24px;"><strong>Tactical counter-surveillance and bug-sweeping tool. 100% on-device processing.</strong></p>
    <p style="margin-bottom: 32px;">
      Find hidden cameras in your Airbnb or hotel in 60 seconds. RoomClear leverages your smartphone&#39;s native hardware sensors to highlight magnetic, optical, and RF anomalies associated with concealed surveillance devices.
    </p>

    <h2 style="margin-bottom: 16px;">Hardware Level Sweeps</h2>
    <ul class="licensing-list" style="margin-bottom: 40px;">
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Tri-Sensor Sweep:</strong> Tap into the native magnetometer, high-contrast IR filters, and a BLE Bloom filter to cross-reference local anomalies against known IoT device signatures.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Retro-Reflective Strobe:</strong> Active optical lens hunting uses high-frequency LED pulses to highlight the specific light refraction of hidden, offline camera glass.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Edge ML Threat Profiler:</strong> AR bounding boxes automatically spot and highlight high-risk objects like smoke detectors, alarm clocks, and ventilation shafts.</span></li>
    </ul>

    <div style="padding-top: 24px; border-top: 1px solid var(--border); display: flex; gap: 16px;">
      <a href="/roomclear-privacy.html" class="btn btn-outline btn-sm">RoomClear Privacy Policy</a>
      <a href="/roomclear-terms.html" class="btn btn-outline btn-sm">RoomClear Terms & Conditions</a>
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''

    page_rc = rc_tmpl.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('roomclear.html', 'w', encoding='utf-8') as f:
        f.write(page_rc)
    print("roomclear.html generated.")

def build_stillnet():
    sn_tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Stillnet | ScutariLabs</title>
  <meta name="description" content="100% offline local network vulnerability scanner and active threat countermeasure utility by ScutariLabs.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 860px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 16px; margin-bottom: 24px;">
      <div>
        <span class="section-eyebrow">NETWORK DIAGNOSTICS // AIR-GAPPED VANGUARD</span>
        <h1>Stillnet</h1>
      </div>
      <span class="badge badge-dev"><span class="badge-pulse"></span> In Development</span>
    </div>

    <p class="lead" style="margin-bottom: 24px;"><strong>Your Local Network Vanguard. 100% Offline. Air-Gapped.</strong></p>
    <p style="margin-bottom: 32px;">
      Stillnet is a local network vulnerability scanner and active threat countermeasure utility. Designed for absolute privacy, it scans for malicious or vulnerable networks and allows you to deploy legally compliant countermeasures without harvesting your data or serving ads.
    </p>

    <h2 style="margin-bottom: 16px;">Core Architecture</h2>
    <ul class="licensing-list" style="margin-bottom: 40px;">
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Local Network Topology:</strong> Rapidly map connected devices and assess local subnets entirely on your device.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Offline Vulnerability Engine:</strong> Cross-reference discovered nodes against an air-gapped threat database to identify malicious intent without relying on cloud processing.</span></li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> <span><strong>Active Countermeasures:</strong> Deploy native security responses to shield your device from identified rogue networks or aggressive tracking.</span></li>
    </ul>

    <div style="padding-top: 24px; border-top: 1px solid var(--border); display: flex; gap: 16px;">
      <a href="/stillnet-privacy.html" class="btn btn-outline btn-sm">Stillnet Privacy Policy</a>
      <a href="/stillnet-terms.html" class="btn btn-outline btn-sm">Stillnet Terms of Service</a>
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''

    page_sn = sn_tmpl.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('stillnet.html', 'w', encoding='utf-8') as f:
        f.write(page_sn)
    print("stillnet.html generated.")

def build_ts_rc_policies():
    ts_priv = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Travel Safe AI | ScutariLabs</title>
  <meta name="description" content="Privacy Policy for Travel Safe AI and ScutariLabs Ltd applications. Zero-cloud, strictly on-device processing.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container prose" style="padding-top: 60px; padding-bottom: 80px; max-width: 820px;">
    <span class="section-eyebrow">PRIVACY POLICY // DATA SOVEREIGNTY</span>
    <h1>Travel Safe AI Privacy Policy</h1>
    <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); margin-bottom: 24px;">
      Effective Date: October 25, 2026 &bull; Developer Entity: ScutariLabs Ltd
    </div>

    <h2>1. Overview & Privacy Commitment</h2>
    <p>Applications developed by ScutariLabs Ltd ("we", "our", or "us") are built with an offline-first, zero-cloud architecture. We do not collect, transmit, track, or sell your personal data.</p>

    <h2>2. Sensitive Permissions & Local Sensor Processing</h2>
    <ul>
      <li><strong>Microphone (<code>RECORD_AUDIO</code>):</strong> Used exclusively for real-time acoustic analysis locally in device memory. Audio streams are never recorded to disk, never streamed to cloud servers, and never reviewed by humans.</li>
      <li><strong>Location (<code>ACCESS_FINE_LOCATION</code>):</strong> Processed strictly on-device to attach coordinates to user-initiated emergency alerts. We do not maintain or upload location histories.</li>
      <li><strong>Bluetooth & Routing:</strong> Used strictly to detect whether connected audio output routing (e.g., wireless earpieces) is active for alert delivery.</li>
    </ul>

    <h2>3. Data Retention and Deletion</h2>
    <p>Because no user data or voice recordings are uploaded to remote servers, there is no personal data held in cloud databases. Clearing the application&#39;s local storage or uninstalling the app permanently deletes all local configuration data.</p>

    <h2>4. Children&#39;s Privacy</h2>
    <p>Our applications are not directed to children under 13, and we do not knowingly collect personal data from minors.</p>

    <h2>5. Developer Support</h2>
    <div class="app-card">
      <p style="margin-bottom: 8px;"><strong>Entity:</strong> ScutariLabs Ltd</p>
      <p style="margin-bottom: 8px;"><strong>Support Email:</strong> <a href="mailto:support@scutarilabs.com">support@scutarilabs.com</a></p>
      <p style="margin-bottom: 0;"><strong>Web:</strong> https://scutarilabs.com</p>
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('travelsafe-privacy.html', 'w', encoding='utf-8') as f:
        f.write(ts_priv)

    rc_priv = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | RoomClear | ScutariLabs</title>
  <meta name="description" content="Privacy Policy for RoomClear bug-sweeping tool by ScutariLabs Ltd. 100% on-device processing.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container prose" style="padding-top: 60px; padding-bottom: 80px; max-width: 820px;">
    <span class="section-eyebrow">PRIVACY POLICY // ZERO-TRUST ARCHITECTURE</span>
    <h1>RoomClear Privacy Policy</h1>
    <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); margin-bottom: 24px;">
      Effective Date: November 2026 &bull; Developer Entity: ScutariLabs Ltd
    </div>

    <p>RoomClear by ScutariLabs Ltd is a tactical counter-surveillance and bug-sweeping tool. We operate on a strict "Zero-Trust, Zero-Cloud" architecture. 100% of sensor processing occurs locally on your device hardware.</p>

    <h2>1. Hardware Permissions & Data Handling</h2>
    <ul>
      <li><strong>Camera & Flashlight:</strong> Used exclusively for real-time optical lens hunting (retro-reflective strobe) and Edge ML object detection. Optical frames are processed ephemerally in volatile RAM and are immediately destroyed. Zero video or photos are ever written to disk or transmitted to a cloud server.</li>
      <li><strong>Microphone (RECORD_AUDIO):</strong> Used exclusively for the Ultrasonic Analyzer to run a local Fast Fourier Transform (FFT) checking for 18kHz-22kHz acoustic beacons. Audio streams are analyzed in volatile RAM and immediately discarded. No audio is ever recorded, stored, or uploaded.</li>
      <li><strong>Bluetooth & Location (ACCESS_FINE_LOCATION):</strong> Android OS requires Fine Location permission to scan for Bluetooth Low Energy (BLE) frequencies and smart trackers. GPS coordinates are strictly used locally to stamp PDF audit logs if the user manually initiates an export. This data never leaves your device.</li>
    </ul>

    <h2>2. Network Access</h2>
    <p>RoomClear is designed to operate in airplane mode. The app&#39;s manifest is air-gapped, meaning it possesses zero internet permissions for data transmission. Network access is strictly restricted to Google Play Billing verification for in-app purchases.</p>

    <h2>3. UK, EU (GDPR) & USA (CCPA) Compliance</h2>
    <p>RoomClear adheres to privacy-by-design principles. Because no personal data, telemetry, or behavioral tracking is collected or stored on external servers, there is no consumer data to monetize or sell.</p>

    <h2>4. Contact</h2>
    <p>For support or privacy inquiries, contact: <strong>support@scutarilabs.com</strong></p>
  </main>

  {{FOOTER}}
</body>
</html>'''.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('roomclear-privacy.html', 'w', encoding='utf-8') as f:
        f.write(rc_priv)

def build_stillnet_privacy():
    sn_priv = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Stillnet | ScutariLabs</title>
  <meta name="description" content="Privacy Policy for Stillnet network vulnerability scanner by ScutariLabs Ltd.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container prose" style="padding-top: 60px; padding-bottom: 80px; max-width: 820px;">
    <span class="section-eyebrow">PRIVACY POLICY // ZERO-TRUST ARCHITECTURE</span>
    <h1>Stillnet Privacy Policy</h1>
    <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); margin-bottom: 24px;">
      Effective Date: November 2026 &bull; Developer Entity: ScutariLabs Ltd
    </div>

    <p>Stillnet by ScutariLabs Ltd is a 100% offline local network vulnerability scanner and active threat countermeasure utility. We operate on a strict "Zero-Trust, Zero-Cloud" architecture.</p>

    <h2>1. Data Collection & Handling</h2>
    <ul>
      <li><strong>Local Network Scanning:</strong> Stillnet scans local network topologies and connected devices. All network mapping, packet analysis, and vulnerability threat assessments are processed entirely on-device.</li>
      <li><strong>Zero Cloud Analytics:</strong> No personal data, telemetry, or behavioral tracking is collected or stored on external servers. There is no consumer data to monetize or sell.</li>
    </ul>

    <h2>2. Network Access Permissions</h2>
    <p>Stillnet requires network permissions exclusively to scan your Local Area Network (LAN) for vulnerabilities and to apply local countermeasures. The app is otherwise air-gapped and does not transmit your scan logs or device profiles to external servers. Network access is strictly restricted to local functions and Google Play Billing verification for in-app purchases.</p>

    <h2>3. UK, EU (GDPR) & USA (CCPA) Compliance</h2>
    <p>Stillnet adheres to privacy-by-design principles. Because no personal data is collected or transmitted off your device, we do not hold identifiable records or tracking profiles.</p>

    <h2>4. Contact</h2>
    <p>For support or privacy inquiries, contact: <strong>support@scutarilabs.com</strong></p>
  </main>

  {{FOOTER}}
</body>
</html>'''.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('stillnet-privacy.html', 'w', encoding='utf-8') as f:
        f.write(sn_priv)
    print("Policies generated.")

def build_blog_template():
    tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ScutariLabs | {{TITLE}}</title>
  <meta name="description" content="Technical articles and research on zero-cloud mobile security and on-device AI by ScutariLabs.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container prose" style="padding-top: 60px; padding-bottom: 80px; max-width: 820px;">
    <div style="text-align: center; margin-bottom: 48px; border-bottom: 1px solid var(--border); padding-bottom: 32px;">
      <span class="section-eyebrow">SCUTARILABS SECURITY RESEARCH</span>
      <h1 style="margin-top: 12px; margin-bottom: 16px;">{{TITLE}}</h1>
      <div style="font-family: var(--font-mono); font-size: 0.9rem; color: var(--accent);">{{DATE}}</div>
    </div>

    <div>
      {{CONTENT}}
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)

    with open('blog_template.html', 'w', encoding='utf-8') as f:
        f.write(tmpl)
    print("blog_template.html generated.")

def build_contact():
    contact_tmpl = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact & Developer Support | ScutariLabs</title>
  <meta name="description" content="Contact ScutariLabs Ltd for commercial SDK licensing, enterprise integrations, and support.">
  <link rel="stylesheet" href="/css/main.css">
</head>
<body>
  {{NAV}}

  <main class="container" style="padding-top: 60px; padding-bottom: 80px; max-width: 800px;">
    <span class="section-eyebrow">DEVELOPER SUPPORT & INQUIRIES</span>
    <h1 style="margin-bottom: 16px;">Contact ScutariLabs</h1>
    <p class="lead" style="margin-bottom: 32px;">Need assistance with an application or have questions regarding our privacy architecture or B2B SDK licensing? Reach out directly:</p>

    <div class="app-card" style="margin-bottom: 32px;">
      <h3 style="margin-bottom: 16px; color: #ffffff;">ScutariLabs Ltd</h3>
      <p style="margin-bottom: 12px;"><strong>Registered Entity:</strong> UK Private Limited Company <!-- TODO: Insert Companies House Number --></p>
      <p style="margin-bottom: 12px;"><strong>Primary Support Email:</strong> <a href="mailto:support@scutarilabs.com" style="color: var(--accent);">support@scutarilabs.com</a></p>
      <p style="margin-bottom: 12px;"><strong>Commercial SDK Licensing:</strong> <a href="mailto:support@scutarilabs.com?subject=Commercial+SDK+Licensing+Inquiry" style="color: var(--accent);">support@scutarilabs.com?subject=Commercial+SDK+Licensing+Inquiry</a></p>
      <p style="margin-bottom: 0;"><strong>App Store Turnaround:</strong> Response turnaround within 1-2 business days.</p>
    </div>
  </main>

  {{FOOTER}}
</body>
</html>'''

    page = contact_tmpl.replace('{{NAV}}', NAV).replace('{{FOOTER}}', FOOTER)
    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(page)
    print("contact.html generated.")

def build_seo():
    robots = '''User-agent: *
Allow: /

Sitemap: https://scutarilabs.com/sitemap.xml
'''
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write(robots)

    sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://scutarilabs.com/</loc><lastmod>2026-11-25</lastmod><priority>1.0</priority></url>
  <url><loc>https://scutarilabs.com/travelsafe.html</loc><lastmod>2026-11-25</lastmod><priority>0.8</priority></url>
  <url><loc>https://scutarilabs.com/roomclear.html</loc><lastmod>2026-11-25</lastmod><priority>0.8</priority></url>
  <url><loc>https://scutarilabs.com/stillnet.html</loc><lastmod>2026-11-25</lastmod><priority>0.8</priority></url>
  <url><loc>https://scutarilabs.com/sdk/</loc><lastmod>2026-11-25</lastmod><priority>0.9</priority></url>
  <url><loc>https://scutarilabs.com/sdk/scutaricore/</loc><lastmod>2026-11-25</lastmod><priority>0.9</priority></url>
  <url><loc>https://scutarilabs.com/blog.html</loc><lastmod>2026-11-25</lastmod><priority>0.8</priority></url>
  <url><loc>https://scutarilabs.com/blog/travel-safe-ai-app-store-launch.html</loc><lastmod>2026-11-23</lastmod></url>
  <url><loc>https://scutarilabs.com/blog/offline-personal-safety-apps-solo-travel-2026.html</loc><lastmod>2026-11-22</lastmod></url>
  <url><loc>https://scutarilabs.com/blog/True-Travel-Safety-Doesnt-Need-a-WIFI-Connection-Introducing-Travel-Safe-AI.html</loc><lastmod>2026-11-18</lastmod></url>
  <url><loc>https://scutarilabs.com/blog/privacy-nightmare.html</loc><lastmod>2026-11-15</lastmod></url>
  <url><loc>https://scutarilabs.com/contact.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/travelsafe-privacy.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/travelsafe-terms.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/roomclear-privacy.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/roomclear-terms.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/stillnet-privacy.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
  <url><loc>https://scutarilabs.com/stillnet-terms.html</loc><lastmod>2026-11-25</lastmod><priority>0.5</priority></url>
</urlset>
'''
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("robots.txt and sitemap.xml generated.")

def main():
    build_index()
    build_sdk_index()
    build_scutaricore()
    build_travelsafe()
    build_roomclear()
    build_stillnet()
    build_ts_rc_policies()
    build_stillnet_privacy()
    build_blog_template()
    build_contact()
    build_seo()
    print("All static pages built.")

if __name__ == '__main__':
    main()


