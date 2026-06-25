import cairosvg, os
OUT="/sessions/clever-practical-brown/mnt/outputs"
F='font-family="Arial, Helvetica, sans-serif"'

def render(name, w, h, body):
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {F}>{body}</svg>'
    cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT,name), scale=2)
    print("wrote",name)

# ---------------- 1. Eisenhower Matrix ----------------
b=f'''
<rect width="600" height="470" fill="#ffffff"/>
<text x="300" y="36" font-size="21" font-weight="bold" fill="#202124" text-anchor="middle">The Eisenhower Matrix</text>
<text x="232" y="82" font-size="13" font-weight="bold" fill="#5f6368" text-anchor="middle">URGENT</text>
<text x="452" y="82" font-size="13" font-weight="bold" fill="#5f6368" text-anchor="middle">NOT URGENT</text>
<text x="46" y="190" font-size="13" font-weight="bold" fill="#5f6368" text-anchor="middle" transform="rotate(-90 46 190)">IMPORTANT</text>
<text x="46" y="370" font-size="12" font-weight="bold" fill="#5f6368" text-anchor="middle" transform="rotate(-90 46 370)">NOT IMPORTANT</text>
<rect x="122" y="96" width="220" height="184" rx="8" fill="#fdecea" stroke="#f3b9b2"/>
<text x="232" y="150" font-size="17" font-weight="bold" fill="#c5221f" text-anchor="middle">DO NOW</text>
<text x="232" y="178" font-size="12.5" fill="#5f6368" text-anchor="middle">Deadlines, crises,</text>
<text x="232" y="196" font-size="12.5" fill="#5f6368" text-anchor="middle">critical tasks</text>
<rect x="346" y="96" width="220" height="184" rx="8" fill="#fff1ee" stroke="#ff5330"/>
<text x="456" y="146" font-size="17" font-weight="bold" fill="#ff5330" text-anchor="middle">SCHEDULE</text>
<text x="456" y="172" font-size="12.5" fill="#5f6368" text-anchor="middle">Strategy, learning, growth</text>
<text x="456" y="200" font-size="11.5" font-weight="bold" fill="#ff5330" text-anchor="middle">where high performers live</text>
<rect x="122" y="284" width="220" height="172" rx="8" fill="#fef7e0" stroke="#f6d97a"/>
<text x="232" y="338" font-size="17" font-weight="bold" fill="#a8600a" text-anchor="middle">DELEGATE</text>
<text x="232" y="366" font-size="12.5" fill="#5f6368" text-anchor="middle">Interruptions,</text>
<text x="232" y="384" font-size="12.5" fill="#5f6368" text-anchor="middle">some meetings</text>
<rect x="346" y="284" width="220" height="172" rx="8" fill="#f1f3f4" stroke="#dadce0"/>
<text x="456" y="338" font-size="17" font-weight="bold" fill="#5f6368" text-anchor="middle">ELIMINATE</text>
<text x="456" y="366" font-size="12.5" fill="#5f6368" text-anchor="middle">Busywork,</text>
<text x="456" y="384" font-size="12.5" fill="#5f6368" text-anchor="middle">distractions</text>
'''
render("eisenhower-matrix.png",600,470,b)

# ---------------- 2. Time-blocked calendar ----------------
rows=[
 (70,34,"8:00","Plan the day","#f1f3f4","#202124",False),
 (108,58,"9:00","Deep work: priority project","#ff5330","#ffffff",True),
 (170,30,"11:00","Email and messages","#e8f0fe","#1a57c2",False),
 (204,34,"11:30","Lunch and recharge","#e6f4ea","#188038",False),
 (242,38,"12:30","Meetings (grouped together)","#f3e8fd","#8430ce",False),
 (284,54,"1:30","Deep work: block two","#ff5330","#ffffff",True),
 (342,30,"3:00","Email and quick tasks","#e8f0fe","#1a57c2",False),
 (376,34,"3:30","Flexible / overflow","#f8f9fa","#5f6368",False),
 (414,34,"4:30","Weekly review","#fff1ee","#ff5330",False),
]
parts=['<rect width="600" height="510" fill="#ffffff"/>',
 '<text x="300" y="36" font-size="21" font-weight="bold" fill="#202124" text-anchor="middle">A time-blocked day</text>']
for y,hh,t,label,fill,tc,prot in rows:
    dash=' stroke-dasharray="5 4"' if "Flexible" in label else ''
    parts.append(f'<text x="150" y="{y+hh/2+5:.0f}" font-size="12" fill="#80868b" text-anchor="end">{t}</text>')
    parts.append(f'<rect x="166" y="{y}" width="374" height="{hh}" rx="6" fill="{fill}" stroke="#dadce0"{dash}/>')
    parts.append(f'<text x="182" y="{y+hh/2+5:.0f}" font-size="13.5" font-weight="bold" fill="{tc}">{label}</text>')
    if prot:
        parts.append(f'<rect x="452" y="{y+hh/2-11:.0f}" width="76" height="22" rx="11" fill="#ffffff" opacity="0.25"/>')
        parts.append(f'<text x="490" y="{y+hh/2+4:.0f}" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PROTECTED</text>')
parts.append('<text x="300" y="484" font-size="12.5" fill="#5f6368" text-anchor="middle">Deep-work blocks go in first and stay protected. Meetings fit around them.</text>')
render("time-blocking-calendar.png",600,510,"".join(parts))

# ---------------- 3. Cultural comparison table ----------------
b='''
<rect width="640" height="430" fill="#ffffff"/>
<text x="320" y="36" font-size="20" font-weight="bold" fill="#202124" text-anchor="middle">Communication styles vary by culture</text>
<rect x="20" y="58" width="170" height="42" fill="#f1f3f4" stroke="#dadce0"/>
<rect x="190" y="58" width="215" height="42" fill="#ff5330"/>
<rect x="405" y="58" width="215" height="42" fill="#ff7a5c"/>
<text x="200" y="84" font-size="13.5" font-weight="bold" fill="#ffffff">Direct / Low-context</text>
<text x="415" y="84" font-size="13.5" font-weight="bold" fill="#ffffff">Indirect / High-context</text>
'''
rows=[("Feedback","Often direct, can be public","Softened, usually private"),
      ("Saying no","A plain \"no\"","\"That might be hard\" can mean no"),
      ("Meaning lives in","The words themselves","Tone, context, what is unsaid"),
      ("Common in","US, Germany, Netherlands","Japan, India, UAE")]
y=100
for i,(a,c1,c2) in enumerate(rows):
    fill="#ffffff" if i%2==0 else "#fafafa"
    b+=f'<rect x="20" y="{y}" width="170" height="60" fill="#f8f9fa" stroke="#dadce0"/>'
    b+=f'<rect x="190" y="{y}" width="215" height="60" fill="{fill}" stroke="#e8eaed"/>'
    b+=f'<rect x="405" y="{y}" width="215" height="60" fill="{fill}" stroke="#e8eaed"/>'
    b+=f'<text x="32" y="{y+35}" font-size="13" font-weight="bold" fill="#202124">{a}</text>'
    b+=f'<text x="202" y="{y+35}" font-size="12.5" fill="#3c4043">{c1}</text>'
    b+=f'<text x="417" y="{y+35}" font-size="12.5" fill="#3c4043">{c2}</text>'
    y+=60
b+=f'<text x="320" y="{y+28}" font-size="12" font-style="italic" fill="#80868b" text-anchor="middle">Tendencies, not rules. Every individual is different.</text>'
render("cultural-comparison.png",640,430,b)

# ---------------- 4. Johari Window ----------------
b='''
<rect width="560" height="470" fill="#ffffff"/>
<text x="280" y="36" font-size="21" font-weight="bold" fill="#202124" text-anchor="middle">The Johari Window</text>
<text x="245" y="84" font-size="12.5" font-weight="bold" fill="#5f6368" text-anchor="middle">KNOWN TO SELF</text>
<text x="435" y="84" font-size="12.5" font-weight="bold" fill="#5f6368" text-anchor="middle">NOT KNOWN TO SELF</text>
<text x="40" y="186" font-size="12.5" font-weight="bold" fill="#5f6368" text-anchor="middle" transform="rotate(-90 40 186)">KNOWN TO OTHERS</text>
<text x="40" y="372" font-size="11.5" font-weight="bold" fill="#5f6368" text-anchor="middle" transform="rotate(-90 40 372)">NOT KNOWN TO OTHERS</text>
<rect x="150" y="96" width="190" height="180" rx="8" fill="#f1f3f4" stroke="#dadce0"/>
<text x="245" y="170" font-size="17" font-weight="bold" fill="#202124" text-anchor="middle">Open</text>
<text x="245" y="196" font-size="12" fill="#5f6368" text-anchor="middle">What you and others</text>
<text x="245" y="213" font-size="12" fill="#5f6368" text-anchor="middle">both see</text>
<rect x="344" y="96" width="190" height="180" rx="8" fill="#fff1ee" stroke="#ff5330"/>
<text x="439" y="164" font-size="17" font-weight="bold" fill="#ff5330" text-anchor="middle">Blind Spot</text>
<text x="439" y="190" font-size="12" fill="#5f6368" text-anchor="middle">What others see</text>
<text x="439" y="207" font-size="12" fill="#5f6368" text-anchor="middle">that you do not</text>
<rect x="150" y="280" width="190" height="176" rx="8" fill="#f1f3f4" stroke="#dadce0"/>
<text x="245" y="352" font-size="17" font-weight="bold" fill="#202124" text-anchor="middle">Hidden</text>
<text x="245" y="378" font-size="12" fill="#5f6368" text-anchor="middle">What you keep</text>
<text x="245" y="395" font-size="12" fill="#5f6368" text-anchor="middle">to yourself</text>
<rect x="344" y="280" width="190" height="176" rx="8" fill="#f1f3f4" stroke="#dadce0"/>
<text x="439" y="352" font-size="17" font-weight="bold" fill="#202124" text-anchor="middle">Unknown</text>
<text x="439" y="378" font-size="12" fill="#5f6368" text-anchor="middle">What no one</text>
<text x="439" y="395" font-size="12" fill="#5f6368" text-anchor="middle">sees yet</text>
'''
render("johari-window.png",560,470,b)

# ---------------- 5. Fixed vs Growth Mindset ----------------
b='''
<rect width="620" height="440" fill="#ffffff"/>
<text x="310" y="36" font-size="21" font-weight="bold" fill="#202124" text-anchor="middle">Fixed vs Growth Mindset</text>
<rect x="20" y="58" width="285" height="40" rx="6" fill="#5f6368"/>
<rect x="315" y="58" width="285" height="40" rx="6" fill="#ff5330"/>
<text x="162" y="84" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Fixed mindset</text>
<text x="457" y="84" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">Growth mindset</text>
'''
pairs=[(["\"I'm not good at this.\""],["\"I'm not good at this yet.\""]),
 (["\"I got tough feedback.","I must be bad at my job.\""],["\"I got feedback. Now I","know what to improve.\""]),
 (["\"This is too hard.\""],["\"This will take more","effort than I expected.\""])]
y=108
for i,(l,r) in enumerate(pairs):
    hgt=78
    b+=f'<rect x="20" y="{y}" width="285" height="{hgt}" rx="6" fill="#f1f3f4" stroke="#e0e0e0"/>'
    b+=f'<rect x="315" y="{y}" width="285" height="{hgt}" rx="6" fill="#fff1ee" stroke="#ffd9cf"/>'
    ly=y+hgt/2 - (len(l)-1)*10 + 4
    for line in l:
        b+=f'<text x="162" y="{ly:.0f}" font-size="13.5" font-style="italic" fill="#5f6368" text-anchor="middle">{line}</text>'
        ly+=20
    ry=y+hgt/2 - (len(r)-1)*10 + 4
    for line in r:
        b+=f'<text x="457" y="{ry:.0f}" font-size="13.5" font-style="italic" fill="#c2410c" text-anchor="middle">{line}</text>'
        ry+=20
    y+=hgt+10
b+=f'<text x="310" y="{y+24}" font-size="13" font-weight="bold" fill="#ff5330" text-anchor="middle">One word, "yet", keeps the door open.</text>'
render("growth-mindset.png",620,440,b)
