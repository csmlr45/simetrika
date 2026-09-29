import streamlit as st

st.set_page_config(page_title="Simetrika | Rénovation au Luxembourg", page_icon="◼", layout="wide", initial_sidebar_state="collapsed")

L = {
"nav_services":"Services","nav_projects":"Notre approche","nav_about":"À propos","nav_contact":"Contact","quote":"Demander un devis",
"eyebrow":"RÉNOVATION DE BÂTIMENT • LUXEMBOURG","hero_title":"Votre projet de rénovation, coordonné de A à Z.",
"hero_text":"Simetrika coordonne vos travaux, vous conseille et vous guide pour transformer maisons, appartements et locaux commerciaux au Luxembourg.",
"hero_cta":"Demander un devis","hero_secondary":"Découvrir nos services","trust1":"Accompagnement personnalisé","trust2":"Solutions sur mesure","trust3":"Coordination des travaux",
"services_kicker":"NOS SERVICES","services_title":"Des solutions adaptées à chaque projet.",
"services_intro":"De la transformation complète d’un intérieur aux travaux extérieurs et aux interventions plus ciblées, Simetrika vous accompagne avec une approche personnalisée.",
"s1":"Rénovation intérieure","s1d":"Salle de bain, cuisine, pièces de vie, chambres, escaliers, électricité, plomberie et plafonds — pour créer un intérieur à votre image.",
"s2":"Rénovation extérieure","s2d":"Façades, fenêtres et toiture : des interventions pensées pour redonner vie à votre extérieur en associant esthétique et durabilité.",
"s3":"Petits travaux & aménagement","s3d":"Peinture, enduits, carrelage, pose de sols, plancher et stratifié, ainsi que des solutions d’aménagement adaptées à vos besoins.",
"projects_kicker":"NOTRE APPROCHE","projects_title":"Un projet suivi avec soin et précision.",
"projects_text":"Simetrika s’appuie sur un savoir-faire personnalisé et un réseau de partenaires pour coordonner les différentes étapes de votre rénovation.",
"why_kicker":"À PROPOS DE SIMETRIKA","why_title":"Un accompagnement humain, du premier échange aux finitions.",
"why1":"Expérience internationale","why1d":"Georgel Rotaru, coordinateur de travaux, a développé son expérience en Roumanie, en Espagne et au Luxembourg.",
"why2":"Projet sur mesure","why2d":"Chaque projet est étudié selon vos besoins, vos envies et les particularités de votre espace.",
"why3":"Suivi personnalisé","why3d":"La qualité, le soin apporté au projet, la satisfaction du client et le respect des délais sont au cœur de l’accompagnement.",
"cta_title":"Besoin d’une rénovation sur mesure ?","cta_text":"Contactez Simetrika pour discuter de votre projet et obtenir un devis personnalisé.","cta_button":"Parler de mon projet",
"contact_kicker":"CONTACT","contact_title":"Parlons de votre projet.","contact_text":"Pour toute demande de renseignements ou de devis, décrivez-nous votre projet en quelques lignes.",
"name":"Nom","email":"Adresse e-mail","phone":"Téléphone","project":"Votre projet","project_ph":"Type de travaux, ville du chantier, pièces concernées, délais souhaités…","send":"Envoyer ma demande",
"footer":"Simetrika · 1 rue Ermesinde · L-1469 Luxembourg"
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root{--ink:#17201b;--muted:#68716b;--paper:#f7f6f1;--white:#fff;--sage:#788b78;--sage-dark:#526553;--line:#dedfd8}
html{scroll-behavior:smooth}.stApp{background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif}.block-container{max-width:1180px;padding-top:1.3rem;padding-bottom:2rem}header[data-testid="stHeader"]{background:transparent}#MainMenu,footer{visibility:hidden}h1,h2,h3{font-family:'Manrope',sans-serif!important;letter-spacing:-.035em;color:var(--ink)!important}p{color:var(--muted);line-height:1.7}
.topbar{display:flex;align-items:center;justify-content:space-between;padding:.55rem 0 1.2rem;border-bottom:1px solid var(--line);margin-bottom:2rem}.brand{font:800 1.55rem 'Manrope';letter-spacing:-.06em}.brand-dot{color:var(--sage)}.nav{display:flex;gap:1.6rem;align-items:center;font-size:.92rem}.nav a{color:var(--ink);text-decoration:none}.nav .pill{background:var(--ink);color:#fff;padding:.7rem 1rem;border-radius:999px}
.hero{min-height:570px;border-radius:30px;padding:5.2rem 4.5rem;display:flex;flex-direction:column;justify-content:center;background:linear-gradient(90deg,rgba(20,30,24,.88),rgba(20,30,24,.68) 48%,rgba(20,30,24,.12)),url('https://primary.jwwb.nl/unsplash/fp2b945RQUg.jpg?enable=upscale&enable-io=true&width=1600');background-size:cover;background-position:center;box-shadow:0 22px 60px rgba(32,38,33,.10)}.eyebrow{font-size:.76rem;font-weight:700;letter-spacing:.18em;color:#d9dfd7;margin-bottom:1.2rem}.hero h1{color:#fff!important;font-size:clamp(2.8rem,6vw,5.3rem);max-width:800px;line-height:.98;margin:0 0 1.5rem}.hero p{color:#edf0ec;font-size:1.15rem;max-width:630px}.hero-actions{margin-top:1.4rem;display:flex;gap:.8rem;flex-wrap:wrap}.btn{display:inline-block;text-decoration:none;border-radius:999px;padding:.9rem 1.25rem;font-weight:700;font-size:.92rem}.btn-primary{background:#fff;color:var(--ink)}.btn-secondary{border:1px solid rgba(255,255,255,.55);color:#fff}
.trustbar{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:1.5rem 0 4.5rem}.trust{text-align:center;font-weight:600;color:var(--ink);font-size:.92rem}.trust span{color:var(--sage);margin-right:.4rem}.section{padding:4.5rem 0}.kicker{color:var(--sage-dark);font-size:.76rem;letter-spacing:.18em;font-weight:800;margin-bottom:.7rem}.section-title{font-size:clamp(2rem,4vw,3.4rem);line-height:1.08;max-width:760px;margin:.2rem 0 1rem}.section-lead{max-width:680px;font-size:1.05rem;margin-bottom:2rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:2rem}.card{background:#fff;border:1px solid var(--line);border-radius:22px;padding:2rem;min-height:220px}.num{color:var(--sage);font-weight:800;font-size:.82rem}.card h3{font-size:1.35rem;margin:2.4rem 0 .7rem}.card p{font-size:.95rem;margin:0}.project-grid{display:grid;grid-template-columns:1.25fr .75fr;gap:1rem;margin-top:2rem}.project-main,.project-small{border-radius:24px;overflow:hidden;min-height:430px;position:relative;background-size:cover;background-position:center}.project-main{background-image:url('https://primary.jwwb.nl/unsplash/XzJAk8MqxTo.jpg?enable=upscale&enable-io=true&width=1400')}.project-small{background-image:url('https://primary.jwwb.nl/unsplash/WEWTGkPUVT0.jpg?enable=upscale&enable-io=true&width=1000')}.project-label{position:absolute;left:1.2rem;bottom:1.2rem;background:rgba(255,255,255,.94);color:var(--ink);padding:.65rem .9rem;border-radius:999px;font-weight:700;font-size:.85rem}
.why{background:#e8ebe5;border-radius:30px;padding:3.4rem;margin:3rem 0}.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2.2rem}.why-item{border-top:1px solid #bfc7bd;padding-top:1.2rem}.why-item h3{font-size:1.15rem;margin:.4rem 0}.big-cta{background:var(--ink);border-radius:30px;padding:4rem;margin:4rem 0;display:flex;align-items:center;justify-content:space-between;gap:2rem}.big-cta h2{color:#fff!important;font-size:clamp(2rem,4vw,3.2rem);margin:0 0 .6rem}.big-cta p{color:#cbd1cc;max-width:650px;margin:0}.big-cta a{white-space:nowrap;background:#fff;color:var(--ink);text-decoration:none;padding:1rem 1.3rem;border-radius:999px;font-weight:800}.contact-box{background:#fff;border:1px solid var(--line);border-radius:28px;padding:2rem}.stTextInput input,.stTextArea textarea{border-radius:12px!important;background:#fbfbf8!important}.stFormSubmitButton button{border-radius:999px!important;background:var(--ink)!important;color:#fff!important;border:0!important;font-weight:700!important}.site-footer{border-top:1px solid var(--line);margin-top:4rem;padding:2rem 0;display:flex;justify-content:space-between;color:var(--muted);font-size:.85rem}
@media(max-width:800px){.nav a:not(.pill){display:none}.hero{padding:3rem 1.6rem;min-height:520px}.cards,.trustbar,.why-grid,.project-grid{grid-template-columns:1fr}.big-cta{padding:2.3rem 1.6rem;flex-direction:column;align-items:flex-start}.why{padding:2.2rem 1.4rem}.project-main,.project-small{min-height:320px}}
</style>
""",unsafe_allow_html=True)

st.markdown(f"""
<div class="topbar"><div class="brand">SIMETRIKA<span class="brand-dot">.</span></div><div class="nav"><a href="#services">{L['nav_services']}</a><a href="#realisations">{L['nav_projects']}</a><a href="#apropos">{L['nav_about']}</a><a href="#contact">{L['nav_contact']}</a><a class="pill" href="#contact">{L['quote']}</a></div></div>
<div class="hero"><div class="eyebrow">{L['eyebrow']}</div><h1>{L['hero_title']}</h1><p>{L['hero_text']}</p><div class="hero-actions"><a class="btn btn-primary" href="#contact">{L['hero_cta']} →</a><a class="btn btn-secondary" href="#services">{L['hero_secondary']}</a></div></div>
<div class="trustbar"><div class="trust"><span>✓</span>{L['trust1']}</div><div class="trust"><span>✓</span>{L['trust2']}</div><div class="trust"><span>✓</span>{L['trust3']}</div></div>
<div id="services" class="section"><div class="kicker">{L['services_kicker']}</div><h2 class="section-title">{L['services_title']}</h2><p class="section-lead">{L['services_intro']}</p><div class="cards"><div class="card"><div class="num">01</div><h3>{L['s1']}</h3><p>{L['s1d']}</p></div><div class="card"><div class="num">02</div><h3>{L['s2']}</h3><p>{L['s2d']}</p></div><div class="card"><div class="num">03</div><h3>{L['s3']}</h3><p>{L['s3d']}</p></div></div></div>
<div id="realisations" class="section"><div class="kicker">{L['projects_kicker']}</div><h2 class="section-title">{L['projects_title']}</h2><p class="section-lead">{L['projects_text']}</p><div class="project-grid"><div class="project-main"><div class="project-label">Rénovation extérieure</div></div><div class="project-small"><div class="project-label">Travaux & aménagement</div></div></div></div>
<div id="apropos" class="why"><div class="kicker">{L['why_kicker']}</div><h2 class="section-title">{L['why_title']}</h2><div class="why-grid"><div class="why-item"><h3>{L['why1']}</h3><p>{L['why1d']}</p></div><div class="why-item"><h3>{L['why2']}</h3><p>{L['why2d']}</p></div><div class="why-item"><h3>{L['why3']}</h3><p>{L['why3d']}</p></div></div></div>
<div class="big-cta"><div><h2>{L['cta_title']}</h2><p>{L['cta_text']}</p></div><a href="#contact">{L['cta_button']} →</a></div>
""",unsafe_allow_html=True)

left,right=st.columns([.8,1.2],gap="large")
with left:
 st.markdown(f"""<div id="contact" class="section"><div class="kicker">{L['contact_kicker']}</div><h2 class="section-title">{L['contact_title']}</h2><p class="section-lead">{L['contact_text']}</p><p><strong>Simetrika</strong><br>1 rue Ermesinde<br>L-1469 Luxembourg<br><br><strong>contact@simetrika.lu</strong></p></div>""",unsafe_allow_html=True)
with right:
 with st.form("contact_form",clear_on_submit=True):
  name=st.text_input(L["name"]);email=st.text_input(L["email"]);phone=st.text_input(L["phone"]);project=st.text_area(L["project"],placeholder=L["project_ph"],height=150)
  if st.form_submit_button(L["send"]+" →"):
   if name and (email or phone) and project: st.success("Merci ! Votre demande a bien été saisie.")
   else: st.warning("Merci d’indiquer votre nom, un moyen de contact et quelques informations sur votre projet.")
st.markdown(f"""<div class="site-footer"><div><strong>SIMETRIKA.</strong></div><div>{L['footer']} · © 2026</div></div>""",unsafe_allow_html=True)
