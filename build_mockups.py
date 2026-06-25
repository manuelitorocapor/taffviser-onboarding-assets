import cairosvg, os

OUT = "/sessions/clever-practical-brown/mnt/outputs"

# ---------- Mockup 1: Fake Google security alert ----------
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="480" viewBox="0 0 600 480" font-family="Arial, Helvetica, sans-serif">
<rect width="600" height="480" fill="#f1f3f4"/>
<rect x="30" y="26" width="540" height="428" rx="12" fill="#ffffff"/>
<rect x="30" y="26" width="540" height="428" rx="12" fill="none" stroke="#e0e0e0"/>

<!-- subject -->
<text x="56" y="68" font-size="22" font-weight="bold" fill="#202124">Security alert</text>

<!-- from row -->
<circle cx="72" cy="104" r="18" fill="#e8eaed"/>
<text x="72" y="111" font-size="18" font-weight="bold" fill="#5f6368" text-anchor="middle">G</text>
<text x="100" y="100" font-size="14" font-weight="bold" fill="#202124">Google</text>
<rect x="98" y="108" width="214" height="20" rx="4" fill="#fde7e9" stroke="#d93025"/>
<text x="104" y="123" font-size="13" fill="#c5221f">&lt;no-reply@gooogle.com&gt;</text>
<text x="492" y="105" font-size="12" fill="#80868b">9:14 AM</text>
<line x1="56" y1="142" x2="544" y2="142" stroke="#eeeeee"/>

<!-- google wordmark -->
<g font-size="30" font-weight="bold" font-family="Arial, sans-serif">
<text x="248" y="190" fill="#4285F4">G</text>
<text x="268" y="190" fill="#EA4335">o</text>
<text x="286" y="190" fill="#FBBC05">o</text>
<text x="304" y="190" fill="#4285F4">g</text>
<text x="322" y="190" fill="#34A853">l</text>
<text x="330" y="190" fill="#EA4335">e</text>
</g>

<!-- shield -->
<path d="M300 212 l24 9 v17 c0 16 -11 27 -24 32 c-13 -5 -24 -16 -24 -32 v-17 z" fill="#fef7e0" stroke="#f9ab00" stroke-width="2"/>
<path d="M291 246 l6 6 l12 -13" fill="none" stroke="#f9ab00" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>

<text x="300" y="300" font-size="18" font-weight="bold" fill="#202124" text-anchor="middle">A new sign-in on Windows</text>
<text x="300" y="328" font-size="13.5" fill="#5f6368" text-anchor="middle">We noticed a new sign-in to your Google Account on a</text>
<text x="300" y="347" font-size="13.5" fill="#5f6368" text-anchor="middle">Windows device. If this wasn't you, secure your account now.</text>

<rect x="232" y="366" width="136" height="38" rx="6" fill="#1a73e8"/>
<text x="300" y="390" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Review activity</text>

<!-- callout -->
<rect x="56" y="416" width="488" height="26" rx="6" fill="#fce8e6"/>
<text x="68" y="433" font-size="12.5" fill="#c5221f">Look at the sender: <tspan font-weight="bold">gooogle.com</tspan> has an extra "o". The real domain is google.com</text>
</svg>'''

# ---------- Mockup 2: Spear phishing email ----------
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="480" viewBox="0 0 600 480" font-family="Arial, Helvetica, sans-serif">
<rect width="600" height="480" fill="#f1f3f4"/>
<rect x="30" y="26" width="540" height="428" rx="12" fill="#ffffff"/>
<rect x="30" y="26" width="540" height="428" rx="12" fill="none" stroke="#e0e0e0"/>

<text x="56" y="66" font-size="20" font-weight="bold" fill="#202124">Re: Project Northwind &#8212; approval needed</text>

<!-- from -->
<circle cx="72" cy="100" r="18" fill="#ff5330"/>
<text x="72" y="106" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">DR</text>
<text x="100" y="95" font-size="14" font-weight="bold" fill="#202124">Daniel Reyes (VP Finance)</text>
<rect x="98" y="103" width="232" height="20" rx="4" fill="#fde7e9" stroke="#d93025"/>
<text x="104" y="118" font-size="13" fill="#c5221f">&lt;d.reyes@staffviser-finance.com&gt;</text>
<text x="486" y="100" font-size="12" fill="#80868b">8:52 AM</text>
<text x="100" y="138" font-size="12" fill="#80868b">to alex@staffviser.com</text>
<line x1="56" y1="152" x2="544" y2="152" stroke="#eeeeee"/>

<!-- body -->
<g font-size="14" fill="#3c4043">
<text x="56" y="184">Hi Alex,</text>
<text x="56" y="212">Great work on the Project Northwind rollout you posted</text>
<text x="56" y="232">about on LinkedIn last week. Quick favor before I board</text>
<text x="56" y="252">my flight in 20 minutes:</text>
<text x="56" y="284">Can you approve the attached vendor invoice today? If we</text>
<text x="56" y="304">miss the cutoff we lose the supplier discount. I can't take</text>
<text x="56" y="324">calls until I land, so just reply once it's done.</text>
<text x="56" y="356">Thanks,</text>
<text x="56" y="376">Daniel</text>
</g>

<!-- attachment chip -->
<rect x="56" y="392" width="220" height="34" rx="6" fill="#f1f3f4" stroke="#dadce0"/>
<rect x="66" y="400" width="16" height="18" rx="2" fill="#d93025"/>
<text x="74" y="413" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">PDF</text>
<text x="90" y="414" font-size="12.5" fill="#3c4043">Northwind_Invoice_4471.pdf</text>

<!-- callout -->
<rect x="296" y="392" width="248" height="50" rx="6" fill="#fce8e6"/>
<text x="308" y="410" font-size="11.5" fill="#c5221f">Red flags: domain is staffviser-finance.com</text>
<text x="308" y="425" font-size="11.5" fill="#c5221f">(not staffviser.com), urgent, can't be called,</text>
<text x="308" y="438" font-size="11.5" fill="#c5221f">and a detail pulled from your LinkedIn.</text>
</svg>'''

for name, svg in [("phishing-google-alert.png", svg1), ("spear-phishing-email.png", svg2)]:
    cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT, name), scale=2, output_width=1200, output_height=960)
    print("wrote", name)
