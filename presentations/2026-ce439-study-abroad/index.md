---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  :root {
    --byu-navy: #002e5d;
    --byu-navy-dark: #001938;
    --byu-royal: #0062b8;
    --accent-gold: #c49a45;
    --accent-gold-light: #f7eedb;
    --bg-light: #f8fafc;
    --text-dark: #1e293b;
    --text-muted: #64748b;
    --card-border: #e2e8f0;
  }
  section {
    background: #ffffff;
    color: var(--text-dark);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 24px;
    line-height: 1.4;
    padding: 44px 56px;
  }
  h1 {
    color: var(--byu-navy);
    font-size: 1.55em;
    font-weight: 700;
    margin: 0 0 0.4em 0;
    letter-spacing: -0.02em;
  }
  h2 {
    color: var(--byu-navy);
    font-size: 1.15em;
    font-weight: 600;
    margin: 0 0 0.3em 0;
  }
  header {
    color: var(--byu-navy);
    font-size: 0.55em;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    border-bottom: 2px solid var(--accent-gold);
    padding-bottom: 4px;
  }
  footer {
    color: var(--text-muted);
    font-size: 0.5em;
    display: flex;
    justify-content: space-between;
  }
  .tag {
    display: inline-block;
    padding: 0.2em 0.6em;
    font-size: 0.55em;
    font-weight: 700;
    border-radius: 4px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  .tag-navy { background: #002e5d; color: #fff; }
  .tag-gold { background: #fef3c7; color: #92400e; }
  .tag-blue { background: #dbeafe; color: #1e40af; }
  .tag-green { background: #dcfce7; color: #166534; }

  /* Slide specific layouts */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    align-items: stretch;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 18px;
    align-items: stretch;
  }
  .grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 16px;
    align-items: stretch;
  }
  .card {
    background: #ffffff;
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 16px 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  }
  .card-tint {
    background: #f8fafc;
    border-left: 4px solid var(--byu-navy);
  }
  .card-gold {
    background: #fdfaf3;
    border-left: 4px solid var(--accent-gold);
  }
  .stat-card {
    text-align: center;
    background: #f8fafc;
    border: 1px solid var(--card-border);
    border-radius: 10px;
    padding: 16px 12px;
  }
  .stat-val {
    font-size: 2.1em;
    font-weight: 800;
    color: var(--byu-navy);
    line-height: 1.05;
    margin-bottom: 4px;
  }
  .stat-lbl {
    font-size: 0.65em;
    color: var(--text-muted);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
  .photo-frame {
    position: relative;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
  }
  .photo-frame img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }
  .photo-caption {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.85));
    color: #fff;
    padding: 24px 14px 10px;
    font-size: 0.6em;
    line-height: 1.25;
  }

  /* Title slide */
  section.lead {
    background: linear-gradient(135deg, #001938 0%, #002e5d 65%, #004080 100%);
    color: #ffffff;
    padding: 48px 56px;
  }
  section.lead h1 {
    color: #ffffff;
    font-size: 1.85em;
    line-height: 1.15;
    margin-bottom: 0.25em;
  }
  section.lead h2 {
    color: #ffd780;
    font-size: 1.15em;
    font-weight: 500;
    margin-bottom: 0.8em;
  }
  section.lead p {
    color: #cbd5e1;
    font-size: 0.85em;
    margin: 0.2em 0;
  }
  section.lead footer {
    color: #94a3b8;
  }
---

<!-- _class: lead -->
<!-- _paginate: skip -->

<div style="display: grid; grid-template-columns: 1.15fr 0.95fr; gap: 36px; align-items: center; height: 100%;">
  <div>
  <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 18px;">
  <img src="images/byu_logo.png" style="height: 52px; width: auto; background: #fff; border-radius: 6px; padding: 4px;" alt="BYU Logo">
  <span class="tag tag-gold" style="font-size: 0.65em;">Civil & Construction Engineering</span>
  </div>
  <h1>Water & Sustainability</h1>
  <h2>The Netherlands & Denmark Study Abroad</h2>
  <div style="height: 3px; width: 80px; background: #c49a45; margin: 18px 0;"></div>
  <p style="font-size: 0.9em; font-weight: 600; color: #ffffff;">CE 439 / CE 498R Capstone Program</p>
  <p style="color: #cbd5e1; font-size: 0.8em;">Dr. Daniel P. Ames · Program Director</p>
  <p style="color: #94a3b8; font-size: 0.72em; margin-top: 14px;">Faculty Meeting Presentation · 5-Minute Overview</p>
  </div>

  <div class="photo-frame" style="height: 530px;">
  <img src="images/keukenhof-cohort.jpg" alt="2026 Student Cohort at Keukenhof">
  <div class="photo-caption">
  <strong>2026 Student Cohort & Ames Family</strong><br>
  Keukenhof Gardens, The Netherlands
  </div>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 1 · 0:00 - 0:40)
- Good afternoon everyone. I'm excited to share a 5-minute report on our CE 439 Water & Sustainability Study Abroad program in The Netherlands and Denmark.
- As many of you know, our department runs biennial study abroad experiences. This year we took an exceptional group of civil engineering students to northern Europe to study the world's most sophisticated flood defenses and water management systems.
- This was an intensive, high-rigor capstone experience that combined winter-semester engineering prep with hands-on post-project audits in the field.
-->

---

<!-- header: "Program Overview · CE 439 / CE 498R" -->
<!-- footer: "BYU Civil & Construction Engineering · Water Resources Study Abroad" -->

# Global Context & Academic Structure

<div class="grid-2" style="margin-top: 14px;">
  <div style="display: flex; flex-direction: column; gap: 16px;">
  <div class="card card-tint">
  <h2 style="font-size: 1.0em; margin-bottom: 6px;">🌍 Why The Netherlands & Denmark?</h2>
  <p style="font-size: 0.78em; margin: 0; color: #334155;">
  <strong>26% of the Netherlands lies below sea level</strong>, and over 50% is flood-vulnerable. Century after century, Dutch civil engineers have pushed the state of the art—moving from historical land reclamation to the modern philosophy of <em>"Building with Nature"</em> and climate resilience.
  </p>
  </div>

  <div class="card card-gold">
  <h2 style="font-size: 1.0em; margin-bottom: 6px;">🎓 Rigorous Two-Stage Curriculum</h2>
  <ul style="font-size: 0.74em; margin: 0 0 0 16px; padding: 0; color: #334155; line-height: 1.55;">
  <li><strong>Phase 1 (Winter Prep):</strong> Students complete CE 414 (GIS) & CE 431 (Hydrology), plus weekly CE 471 prep covering Dutch hydraulic models and HEC-RAS flood modeling.</li>
  <li><strong>Phase 2 (Spring Field Study):</strong> 18 days in Europe (Copenhagen & Delft hub) performing site inspections and capstone project audits.</li>
  </ul>
  </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 14px;">
  <div class="photo-frame" style="height: 310px;">
  <img src="images/copenhagen.jpg" alt="Copenhagen Harbor">
  <div class="photo-caption">
  <strong>Copenhagen & Delft Field Hubs</strong><br>
  Urban water resiliency, coastal barriers & harbor sustainability
  </div>
  </div>

  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
  <div class="stat-card">
  <div class="stat-val">18</div>
  <div class="stat-lbl">Days in Field</div>
  </div>
  <div class="stat-card">
  <div class="stat-val">3</div>
  <div class="stat-lbl">Credit Hours</div>
  </div>
  <div class="stat-card">
  <div class="stat-val">100%</div>
  <div class="stat-lbl">Capstone Aligned</div>
  </div>
  </div>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 2 · 0:40 - 1:25)
- Why the Netherlands? There is literally no better place on Earth to study water resources engineering. Over a quarter of the country is below sea level. They invented polders and dikes, and now they are leading the global transition to "Building with Nature."
- Academically, this is not a sightseeing tour. Students prepare throughout winter semester: they must take GIS and Hydrology, and in our prep sessions they build digital elevation models and run hydraulic flood inundation simulations.
- When they land in Europe, they already understand the hydraulic engineering behind each site they inspect.
-->

---

<!-- header: "Student Cohort · Diversity & Logistical Success" -->
<!-- footer: "BYU Civil & Construction Engineering · Water Resources Study Abroad" -->

# Student Cohort & Key Best Practices

<div class="grid-2" style="margin-top: 14px;">
  <div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
  <div class="stat-card" style="border-top: 4px solid var(--accent-gold);">
  <div class="stat-val" style="color: #002e5d;">19</div>
  <div class="stat-lbl">Students in 2026</div>
  </div>
  <div class="stat-card" style="border-top: 4px solid #16a34a;">
  <div class="stat-val" style="color: #16a34a;">79%</div>
  <div class="stat-lbl">Female Enrollment</div>
  </div>
  </div>

  <div class="card card-tint" style="margin-bottom: 14px;">
  <h2 style="font-size: 0.95em; margin-bottom: 6px;">🌟 Exceptional Gender Diversity</h2>
  <p style="font-size: 0.75em; margin: 0; color: #334155;">
  With <strong>15 female and 4 male engineering students</strong>, the program achieved historic female participation for our department, creating an incredibly supportive, dynamic team environment.
  </p>
  </div>

  <div class="card card-gold">
  <h2 style="font-size: 0.95em; margin-bottom: 6px;">🤝 Department & Weidman Center Support</h2>
  <p style="font-size: 0.74em; margin: 0; color: #334155;">
  Generous funding from the <strong>Department of Civil & Construction Engineering</strong> and <strong>$1,400 scholarships per student</strong> from the Weidman Center for Global Leadership kept the program affordable and accessible.
  </p>
  </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 12px;">
  <div class="photo-frame" style="height: 270px;">
  <img src="images/delft-town.jpg" alt="Delft Netherlands Home Base">
  <div class="photo-caption">
  <strong>Delft, The Netherlands</strong> — Our 14-Night Central Field Hub
  </div>
  </div>

  <div class="card" style="background: #f8fafc; padding: 14px 18px;">
  <h2 style="font-size: 0.9em; margin-bottom: 4px; color: #002e5d;">🏨 Operational Best Practice: Single Hotel Hub</h2>
  <p style="font-size: 0.72em; margin: 0; color: #475569; line-height: 1.45;">
  In prior years, moving between 6–7 hotels caused logistics friction. In 2026, anchoring at <strong>one hotel in Delft</strong> for all 14 Dutch nights was our biggest operational win: day drives never exceeded 2.5 hours, students settled in, and group cohesion flourished.
  </p>
  </div>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 3 · 1:25 - 2:05)
- Look at these cohort numbers: 19 students, with 15 women and 4 men. Having 79% female representation in a Civil Engineering capstone cohort is something our entire department can celebrate.
- I want to publicly thank our department chair and the Weidman Center for Global Leadership. With departmental subsidies and the $1,400 Weidman scholarships, this life-changing experience was made affordable.
- Logistically, our best practice this year was staying in a single hotel in Delft rather than packing up every 2 nights. We did day trips in rental cars across the country, which saved huge administrative overhead and let the students focus on learning.
-->

---

<!-- header: "World-Class Engineering Field Laboratories" -->
<!-- footer: "BYU Civil & Construction Engineering · Water Resources Study Abroad" -->

# Monumental Hydraulic Infrastructure

<div class="grid-4" style="margin-top: 14px;">
  <div class="card" style="padding: 12px; display: flex; flex-direction: column;">
  <div class="photo-frame" style="height: 200px; margin-bottom: 10px;">
  <img src="images/oosterschelde-barrier.jpg" alt="Delta Works Oosterschelde Barrier">
  <div class="photo-caption"><strong>Delta Works</strong></div>
  </div>
  <span class="tag tag-navy" style="margin-bottom: 6px; align-self: flex-start;">Storm Surge Barrier</span>
  <h2 style="font-size: 0.85em; margin-bottom: 4px;">Oosterscheldekering</h2>
  <p style="font-size: 0.68em; color: #475569; margin: 0; line-height: 1.35;">
  9 km barrier with 62 steel gates protecting Zeeland province; one of modern engineering's 7 wonders.
  </p>
  </div>

  <div class="card" style="padding: 12px; display: flex; flex-direction: column;">
  <div class="photo-frame" style="height: 200px; margin-bottom: 10px;">
  <img src="images/sand-motor.jpg" alt="The Sand Motor Zandmotor">
  <div class="photo-caption"><strong>The Sand Motor</strong></div>
  </div>
  <span class="tag tag-green" style="margin-bottom: 6px; align-self: flex-start;">Building with Nature</span>
  <h2 style="font-size: 0.85em; margin-bottom: 4px;">Zandmotor Mega-Dune</h2>
  <p style="font-size: 0.68em; color: #475569; margin: 0; line-height: 1.35;">
  21.5M m³ sand peninsula placed offshore, letting wind and currents replenish 20 km of coastline naturally.
  </p>
  </div>

  <div class="card" style="padding: 12px; display: flex; flex-direction: column;">
  <div class="photo-frame" style="height: 200px; margin-bottom: 10px;">
  <img src="images/afsluitdijk.jpg" alt="Afsluitdijk Enclosure Dike">
  <div class="photo-caption"><strong>The Afsluitdijk</strong></div>
  </div>
  <span class="tag tag-blue" style="margin-bottom: 6px; align-self: flex-start;">Enclosure Dike</span>
  <h2 style="font-size: 0.85em; margin-bottom: 4px;">32 km Sea Barrier</h2>
  <p style="font-size: 0.68em; color: #475569; margin: 0; line-height: 1.35;">
  Separating the North Sea from IJsselmeer since 1932; currently reinforced with eco-concrete wave-dissipating blocks.
  </p>
  </div>

  <div class="card" style="padding: 12px; display: flex; flex-direction: column;">
  <div class="photo-frame" style="height: 200px; margin-bottom: 10px;">
  <img src="images/cruquius-steam.jpg" alt="Cruquius Steam Pumping Engine">
  <div class="photo-caption"><strong>Cruquius & Windmills</strong></div>
  </div>
  <span class="tag tag-gold" style="margin-bottom: 6px; align-self: flex-start;">Historical Evolution</span>
  <h2 style="font-size: 0.85em; margin-bottom: 4px;">Pumping Technology</h2>
  <p style="font-size: 0.68em; color: #475569; margin: 0; line-height: 1.35;">
  From 18th-century Kinderdijk drainage windmills to Cruquius (world's largest steam cylinder) draining Haarlemmermeer lake.
  </p>
  </div>
</div>

<div style="margin-top: 14px; background: #f1f5f9; border-radius: 8px; padding: 10px 18px; font-size: 0.72em; color: #334155; display: flex; justify-content: space-between; align-items: center;">
  <span><strong>Key Takeaway:</strong> Students witnessed the historical transition from mechanical brute-force pumping to passive, nature-based hydraulic engineering.</span>
  <span class="tag tag-navy">Field Ground-Truthing</span>
</div>

<!--
SPEAKER NOTES (Slide 4 · 2:05 - 2:55)
- Here are four of the incredible infrastructure sites our students inspected in person.
- The Oosterschelde Barrier in Zeeland—they walked inside the sluice gate chambers and took a boat out into the tidal channels.
- The Sand Motor: instead of dredging sand onto beaches every 3 years, the Dutch deposited 21 million cubic meters in one spot, and let natural wave energy distribute it over 20 years. That is "Building with Nature."
- The Afsluitdijk: a 20-mile causeway dam holding back the North Sea.
- And the history: seeing how they evolved from Kinderdijk windmills to the Cruquius steam pump which drained the lake where Schiphol Airport now sits.
-->

---

<!-- header: "Capstone Engineering Projects" -->
<!-- footer: "BYU Civil & Construction Engineering · Water Resources Study Abroad" -->

# Auditing "Room for the River" (*Ruimte voor de Rivier*)

<div class="grid-2" style="margin-top: 14px;">
  <div style="display: flex; flex-direction: column; gap: 14px;">
  <div class="card card-tint">
  <h2 style="font-size: 0.95em; margin-bottom: 4px;">🌊 National Paradigm Shift Under Evaluation</h2>
  <p style="font-size: 0.73em; margin: 0; color: #334155;">
  After major floods in 1993 & 1995, the Dutch government rejected merely raising dikes. Instead, the <strong>€2.3 billion "Room for the River"</strong> program gave rivers room to expand during extreme events.
  </p>
  </div>

  <div class="card" style="padding: 14px 18px;">
  <h2 style="font-size: 0.92em; margin-bottom: 8px; color: #002e5d;">📋 5 Student Capstone Teams Conducted Audits:</h2>
  <div style="font-size: 0.71em; color: #334155; line-height: 1.5;">
  <div><strong>Team 1 · Noordwaard:</strong> Depoldered 4,450 ha; dropped downstream flood peaks by 30 cm.</div>
  <div style="margin-top: 4px;"><strong>Team 2 · SBA (Kampen):</strong> IJssel delta bypass channel (*Reevediep*).</div>
  <div style="margin-top: 4px;"><strong>Team 3 · Nijmegen / Waal:</strong> Relocated dike 350m inland, creating river bypass & Veur-Lent island.</div>
  <div style="margin-top: 4px;"><strong>Team 4 · Overdiepse Polder:</strong> Moved farms to raised <em>terpen</em> (mounds) so agricultural land acts as flood storage.</div>
  <div style="margin-top: 4px;"><strong>Team 5 · Cortenoever:</strong> Lowered floodplains along the IJssel river.</div>
  </div>
  </div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 12px;">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
  <div class="photo-frame" style="height: 220px;">
  <img src="images/room-for-river-cortenoever.jpg" alt="Students making room for river">
  <div class="photo-caption"><strong>Cortenoever Site Inspection</strong><br>BYU Capstone students in field</div>
  </div>
  <div class="photo-frame" style="height: 220px;">
  <img src="images/noordwaard-tower.jpg" alt="Team 1 at Noordwaard Tower">
  <div class="photo-caption"><strong>Depoldering Noordwaard</strong><br>Team 1 audit inspection</div>
  </div>
  </div>

  <div class="card card-gold" style="padding: 12px 16px;">
  <h2 style="font-size: 0.88em; margin-bottom: 4px;">📊 Capstone Project Deliverables</h2>
  <p style="font-size: 0.7em; margin: 0; color: #475569;">
  Each team produced full professional reports evaluating: <strong>1)</strong> Hydraulic modeling accuracy (pre- vs post-project DEMs & flood maps), <strong>2)</strong> Economic and environmental ROI, and <strong>3)</strong> On-site ground verification.
  </p>
  </div>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 5 · 2:55 - 3:45)
- For their capstone deliverable, our students audited the Dutch "Room for the River" program.
- In the 1990s, the Dutch realized that building dikes higher and higher was unsustainable. They shifted to giving rivers room to flood safely: depoldering farmland, setting dikes back, and excavating side channels.
- We divided our students into 5 teams, each assigned to a different major project site: Noordwaard, Overdiepse Polder, Nijmegen on the Waal, and Cortenoever.
- In the classroom, they modeled these sites using DEMs and GIS; in Europe, they walked the dikes, interviewed engineers, and audited whether the real-world engineering delivered on its promises.
-->

---

<!-- header: "Intercultural & Spiritual Foundations" -->
<!-- footer: "BYU Civil & Construction Engineering · Water Resources Study Abroad" -->

# Fulfilling the AIMS of a BYU Education

<div class="grid-3" style="margin-top: 14px;">
  <div class="card" style="display: flex; flex-direction: column; padding: 16px;">
  <div class="photo-frame" style="height: 220px; margin-bottom: 12px;">
  <img src="images/delta-works-students.jpg" alt="Students at Delta Works Visitor Center">
  <div class="photo-caption"><strong>Unity & Leadership</strong><br>Neeltje Jans, Zeeland</div>
  </div>
  <span class="tag tag-gold" style="margin-bottom: 6px; align-self: flex-start;">Spiritually Strengthening</span>
  <h2 style="font-size: 0.9em; margin-bottom: 6px;">Daily Group Devotionals</h2>
  <p style="font-size: 0.72em; color: #475569; margin: 0; line-height: 1.45;">
  Every evening at 9:00 PM, the group gathered at the hotel for student-led devotionals, connecting spiritual truths with civil engineering stewardship.
  </p>
  </div>

  <div class="card" style="display: flex; flex-direction: column; padding: 16px;">
  <div class="photo-frame" style="height: 220px; margin-bottom: 12px;">
  <img src="images/annefrank.jpg" alt="Anne Frank House Amsterdam">
  <div class="photo-caption"><strong>Heritage & Empathy</strong><br>Anne Frank House, Amsterdam</div>
  </div>
  <span class="tag tag-blue" style="margin-bottom: 6px; align-self: flex-start;">Character Building</span>
  <h2 style="font-size: 0.9em; margin-bottom: 6px;">Temple & Sacred History</h2>
  <p style="font-size: 0.72em; color: #475569; margin: 0; line-height: 1.45;">
  Students performed proxy baptisms at <strong>The Hague Netherlands Temple</strong> (Zoetermeer) and visited the historic 1861 LDS baptism site at Broeksterwoude in Friesland.
  </p>
  </div>

  <div class="card" style="display: flex; flex-direction: column; padding: 16px;">
  <div class="photo-frame" style="height: 220px; margin-bottom: 12px;">
  <img src="images/hoge-veluwe-bikes.jpg" alt="Students cycling in Hoge Veluwe">
  <div class="photo-caption"><strong>Cultural Immersion</strong><br>Hoge Veluwe White Bikes</div>
  </div>
  <span class="tag tag-green" style="margin-bottom: 6px; align-self: flex-start;">Intellectually Enlarging</span>
  <h2 style="font-size: 0.9em; margin-bottom: 6px;">Intercultural Competence</h2>
  <p style="font-size: 0.72em; color: #475569; margin: 0; line-height: 1.45;">
  Visiting the Anne Frank House, Rijksmuseum, Van Gogh Museum, cycling across Hoge Veluwe National Park, and experiencing European urban transit.
  </p>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 6 · 3:45 - 4:25)
- A BYU study abroad must fulfill the university's AIMS: spiritually strengthening, character building, and intellectually enlarging.
- Every night at 9 PM we held student-led devotionals. We visited The Hague Temple in Zoetermeer for proxy baptisms. We even visited Broeksterwoude in Friesland, the site of the very first LDS baptisms in the Netherlands in 1861.
- And culturally: standing inside the Anne Frank Secret Annex, exploring the Rijksmuseum, and riding the famous white bicycles through Hoge Veluwe. The students return home as more mature, empathetic global citizens.
-->

---

<!-- _class: lead -->
<!-- header: "" -->

<div style="max-width: 900px; margin: 0 auto; text-align: center;">
  <span class="tag tag-gold" style="font-size: 0.7em; margin-bottom: 12px;">Looking Ahead</span>
  <h1 style="color: #ffffff; font-size: 1.85em; margin-bottom: 12px;">Key Takeaways & Future Outlook</h1>
  <p style="color: #cbd5e1; font-size: 0.9em; margin-bottom: 24px;">
  An established, safe, and academically rigorous experiential learning model for BYU Civil & Construction Engineering.
  </p>

  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; text-align: left; margin-bottom: 28px;">
  <div style="background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 10px; padding: 16px;">
  <div style="font-size: 1.5em; margin-bottom: 6px;">✅</div>
  <h3 style="color: #ffd780; font-size: 0.85em; margin: 0 0 6px 0;">100% On-Target</h3>
  <p style="color: #e2e8f0; font-size: 0.72em; margin: 0; line-height: 1.4;">
  On-schedule, on-budget, zero incidents, and 100% student capstone completion.
  </p>
  </div>

  <div style="background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 10px; padding: 16px;">
  <div style="font-size: 1.5em; margin-bottom: 6px;">🔄</div>
  <h3 style="color: #ffd780; font-size: 0.85em; margin: 0 0 6px 0;">Biennial Rotation</h3>
  <p style="color: #e2e8f0; font-size: 0.72em; margin: 0; line-height: 1.4;">
  Europe (2024, 2026, 2028) alternating with the Dominican Republic (2025, 2027).
  </p>
  </div>

  <div style="background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 10px; padding: 16px;">
  <div style="font-size: 1.5em; margin-bottom: 6px;">🤝</div>
  <h3 style="color: #ffd780; font-size: 0.85em; margin: 0 0 6px 0;">Faculty Invitation</h3>
  <p style="color: #e2e8f0; font-size: 0.72em; margin: 0; line-height: 1.4;">
  Encourage your undergrads to apply for 2027/2028, and let's explore co-teaching!
  </p>
  </div>
  </div>

  <div style="border-top: 1px solid rgba(255,255,255,0.2); padding-top: 18px;">
  <p style="color: #ffffff; font-size: 0.95em; font-weight: 700; margin: 0;">Thank you! Questions & Discussion</p>
  <p style="color: #94a3b8; font-size: 0.75em; margin-top: 4px;">
  Explore live web slides: <a href="https://danames.com/ames-presentations/presentations/2026-ce439-study-abroad/" style="color: #93c5fd; text-decoration: underline;">danames.com/ames-presentations/</a>
  </p>
  </div>
</div>

<!--
SPEAKER NOTES (Slide 7 · 4:25 - 5:00)
- In conclusion: this program was on schedule, on budget, safe, and delivered real capstone engineering value for our students.
- Our department now has a proven biennial rotation: Northern Europe in even years, and the Dominican Republic in odd years.
- I encourage each of you to tell your students about this opportunity when they are planning their junior and senior years. If any faculty member is interested in partnering or participating in future trips, my door is always open.
- Thank you, and I'd be happy to take any questions!
-->