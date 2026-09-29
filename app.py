import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Simetrika | Rénovation au Luxembourg", page_icon="◼", layout="wide", initial_sidebar_state="collapsed")

L = {
"nav_services":"Services","nav_estimator":"Estimateur de prix","nav_projects":"Réalisations","nav_about":"À propos","nav_contact":"Contact","quote":"Demander un devis",
"eyebrow":"RÉNOVATION DE BÂTIMENT • LUXEMBOURG","hero_title":"Votre projet de rénovation, coordonné de A à Z.",
"hero_text":"Simetrika coordonne vos travaux, vous conseille et vous guide pour transformer maisons, appartements et locaux commerciaux au Luxembourg.",
"hero_cta":"Demander un devis","hero_secondary":"Découvrir nos services","trust1":"Accompagnement personnalisé","trust2":"Solutions sur mesure","trust3":"Coordination des travaux",
"services_kicker":"NOS SERVICES","services_title":"Des solutions adaptées à chaque projet.",
"services_intro":"De la transformation complète d’un intérieur aux travaux extérieurs et aux interventions plus ciblées, Simetrika vous accompagne avec une approche personnalisée.",
"s1":"Rénovation intérieure","s1d":"Transformation et rénovation de cuisines, salles de bain, pièces de vie, chambres et escaliers, avec une attention particulière portée aux finitions et à la fonctionnalité.",
"s2":"Rénovation extérieure","s2d":"Rénovation et amélioration de l’extérieur de votre bâtiment : façade, fenêtres et toiture, avec des solutions adaptées à l’état du bâtiment et à votre projet.",
"s3":"Petits travaux & aménagement","s3d":"Des interventions ciblées pour rénover, rafraîchir ou améliorer votre intérieur sans engager une rénovation complète.",
"projects_kicker":"NOTRE APPROCHE","projects_title":"Un projet suivi avec soin et précision.",
"projects_text":"Simetrika s’appuie sur un savoir-faire personnalisé et un réseau de partenaires pour coordonner les différentes étapes de votre rénovation.",
"why_kicker":"À PROPOS DE SIMETRIKA","why_title":"Un interlocuteur unique, du premier échange aux finitions.",
"why1":"Expérience internationale","why1d":"Georgel Rotaru, coordinateur de travaux, a développé son expérience en Roumanie, en Espagne et au Luxembourg.",
"why2":"Projet sur mesure","why2d":"Chaque projet est étudié selon vos besoins, vos envies et les particularités de votre espace.",
"why3":"Suivi personnalisé","why3d":"La qualité, le soin apporté au projet, la satisfaction du client et le respect des délais sont au cœur de l’accompagnement.",
"cta_title":"Besoin d’une rénovation sur mesure ?","cta_text":"Contactez Simetrika pour discuter de votre projet et obtenir un devis personnalisé.","cta_button":"Parler de mon projet",
"contact_kicker":"CONTACT","contact_title":"Décrivez-nous votre projet.","contact_text":"Envoyez-nous les informations essentielles sur votre projet. Simetrika vous recontactera pour en discuter avec vous.",
"name":"Nom","email":"Adresse e-mail","phone":"Téléphone","project":"Votre projet","project_ph":"Type de travaux, ville du chantier, pièces concernées, délais souhaités…","send":"Envoyer ma demande",
"s1more":"Selon votre projet, les travaux peuvent inclure la peinture, les enduits, les sols, le carrelage, les plafonds ainsi que les interventions nécessaires en électricité et plomberie. Simetrika assure le suivi des différentes étapes pour vous offrir un projet cohérent, du début aux finitions.",
"s2more":"Simetrika vous accompagne dans l’organisation et le suivi des travaux extérieurs et coordonne, lorsque nécessaire, les différents corps de métier afin de simplifier la réalisation de votre projet.",
"s3more":"Peinture, enduits, carrelage, pose de sols, plancher et stratifié : Simetrika réalise et organise les travaux nécessaires pour remettre une pièce en état, améliorer ses finitions ou l’adapter à vos besoins.",
"more":"Plus d’informations",
"process_kicker":"COMMENT ÇA MARCHE ?","process_title":"Votre projet, étape par étape",
"process_intro":"Un accompagnement clair et structuré, du premier échange jusqu’à la réalisation des travaux.",
"p1":"1. Premier contact","p1d":"Vous nous présentez votre projet, vos besoins et vos attentes par téléphone, WhatsApp ou via notre formulaire.",
"p2":"2. Échange & visite","p2d":"Nous discutons ensemble des travaux à réaliser et, si nécessaire, organisons une visite sur place afin d’évaluer votre projet.",
"p3":"3. Proposition & devis","p3d":"Sur la base des besoins définis ensemble, nous préparons une proposition claire et un devis adapté à votre projet.",
"p4":"4. Réalisation & suivi","p4d":"Simetrika réalise et suit les travaux jusqu’aux finitions, en coordonnant si nécessaire les différents corps de métier.",
"about_text":"Derrière Simetrika, il y a <strong>Georgel Rotaru</strong>, coordinateur de travaux avec une expérience acquise en Roumanie, en Espagne et au Luxembourg.<br><br>Georgel accompagne personnellement chaque projet, de la première discussion jusqu’aux finitions. Selon les besoins, Simetrika réalise les travaux et coordonne des partenaires spécialisés afin de garantir un suivi simple et cohérent.<br><br><strong>Une approche directe, des solutions adaptées et un seul interlocuteur tout au long de votre projet.</strong>",
"portfolio_kicker":"NOS RÉALISATIONS","portfolio_title":"Quelques projets réalisés.","portfolio_intro":"Découvrez trois projets qui illustrent la diversité des travaux réalisés et coordonnés par Simetrika.","footer":"Simetrika · 1 rue Ermesinde · L-1469 Luxembourg",
"roof_meta":"Langsur · Toiture","roof_title":"Rénovation de toiture","roof_desc":"Travaux de rénovation de toiture réalisés à Langsur, avec intervention sur la structure et la couverture.",
"kitchen_meta":"Rénovation intérieure","kitchen_title":"Rénovation de cuisine","kitchen_desc":"Rénovation et aménagement d’une cuisine, avec pose du mobilier, du plan de travail et de la crédence.",
"pool_meta":"Aménagement extérieur","pool_title":"Aménagement d’une terrasse autour d’une piscine","pool_desc":"Réalisation d’une terrasse autour d’une piscine, avec préparation de la structure et pose du revêtement.",
"view_project":"Voir le projet","call":"Appeler","email_btn":"E-mail","footer_tagline":"Le savoir-faire personnalisé",
"response_24h":"Décrivez-nous votre projet. Nous vous recontacterons par téléphone ou par e-mail dans un délai maximum de 24 heures.","form_success":"Merci ! Votre demande a bien été saisie.","form_warning":"Merci d’indiquer votre nom, un moyen de contact et quelques informations sur votre projet."
}


DE = {
"nav_services":"Leistungen","nav_estimator":"Preisrechner","nav_projects":"Referenzen","nav_about":"Über uns","nav_contact":"Kontakt","quote":"Angebot anfragen",
"eyebrow":"GEBÄUDERENOVIERUNG • LUXEMBURG","hero_title":"Ihr Renovierungsprojekt – von A bis Z koordiniert.",
"hero_text":"Simetrika koordiniert Ihre Arbeiten, berät Sie und begleitet Sie bei der Renovierung von Häusern, Wohnungen und Gewerberäumen in Luxemburg.",
"hero_cta":"Angebot anfragen","hero_secondary":"Unsere Leistungen","trust1":"Persönliche Betreuung","trust2":"Individuelle Lösungen","trust3":"Koordination der Arbeiten",
"services_kicker":"UNSERE LEISTUNGEN","services_title":"Passende Lösungen für jedes Projekt.",
"services_intro":"Von der kompletten Innenrenovierung über Außenarbeiten bis zu gezielten Einzelmaßnahmen begleitet Simetrika Ihr Projekt persönlich und zuverlässig.",
"s1":"Innenrenovierung","s1d":"Umbau und Renovierung von Küchen, Bädern, Wohnräumen, Schlafzimmern und Treppen – mit besonderem Augenmerk auf saubere Ausführung und Funktionalität.",
"s2":"Außenrenovierung","s2d":"Renovierung und Aufwertung der Gebäudehülle: Fassade, Fenster und Dach – abgestimmt auf den Zustand des Gebäudes und Ihr Vorhaben.",
"s3":"Kleinere Arbeiten & Ausbau","s3d":"Gezielte Arbeiten, um Innenräume zu renovieren, aufzufrischen oder zu verbessern, ohne eine Komplettsanierung durchzuführen.",
"s1more":"Je nach Projekt können Maler- und Verputzarbeiten, Bodenbeläge, Fliesen, Decken sowie erforderliche Elektro- und Sanitärarbeiten dazugehören. Simetrika begleitet die einzelnen Schritte für ein stimmiges Ergebnis bis ins Detail.",
"s2more":"Simetrika begleitet die Organisation und Ausführung der Außenarbeiten und koordiniert bei Bedarf die verschiedenen Gewerke, damit Ihr Projekt möglichst unkompliziert umgesetzt wird.",
"s3more":"Maler- und Verputzarbeiten, Fliesen, Bodenbeläge, Dielen und Laminat: Simetrika führt die erforderlichen Arbeiten aus und organisiert sie, um Räume instand zu setzen, Oberflächen zu verbessern oder sie an Ihre Bedürfnisse anzupassen.",
"more":"Mehr erfahren","process_kicker":"SO LÄUFT ES AB","process_title":"Ihr Projekt, Schritt für Schritt","process_intro":"Eine klare und strukturierte Begleitung vom ersten Gespräch bis zur Ausführung.",
"p1":"1. Erstkontakt","p1d":"Sie schildern uns Ihr Projekt, Ihre Wünsche und Anforderungen per Telefon, WhatsApp oder über unser Formular.",
"p2":"2. Gespräch & Besichtigung","p2d":"Wir besprechen die geplanten Arbeiten und vereinbaren bei Bedarf einen Termin vor Ort, um das Projekt einzuschätzen.",
"p3":"3. Vorschlag & Angebot","p3d":"Auf Grundlage der gemeinsam definierten Anforderungen erstellen wir einen klaren Vorschlag und ein passendes Angebot.",
"p4":"4. Ausführung & Betreuung","p4d":"Simetrika führt die Arbeiten bis zur Fertigstellung aus und begleitet sie; bei Bedarf werden die verschiedenen Gewerke koordiniert.",
"why_kicker":"ÜBER SIMETRIKA","why_title":"Ein Ansprechpartner – vom ersten Gespräch bis zur Fertigstellung.",
"about_text":"Hinter Simetrika steht <strong>Georgel Rotaru</strong>, Baukoordinator mit Erfahrung aus Rumänien, Spanien und Luxemburg.<br><br>Georgel begleitet jedes Projekt persönlich – vom ersten Gespräch bis zur Fertigstellung. Je nach Bedarf führt Simetrika Arbeiten selbst aus und koordiniert spezialisierte Partner, damit die Umsetzung einfach und stimmig bleibt.<br><br><strong>Direkte Kommunikation, passende Lösungen und ein Ansprechpartner während des gesamten Projekts.</strong>",
"cta_title":"Sie planen eine individuelle Renovierung?","cta_text":"Kontaktieren Sie Simetrika, um Ihr Projekt zu besprechen und ein individuelles Angebot zu erhalten.","cta_button":"Projekt besprechen",
"contact_kicker":"KONTAKT","contact_title":"Beschreiben Sie uns Ihr Projekt.","contact_text":"Senden Sie uns die wichtigsten Informationen zu Ihrem Vorhaben. Simetrika meldet sich anschließend bei Ihnen, um alles Weitere zu besprechen.",
"name":"Name","email":"E-Mail-Adresse","phone":"Telefon","project":"Ihr Projekt","project_ph":"Art der Arbeiten, Ort der Baustelle, betroffene Räume, gewünschter Zeitraum …","send":"Anfrage senden",
"portfolio_kicker":"REFERENZEN","portfolio_title":"Ausgewählte Projekte.","portfolio_intro":"Drei Projekte, die einen Einblick in die von Simetrika ausgeführten Arbeiten geben.",
"roof_meta":"Langsur · Dach","roof_title":"Dachrenovierung","roof_desc":"Dachrenovierung in Langsur mit Arbeiten an der Konstruktion und Dacheindeckung.",
"kitchen_meta":"Innenrenovierung","kitchen_title":"Küchenrenovierung","kitchen_desc":"Renovierung und Ausbau einer Küche mit Montage der Möbel, Arbeitsplatte und Küchenrückwand.",
"pool_meta":"Außenbereich","pool_title":"Terrasse rund um einen Pool","pool_desc":"Ausführung einer Terrasse rund um einen Pool einschließlich Vorbereitung der Unterkonstruktion und Verlegung des Belags.",
"view_project":"Projekt ansehen","call":"Anrufen","email_btn":"E-Mail","footer_tagline":"Individuelles Handwerk",
"response_24h":"Beschreiben Sie uns Ihr Projekt. Wir melden uns innerhalb von maximal 24 Stunden telefonisch oder per E-Mail bei Ihnen.","form_success":"Vielen Dank! Ihre Anfrage wurde erfasst.","form_warning":"Bitte geben Sie Ihren Namen, eine Kontaktmöglichkeit und einige Informationen zu Ihrem Projekt an."
}

EN = {
"nav_services":"Services","nav_estimator":"Price estimator","nav_projects":"Projects","nav_about":"About","nav_contact":"Contact","quote":"Request a quote",
"eyebrow":"BUILDING RENOVATION • LUXEMBOURG","hero_title":"Your renovation project, coordinated from A to Z.",
"hero_text":"Simetrika coordinates your work, advises you and guides you through the renovation of houses, apartments and commercial spaces in Luxembourg.",
"hero_cta":"Request a quote","hero_secondary":"Discover our services","trust1":"Personal support","trust2":"Tailored solutions","trust3":"Work coordination",
"services_kicker":"OUR SERVICES","services_title":"Solutions tailored to every project.",
"services_intro":"From complete interior renovations to exterior work and smaller targeted jobs, Simetrika supports your project with a personalised approach.",
"s1":"Interior renovation","s1d":"Transformation and renovation of kitchens, bathrooms, living areas, bedrooms and staircases, with particular attention to finish and functionality.",
"s2":"Exterior renovation","s2d":"Renovation and improvement of your building’s exterior, including façades, windows and roofing, with solutions adapted to the building and your project.",
"s3":"Small works & improvements","s3d":"Targeted work to renovate, refresh or improve your interior without undertaking a complete renovation.",
"s1more":"Depending on the project, work may include painting, plastering, flooring, tiling, ceilings and any necessary electrical and plumbing work. Simetrika follows the different stages to deliver a coherent project through to the finishing touches.",
"s2more":"Simetrika supports the organisation and follow-up of exterior work and, when needed, coordinates the different trades to make your project easier to deliver.",
"s3more":"Painting, plastering, tiling, flooring, floorboards and laminate: Simetrika carries out and organises the work needed to restore a room, improve its finish or adapt it to your needs.",
"more":"More information","process_kicker":"HOW IT WORKS","process_title":"Your project, step by step","process_intro":"Clear, structured support from the first conversation through to completion.",
"p1":"1. First contact","p1d":"Tell us about your project, needs and expectations by phone, WhatsApp or through our form.",
"p2":"2. Discussion & visit","p2d":"We discuss the work together and, if needed, arrange an on-site visit to assess your project.",
"p3":"3. Proposal & quote","p3d":"Based on the requirements defined together, we prepare a clear proposal and a quote tailored to your project.",
"p4":"4. Work & follow-up","p4d":"Simetrika carries out and follows the work through to completion, coordinating the different trades when needed.",
"why_kicker":"ABOUT SIMETRIKA","why_title":"One point of contact, from the first conversation to the finishing touches.",
"about_text":"Behind Simetrika is <strong>Georgel Rotaru</strong>, a works coordinator with experience gained in Romania, Spain and Luxembourg.<br><br>Georgel personally follows each project from the first discussion through to completion. Depending on the needs, Simetrika carries out the work and coordinates specialist partners to keep the process simple and consistent.<br><br><strong>A direct approach, tailored solutions and one point of contact throughout your project.</strong>",
"cta_title":"Planning a tailored renovation?","cta_text":"Contact Simetrika to discuss your project and receive a personalised quote.","cta_button":"Discuss my project",
"contact_kicker":"CONTACT","contact_title":"Tell us about your project.","contact_text":"Send us the key details of your project. Simetrika will get back to you to discuss the next steps.",
"name":"Name","email":"Email address","phone":"Phone","project":"Your project","project_ph":"Type of work, project location, rooms involved, preferred timing…","send":"Send my request",
"portfolio_kicker":"OUR PROJECTS","portfolio_title":"Selected projects.","portfolio_intro":"Three projects illustrating the range of work carried out by Simetrika.",
"roof_meta":"Langsur · Roofing","roof_title":"Roof renovation","roof_desc":"Roof renovation work carried out in Langsur, including work on the structure and roof covering.",
"kitchen_meta":"Interior renovation","kitchen_title":"Kitchen renovation","kitchen_desc":"Kitchen renovation and fit-out, including installation of cabinetry, worktop and backsplash.",
"pool_meta":"Exterior works","pool_title":"Poolside terrace","pool_desc":"Construction of a terrace around a swimming pool, including preparation of the supporting structure and installation of the decking.",
"view_project":"View project","call":"Call","email_btn":"Email","footer_tagline":"Personalised craftsmanship",
"response_24h":"Tell us about your project. We will get back to you by phone or email within a maximum of 24 hours.","form_success":"Thank you! Your request has been recorded.","form_warning":"Please enter your name, a way to contact you and a few details about your project."
}

# PROVISIONAL TEST PRICES — replace with Georgel's confirmed tariffs later.
PRICE_CONFIG = {
    "peinture": {"unit": "m²", "min": 18, "max": 30},
    "enduit": {"unit": "m²", "min": 20, "max": 35},
    "stratifie": {"unit": "m²", "min": 25, "max": 45},
    "parquet": {"unit": "m²", "min": 45, "max": 75},
    "vinyle": {"unit": "m²", "min": 30, "max": 50},
    "carrelage_sol": {"unit": "m²", "min": 45, "max": 75},
    "carrelage_mur": {"unit": "m²", "min": 50, "max": 85},
    "terrasse": {"unit": "m²", "min": 70, "max": 120},
    "facade": {"unit": "m²", "min": 40, "max": 75},
    "demolition": {"unit": "m²", "min": 15, "max": 30},
    "prise": {"unit": "pc", "min": 55, "max": 90},
    "luminaire": {"unit": "pc", "min": 45, "max": 80},
    "lavabo": {"unit": "pc", "min": 180, "max": 320},
    "wc": {"unit": "pc", "min": 220, "max": 380},
    "robinetterie": {"unit": "pc", "min": 100, "max": 220},
    "cuisine": {"unit": "ml", "min": 180, "max": 320},
}

CALC_FR = {
"calc_kicker":"ESTIMATEUR DE PRIX","calc_title":"Estimez votre projet en quelques clics.",
"calc_intro":"Sélectionnez les travaux et indiquez les quantités. Vous obtenez immédiatement une fourchette indicative pour votre projet.",
"calc_provisional":"Tarifs de démonstration provisoires — ils seront remplacés par les tarifs confirmés de Simetrika.",
"calc_add":"Ajouter des travaux","calc_empty":"Ajoutez une ou plusieurs prestations pour obtenir une estimation.",
"calc_work":"Prestation","calc_qty":"Quantité","calc_unit":"Unité","calc_range":"Estimation","calc_rate":"Tarif indicatif","calc_line_total":"Sous-total","calc_remove":"Supprimer",
"calc_total":"Estimation indicative du projet","calc_disclaimer":"Cette estimation est indicative et ne constitue pas une offre. Le prix final dépend notamment de l’état du support, des matériaux choisis, de l’accessibilité et des conditions du chantier. Une offre définitive est établie après évaluation du projet.",
"calc_quote":"Demander un devis précis","calc_select":"Choisir une prestation",
"calc_cat_walls":"Murs & peinture","calc_cat_floors":"Sols","calc_cat_tiles":"Carrelage","calc_cat_ext":"Extérieur","calc_cat_demo":"Dépose & démolition","calc_cat_elec":"Électricité","calc_cat_plumb":"Plomberie","calc_cat_kitchen":"Cuisine",
"work_peinture":"Peinture","work_enduit":"Enduit","work_stratifie":"Sol stratifié","work_parquet":"Parquet","work_vinyle":"Sol vinyle","work_carrelage_sol":"Carrelage au sol","work_carrelage_mur":"Carrelage mural","work_terrasse":"Terrasse","work_facade":"Façade","work_demolition":"Dépose / démolition","work_prise":"Prise électrique","work_luminaire":"Pose de luminaire","work_lavabo":"Pose de lavabo","work_wc":"Pose de WC","work_robinetterie":"Robinetterie","work_cuisine":"Montage / aménagement cuisine",
"unit_pc":"pièce","unit_ml":"mètre linéaire","unit_m2":"m²"
}
CALC_DE = {
"calc_kicker":"PREISRECHNER","calc_title":"Schätzen Sie Ihr Projekt mit wenigen Klicks.",
"calc_intro":"Wählen Sie die gewünschten Arbeiten und Mengen. Sie erhalten sofort eine unverbindliche Preisspanne.",
"calc_provisional":"Vorläufige Testpreise — sie werden später durch die bestätigten Simetrika-Preise ersetzt.",
"calc_add":"Arbeiten hinzufügen","calc_empty":"Fügen Sie eine oder mehrere Leistungen hinzu, um eine Schätzung zu erhalten.",
"calc_work":"Leistung","calc_qty":"Menge","calc_unit":"Einheit","calc_range":"Schätzung","calc_rate":"Richtpreis","calc_line_total":"Zwischensumme","calc_remove":"Entfernen",
"calc_total":"Unverbindliche Projektschätzung","calc_disclaimer":"Diese Schätzung ist unverbindlich und stellt kein Angebot dar. Der endgültige Preis hängt unter anderem vom Zustand des Untergrunds, den gewählten Materialien, der Zugänglichkeit und den Bedingungen auf der Baustelle ab. Ein verbindliches Angebot wird nach Prüfung des Projekts erstellt.",
"calc_quote":"Genaues Angebot anfragen","calc_select":"Leistung auswählen",
"calc_cat_walls":"Wände & Malerarbeiten","calc_cat_floors":"Böden","calc_cat_tiles":"Fliesen","calc_cat_ext":"Außenbereich","calc_cat_demo":"Rückbau & Abbruch","calc_cat_elec":"Elektro","calc_cat_plumb":"Sanitär","calc_cat_kitchen":"Küche",
"work_peinture":"Malerarbeiten","work_enduit":"Spachtel- / Putzarbeiten","work_stratifie":"Laminat","work_parquet":"Parkett","work_vinyle":"Vinylboden","work_carrelage_sol":"Bodenfliesen","work_carrelage_mur":"Wandfliesen","work_terrasse":"Terrasse","work_facade":"Fassade","work_demolition":"Rückbau / Abbruch","work_prise":"Steckdose","work_luminaire":"Leuchtenmontage","work_lavabo":"Waschbeckenmontage","work_wc":"WC-Montage","work_robinetterie":"Armaturen","work_cuisine":"Küchenmontage / Ausbau",
"unit_pc":"Stück","unit_ml":"lfm","unit_m2":"m²"
}
CALC_EN = {
"calc_kicker":"PRICE ESTIMATOR","calc_title":"Estimate your project in a few clicks.",
"calc_intro":"Select the work you need and enter the quantities to receive an instant indicative price range.",
"calc_provisional":"Provisional demonstration prices — these will later be replaced with Simetrika's confirmed rates.",
"calc_add":"Add work","calc_empty":"Add one or more services to receive an estimate.",
"calc_work":"Service","calc_qty":"Quantity","calc_unit":"Unit","calc_range":"Estimate","calc_rate":"Indicative rate","calc_line_total":"Subtotal","calc_remove":"Remove",
"calc_total":"Indicative project estimate","calc_disclaimer":"This estimate is indicative and does not constitute a quotation. The final price depends on factors including the condition of the existing surfaces, materials selected, accessibility and site conditions. A final quotation is provided after the project has been assessed.",
"calc_quote":"Request a precise quote","calc_select":"Choose a service",
"calc_cat_walls":"Walls & painting","calc_cat_floors":"Flooring","calc_cat_tiles":"Tiling","calc_cat_ext":"Exterior","calc_cat_demo":"Removal & demolition","calc_cat_elec":"Electrical","calc_cat_plumb":"Plumbing","calc_cat_kitchen":"Kitchen",
"work_peinture":"Painting","work_enduit":"Plastering / skim coat","work_stratifie":"Laminate flooring","work_parquet":"Parquet flooring","work_vinyle":"Vinyl flooring","work_carrelage_sol":"Floor tiling","work_carrelage_mur":"Wall tiling","work_terrasse":"Terrace","work_facade":"Façade","work_demolition":"Removal / demolition","work_prise":"Electrical socket","work_luminaire":"Light fitting installation","work_lavabo":"Washbasin installation","work_wc":"Toilet installation","work_robinetterie":"Tap / fixture installation","work_cuisine":"Kitchen fitting / installation",
"unit_pc":"piece","unit_ml":"linear metre","unit_m2":"m²"
}

WORK_GROUPS = [
("calc_cat_walls", ["peinture","enduit"]),
("calc_cat_floors", ["stratifie","parquet","vinyle"]),
("calc_cat_tiles", ["carrelage_sol","carrelage_mur"]),
("calc_cat_ext", ["terrasse","facade"]),
("calc_cat_demo", ["demolition"]),
("calc_cat_elec", ["prise","luminaire"]),
("calc_cat_plumb", ["lavabo","wc","robinetterie"]),
("calc_cat_kitchen", ["cuisine"]),
]

lang = st.query_params.get("lang", "fr")
if lang not in ("fr", "de", "en"):
    lang = "fr"
if lang == "de":
    L.update(DE)
elif lang == "en":
    L.update(EN)

L.update(CALC_DE if lang == "de" else CALC_EN if lang == "en" else CALC_FR)

st.markdown("""
<style>html{scroll-behavior:auto!important}
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
:root{--ink:#17201b;--muted:#68716b;--paper:#f7f6f1;--white:#fff;--sage:#9aa79b;--sage-dark:#6f7d72;--line:#dedfd8}
html{scroll-behavior:smooth}.stApp{background:var(--paper);color:var(--ink);font-family:'DM Sans',sans-serif}.block-container{max-width:1180px;padding-top:1.3rem;padding-bottom:2rem}header[data-testid="stHeader"]{background:transparent}#MainMenu,footer{visibility:hidden}h1,h2,h3{font-family:'Manrope',sans-serif!important;letter-spacing:-.035em;color:var(--ink)!important}p{color:var(--muted);line-height:1.7}
.topbar{display:flex;align-items:center;justify-content:space-between;padding:.55rem 0 1.2rem;border-bottom:1px solid var(--line);margin-bottom:2rem}.brand{font:800 1.55rem 'Manrope';letter-spacing:-.06em}.brand-dot{color:var(--sage)}.nav{display:flex;gap:1.6rem;align-items:center;font-size:.92rem}.nav a{color:var(--ink);text-decoration:none}.nav .pill{background:var(--ink);color:#fff;padding:.7rem 1rem;border-radius:999px}.lang-switch{display:flex;gap:.18rem;border:1px solid var(--line);border-radius:999px;padding:.2rem}.lang-switch a{font-size:.72rem;font-weight:800;padding:.28rem .42rem;border-radius:999px;color:var(--muted)}.lang-switch a.active{background:var(--ink);color:#fff}
.hero{min-height:570px;border-radius:30px;padding:5.2rem 4.5rem;display:flex;flex-direction:column;justify-content:center;background:url('https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/ChatGPT%20Image%20Sep%2029%2C%202026%2C%2010_39_50%20PM.png');background-size:cover;background-position:center;box-shadow:none}.eyebrow{font-size:.76rem;font-weight:800;letter-spacing:.18em;color:var(--ink);margin-bottom:1.2rem}.hero h1{color:var(--ink)!important;font-size:clamp(2.55rem,4.25vw,4rem);font-weight:600;letter-spacing:-.04em;max-width:610px;line-height:1.08;margin:0 0 1.7rem;overflow-wrap:normal;word-break:normal}.hero.hero-de h1{font-size:clamp(2.35rem,3.8vw,3.65rem);max-width:650px;letter-spacing:-.04em}.hero p{color:#39423d;font-size:1rem;line-height:1.65;max-width:570px;font-weight:500}.hero-actions{margin-top:1.4rem;display:flex;gap:.8rem;flex-wrap:wrap}.hero-actions a,.hero-actions a:link,.hero-actions a:visited,.hero-actions a:hover,.hero-actions a:active{text-decoration:none!important}.btn{display:inline-flex;align-items:center;justify-content:center;text-decoration:none!important;border-radius:999px;padding:.92rem 1.35rem;font-weight:800;font-size:.92rem;box-shadow:none!important;text-shadow:none!important;backdrop-filter:none!important;transition:background .18s ease,color .18s ease,border-color .18s ease}.hero .btn-primary{background:var(--ink);color:#fff!important;border:1.5px solid var(--ink)}.hero .btn-primary:hover{background:#26322b;border-color:#26322b;color:#fff!important}.hero .btn-secondary{background:transparent!important;color:var(--ink)!important;border:1.5px solid var(--ink)}.hero .btn-secondary:hover{background:rgba(247,246,241,.55)!important;border-color:var(--ink);color:var(--ink)!important}.hero .btn-secondary:last-child{background:var(--sage-dark)!important;color:#fff!important;border-color:var(--sage-dark)}.hero .btn-secondary:last-child:hover{background:#5f6d63!important;border-color:#5f6d63;color:#fff!important}
.trustbar{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;padding:1.5rem 0 4.5rem}.trust{text-align:center;font-weight:600;color:var(--ink);font-size:.92rem}.trust span{color:var(--sage);margin-right:.4rem}.section{padding:4.5rem 0}.kicker{color:var(--sage-dark);font-size:.76rem;letter-spacing:.18em;font-weight:800;margin-bottom:.7rem}.section-title{font-size:clamp(2rem,4vw,3.4rem);line-height:1.08;max-width:760px;margin:.2rem 0 1rem}.section-lead{max-width:680px;font-size:1.05rem;margin-bottom:2rem}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:2rem;align-items:start}.card{background:#fff;border:1px solid var(--line);border-radius:22px;padding:2rem;min-height:384px;box-sizing:border-box;display:flex;flex-direction:column}.card .num{flex:0 0 auto}.card h3{min-height:3.4rem}.card>p{min-height:7.2rem}.card>details{margin-top:auto}.num{color:var(--sage);font-weight:800;font-size:.82rem}.card h3{font-size:1.35rem;margin:2.4rem 0 .7rem}.card p{font-size:.95rem;margin:0}.service-link{display:inline-block;margin-top:1.2rem;color:var(--sage-dark);font-weight:800;text-decoration:none}.service-detail{margin-top:1rem;padding-top:1rem;border-top:1px solid var(--line);font-size:.9rem!important}.process-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-top:2rem}.process-step{background:#fff;border:1px solid var(--line);border-radius:20px;padding:1.6rem}.process-step h3{font-size:1.05rem;margin:.2rem 0 .7rem}.process-step p{font-size:.9rem;margin:0}.contact-actions{display:flex;gap:.55rem;flex-wrap:nowrap;margin-top:1.4rem;align-items:center}.contact-actions a{white-space:nowrap;flex:0 1 auto}.contact-actions a{padding:.72rem .82rem;border-radius:999px;text-decoration:none;font-weight:800;font-size:.82rem}.contact-actions .dark{background:var(--ink);color:#fff}.contact-actions .outline{border:1px solid var(--ink);color:var(--ink)}.about-copy{max-width:780px;font-size:1.02rem;margin:0 0 2rem}.portfolio-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem;margin-top:2rem;align-items:start}.portfolio-card{background:#fff;border:1px solid var(--line);border-radius:24px;overflow:hidden;display:flex;flex-direction:column;min-height:594px;box-sizing:border-box}.portfolio-card img{width:100%;height:300px;object-fit:cover;display:block}.portfolio-copy{padding:1.5rem;display:flex;flex-direction:column;flex:1}.portfolio-meta{font-size:.75rem;letter-spacing:.12em;color:var(--sage-dark);font-weight:800;text-transform:uppercase}.portfolio-copy h3{font-size:1.3rem;margin:.55rem 0 .65rem;min-height:4.8rem}.portfolio-copy>p{font-size:.92rem;margin:0;min-height:5.4rem}.portfolio-more{margin-top:auto;padding-top:1rem}.portfolio-more summary{cursor:pointer;color:var(--sage-dark);font-weight:800}.portfolio-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:.45rem;margin-top:.9rem}.portfolio-gallery img{height:105px;border-radius:10px}.zoomable{display:block;cursor:zoom-in}.zoomable>img{transition:transform .18s ease,filter .18s ease}.zoomable:hover>img{transform:scale(1.015);filter:brightness(.94)}.lightbox{display:none;position:fixed;inset:0;z-index:99999;background:rgba(10,14,11,.92);padding:2rem;align-items:center;justify-content:center}.lightbox:target{display:flex}.lightbox-backdrop{position:absolute;inset:0;z-index:1}.lightbox img{position:relative;z-index:2;max-width:min(94vw,1400px);max-height:90vh;width:auto;height:auto;object-fit:contain;border-radius:12px;box-shadow:0 24px 70px rgba(0,0,0,.45)}.lightbox-close{position:fixed;z-index:100001;top:1.2rem;right:1.5rem;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:#fff;color:var(--ink);text-decoration:none;font:700 1.6rem/1 'DM Sans';box-shadow:0 6px 24px rgba(0,0,0,.25)}
.calculator-shell{background:#eef0eb;border:1px solid var(--line);border-radius:30px;padding:2.4rem;margin-top:2rem}.calculator-note{background:#fff7df;border:1px solid #ead8a4;border-radius:14px;padding:.85rem 1rem;color:#675b3a;font-size:.86rem;margin-bottom:1.4rem}
#calculateur{padding-bottom:.4rem}
.calc-ui-marker{height:0}
div[data-testid="stVerticalBlock"]:has(> div > .calc-ui-marker){background:#f3f1ec;border:1px solid #ddd9d1;border-radius:24px;padding:1.55rem 1.6rem 1.7rem;margin-top:1.35rem;box-shadow:0 10px 30px rgba(30,34,31,.035)}
div[data-testid="stVerticalBlock"]:has(> div > .calc-ui-marker) [data-testid="stSelectbox"]>div>div,
div[data-testid="stVerticalBlock"]:has(> div > .calc-ui-marker) [data-testid="stNumberInput"]>div>div{background:#fff!important;border-color:#d8d4cc!important}
div[data-testid="stVerticalBlock"]:has(> div > .calc-ui-marker) button{background:#fff;border-color:#d4d0c8;color:#303633}
div[data-testid="stVerticalBlock"]:has(> div > .calc-ui-marker) button:hover{border-color:#8c8175;color:#171c19}
#calculateur + div [data-testid="stHorizontalBlock"]{background:#f0f2ed;border:1px solid #dde2da;border-radius:20px;padding:.7rem .8rem;margin:.55rem 0}
#calculateur + div [data-testid="stSelectbox"]>div>div,#calculateur + div [data-testid="stNumberInput"] input{background:#fff!important}
#calculateur + div button{border-radius:12px}
.calculator-total{background:#fff;border:1px solid #ddd9d1;border-radius:18px;padding:1.25rem 1.5rem;margin-top:1.35rem;color:#171c19}

.calculator-total .label{color:#756f68;font-size:.7rem;font-weight:750;letter-spacing:.065em;text-transform:uppercase}
.calculator-total .price{font:700 clamp(1.75rem,3vw,2.45rem) 'Manrope';letter-spacing:-.035em;margin:.18rem 0;color:var(--ink)}
.calculator-disclaimer{font-size:.8rem;line-height:1.6;color:#6f6a64;margin:.75rem 0 0;max-width:900px}
.calculator-quote,.calculator-quote:link,.calculator-quote:visited{display:inline-flex;align-items:center;justify-content:center;margin-top:1.15rem;background:#2f3733;color:#fff!important;text-decoration:none!important;padding:.68rem 1rem;border:1px solid #2f3733;border-radius:999px;font-weight:750;font-size:.84rem;box-shadow:none}
.calculator-quote:hover,.calculator-quote:active{background:#171c19;border-color:#171c19;color:#fff!important;text-decoration:none!important}
.calc-row{background:#fff;border:1px solid var(--line);border-radius:18px;padding:1rem;margin:.7rem 0}.calc-row-title{font-weight:800;color:var(--ink);margin-bottom:.2rem}.calc-row-meta{font-size:.86rem;color:var(--muted)}.calc-field-label{font-size:.72rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#756f68;margin:0 0 .42rem}.calc-rate,.calc-subtotal{min-height:42px;display:flex;align-items:center;font-weight:750;white-space:nowrap}.calc-rate{color:#756a60}.calc-subtotal{color:var(--ink);font-size:1.02rem}.calc-remove-space{height:1.65rem}
button[kind="secondary"]{box-shadow:none!important}
div[data-testid="stButton"] button{transition:background .18s ease,border-color .18s ease}
.why{background:#e8ebe5;border-radius:30px;padding:3.4rem;margin:3rem 0}.why-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem;margin-top:2.2rem}.why-item{border-top:1px solid #bfc7bd;padding-top:1.2rem}.why-item h3{font-size:1.15rem;margin:.4rem 0}.big-cta{background:var(--ink);border-radius:30px;padding:4rem;margin:4rem 0;display:flex;align-items:center;justify-content:space-between;gap:2rem}.big-cta h2{color:#fff!important;font-size:clamp(2rem,4vw,3.2rem);margin:0 0 .6rem}.big-cta p{color:#cbd1cc;max-width:650px;margin:0}.big-cta a{white-space:nowrap;background:#fff;color:var(--ink);text-decoration:none;padding:1rem 1.3rem;border-radius:999px;font-weight:800}.contact-grid{align-items:flex-start}.contact-left{padding-top:0;min-height:580px;display:flex;flex-direction:column}.contact-left .contact-actions{margin-top:auto}.contact-response{margin:0 0 .8rem;padding:1rem 1.1rem;background:#eef0eb;border-radius:14px;color:var(--ink);font-size:.9rem;line-height:1.55}.contact-response strong{color:var(--sage-dark)}.contact-box{background:#fff;border:1px solid var(--line);border-radius:28px;padding:2rem}.stTextInput input,.stTextArea textarea{border-radius:12px!important;background:#fbfbf8!important}.stFormSubmitButton button{border-radius:999px!important;background:var(--ink)!important;color:#fff!important;border:0!important;font-weight:700!important}.stFormSubmitButton button p,.stFormSubmitButton button span{color:#fff!important}.stFormSubmitButton button:hover,.stFormSubmitButton button:focus{background:var(--sage-dark)!important;color:#fff!important}.stFormSubmitButton button:hover p,.stFormSubmitButton button:focus p{color:#fff!important}.site-footer{border-top:1px solid var(--line);margin-top:4rem;padding:2rem 0;display:flex;justify-content:space-between;align-items:flex-start;gap:2rem;color:var(--muted);font-size:.85rem}.footer-brand-text{font:800 1.35rem 'Manrope';letter-spacing:-.055em;color:var(--ink);margin-bottom:.35rem}.footer-brand-text span{color:var(--sage)}.footer-details{text-align:right;line-height:1.8}.footer-details a{color:var(--muted);text-decoration:none}.contact-details{line-height:1.9}.contact-details a{color:var(--ink);text-decoration:none}.contact-actions .whatsapp{background:#526553;color:#fff;border:1px solid #526553}.back-to-top{border:0;cursor:pointer;position:fixed;right:24px;bottom:24px;z-index:9999;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--ink);color:#fff!important;text-decoration:none;font:800 1.25rem 'Manrope';box-shadow:0 8px 24px rgba(23,32,27,.22);opacity:.92;transition:opacity .2s ease,transform .2s ease}.back-to-top:hover{opacity:1;transform:translateY(-2px)}
@media(max-width:800px){.back-to-top{right:14px;bottom:14px;width:42px;height:42px}.nav .pill{display:none}.contact-left{min-height:0;display:block}.contact-left .contact-actions{margin-top:1.4rem}.site-footer{flex-direction:column}.footer-details{text-align:left}.card{min-height:0}.card h3,.card>p,.portfolio-copy h3,.portfolio-copy>p{min-height:0}.card>details,.portfolio-more{margin-top:1rem}.nav>a:not(.pill){display:none}.lang-switch a{display:inline-block!important}.hero{padding:3rem 1.6rem;min-height:520px}.cards,.trustbar,.why-grid,.portfolio-grid,.process-grid{grid-template-columns:1fr}.portfolio-card img{height:280px}.big-cta{padding:2.3rem 1.6rem;flex-direction:column;align-items:flex-start}.why{padding:2.2rem 1.4rem}.calculator-shell{padding:1.3rem}.contact-actions{flex-wrap:wrap}.project-main,.project-small{min-height:320px}}
</style>
""",unsafe_allow_html=True)

st.markdown(f"""
<div id="page-top"></div><div class="topbar"><div class="brand">SIMETRIKA<span class="brand-dot">.</span></div><div class="nav"><a href="#services">{L['nav_services']}</a><a href="#calculateur">{L['nav_estimator']}</a><a href="#realisations">{L['nav_projects']}</a><a href="#apropos">{L['nav_about']}</a><a href="#contact">{L['nav_contact']}</a><span class="lang-switch"><a class="{'active' if lang=='fr' else ''}" href="?lang=fr">FR</a><a class="{'active' if lang=='de' else ''}" href="?lang=de">DE</a><a class="{'active' if lang=='en' else ''}" href="?lang=en">EN</a></span><a class="pill" href="#contact">{L['quote']}</a></div></div>
<div class="hero {'hero-de' if lang=='de' else ''}"><div class="eyebrow">{L['eyebrow']}</div><h1>{L['hero_title']}</h1><p>{L['hero_text']}</p><div class="hero-actions"><a class="btn btn-primary" href="#contact">{L['hero_cta']} →</a><a class="btn btn-secondary" href="#services">{L['hero_secondary']}</a><a class="btn btn-secondary" href="#calculateur">{L['nav_estimator']}</a></div></div>
<div class="trustbar"><div class="trust"><span>✓</span>{L['trust1']}</div><div class="trust"><span>✓</span>{L['trust2']}</div><div class="trust"><span>✓</span>{L['trust3']}</div></div>
<div id="services" class="section"><div class="kicker">{L['services_kicker']}</div><h2 class="section-title">{L['services_title']}</h2><p class="section-lead">{L['services_intro']}</p><div class="cards">
<div class="card"><div class="num">01</div><h3>{L['s1']}</h3><p>{L['s1d']}</p><details><summary class="service-link">{L['more']} ↓</summary><p class="service-detail">{L['s1more']}</p></details></div>
<div class="card"><div class="num">02</div><h3>{L['s2']}</h3><p>{L['s2d']}</p><details><summary class="service-link">{L['more']} ↓</summary><p class="service-detail">{L['s2more']}</p></details></div>
<div class="card"><div class="num">03</div><h3>{L['s3']}</h3><p>{L['s3d']}</p><details><summary class="service-link">{L['more']} ↓</summary><p class="service-detail">{L['s3more']}</p></details></div>
</div></div>
""",unsafe_allow_html=True)

# Complete, configurable estimator. Prices above are deliberately provisional.
st.markdown(f"""<div id="calculateur" class="section"><div class="kicker">{L['calc_kicker']}</div><h2 class="section-title">{L['calc_title']}</h2><p class="section-lead">{L['calc_intro']}</p><div class="calc-ui-marker"></div>""", unsafe_allow_html=True)

if "calc_rows" not in st.session_state:
    st.session_state.calc_rows = [{"work":"peinture","qty":50.0}]

# Localized flat option labels; category remains visible in the label.
option_labels = {}
for group_key, work_ids in WORK_GROUPS:
    for wid in work_ids:
        option_labels[wid] = f"{L[group_key]} · {L['work_'+wid]}"

for idx, row in enumerate(list(st.session_state.calc_rows)):
    st.markdown('<div class="calc-row-start"></div>', unsafe_allow_html=True)
    cols = st.columns([2.5, 1.05, .95, 1.25, .38], gap="small")
    work_ids = list(PRICE_CONFIG.keys())
    current_index = work_ids.index(row["work"]) if row["work"] in work_ids else 0
    with cols[0]:
        selected = st.selectbox(L["calc_work"], work_ids, index=current_index, format_func=lambda x: option_labels[x], key=f"calc_work_{idx}")
    cfg = PRICE_CONFIG[selected]
    with cols[1]:
        qty = st.number_input(L["calc_qty"], min_value=0.0, max_value=10000.0, value=float(row.get("qty",1.0)), step=1.0, key=f"calc_qty_{idx}")
    unit_label = L["unit_m2"] if cfg["unit"]=="m²" else L["unit_ml"] if cfg["unit"]=="ml" else L["unit_pc"]
    with cols[2]:
        st.markdown(f"<div class='calc-field-label'>{L['calc_rate']}</div><div class='calc-rate'>{cfg['min']:,.0f}–{cfg['max']:,.0f} € / {unit_label}</div>".replace(",", " "), unsafe_allow_html=True)
    low, high = qty*cfg["min"], qty*cfg["max"]
    with cols[3]:
        st.markdown(f"<div class='calc-field-label'>{L['calc_line_total']}</div><div class='calc-subtotal'>{low:,.0f}–{high:,.0f} €</div>".replace(",", " "), unsafe_allow_html=True)
    with cols[4]:
        st.markdown("<div class='calc-remove-space'></div>", unsafe_allow_html=True)
        if st.button("×", key=f"calc_remove_{idx}", help=L["calc_remove"]):
            st.session_state.calc_rows.pop(idx)
            st.rerun()
    st.session_state.calc_rows[idx] = {"work":selected,"qty":qty}

add_col, reset_col = st.columns([1,4])
with add_col:
    if st.button("+ "+L["calc_add"], key="calc_add"):
        st.session_state.calc_rows.append({"work":"peinture","qty":10.0})
        st.rerun()

total_low = sum(r["qty"]*PRICE_CONFIG[r["work"]]["min"] for r in st.session_state.calc_rows)
total_high = sum(r["qty"]*PRICE_CONFIG[r["work"]]["max"] for r in st.session_state.calc_rows)
if st.session_state.calc_rows:
    total_txt = f"{total_low:,.0f} – {total_high:,.0f} €".replace(",", " ")
    st.markdown(f"""<div class="calculator-total"><div class="label">{L['calc_total']}</div><div class="price">{total_txt}</div></div><p class="calculator-disclaimer">{L['calc_disclaimer']}</p><a class="calculator-quote" href="#contact">{L['calc_quote']} →</a>""", unsafe_allow_html=True)
else:
    st.info(L["calc_empty"])
st.markdown("</div>", unsafe_allow_html=True)

st.markdown(f"""
<div id="realisations" class="section"><div class="kicker">{L['portfolio_kicker']}</div><h2 class="section-title">{L['portfolio_title']}</h2><p class="section-lead">{L['portfolio_intro']}</p><div class="portfolio-grid">
<div class="portfolio-card"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-08.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-08.webp" alt="Rénovation de toiture à Langsur"></a><div class="portfolio-copy"><div class="portfolio-meta">{L['roof_meta']}</div><h3>{L['roof_title']}</h3><p>{L['roof_desc']}</p><details class="portfolio-more"><summary>{L['view_project']} ↓</summary><div class="portfolio-gallery"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-01.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-01.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-06.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-06.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-07.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-07.webp"></a></div></details></div></div>
<div class="portfolio-card"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-04.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-04.webp" alt="Rénovation de cuisine"></a><div class="portfolio-copy"><div class="portfolio-meta">{L['kitchen_meta']}</div><h3>{L['kitchen_title']}</h3><p>{L['kitchen_desc']}</p><details class="portfolio-more"><summary>{L['view_project']} ↓</summary><div class="portfolio-gallery"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-02.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-02.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-03.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-03.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-05.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-05.webp"></a></div></details></div></div>
<div class="portfolio-card"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-02.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-02.webp" alt="Aménagement d’une terrasse autour d’une piscine"></a><div class="portfolio-copy"><div class="portfolio-meta">{L['pool_meta']}</div><h3>{L['pool_title']}</h3><p>{L['pool_desc']}</p><details class="portfolio-more"><summary>{L['view_project']} ↓</summary><div class="portfolio-gallery"><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-06.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-06.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-07.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-07.webp"></a><a class="zoomable" href="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-03.webp" target="_blank" aria-label="Agrandir l’image"><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-03.webp"></a></div></details></div></div>
</div></div>
<div id="lb-toit-main" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-08.webp" alt="Rénovation de toiture à Langsur"></div><div id="lb-toit-1" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-01.webp" alt="Rénovation de toiture à Langsur"></div><div id="lb-toit-2" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-06.webp" alt="Rénovation de toiture à Langsur"></div><div id="lb-toit-3" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/toiture-langsur-07.webp" alt="Rénovation de toiture à Langsur"></div><div id="lb-cuisine-main" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-04.webp" alt="Rénovation de cuisine"></div><div id="lb-cuisine-1" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-02.webp" alt="Rénovation de cuisine"></div><div id="lb-cuisine-2" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-03.webp" alt="Rénovation de cuisine"></div><div id="lb-cuisine-3" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/cuisine-05.webp" alt="Rénovation de cuisine"></div><div id="lb-piscine-main" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-02.webp" alt="Terrasse autour d’une piscine"></div><div id="lb-piscine-1" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-06.webp" alt="Terrasse autour d’une piscine"></div><div id="lb-piscine-2" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-07.webp" alt="Terrasse autour d’une piscine"></div><div id="lb-piscine-3" class="lightbox"><a class="lightbox-backdrop" href="#realisations" target="_self" aria-label="Fermer"></a><a class="lightbox-close" href="#realisations" target="_self" aria-label="Fermer">×</a><img src="https://raw.githubusercontent.com/csmlr45/simetrika/main/assets/piscine-terrasse-03.webp" alt="Terrasse autour d’une piscine"></div>\n<div id="processus" class="section"><div class="kicker">{L['process_kicker']}</div><h2 class="section-title">{L['process_title']}</h2><p class="section-lead">{L['process_intro']}</p><div class="process-grid"><div class="process-step"><h3>{L['p1']}</h3><p>{L['p1d']}</p></div><div class="process-step"><h3>{L['p2']}</h3><p>{L['p2d']}</p></div><div class="process-step"><h3>{L['p3']}</h3><p>{L['p3d']}</p></div><div class="process-step"><h3>{L['p4']}</h3><p>{L['p4d']}</p></div></div></div>
<div id="apropos" class="why"><div class="kicker">{L['why_kicker']}</div><h2 class="section-title">{L['why_title']}</h2><p class="about-copy">{L['about_text']}</p></div>
<div class="big-cta"><div><h2>{L['cta_title']}</h2><p>{L['cta_text']}</p></div><a href="#contact">{L['cta_button']} →</a></div>
""",unsafe_allow_html=True)


st.markdown('<a id="back-to-top" class="back-to-top" href="#page-top" aria-label="Retour en haut">↑</a>', unsafe_allow_html=True)

components.html("""
<script>
const doc = window.parent.document;
try { delete window.parent.__simetrikaDelegatedNavBound; } catch (_) {}

function closeSimetrikaLightbox(){
  const old = doc.getElementById('simetrika-js-lightbox');
  if(old) old.remove();
}
function openSimetrikaLightbox(src, alt){
  closeSimetrikaLightbox();
  const box = doc.createElement('div');
  box.id='simetrika-js-lightbox';
  box.style.cssText='position:fixed;inset:0;z-index:999999;background:rgba(10,14,11,.94);display:flex;align-items:center;justify-content:center;padding:32px;box-sizing:border-box;';
  const img=doc.createElement('img');
  img.src=src; img.alt=alt||'';
  img.style.cssText='max-width:94vw;max-height:90vh;width:auto;height:auto;object-fit:contain;border-radius:12px;box-shadow:0 24px 70px rgba(0,0,0,.45);';
  const close=doc.createElement('button');
  close.type='button'; close.innerHTML='×'; close.setAttribute('aria-label','Fermer');
  close.style.cssText='position:fixed;top:18px;right:22px;z-index:1000000;width:48px;height:48px;border:0;border-radius:50%;background:white;color:#17201b;font:700 28px/1 sans-serif;cursor:pointer;box-shadow:0 6px 24px rgba(0,0,0,.25);';
  close.onclick=(e)=>{e.stopPropagation();closeSimetrikaLightbox();};
  img.onclick=(e)=>e.stopPropagation();
  box.onclick=closeSimetrikaLightbox;
  box.appendChild(img); box.appendChild(close); doc.body.appendChild(box);
}
doc.querySelectorAll('a.zoomable').forEach(a=>{
  a.onclick=(e)=>{e.preventDefault();openSimetrikaLightbox(a.href,a.querySelector('img')?.alt);};
});
if(!window.parent.__simetrikaEscBound){
  doc.addEventListener('keydown',e=>{if(e.key==='Escape')closeSimetrikaLightbox();});
  window.parent.__simetrikaEscBound=true;
}
</script>
""", height=0, width=0)

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
left,right=st.columns([.8,1.2],gap="large", vertical_alignment="top")
with left:
 st.markdown(f"""<div class="contact-left"><div class="kicker">{L['contact_kicker']}</div><h2 class="section-title">{L['contact_title']}</h2><p class="section-lead">{L['contact_text']}</p><p class="contact-details"><strong>Simetrika Sàrl</strong><br>1 rue Ermesinde<br>L-1469 Luxembourg<br><br><a href="mailto:contact@simetrika.lu"><strong>contact@simetrika.lu</strong></a></p><div class="contact-actions"><a class="dark" href="#contact">{L['quote']}</a><a class="whatsapp" href="https://wa.me/352691115110" target="_blank" rel="noopener">WhatsApp</a><a class="outline" href="mailto:contact@simetrika.lu">{L['email_btn']}</a></div></div>""",unsafe_allow_html=True)
with right:
 st.markdown(f"""<div style="height:2.15rem"></div><div class="contact-response"><strong>✓</strong> {L['response_24h']}</div>""", unsafe_allow_html=True)
 with st.form("contact_form",clear_on_submit=True):
  name=st.text_input(L["name"]);email=st.text_input(L["email"]);phone=st.text_input(L["phone"]);project=st.text_area(L["project"],placeholder=L["project_ph"],height=150)
  if st.form_submit_button(L["send"]+" →"):
   if name and (email or phone) and project: st.success(L["form_success"])
   else: st.warning(L["form_warning"])
st.markdown(f"""<div class="site-footer"><div class="footer-brand"><div class="footer-brand-text">SIMETRIKA<span>.</span></div><span>{L['footer_tagline']}</span></div><div class="footer-details"><strong>Simetrika Sàrl</strong><br>1 rue Ermesinde · L-1469 Luxembourg<br><a href="mailto:contact@simetrika.lu">contact@simetrika.lu</a><br>© 2026</div></div>""",unsafe_allow_html=True)
