from weasyprint import HTML, CSS

html_content = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<style>
  @page {
    size: A4;
    margin: 0;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: "DejaVu Serif", "Liberation Serif", serif;
    background: #F5F0E8;
    color: #1C1A14;
    width: 210mm;
    min-height: 297mm;
  }

  .page {
    width: 210mm;
    min-height: 297mm;
    background: #F5F0E8;
    padding: 22mm 20mm 18mm 20mm;
    position: relative;
  }

  /* Top accent line */
  .top-line {
    width: 38mm;
    height: 1.2px;
    background: #B8905A;
    margin: 0 auto 14mm auto;
  }

  /* Chapter label */
  h2 {
    font-family: "DejaVu Serif", serif;
    font-size: 8pt;
    letter-spacing: 0.38em;
    color: #B8905A;
    text-align: center;
    text-transform: uppercase;
    font-weight: normal;
    margin-bottom: 7mm;
  }

  /* Main title */
  h1 {
    font-family: "DejaVu Serif", serif;
    font-size: 38pt;
    font-weight: normal;
    text-align: center;
    color: #1C1A14;
    letter-spacing: 0.06em;
    line-height: 1.05;
    margin-bottom: 10mm;
  }

  /* Title divider */
  .divider {
    width: 24mm;
    height: 0.8px;
    background: rgba(28,26,20,0.2);
    margin: 0 auto 12mm auto;
  }

  /* Standard body paragraph */
  p {
    font-family: "DejaVu Serif", serif;
    font-size: 10.5pt;
    line-height: 1.78;
    color: #1C1A14;
    text-align: justify;
    margin-bottom: 5mm;
  }

  /* Dramatic standalone line — centered, italic */
  p.alone {
    font-size: 11.5pt;
    font-style: italic;
    text-align: center;
    color: #3A3224;
    margin-top: 7mm;
    margin-bottom: 7mm;
    line-height: 1.5;
  }

  /* Single-word climax line */
  p.climax {
    font-size: 22pt;
    font-style: italic;
    text-align: center;
    color: #B8905A;
    margin-top: 10mm;
    margin-bottom: 2mm;
    letter-spacing: 0.04em;
    line-height: 1.2;
  }

  /* Tense short burst lines */
  p.stark {
    font-size: 10.5pt;
    font-style: italic;
    text-align: center;
    color: #1C1A14;
    opacity: 0.7;
    margin-bottom: 1.5mm;
    margin-top: 1.5mm;
    line-height: 1.5;
  }

  /* Bottom decorative element */
  .bottom-ornament {
    text-align: center;
    margin-top: 14mm;
    color: #B8905A;
    font-size: 14pt;
    letter-spacing: 0.3em;
    opacity: 0.55;
  }

  /* Page number */
  .page-num {
    position: absolute;
    bottom: 10mm;
    right: 20mm;
    font-size: 8pt;
    letter-spacing: 0.22em;
    color: #1C1A14;
    opacity: 0.4;
  }
</style>
</head>
<body>
<div class="page">

  <div class="top-line"></div>

  <h2>Wide Eyes &mdash; Buch 01</h2>
  <h1>Vorwort</h1>
  <div class="divider"></div>

  <p>Manche Momente teilen ein Leben in davor und danach.</p>

  <p>Bei mir war es eine ruhige Nacht. Kein Unfall. Keine schlechte Nachricht.
  Kein dramatisches Ereignis.</p>

  <p class="alone">Ich sa&szlig; einfach da.</p>

  <p>Die Jahre davor hatten mich gefordert. Beruflich. Privat. Dauerhaft
  funktionieren, dauerhaft unter Strom. Und an diesem Abend war es zum ersten
  Mal still.</p>

  <p class="alone">Dann h&ouml;rte ich meinen Herzschlag.</p>

  <p class="stark">Nicht normal.</p>

  <p>Als w&uuml;rde jemand von innen gegen meine Brust h&auml;mmern. Hitze
  scho&szlig; meinen Nacken hoch bis hinter die Augen. Mein K&ouml;rper begann
  zu zittern. Meine Gedanken rasten zwischen Herzinfarkt und komplettem
  Kontrollverlust.</p>

  <p class="alone">Ich rief den Rettungswagen.</p>

  <p class="alone">Die Untersuchungen ergaben nichts.</p>

  <p>Dann sagte der Arzt ein Wort das ich bis dahin kaum beachtet hatte.</p>

  <p class="climax">Psychosomatisch.</p>

  <div class="bottom-ornament">&mdash; &nbsp; &mdash; &nbsp; &mdash;</div>

  <div class="page-num">01</div>
</div>
</body>
</html>"""

HTML(string=html_content).write_pdf("/home/user/etsy-agent-final/vorwort.pdf")
print("PDF generated: vorwort.pdf")
