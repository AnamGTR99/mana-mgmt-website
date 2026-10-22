"""Site copy and facts for mana-mgmt.com.

Every figure here must come from the vault: Mesh/MAIN/Outreach/FACTS/(Facts) <Name>.md, the creators'
media kits, or a closed deal in the commission sheets. No prices anywhere on the site (Anam, 22 Oct 2026).
Oner is under NDA: never list it.
"""

ORG_DESCRIPTION = ("MANA is an influencer and talent management agency in Melbourne, Australia. It represents Australian content creators "
                   "Hugo Zbor, Kevin Chiang and Preston Young and runs their brand partnerships from brief to final post.")

KNOWS_ABOUT = ["Talent management", "Creator management", "Influencer marketing", "Brand partnerships",
               "UGC (user-generated content)", "Instagram Reels", "Usage rights and whitelisting"]

ORG_SAMEAS = ["https://www.instagram.com/manamgmt/"]

NAV = [("/#creators", "Creators"), ("/#process", "For brands"), ("/#faq", "FAQ")]

NEEDS = [
    ("kit-all", "Media kits for all creators"),
    ("kit-hugo", "Media kit: Hugo Zbor"),
    ("kit-kevin", "Media kit: Kevin Chiang"),
    ("kit-preston", "Media kit: Preston Young"),
    ("brief", "I have a brief or campaign"),
    ("creator", "I’m a creator looking for management"),
    ("other", "Press or something else"),
]

CREATORS = [
    {
        "key": "hugo", "slug": "hugo-zbor", "name": "Hugo Zbor", "handle": "@hugozbor",
        "instagram": "https://www.instagram.com/hugozbor/",
        "niche": "Creative direction, green-screen and 3D",
        "job_title": "Creative director and content creator",
        "blurb": "Green-screen concept films for Converse, ASICS and Named Collective, from idea to final cut.",
        "stats": [("40+", "Projects shipped"), ("2×", "Converse videos")],
        "photo_alt": "Hugo Zbor standing in a white studio",
        "knows_about": ["Creative direction", "Green-screen video", "Motion design", "3D", "Streetwear"],
        "same_as": ["https://www.instagram.com/hugozbor/", "https://www.tiktok.com/@hugozbor", "https://hugozbor.com"],
    },
    {
        "key": "kevin", "slug": "kevin-chiang", "name": "Kevin Chiang", "handle": "@kevnchiang",
        "instagram": "https://www.instagram.com/kevnchiang/",
        "niche": "Architecture, design and lifestyle",
        "job_title": "Architecture and design content creator",
        "blurb": "Architecture and design content for students, young architects and creatives aged 18 to 34.",
        "stats": [("928K+", "Monthly views"), ("92%", "Non-follower reach")],
        "photo_alt": "Kevin Chiang building an architecture model at his desk",
        "knows_about": ["Architecture", "Design software", "Student life", "Lifestyle"],
        "same_as": ["https://www.instagram.com/kevnchiang/", "https://www.bykevinchiang.com"],
    },
    {
        "key": "preston", "slug": "preston-young", "name": "Preston Young", "handle": "@by.preston",
        "instagram": "https://www.instagram.com/by.preston/",
        "niche": "Life lessons, lifestyle and self-growth",
        "job_title": "Lifestyle and self-growth content creator",
        "blurb": "Cinematic, story-led reels on life lessons, student life and training.",
        "stats": [("1.86M", "Views in 90 days"), ("81K", "Average reel views")],
        "photo_alt": "Preston Young checking a camera on a Melbourne street",
        "knows_about": ["Self-growth", "Lifestyle", "Student life", "Fitness"],
        "same_as": ["https://www.instagram.com/by.preston/"],
    },
]

HOME = {
    "title": "MANA | Influencer and content creator management, Melbourne, Australia",
    "description": ("MANA is a Melbourne influencer and talent management agency. We represent Australian content creators "
                    "Hugo Zbor, Kevin Chiang and Preston Young and run brand partnerships end to end."),
    "eyebrow": "Influencer and talent management · Based in Australia, working globally",
    "h1": "Creators whose content gets watched, managed properly.",
    "lede_html": ("<b>MANA is an influencer and talent management agency in Melbourne, Australia</b>, "
                  "representing Hugo Zbor, Kevin Chiang and Preston Young."),
    "trust": "Worked with Converse, ASICS, Ultrahuman, D5 Render, Chief and more.",
    "roster_h": "Our creators",
    "roster_sub": "A small roster, so every creator gets real management.",
    "work_h": "Selected work",
    "work_sub": "Organic numbers from Instagram insights. No paid boosts.",
    "proc_h": "How it works",
    "proc_sub": "One point of contact from first email to final post.",
    "join_h": "Creators: looking for management?",
    "join_p": "We take on a few creators at a time and handle the brand side for them.",
    "contact_h": "Get a media kit",
    "contact_sub": "We’ll reply with the media kit, usually within a day.",
}

WORK = [
    {
        "who": "Kevin Chiang × Suapp", "title": "One reel, 100+ paid sign-ups",
        "body": "An organic reel showing Suapp’s SketchUp plug-in to architecture students. No boost.",
        "big": "100+", "big_label": "paid sign-ups from one reel",
        "chips": ["490K+ views", "29K saves"],
    },
    {
        "who": "Hugo Zbor × Converse", "title": "A green-screen film, then a second",
        "body": "Idea to final composite by one creative. Converse re-booked him for a second.",
        "image": "work-converse-hugo.webp", "image_alt": "Still from Hugo Zbor’s green-screen video for Converse",
        "chips": ["2 videos", "Re-booked"],
    },
    {
        "who": "Preston Young · organic", "title": "Ichi-go Ichi-e: 2.9M views",
        "body": "One idea told in under a minute. The reach a brand placement sits inside.",
        "big": "2.9M", "big_label": "views on one reel",
        "chips": ["58.2K shares", "284K likes"],
    },
]

# Marquee logos (file in src/assets/logos/, or None to show the name as text). Same brands as BRANDS.
BRAND_LOGOS = [("Converse", "converse.png"), ("ASICS", "asics.svg"), ("Ultrahuman", "ultrahuman.svg"),
               ("Starface", "starface.svg"), ("Named Collective", "named-collective.png"), ("D5 Render", "d5-render.png"),
               ("Chief", "chief.png"), ("Status Audio", "status-audio.svg"), ("Astropad", "astropad.svg"),
               ("Secretlab", "secretlab.png"), ("Meliora", "meliora.png"), ("Lowheads", "lowheads.png"),
               ("Good Optiks", "good-optiks.svg"), ("Ultralight LDN", "ultralight.png"), ("Enscape", "enscape.png"),
               ("Corel", "corel.svg"), ("Suapp", "suapp.png"), ("Element Brooklyn", "element-brooklyn.svg"),
               ("MakeUGC", "makeugc.png")]  # 8illy has no logo (YouTube channel), so it stays in BRANDS only

# Closed, public-safe partners across the roster (deal audit 20 Oct 2026, media kits). Oner is NDA: never add.
BRANDS = ["Converse", "ASICS", "Ultrahuman", "Starface", "Named Collective", "Meliora", "Lowheads", "Good Optiks",
          "Ultralight LDN", "8illy", "D5 Render", "Enscape", "Corel", "Suapp", "Chief", "Status Audio", "Astropad",
          "Element Brooklyn", "Secretlab", "MakeUGC"]

STEPS = [
    ("Send a brief", "Or just the product and the goal."),
    ("Get the media kit", "The creators who fit, with audience data."),
    ("Agree the scope", "Deliverables, usage and dates in writing."),
    ("Content goes live", "On the agreed date, revisions capped."),
]

FAQ = [
    ("What is MANA?",
     "MANA is a talent management agency based in Melbourne, Australia. We represent content creators and handle their "
     "brand partnerships: finding the right brands, scoping and negotiating deals, contracts and usage rights, "
     "deadlines and payment."),
    ("How do I find content creators and influencers in Australia for my brand?",
     "Tell us the product, the audience and the goal. MANA represents three Melbourne-based content creators across "
     "creative direction, architecture and design, and lifestyle and self-growth, and sends you the media kit of the "
     "creator who fits. If none of ours fit, we’ll tell you."),
    ("Which creators does MANA represent?",
     "Hugo Zbor (creative direction, green-screen concept films and 3D), Kevin Chiang (architecture, design and lifestyle) "
     "and Preston Young (life lessons, lifestyle and self-growth). All three are based in Melbourne."),
    ("Do you work with brands outside Australia?",
     "Yes. Our creators have made work for brands in Australia, the US, the UK and Europe, including Converse, ASICS, "
     "Ultrahuman and D5 Render. Most campaigns run remotely, with shoots in Melbourne."),
    ("What content can your creators make?",
     "Sponsored Instagram Reels, carousels and stories, UGC for your own channels, partnership ads and whitelisting, "
     "product reviews, and concept films with motion and 3D from Hugo Zbor."),
    ("How do I get a media kit or rates?",
     "Use the form on this page or email shei@mana-mgmt.com. We send the creator’s media kit with audience data "
     "and campaign options, and quote rates for your exact scope. We don’t publish prices."),
    ("I’m a creator. How do I join MANA?",
     "Choose “I’m a creator looking for management” in the form with your handle and a line about your "
     "content. We take on a few creators at a time and reply to every application."),
]

FOOTER_BLURB = ("Talent management for content creators. Based in Melbourne, working with brands in Australia "
                "and around the world.")

FOOTER = [
    ("Creators", [("Hugo Zbor", "/#hugo-zbor"), ("Kevin Chiang", "/#kevin-chiang"), ("Preston Young", "/#preston-young")]),
    ("MANA", [("For brands", "/#process"), ("FAQ", "/#faq"), ("Get a media kit", "/#contact")]),
    ("Contact", [("shei@mana-mgmt.com", "mailto:shei@mana-mgmt.com"), ("Instagram", "https://www.instagram.com/manamgmt/")]),
]
