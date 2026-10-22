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

NAV = [("/#creators", "Creators"), ("/#work", "Work"), ("/#about", "About"), ("/#contact", "Contact")]

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
        "photo_alt": "Preston Young checking a camera on a Melbourne street",
        "knows_about": ["Self-growth", "Lifestyle", "Student life", "Fitness"],
        "same_as": ["https://www.instagram.com/by.preston/"],
    },
]

HOME = {
    "title": "MANA | Influencer and content creator management, Melbourne, Australia",
    "description": ("MANA is a Melbourne influencer and talent management agency. We represent Australian content creators "
                    "Hugo Zbor, Kevin Chiang and Preston Young and run brand partnerships end to end."),
    "h1": "Talent management for creators.",
    "lede_html": ("MANA is an influencer and talent management agency in Melbourne, Australia. "
                  "We represent Hugo Zbor, Kevin Chiang and Preston Young, and run their brand work from brief to final post."),
    "proof": ("Kevin’s organic reel for Suapp drove 100+ paid sign-ups. Converse booked Hugo twice. "
              "We keep the roster small, so every creator gets real management and every brand deals with one person."),
    "brands_h": "For brands",
    "brands_p": ("Send us the product and the goal, or ask for a media kit. We reply with the creator who fits, "
                 "their audience and options for your campaign. Deliverables, usage rights and dates go in writing "
                 "before anything is filmed."),
    "creators_h": "For creators",
    "creators_p": ("We take on a few creators at a time and handle the brand side: pitching, negotiating, contracts, "
                   "deadlines and getting paid."),
    "contact_h": "Work with us.",
    "contact_sub": "Ask for a media kit or send a brief. You\u2019ll hear back from shei@mana-mgmt.com, usually within a day.",
}

# Work stills, all from closed deals or the creator's own reels.
WORK = [
    {"image": "work-converse-1.webp", "brand": "Converse", "creator": "Hugo Zbor", "what": "Green-screen campaign video",
     "alt": "Hugo Zbor seated above a city skyline in his green-screen video for Converse"},
    {"image": "work-kevin-reel.webp", "brand": "Branded reel", "creator": "Kevin Chiang", "what": "5 tools you should know as an architecture student",
     "alt": "Kevin Chiang sketching at his desk, from his reel on tools for architecture students"},
    {"image": "work-named-collective.webp", "brand": "Named Collective", "creator": "Hugo Zbor", "what": "LOCK IN campaign video",
     "alt": "Figure in a fur-trimmed coat from Hugo Zbor's LOCK IN video for Named Collective"},
    {"image": "work-converse-2.webp", "brand": "Converse", "creator": "Hugo Zbor", "what": "Campaign video #2",
     "alt": "Hugo Zbor at a robotic workstation in his second Converse video"},
    {"image": "work-lowheads.webp", "brand": "Lowheads", "creator": "Hugo Zbor", "what": "Dynamic magazine, issue #01",
     "alt": "Cover of the Lowheads underground marketplace magazine designed by Hugo Zbor"},
    {"image": "work-ultralight.webp", "brand": "Ultralight LDN", "creator": "Hugo Zbor", "what": "FIFA street style video",
     "alt": "Figure in a striped jumper in a stadium, from Hugo Zbor's video for Ultralight LDN"},
]

# Closed, public-safe partners across the roster (deal audit 20 Oct 2026, media kits). Oner is NDA: never add.
BRANDS = ["Converse", "ASICS", "Ultrahuman", "Starface", "Named Collective", "Meliora", "Lowheads", "Good Optiks",
          "Ultralight LDN", "8illy", "D5 Render", "Enscape", "Corel", "Suapp", "Chief", "Status Audio", "Astropad",
          "Element Brooklyn", "Secretlab", "MakeUGC"]

FAQ = [
    ("What is MANA?",
     "MANA is an influencer and talent management agency based in Melbourne, Australia. We represent content creators and handle their "
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
    ("MANA", [("Work", "/#work"), ("About", "/#about"), ("Get a media kit", "/#contact")]),
    ("Contact", [("shei@mana-mgmt.com", "mailto:shei@mana-mgmt.com"), ("Instagram", "https://www.instagram.com/manamgmt/")]),
]
