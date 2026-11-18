"""Shared chrome plus biography, myths, and opposition pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def esc(s) -> str:
    import html
    return html.escape("" if s is None else str(s), quote=True)


FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,650&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">"""


def nav(current: str) -> str:
    links = [
        ("index.html", "tracker", "Tracker"),
        ("bio.html", "bio", "Biography"),
        ("bio.html#critic-to-ally", "critic", "Critic to ally"),
        ("myths.html", "myths", "Myths vs. facts"),
        ("opposition.html", "opposition", "Top opposition"),
        ("index.html#favorability", "polls", "Polls"),
    ]
    items = []
    for href, key, label in links:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""
  <header class="site-top">
    <div class="wrap nav-row">
      <a class="wordmark" href="index.html">JD Vance Tracker</a>
      <nav class="site-nav" aria-label="Site">{''.join(items)}</nav>
    </div>
  </header>"""


def footer() -> str:
    return """
  <footer class="site">
    <div class="wrap">
      <p>Independent tracker. Not affiliated with JD Vance or any campaign, political party, or government office. Polling and sentiment figures are recorded as published; authenticity ratings are heuristics, not proof.</p>
      <p><a href="index.html">Tracker</a> · <a href="bio.html">Biography</a> · <a href="myths.html">Myths vs. facts</a> · <a href="opposition.html">Top opposition</a> · <a href="images/CREDITS.md">Photo credits</a></p>
    </div>
  </footer>"""


def page_shell(title: str, desc: str, current: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="index,follow">
  {FONTS}
</head>
<body>
{nav(current)}
{body}
{footer()}
</body>
</html>
"""


def bio_page(updated: str) -> str:
    body = f"""
  <article class="wrap">
    <header class="page-hero">
      <p class="kicker">Biography</p>
      <h1>The arc of JD Vance</h1>
      <p>From Middletown and Jackson to the Marine Corps, Yale Law, a bestselling memoir, the Senate, and the vice presidency — and the public record of how he changed his mind about Donald Trump.</p>
      <p class="fine">Last updated {esc(updated)}. Personal details below are drawn from official biographies and contemporaneous reporting. Every factual claim is linked to a source.</p>
    </header>

    <div class="split">
      <figure>
        <img src="images/vance-vp-portrait.jpg" alt="Official 2025 vice-presidential portrait of JD Vance, photographed by Daniel Torok" width="960" height="1244">
        <figcaption class="caption">Official vice-presidential portrait, January 15, 2025. Photograph by Daniel Torok, The White House. Public domain. <a href="images/CREDITS.md">Credits</a></figcaption>
      </figure>
      <div>
        <h2>Early life</h2>
        <p>Vice President JD Vance “was born and raised in Middletown, Ohio,” a manufacturing town whose good jobs, the official White House biography says, disappeared over time, with his family among those who “suffered the effects.” He has described a childhood marked by financial strain, his mother’s struggle with addiction, and his father’s absence. His grandparents — “Mamaw” and “Papaw” — “filled [that void] with unwavering support and guidance.” <a href="https://www.whitehouse.gov/administration/jd-vance/">White House biography</a></p>
        <p>His family’s roots, and the summers he spent with them, run through Jackson, in eastern Kentucky’s Appalachia, a setting he later placed at the center of his memoir <cite>Hillbilly Elegy</cite>. In 2016 he told NPR that the book recalled “a childhood where poverty was ‘the family tradition.’” <a href="https://www.npr.org/2016/08/17/490328484/hillbilly-elegy-recalls-a-childhood-where-poverty-was-the-family-tradition">NPR, Aug. 17, 2016</a></p>
        <p>After graduating from Middletown High School, he enlisted in the United States Marine Corps, “serving for four years with a tour in Iraq,” then used the G.I. Bill to attend Ohio State University and later Yale Law School. <a href="https://www.whitehouse.gov/administration/jd-vance/">White House biography</a></p>
      </div>
    </div>

    <section class="block" id="career">
      <h2>Writer, investor, senator, vice president</h2>
      <p>In 2016 Vance published <cite>Hillbilly Elegy: A Memoir of a Family and Culture in Crisis</cite>, which became a New York Times bestseller and, in 2020, a feature-film adaptation. <a href="https://www.theguardian.com/us-news/2021/jul/06/hillbilly-elegy-jd-vance-trump-republicans">The Guardian, July 6, 2021</a> (noting the prior year’s film adaptation). The official White House biography describes him after law school as “an investor in startups across the Midwest, and as the author of the bestselling memoir.” <a href="https://www.whitehouse.gov/administration/jd-vance/">White House biography</a></p>
      <p>In 2022 he was elected to the U.S. Senate from Ohio. In 2024, the White House biography says, “President Donald J. Trump extended JD the incredible honor of asking him to serve as the Vice-Presidential Nominee.” He took office as vice president in January 2025.</p>
    </section>

    <section class="block" id="family">
      <h2>Usha Vance and their children</h2>
      <p>Vance met his wife, Usha Chilukuri Vance, at Yale Law School. A Voice of America profile reports that she is “the daughter of Indian immigrants”; her parents, Krish and Lakshmi Chilukuri, are from Andhra Pradesh and later settled in San Diego, where she was born. She earned a bachelor’s degree from Yale, a master’s degree from the University of Cambridge, and a law degree from Yale Law, where the two met; they married about a year after graduating in 2013. After law school she clerked for Judge Brett Kavanaugh on the U.S. Court of Appeals for the D.C. Circuit and later for Chief Justice John Roberts. VOA, citing the memoir, notes that Vance called her his “Yale spirit guide” and wrote that he “fell hard” for her. She is, like her parents, a practicing Hindu. <a href="https://www.voanews.com/a/wife-of-trump-s-vp-pick-is-yale-law-graduate-daughter-of-indian-immigrants-/7702255.html">VOA, July 17, 2024</a> Clerkships are also recorded in a U.S. State Department biography. <a href="https://me.usembassy.gov/meet-second-lady-usha-vance/">U.S. Mission Montenegro, Jan. 24, 2025</a></p>
      <p>That January 2025 State Department biography named three children: sons Ewan and Vivek and daughter Mirabel. The current White House biography says the couple are “proud parents to four beautiful children.” <a href="https://www.whitehouse.gov/administration/jd-vance/">White House biography</a> In a statement reported on July 19, 2026, the Vances announced that a son, Alec Neel Vance, “was born this morning” at Walter Reed National Military Medical Center, and that “Usha and the baby are happy and healthy, and our kids are overjoyed to meet their little brother.” Reporting on the statement also gave the earlier children’s years of birth as Ewan, 2017; Vivek, 2020; and Mirabel, 2021. <a href="https://www.aljazeera.com/news/2026/7/19/us-vice-president-jd-vance-and-his-wife-announce-birth-of-fourth-child">Al Jazeera, July 19, 2026, citing AP and Reuters</a></p>
    </section>

    <section class="block" id="faith">
      <h2>Catholic conversion</h2>
      <p>Vance was baptized and received into the Catholic Church on August 11, 2019, by the Dominican priest Father Henry Stephan at St. Gertrude Priory in Cincinnati. In an interview published the same day he said: “I became persuaded over time that Catholicism was true.” He added that he “was raised Christian, but never had a super-strong attachment to any denomination, and was never baptized,” and that when he became more interested in faith he “started out with a clean slate, and looked at the church that appealed most to me intellectually.” He chose St. Augustine as his patron saint. <a href="https://www.theamericanconservative.com/j-d-vance-becomes-catholic/">Rod Dreher, The American Conservative, Aug. 11, 2019</a></p>
    </section>

    <section class="block" id="critic-to-ally">
      <h2>From critic to ally</h2>
      <p class="lede">Vance’s opposition to Donald Trump in 2016 is a matter of public record — including a widely quoted magazine essay, a television interview, and a private message later published by a former roommate. So are his later explanations, in his own words, of when and why he changed his mind. The quotations below are his, as reported by the cited outlets. They are not paraphrases dressed as quotations.</p>

      <h3>What he said in 2016</h3>
      <p>In a July 4, 2016 essay for <cite>The Atlantic</cite>, “Opioid of the Masses,” Vance wrote of Trump’s campaign: “Trump is cultural heroin. He makes some feel better for a bit. But he cannot fix what ails them, and one day they’ll realize it.” He also wrote, “Trump’s promises are the needle in America’s collective vein.” <a href="https://www.theatlantic.com/politics/archive/2016/07/opioid-of-the-masses/489911/">The Atlantic, July 4, 2016</a> The wording is also quoted in later roundups. <a href="https://www.axios.com/2024/07/16/jd-vance-trump-statements">Axios, July 16, 2024</a></p>
      <blockquote class="pull">“Trump is cultural heroin. He makes some feel better for a bit. But he cannot fix what ails them, and one day they’ll realize it.”
        <cite>Vance, The Atlantic, July 4, 2016</cite>
      </blockquote>
      <p>In an October 2016 interview with Charlie Rose, Vance said he was “a Never Trump guy” and that he “never liked him.” <a href="https://www.axios.com/2024/07/16/jd-vance-trump-statements">Axios, July 16, 2024</a> <a href="https://www.politico.com/news/magazine/2024/07/15/jd-vance-55-things-trump-vp-00167882">Politico, July 15, 2024</a></p>
      <p>In February 2016, in a private message to his former Yale roommate Josh McLaurin — later published by McLaurin and widely quoted — Vance wrote that he went “back and forth between thinking Trump is a cynical asshole like Nixon who wouldn’t be that bad (and might even prove useful) or that he’s America’s Hitler.” <a href="https://www.washingtonpost.com/elections/2024/07/15/jd-vance-trump-criticism/">The Washington Post, July 15, 2024</a> <a href="https://www.politico.com/news/magazine/2024/07/15/jd-vance-55-things-trump-vp-00167882">Politico, July 15, 2024</a></p>
      <p>Deleted 2016 posts later reported by CNN included one calling Trump’s rhetoric toward immigrants and Muslims “reprehensible,” and another saying Vance would vote for the independent candidate Evan McMullin. <a href="https://www.axios.com/2024/07/16/jd-vance-trump-statements">Axios, July 16, 2024, citing CNN</a></p>

      <h3>How he explained the change</h3>
      <p>By the time he entered the 2022 Senate race, Vance said his view of Trump had changed after watching him in office. In a July 2, 2021 interview with TIME, over breakfast in Cincinnati, he said: “I sort of got Trump’s issues from the beginning. I just thought that this guy was not serious and was not going to be able to really make progress on the issues I cared about.” He added that Trump is “the leader of this movement,” and “if I actually care about these people and the things I say I care about, I need to just suck it up and support him.” <a href="https://time.com/6078483/j-d-vance-interview-trump/">Molly Ball, TIME, July 7, 2021</a> (the diner conversation was on July 2).</p>
      <blockquote class="pull">“I just thought that this guy was not serious and was not going to be able to really make progress on the issues I cared about.”
        <cite>Vance, interview with TIME, July 2, 2021</cite>
      </blockquote>
      <p>To WCPO, he put the same point in terms of results: “I think he delivered on his promises to make the country a better place. So, I think I saw this guy, he was an outsider. I didn’t really believe he was serious. And then I saw the guy in action. And I thought he was a successful president. That’s why I supported him enthusiastically in 2020. … So I changed because he did a good job.” <a href="https://www.wcpo.com/news/government/local-politics/hillbilly-elegy-author-j-d-vance-tells-tanya-orourke-why-he-decided-to-run-for-senate">WCPO</a></p>
      <p>On Fox News in July 2021, after old tweets resurfaced, he said: “Like a lot of people, I criticised Trump back in 2016. And I ask folks not to judge me based on what I said in 2016, because I’ve been very open that I did say those critical things and I regret them, and I regret being wrong about the guy.” He also said Trump was “a good president. I think he made a lot of good decisions for people, and I think he took a lot of flak.” <a href="https://www.theguardian.com/us-news/2021/jul/06/hillbilly-elegy-jd-vance-trump-republicans">The Guardian, July 6, 2021, quoting Fox News</a></p>
      <p>In his first interview as the 2024 vice-presidential nominee, Axios reported, Vance said he had been “certainly skeptical” of Trump but that the former president “changed my mind,” and: “I actually think it’s a good thing, when you see somebody, you were wrong about them, you ought to admit the mistake and admit that you were wrong.” <a href="https://www.axios.com/2024/07/16/jd-vance-trump-statements">Axios, July 16, 2024</a></p>
    </section>

    <section class="block" id="vp-selection">
      <h2>How he was chosen as vice president</h2>
      <div class="split">
        <figure>
          <img src="images/vance-senate-portrait.jpg" alt="Official U.S. Senate portrait of JD Vance, 118th Congress, 2023" width="960" height="1200">
          <figcaption class="caption">Official Senate portrait, January 3, 2023, 118th Congress. U.S. Senate. Public domain. <a href="images/CREDITS.md">Credits</a></figcaption>
        </figure>
        <div>
          <p>On July 15, 2024, the first day of the Republican National Convention in Milwaukee — and two days after an assassination attempt on Trump at a rally in Butler, Pennsylvania — Trump named Vance as his running mate. On Truth Social he wrote: “After lengthy deliberation and thought, and considering the tremendous talents of many others, I have decided that the person best suited to assume the position of Vice President of the United States is Senator J.D. Vance of the Great State of Ohio.” <a href="https://www.cnn.com/2024/07/15/politics/trump-vp-pick-jd-vance">CNN, July 15, 2024</a> <a href="https://www.reuters.com/world/us/trump-picks-onetime-critic-jd-vance-now-fierce-defender-his-running-mate-2024-07-15/">Reuters, July 15, 2024</a></p>
          <p>CNN, citing sources familiar with the process, reported that the finalists also included Sen. Marco Rubio of Florida and Gov. Doug Burgum of North Dakota; that Trump formally offered Vance the job by phone about 20 minutes before the Truth Social post; and that the two had met at Mar-a-Lago on Saturday, before the Butler rally. The same report said Vance’s supporters, “including Trump’s son Donald Trump Jr. and conservative media figure Tucker Carlson, had argued that Vance has the strongest relationship with Trump” among the finalists “and would be the most loyal selection.” <a href="https://www.cnn.com/2024/07/15/politics/trump-vp-pick-jd-vance">CNN, July 15, 2024</a></p>
        </div>
      </div>
    </section>
  </article>
"""
    return page_shell(
        "Biography — JD Vance Tracker",
        "A sourced biography of JD Vance: early life, Usha Vance and their children, his Catholic conversion, his 2016 criticism of Donald Trump and later explanations, and the 2024 vice-presidential selection.",
        "bio",
        body,
    )


def myths_page(updated: str) -> str:
    body = f"""
  <article class="wrap">
    <header class="page-hero">
      <p class="kicker">Fact checks</p>
      <h1>Myths vs. facts</h1>
      <p>Viral claims about JD Vance that independent fact-checkers have examined. This page includes only items for which a rating or investigation by a major fact-checking organization was opened for this update. It is not a catalog of political arguments, and it does not treat a disagreement about policy as a “myth.”</p>
      <p class="fine">Last updated {esc(updated)}.</p>
    </header>

    <section class="block">
      <div class="myth">
        <div class="tag">The claim</div>
        <h3>That Vance wrote in <cite>Hillbilly Elegy</cite> about a sexual encounter with a couch</h3>
        <p>In July 2024, after Vance was named as Trump’s running mate, a social-media post claimed that pages of his 2016 memoir described a sexual encounter involving an inside-out latex glove and couch cushions. The post spread widely and was repeated as if it were in the book.</p>
        <div class="tag fact-tag">The fact</div>
        <p>The passage does not exist. Snopes rated the rumor false: the memoir “contained no such passage, including in the first edition,” and the original poster “signaled that he was joking” in a follow-up. <a href="https://www.snopes.com/fact-check/jd-vance-couch-cushions/">Snopes, July 23, 2024 (updated July 26, 2024)</a>. PolitiFact, reviewing a later repetition of the claim by Illinois Gov. J.B. Pritzker, rated it Pants on Fire and noted that the claim “surfaced on social media in a satirical post.” <a href="https://www.politifact.com/factchecks/2024/jul/31/jb-pritzker/pritzker-repeats-a-baseless-claim-about-jd-vance-a/">PolitiFact, July 31, 2024</a></p>
        <p class="sources">Fact-checks: <a href="https://www.snopes.com/fact-check/jd-vance-couch-cushions/">Snopes</a> · <a href="https://www.politifact.com/factchecks/2024/jul/31/jb-pritzker/pritzker-repeats-a-baseless-claim-about-jd-vance-a/">PolitiFact</a> · related: <a href="https://www.snopes.com/fact-check/jd-vance-hillbilly-elegy-first-edition-couch-erotica/">Snopes on the first edition</a></p>
      </div>

      <div class="myth">
        <div class="tag">The claim</div>
        <h3>That he has changed his name three times, as if to hide who he is</h3>
        <p>A 2024 social-media meme claimed Vance was born James Donald Bowman and had since changed his name three times, sometimes tying the last change to his marriage and asking, “What is JD Vance hiding?”</p>
        <div class="tag fact-tag">The fact</div>
        <p>Snopes rated the meme a mixture. It is true that he was born James Donald Bowman, named in part for his biological father. It is not true that he has officially changed his name three times, or that the final change came “when he married.” Snopes found two official changes: the first when he was adopted by a stepfather, and the second a change he requested around the time he was graduating from Yale Law School, a year before he got married, becoming James David Vance. <a href="https://www.snopes.com/fact-check/jd-vance-born-james-donald-bowman/">Snopes, Aug. 16, 2024</a></p>
        <p class="sources">Fact-check: <a href="https://www.snopes.com/fact-check/jd-vance-born-james-donald-bowman/">Snopes</a></p>
      </div>
    </section>

    <section class="block">
      <h2>What this page does not do</h2>
      <p>It does not collect every harsh joke, policy dispute, or campaign attack. It also does not use fact-checks of <em>Vance’s own claims</em> (for example, statements he made about the 2024 campaign) as “myths about him.” Those are a different question, and they belong in political reporting, not on a list of fabrications about his life.</p>
    </section>
  </article>
"""
    return page_shell(
        "Myths vs. facts — JD Vance Tracker",
        "Fact-checks of viral claims about JD Vance, including the fabricated couch rumor and claims about his name, with links to Snopes and PolitiFact.",
        "myths",
        body,
    )



def _fmt_followers(n) -> str:
    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""
    if n >= 1_000_000:
        s = f"{n / 1_000_000:.2f}".rstrip("0").rstrip(".")
        return f"{s}M"
    if n >= 10_000:
        s = f"{n / 1_000:.1f}".rstrip("0").rstrip(".")
        return f"{s}K"
    return f"{n:,}"


def _side_label(side: str) -> str:
    return {
        "right": "Right",
        "left": "Left",
        "institutional": "Institutional",
        "unspecified": "Unspecified",
    }.get(side or "", esc(side or ""))


def opposition_page(updated: str) -> str:
    import json

    data_path = ROOT / "data" / "opposition.json"
    doc = json.loads(data_path.read_text(encoding="utf-8"))
    opponents = doc.get("opponents") or []
    counts = doc.get("counts") or {}
    cards = []
    for o in opponents:
        side = o.get("side") or "unspecified"
        handle = o.get("handle") or ""
        name = o.get("name") or handle
        fol = _fmt_followers(o.get("followers"))
        items = o.get("critical_items") or 0
        item_label = "1 critical item" if items == 1 else f"{items} critical items"
        criticisms = o.get("main_criticisms") or []
        lis = "".join("<li>%s</li>" % esc(c) for c in criticisms)
        links = o.get("links") or []
        parts = []
        for l in links:
            if l.get("url"):
                parts.append('<a href="%s">%s</a>' % (esc(l.get("url")), esc(l.get("label") or "Link")))
        link_html = " · ".join(parts)
        title = esc(name)
        if handle:
            title += ' <a class="handle" href="https://x.com/%s">@%s</a>' % (esc(handle), esc(handle))
        related = o.get("related_handle") or {}
        related_html = ""
        if related.get("handle"):
            related_html = (
                'Parent account: <a href="https://x.com/%s">@%s</a> (%s followers)'
                % (esc(related["handle"]), esc(related["handle"]), esc(_fmt_followers(related.get("followers"))))
            )
        notes = esc(o.get("source_notes") or "")
        if related_html:
            notes = (notes + " " + related_html).strip()
        last = esc(o.get("last_seen_pt") or o.get("last_seen") or "")
        rank = esc(o.get("rank"))
        cards.append(
            '<article class="card %s" data-side="%s" data-rank="%s">'
            '<div class="opp-head">'
            '<div class="opp-rank">%s</div>'
            '<div>'
            '<p class="card-meta">'
            '<span class="badge %s">%s</span>'
            '<span class="followers">%s followers</span>'
            '<span>%s</span>'
            '<span>Last seen %s</span>'
            '</p>'
            '<h3>%s</h3>'
            '<p class="summary">%s</p>'
            '<ul class="critiques">%s</ul>'
            '<p class="opp-links">%s</p>'
            '<p class="auth">%s</p>'
            '</div></div></article>'
            % (
                esc(side), esc(side), rank, rank, esc(side), _side_label(side),
                esc(fol), esc(item_label), last, title, esc(o.get("affiliation") or ""),
                lis, link_html, notes,
            )
        )

    n = counts.get("listed", len(opponents))
    n_right = counts.get("right", 0)
    n_left = counts.get("left", 0)
    n_inst = counts.get("institutional", 0)
    n_uns = counts.get("unspecified", 0)
    uns_det = (" · %s unspecified" % n_uns) if n_uns else ""
    snap = esc(doc.get("follower_snapshot_pt") or updated)
    script = """
  <script>
    (function () {
      var buttons = document.querySelectorAll(".filter");
      var cards = document.querySelectorAll("#opp-cards article.card");
      var empty = document.getElementById("opp-empty");
      function apply(side) {
        var shown = 0;
        cards.forEach(function (c) {
          var on = (side === "all" || c.getAttribute("data-side") === side);
          c.style.display = on ? "" : "none";
          if (on) shown++;
        });
        if (empty) empty.style.display = shown ? "none" : "block";
      }
      buttons.forEach(function (b) {
        b.addEventListener("click", function () {
          buttons.forEach(function (x) {
            x.classList.toggle("active", x === b);
            x.setAttribute("aria-pressed", x === b ? "true" : "false");
          });
          apply(b.getAttribute("data-side"));
        });
      });
    })();
  </script>
"""
    body = """
  <article class="wrap">
    <header class="page-hero">
      <p class="kicker">Top opposition</p>
      <h1>Who is criticizing JD Vance</h1>
      <p>A running list of high-reach critics — accounts with 50,000 or more X followers, or people and groups tied to a major organization or elected office — drawn from the tracker, from prominent replies and quote-posts under those items (including the Matt Walsh poll thread), and from a fresh search on the right and the left.</p>
      <p class="fine">Last updated %s. Follower counts are X public metrics from %s. Only accounts and items that were actually opened are listed. Affiliations are taken from bios, official pages, or the reporting cited below; none are invented.</p>
    </header>

    <div class="metrics">
      <div class="metric"><div class="num">%s</div><div class="label">Listed critics</div><div class="det">Opened this update</div></div>
      <div class="metric"><div class="num">%s</div><div class="label">Right</div><div class="det">Conservative or Republican-aligned</div></div>
      <div class="metric"><div class="num">%s</div><div class="label">Left</div><div class="det">Democratic or liberal-aligned</div></div>
      <div class="metric"><div class="num">%s</div><div class="label">Institutional</div><div class="det">Advocacy groups or foreign newspapers%s</div></div>
    </div>

    <section class="block">
      <h2>Ranked list</h2>
      <p>Ranked by reach and frequency: follower count times a modest bump for repeat critical items. The formula and exceptions are in the methodology below.</p>
      <div class="filters" role="group" aria-label="Filter by side">
        <button class="filter active" type="button" data-side="all" aria-pressed="true">All</button>
        <button class="filter" type="button" data-side="right" aria-pressed="false">Right</button>
        <button class="filter" type="button" data-side="left" aria-pressed="false">Left</button>
        <button class="filter" type="button" data-side="institutional" aria-pressed="false">Institutional</button>
        <button class="filter" type="button" data-side="unspecified" aria-pressed="false">Unspecified</button>
      </div>
      <div class="cards" id="opp-cards">
        %s
        <p class="empty" id="opp-empty">No critics in this category.</p>
      </div>
    </section>

    <section class="block">
      <h2>Methodology</h2>
      <p>A critic is listed only if we opened a post, interview, editorial, or official statement, and if the account has at least 50,000 X followers or is tied to a major media outlet, think tank, campaign, PAC, party body, elected office, or advocacy organization.</p>
      <p>The list is assembled from three sources: (a) authors of critical items already in the tracker; (b) prominent accounts in the replies and quote-posts under those items, including the Matt Walsh poll thread of November 17–18, 2026; and (c) a fresh X and web search for high-reach critics on the right and the left. Ranking score equals rank reach times (1 + 0.25 × (critical items − 1)). For CUFI Action Fund, rank reach is the parent @CUFI follower count, which is disclosed on that card, because the Action Fund account itself is small.</p>
      <p>“Right” and “left” describe public office, stated affiliation, or an outlet’s obvious editorial identity. “Institutional” is used for organizations that are not primarily a U.S. party office — here, the Anti-Defamation League and The Jerusalem Post. “Unspecified” is used only when the bio and opened posts do not state a partisan identity.</p>
      <p>This is not a complete census. A missing name is not a finding that someone is not a critic. Matt Walsh is not listed; his talent poll included Vance and did not attack him. Tomi Lahren commented in that thread with a preference for Ron DeSantis, which is not treated as a critique of Vance. Sen. Tom Cotton was described in Jewish Insider as taking a “veiled swipe” without naming Vance, so he is not listed. News outlets that only reported criticism are not listed as critics; signed editorials, signed columns, and organizational statements are. Michael Doran’s Hudson Institute essay is listed; a later X post in which he said it is “simply false” that he is “against JD Vance” is noted on his card.</p>
    </section>
  </article>
%s
""" % (esc(updated), snap, n, n_right, n_left, n_inst, uns_det, "".join(cards), script)
    return page_shell(
        "Top opposition — JD Vance Tracker",
        "High-reach critics of JD Vance, including officials and commentators on the right and the left, with follower counts, affiliations, and links to opened posts and articles.",
        "opposition",
        body,
    )


def write_pages(updated: str) -> None:
    (ROOT / "bio.html").write_text(bio_page(updated), encoding="utf-8")
    (ROOT / "myths.html").write_text(myths_page(updated), encoding="utf-8")
    (ROOT / "opposition.html").write_text(opposition_page(updated), encoding="utf-8")
    print("Wrote bio.html, myths.html, and opposition.html")
