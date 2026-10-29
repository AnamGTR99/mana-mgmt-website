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

# Consistency card (29 Oct 2026): the same strings wherever MANA is listed, on this site or elsewhere.
COMPANY = {
    "name": "MANA", "locality": "Melbourne", "region": "VIC", "country": "Australia",
    "email": "shei@manacreators.com",
    "site": "https://www.mana-mgmt.com", "founded": "2026-04", "instagram": "https://www.instagram.com/manamgmt/",
    "legal": ("MANA is the trading name of a talent management business run by Sheik Anam Milfer from Melbourne, "
              "Victoria, Australia, since April 2026."),
}

# The person behind the site. Facts from Anam (anam.info/about, 30 Oct 2026). Nothing invented.
FOUNDER = {
    "name": "Sheik Anam Milfer", "short": "Shei", "slug": "shei",
    "job_title": "Founder and talent manager",
    "one_line": "Founder of MANA. Manages the roster and builds the agency\u2019s own tools.",
    "bio": [
        "MANA is run by Shei (Sheik Anam Milfer), who started it in Melbourne in April 2026 and manages the roster himself. "
        "Born and raised in Hong Kong, based in Melbourne.",
        "He is an engineer by training and builds the agency\u2019s own systems for briefs, deals and approvals. "
        "That is why brands deal with one person from the first email to the final post, and why nothing a brand "
        "agreed to gets lost between the brief and the live date.",
    ],
    "photo": "/assets/img/shei.webp",
    "photo_alt": "Shei, founder of MANA, at a rooftop table in Melbourne at night",
    "links": [("LinkedIn", "https://www.linkedin.com/in/sheik-anam-milfer-9aa15b213/"),
              ("Instagram", "https://www.instagram.com/sheivault/"),
              ("anam.info", "https://www.anam.info")],
    "knows_about": ["Talent management", "Brand partnerships", "Creator contracts and usage rights", "Software engineering"],
}

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
        "key": "hugo", "slug": "hugo-zbor", "followers": "64K", "name": "Hugo Zbor", "handle": "@hugozbor",
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
        "key": "kevin", "slug": "kevin-chiang", "followers": "14K", "name": "Kevin Chiang", "handle": "@kevnchiang",
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
        "key": "preston", "slug": "preston-young", "followers": "23K", "name": "Preston Young", "handle": "@by.preston",
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
     "Use the form on this page or email shei@manacreators.com. We send the creator’s media kit with audience data "
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
    ("Contact", [("Contact and details", "/contact"), ("shei@manacreators.com", "mailto:shei@manacreators.com"),
                 ("Instagram", "https://www.instagram.com/manamgmt/")]),
]


# ---------------------------------------------------------------------------
# Interior pages (SEO / GEO). Same fact rules as above: only figures from the Facts files,
# media kits and closed deals. No prices. Each page opens with a plain, quotable definition.
# ---------------------------------------------------------------------------

NAV = [("/creators", "Creators"), ("/brands", "For brands"), ("/ugc-creators-australia", "UGC"), ("/about", "About")]

FOOTER = [
    ("Creators", [("All creators", "/creators"), ("Hugo Zbor", "/creators/hugo-zbor"), ("Kevin Chiang", "/creators/kevin-chiang"),
                  ("Preston Young", "/creators/preston-young")]),
    ("MANA", [("For brands", "/brands"), ("UGC creators", "/ugc-creators-australia"), ("About", "/about"), ("Get a media kit", "/#contact")]),
    ("Contact", [("Contact and details", "/contact"), ("shei@manacreators.com", "mailto:shei@manacreators.com"),
                 ("Instagram", "https://www.instagram.com/manamgmt/")]),
]

PROFILES = {
    "hugo": {
        "title": "Hugo Zbor | Melbourne creative director and content creator | MANA",
        "description": ("Hugo Zbor is a Melbourne creative director known for green-screen concept films for Converse, ASICS "
                        "and Named Collective. Managed by MANA. Get his media kit."),
        "eyebrow": "Creative direction, green-screen and 3D · Melbourne",
        "lede": ("Hugo Zbor is a Melbourne-based creative director and content creator, managed by MANA. He makes "
                 "green-screen concept films, motion, 3D and print for brands, labels and artists, from the first idea "
                 "to the final composite."),
        "facts": [("Instagram", "@hugozbor"), ("TikTok", "@hugozbor"), ("Based in", "Melbourne, Australia"),
                  ("Makes", "Concept films, motion and CGI, print and identity, websites"),
                  ("Projects shipped", "40+ (media kit, July 2026)"), ("Website", "hugozbor.com")],
        "brands": ["Converse", "ASICS", "Named Collective", "Starface", "Meliora", "Lowheads", "Good Optiks", "Ultralight LDN", "8illy"],
        "highlights": [
            "Converse commissioned a green-screen video, then booked Hugo again for a second.",
            "Concept, shoot direction and the full composite come from one person, so the work holds together.",
            "His most frequent collaborator has come back seven times.",
        ],
        "gallery": [("work-converse-1.webp", "Converse", "Green-screen campaign video"),
                    ("work-converse-2.webp", "Converse", "Campaign video #2"),
                    ("work-named-collective.webp", "Named Collective", "LOCK IN campaign video"),
                    ("work-lowheads.webp", "Lowheads", "Dynamic magazine, issue #01"),
                    ("work-ultralight.webp", "Ultralight LDN", "FIFA street style video")],
        "fit": "Product drops, campaign launches, streetwear, footwear, music and any brand that wants a visual world, not a template.",
        "faq": [
            ("What does Hugo Zbor make?", "Green-screen concept films and composites, motion and CGI, print and identity work "
             "such as cover art and magazines, and art-directed websites."),
            ("Which brands has Hugo Zbor worked with?", "Converse (twice), ASICS, Named Collective, Starface, Meliora, Lowheads, "
             "Good Optiks, Ultralight LDN and 8illy, plus independent labels and artists."),
            ("How do I book Hugo Zbor?", "Ask MANA for his media kit using the form below or at shei@manacreators.com. "
             "Every project is scoped to the brief and quoted for your exact deliverables."),
        ],
    },
    "kevin": {
        "title": "Kevin Chiang | Architecture and design content creator, Melbourne | MANA",
        "description": ("Kevin Chiang is a Melbourne architecture and design creator with 928K+ monthly views, 92% from non-followers. "
                        "One reel drove 100+ paid sign-ups for Suapp. Managed by MANA."),
        "eyebrow": "Architecture, design and lifestyle · Melbourne",
        "lede": ("Kevin Chiang is a Melbourne architecture and design content creator, managed by MANA. His Instagram reels "
                 "reach design students, young architects and creatives: 928K+ monthly views, 92% of them from non-followers."),
        "facts": [("Instagram", "@kevnchiang"), ("Based in", "Melbourne, Australia"),
                  ("Content", "Architecture, design, student life, tech, lifestyle"),
                  ("Reach", "928K+ monthly views · 40K average reel views · 359K unique viewers in 30 days"),
                  ("Audience", "88% aged 18 to 34 · 49% men, 51% women"),
                  ("Top markets", "India 12.1% · Australia 9.2% · United States 6.9% · #1 city Melbourne"),
                  ("Source", "Instagram insights, 30 days, June 2026")],
        "brands": ["Suapp", "D5 Render", "Enscape", "Corel", "Chief", "Status Audio", "Astropad", "Element Brooklyn",
                   "Ultrahuman", "Secretlab", "Genetix Nutrition", "MakeUGC"],
        "highlights": [
            "Suapp: one organic reel showing its SketchUp plug-in reached 490K+ views and drove 100+ paid sign-ups, with no boost and no whitelisting.",
            "“5 tools you should know as an architecture student”: 161K views and 11K saves, and 25 sign-ups for a mobile app.",
            "45+ brand partnerships across design software, tech and lifestyle.",
        ],
        "gallery": [("work-kevin-reel.webp", "Branded reel", "5 tools you should know as an architecture student")],
        "fit": "Design and 3D software, apps and SaaS for students and creatives, tech, desk setups and lifestyle brands.",
        "faq": [
            ("Who watches Kevin Chiang?", "Design students, young architects and creatives. 88% of his audience is aged 18 to 34, "
             "split evenly between men and women, with India, Australia and the US as top markets."),
            ("Does Kevin Chiang's content drive sign-ups?", "Yes. One organic reel for Suapp drove 100+ paid sign-ups, and a "
             "branded reel on architecture tools drove 25 app sign-ups."),
            ("How do I book Kevin Chiang?", "Ask MANA for his media kit using the form below or at shei@manacreators.com. "
             "Rates are quoted for your exact deliverables."),
        ],
    },
    "preston": {
        "title": "Preston Young | Lifestyle and self-growth creator, Melbourne | MANA",
        "description": ("Preston Young is a Melbourne lifestyle and self-growth creator: 1.86M views and 1.09M unique viewers in "
                        "90 days, and a 2.9M-view reel. Managed by MANA."),
        "eyebrow": "Life lessons, lifestyle and self-growth · Melbourne",
        "lede": ("Preston Young is a Melbourne lifestyle and self-growth content creator, managed by MANA. His cinematic, "
                 "story-led reels on life lessons, student life and training reached 1.86M views and 1.09M unique viewers in 90 days."),
        "facts": [("Instagram", "@by.preston"), ("Based in", "Melbourne, Australia · student at the University of Melbourne"),
                  ("Content", "Life lessons, self-growth, day in the life, student life, fitness, Asian culture"),
                  ("Reach", "1.86M views · 81K average reel views · 86.6% non-follower reach"),
                  ("Audience", "Two in three aged 18 to 34 · 65% men, 35% women"),
                  ("Top markets", "United States 18.0% · Philippines 16.1% · Indonesia 7.2% · #1 city Singapore"),
                  ("Source", "Instagram insights, 90 days, June to September 2026")],
        "brands": [],
        "highlights": [
            "“Ichi-go Ichi-e” reached 2.9M views, with 58.2K shares, 284.3K likes and 30K reposts.",
            "“One of the hardest lessons I’ve learned” reached 1.0M views and 22.3K reposts.",
            "Six reels past 750K views in the last 12 months.",
        ],
        "gallery": [],
        "fit": "Lifestyle, wellness, fitness, education and apps for young adults, especially brands reaching the US and Southeast Asia.",
        "faq": [
            ("Who watches Preston Young?", "Young adults: two in three viewers are aged 18 to 34, 65% are men, and the top markets "
             "are the United States, the Philippines and Indonesia."),
            ("What does Preston Young make for brands?", "Sponsored reels, whitelisting, UGC, affiliate and ambassador "
             "partnerships, and product reviews, in the same cinematic, story-led style as his own reels."),
            ("How do I book Preston Young?", "Ask MANA for his media kit using the form below or at shei@manacreators.com. "
             "Rates are quoted for your exact deliverables."),
        ],
    },
}

CREATORS_PAGE = {
    "title": "Australian content creators and influencers | MANA talent management",
    "description": ("Meet the Melbourne-based content creators MANA represents: Hugo Zbor, Kevin Chiang and Preston Young. "
                    "Audiences, results and brands, plus media kits on request."),
    "eyebrow": "Creators",
    "h1": "Australian content creators, managed by MANA.",
    "lede": ("MANA represents three Melbourne-based content creators and influencers, each with an audience that watches to "
             "the end. Every creator has a media kit with audience data; ask for it and we reply within a day."),
    "followers_note": "Instagram follower counts, updated October 2026.",
    "fit_h": "Which creator fits your brand?",
    "fit": [("Design software, apps, tech, desk setups", "Kevin Chiang"),
            ("Drops, campaign films, streetwear, footwear, music", "Hugo Zbor"),
            ("Lifestyle, wellness, fitness, education, young adults in the US and Asia", "Preston Young")],
    "faq": [
        ("Are MANA's creators based in Australia?", "Yes. Hugo Zbor, Kevin Chiang and Preston Young are all based in Melbourne. "
         "Their audiences are global, and they work with brands in Australia and around the world."),
        ("Can I book more than one creator?", "Yes. Ask for all three media kits and tell us the campaign; we'll suggest the "
         "creator or combination that fits."),
    ],
}

BRANDS_PAGE = {
    "title": "Hire Australian content creators for your brand | MANA",
    "description": ("Work with Melbourne content creators through MANA: creator matching, scope, contracts and usage rights, "
                    "production and posting, handled by one point of contact."),
    "eyebrow": "For brands",
    "h1": "Work with Australian content creators.",
    "lede": ("MANA runs creator partnerships end to end: we match your brief to the right creator, put the scope and usage "
             "rights in writing, manage production and approvals, and make sure the content goes live on the agreed date."),
    "book_h": "What you can book",
    "book": ["Sponsored Instagram Reels, carousels and stories", "UGC for your own channels and ads",
             "Partnership ads and whitelisting", "Product reviews and launches", "Ambassador and affiliate partnerships",
             "Concept films with motion and 3D (Hugo Zbor)"],
    "steps": [("Send a brief", "Or just the product, the audience and the goal. We usually reply within a day."),
              ("Get the media kit", "The creator who fits, their audience data and the options for your campaign."),
              ("Agree the scope", "Deliverables, revision rounds, usage period, whitelisting, exclusivity and the live date, in writing."),
              ("Content goes live", "Drafts land on the agreed dates and the post goes live on time.")],
    "writing_h": "What we put in writing before anything is filmed",
    "writing": [("Deliverables", "Exactly what gets made, for which platform."), ("Revision rounds", "How many, and when they're due."),
                ("Usage rights", "Where you can use the content, and for how long."), ("Whitelisting", "Whether you can run it as an ad from the creator's handle."),
                ("Exclusivity", "Whether the creator holds off on competitors, and for how long."), ("Dates", "Draft, approval and live dates.")],
    "faq": [
        ("Do you publish creator rates?", "No. Rates depend on deliverables, usage and exclusivity, so we quote for your exact scope "
         "and send it with the media kit."),
        ("Do you work with brands outside Australia?", "Yes. Our creators have made work for brands in Australia, the US, the UK and "
         "Europe, including Converse, ASICS, Ultrahuman and D5 Render."),
        ("Can your creators make content for our ads?", "Yes. They make UGC for brand channels and can license organic posts for "
         "paid use or whitelisting. See UGC creators in Australia."),
        ("How quickly do you reply?", "Usually within a day. Every brief gets a real answer, including when none of our creators fit."),
    ],
}

UGC_PAGE = {
    "title": "UGC creators in Australia | MANA talent management",
    "description": ("MANA represents Melbourne UGC creators who make videos for your brand's channels and ads, with usage rights "
                    "agreed up front. Kevin Chiang, Preston Young and Hugo Zbor."),
    "eyebrow": "UGC creators · Australia",
    "h1": "UGC creators in Australia.",
    "lede": ("UGC (user-generated content) is content a creator makes for a brand to post on its own channels or run as ads, "
             "rather than on the creator's feed. MANA represents Melbourne-based creators who make UGC as well as sponsored posts, "
             "with usage rights agreed before filming."),
    "vs_h": "UGC or a sponsored post?",
    "vs": [("Where it runs", "Your channels and ads", "The creator's Instagram"),
           ("Whose audience", "Yours, or paid reach", "The creator's audience"),
           ("What you get", "Raw footage or an edited video", "A live post, plus insights"),
           ("Usage", "Licensed for an agreed period", "Organic; paid use or whitelisting is an add-on")],
    "who_h": "Our UGC creators",
    "who": [("kevin", "Raw footage and edited reels for design software, apps, tech and lifestyle. Delivered UGC for Chief and MakeUGC."),
            ("preston", "Cinematic lifestyle, fitness and self-growth videos for brands reaching young adults."),
            ("hugo", "Concept films and composites for brand channels, when you want something nobody else has.")],
    "steps": [("Brief", "Product, audience, where it will run and the angle you want."),
              ("Script and shot list", "Agreed before filming, so the first draft is close."),
              ("Filming and edit", "Raw footage, an edited cut, or both."),
              ("Usage", "Paid usage licensed for 3, 6 or 12 months, agreed in writing.")],
    "faq": [
        ("What is UGC?", "User-generated content: photos or videos a creator makes for a brand to use on its own channels or in ads. "
         "It looks native to social feeds because a real creator makes it."),
        ("How are usage rights handled for UGC?", "The usage period (for example 3, 6 or 12 months), the channels and whether it runs "
         "as paid ads are agreed in writing before filming."),
        ("Can I get raw footage?", "Yes. Kevin Chiang delivers raw footage or fully edited reels, and Preston Young offers UGC "
         "in his cinematic style."),
    ],
}

ABOUT_PAGE = {
    "title": "About MANA | Influencer and talent management agency, Melbourne",
    "description": ("MANA is an influencer and talent management agency in Melbourne, Australia, started in April 2026. A small roster, "
                    "one point of contact, and everything agreed in writing."),
    "eyebrow": "About",
    "h1": "About MANA.",
    "lede": ("MANA is an influencer and talent management agency in Melbourne, Australia, started in April 2026. We represent content "
             "creators Hugo Zbor, Kevin Chiang and Preston Young and run their brand partnerships from brief to final post."),
    "who_h": "Who runs MANA",
    "points": [("A small roster", "We take on a few creators at a time, so each one gets real management and every brand gets a fast answer."),
               ("One point of contact", "Brands deal with MANA from the first email to the final post. Creators get to create."),
               ("Everything in writing", "Deliverables, revisions, usage rights and dates are agreed before anything is filmed."),
               ("Built like a product", "MANA is run by an engineer, Shei, who builds the agency's own tools so no brief, date or approval gets lost.")],
    "faq": [
        ("Where is MANA based?", "Melbourne, Australia. We work with brands in Australia and around the world, mostly remotely."),
        ("Who runs MANA?", "MANA is run by its founder, Shei (Sheik Anam Milfer), an engineer who manages the roster and builds "
         "the agency's own systems for briefs, deals and approvals. He is based in Melbourne."),
        ("How do I contact MANA?", "Use the form below or email shei@manacreators.com. We usually reply within a day."),
    ],
}

CONTACT_PAGE = {
    "title": "Contact MANA | Melbourne influencer and talent management agency",
    "description": ("Contact MANA in Melbourne, Australia: shei@manacreators.com. Run by founder Sheik Anam Milfer. "
                    "Media kits, briefs and creator applications, usually answered within a day."),
    "eyebrow": "Contact",
    "h1": "Contact MANA.",
    "lede": ("One point of contact for media kits, briefs and creator applications. Email is fastest. We usually reply within "
             "a day, Melbourne time."),
    "facts": [("Email", "shei@manacreators.com", "mailto:shei@manacreators.com"),
              ("Based in", "Melbourne, Victoria, Australia", None),
              ("Instagram", "@manamgmt", "https://www.instagram.com/manamgmt/"),
              ("Run by", "Sheik Anam Milfer (Shei), founder", "/about#shei")],
    "legal_h": "Who you are dealing with",
    "legal": [
        "MANA is the trading name of a talent management business run by Sheik Anam Milfer from Melbourne, Victoria, "
        "Australia, since April 2026.",
        "MANA represents its creators under written management agreements and acts for them in brand partnerships. "
        "Deliverables, usage rights, exclusivity and dates are agreed in writing before anything is filmed. Rates are "
        "quoted for each scope and are not published.",
        "The email address above is read by Shei. There is no info@ or hello@ inbox.",
    ],
}
