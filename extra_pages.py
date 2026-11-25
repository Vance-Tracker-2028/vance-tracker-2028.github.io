"""Shared chrome plus biography, myths, and opposition pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent


def esc(s) -> str:
    import html
    return html.escape("" if s is None else str(s), quote=True)


def fonts(root: str = "") -> str:
    return f"""<link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}styles.css">"""


FONTS = fonts()


def nav(current: str, root: str = "") -> str:
    links = [
        ("index.html", "tracker", "Tracker"),
        ("bio.html", "bio", "Biography"),
        ("bio.html#critic-to-ally", "critic", "Critic to ally"),
        ("myths.html", "myths", "Myths vs. facts"),
        ("media.html", "media", "Media"),
        ("opposition.html", "opposition", "Top opposition"),
        ("index.html#favorability", "polls", "Polls"),
    ]
    items = []
    for href, key, label in links:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<a href="{root}{href}"{cur}>{label}</a>')
    return f"""
  <header class="site-top">
    <div class="wrap nav-row">
      <a class="wordmark" href="{root}index.html">JD Vance Tracker</a>
      <nav class="site-nav" aria-label="Site">{''.join(items)}</nav>
    </div>
  </header>"""


def footer(root: str = "") -> str:
    return f"""
  <footer class="site">
    <div class="wrap">
      <p class="disclaimer">Unofficial supporter site. Independently created by supporters of JD Vance. Not affiliated with, authorized, or endorsed by JD Vance, his office, any campaign, committee, or the White House. No funds are solicited or accepted. Local photos are public-domain U.S. government works or Creative Commons–licensed with attribution.</p>
      <p>Polling and sentiment figures are recorded as published; authenticity ratings are heuristics, not proof.</p>
      <p><a href="{root}index.html">Tracker</a> · <a href="{root}bio.html">Biography</a> · <a href="{root}myths.html">Myths vs. facts</a> · <a href="{root}media.html">Media</a> · <a href="{root}opposition.html">Top opposition</a> · <a href="{root}images/CREDITS.md">Photo credits</a></p>
    </div>
  </footer>"""


def page_shell(title: str, desc: str, current: str, body: str, root: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="index,follow">
  {fonts(root)}
</head>
<body>
{nav(current, root)}
{body}
{footer(root)}
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

    <section class="block" id="lighter-moment">
      <h2>Online humor &amp; memes</h2>
      <div class="meme-spot">
        <div class="meme-spot-grid">
          <div>
            <h3>In on the joke</h3>
            <p>Vance has occasionally leaned into viral internet edits of himself on his personal X account. On March 8, 2025, he posted a face-edited version of the Leonardo DiCaprio pointing meme — a post that drew over 502,000 likes and 154 million views.</p>
            <p class="fine">Posted by JD Vance (<code>@JDVance</code>) on March 8, 2025. Embedded via official X embed. <a href="https://x.com/JDVance/status/1898372454235451694">Original X post</a> · <a href="media.html#memes">See more official memes</a></p>
          </div>
          <div>
            <blockquote class="twitter-tweet" data-dnt="true"><p lang="zxx" dir="ltr"><a href="https://t.co/rPloNGHLej">pic.twitter.com/rPloNGHLej</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/1898372454235451694?ref_src=twsrc%5Etfw">March 8, 2025</a></blockquote>
          </div>
        </div>
      </div>
    </section>
  </article>
  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
"""
    return page_shell(
        "Biography — JD Vance Tracker",
        "A sourced biography of JD Vance: early life, Usha Vance and their children, his Catholic conversion, his 2016 criticism of Donald Trump and later explanations, and the 2024 vice-presidential selection.",
        "bio",
        body,
    )


from myths_copy import myths as _myths, myths_page, myth_detail_page



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




def media_page(updated: str) -> str:
    photos = [
        {
            "file": "vance-vp-portrait.jpg",
            "title": "Official vice-presidential portrait",
            "date": "January 15, 2025",
            "author": "Daniel Torok / The White House",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:VancePortrait.jpg",
            "alt": "Official 2025 vice-presidential portrait of JD Vance",
        },
        {
            "file": "vance-swearing-in-2025.jpg",
            "title": "Swearing-in as the 50th Vice President",
            "date": "January 20, 2025",
            "author": "Office of the Vice President (@VP)",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Vice_President_JD_Vance_is_sworn_in_(01).jpg",
            "alt": "JD Vance taking the oath of office alongside Usha Vance and their children on January 20, 2025",
        },
        {
            "file": "vance-day1-signing.jpg",
            "title": "Day One executive order signing",
            "date": "January 20, 2025",
            "author": "Office of the Vice President (@VP)",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Trump_Day_1_Executive_Order_Signing.jpg",
            "alt": "President Donald Trump signing executive orders on Day One with Vice President JD Vance",
        },
        {
            "file": "vance-capitol-signing-2025.jpg",
            "title": "Post-inaugural document signing at the U.S. Capitol",
            "date": "January 20, 2025",
            "author": "Office of Speaker Mike Johnson",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:President_Trump_signs_post-inaugural_documents_(January_20,_2025).jpg",
            "alt": "Post-inaugural signing ceremony at the Capitol with Vice President Vance and congressional leaders",
        },
        {
            "file": "vance-duffy-swearing-in.jpg",
            "title": "Swearing in Transportation Secretary Sean Duffy",
            "date": "January 29, 2025",
            "author": "U.S. Department of Transportation",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Vice_President_JD_Vance_swears_in_Sean_Duffy_as_Secretary_of_Transportation.jpg",
            "alt": "Vice President Vance swearing in Transportation Secretary Sean Duffy",
        },
        {
            "file": "vance-paris-ai-summit-2025.jpg",
            "title": "AI Action Summit meeting with Ursula von der Leyen in Paris",
            "date": "February 11, 2025",
            "author": "Dati Bendo / European Union (EC – Audiovisual Service)",
            "license": "CC BY 4.0",
            "license_url": "https://creativecommons.org/licenses/by/4.0",
            "source_url": "https://commons.wikimedia.org/wiki/File:Meeting_between_Ursula_von_der_Leyen_%26_J._D._Vance_-_AI_Action_Summit,_Paris,_France,_2025.jpg",
            "alt": "Vice President JD Vance meeting European Commission President Ursula von der Leyen in Paris",
        },
        {
            "file": "vance-munich-2025.jpg",
            "title": "Remarks at the 61st Munich Security Conference",
            "date": "February 14, 2025",
            "author": "MSC / Preis",
            "license": "CC BY-SA 4.0",
            "license_url": "https://creativecommons.org/licenses/by-sa/4.0",
            "source_url": "https://commons.wikimedia.org/wiki/File:JD_Vance%27s_Speech_at_the_61st_Munich_Security_Conference_(20250214-MSC2025-mc2931).jpg",
            "alt": "Vice President JD Vance speaking at the 61st Munich Security Conference in Germany",
        },
        {
            "file": "vance-driscoll-swearing-in.jpg",
            "title": "Swearing in Army Secretary Dan Driscoll",
            "date": "February 25, 2025",
            "author": "Office of the Vice President (@VP)",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Dan_Driscoll_Swearing-In.jpg",
            "alt": "Vice President Vance swearing in Army Secretary Dan Driscoll",
        },
        {
            "file": "vance-pituffik-allcall.jpg",
            "title": "All-call with troops at Pituffik Space Base, Greenland",
            "date": "March 28, 2025",
            "author": "DVIDS / U.S. Department of Defense",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Vice_President_visits_Pituffik_Space_Base_(Image_3_of_6).jpg",
            "alt": "Vice President JD Vance addressing Space Force Guardians and Airmen at Pituffik Space Base",
        },
        {
            "file": "vance-pituffik-arrival.jpg",
            "title": "Arrival with Second Lady Usha Vance at Pituffik Space Base",
            "date": "March 28, 2025",
            "author": "DVIDS / U.S. Department of Defense",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Vice_President_visits_Pituffik_Space_Base_(Image_4_of_6).jpg",
            "alt": "Col. Susan Meyers greeting Vice President JD Vance and Usha Vance at Pituffik Space Base, Greenland",
        },
        {
            "file": "vance-oval-office-2025.jpg",
            "title": "Oval Office bilateral meeting with South African President Ramaphosa",
            "date": "May 21, 2025",
            "author": "Daniel Torok / The White House",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:President_Donald_Trump_meets_with_President_of_South_Africa_Cyril_Ramaphosa_(54537774949).jpg",
            "alt": "President Trump and Vice President Vance in an Oval Office bilateral meeting on May 21, 2025",
        },
        {
            "file": "vance-maha-summit-2025.jpg",
            "title": "Remarks at the MAHA Summit in Washington, D.C.",
            "date": "November 12, 2025",
            "author": "Steve Jurvetson",
            "license": "CC BY 4.0",
            "license_url": "https://creativecommons.org/licenses/by/4.0",
            "source_url": "https://commons.wikimedia.org/wiki/File:JD_Vance_at_the_MAHA_Summit_(54920086170).jpg",
            "alt": "Vice President JD Vance speaking at the MAHA Summit in Washington, D.C.",
        },
        {
            "file": "vance-americafest-2025.jpg",
            "title": "Speaking at AmericaFest 2025 in Phoenix",
            "date": "December 21, 2025",
            "author": "Gage Skidmore",
            "license": "CC BY-SA 4.0",
            "license_url": "https://creativecommons.org/licenses/by-sa/4.0",
            "source_url": "https://commons.wikimedia.org/wiki/File:J._D._Vance_(55023973013).jpg",
            "alt": "Vice President JD Vance speaking at AmericaFest 2025 in Phoenix, Arizona",
        },
        {
            "file": "vance-senate-portrait.jpg",
            "title": "Official U.S. Senate portrait (118th Congress)",
            "date": "January 3, 2023",
            "author": "United States Congress / U.S. Senate",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Senator_Vance_official_portrait._118th_Congress.jpg",
            "alt": "Official U.S. Senate portrait of Sen. JD Vance",
        },
        {
            "file": "vance-usmc-birthday-2023.jpg",
            "title": "Marine Corps 248th birthday celebration",
            "date": "November 2023",
            "author": "U.S. Marine Corps",
            "license": "Public domain",
            "license_url": "",
            "source_url": "https://commons.wikimedia.org/wiki/File:Lt._Gen._David_G._Bellon_and_Senator_JD_Vance_celebrating_the_Marine_Corps_248th_birthday.jpg",
            "alt": "Lt. Gen. David G. Bellon and Sen. JD Vance celebrating the 248th Marine Corps birthday",
        },
    ]
    photo_cards = []
    for p in photos:
        if p["license_url"]:
            lic_html = '<a href="%s">%s</a>' % (esc(p["license_url"]), esc(p["license"]))
        else:
            lic_html = esc(p["license"])
        photo_cards.append(
            """<figure class="media-card">
              <div class="media-frame"><img src="images/%s" alt="%s" loading="lazy"></div>
              <figcaption class="media-cap">
                <p class="media-title">%s</p>
                <p class="media-meta">%s · %s</p>
                <p class="media-lic">License: %s · <a href="%s">Source &amp; file page</a></p>
              </figcaption>
            </figure>"""
            % (
                esc(p["file"]),
                esc(p["alt"]),
                esc(p["title"]),
                esc(p["date"]),
                esc(p["author"]),
                lic_html,
                esc(p["source_url"]),
            )
        )

    videos = [
        {
            "yt": "pCOsgfINdKg",
            "title": "Remarks at the 61st Munich Security Conference",
            "date": "February 14, 2025",
            "channel": "The White House (@WhiteHouse)",
            "url": "https://www.youtube.com/watch?v=pCOsgfINdKg",
        },
        {
            "yt": "FTh-FX25Eps",
            "title": "Commencement Address to the U.S. Air Force Academy",
            "date": "May 2026",
            "channel": "The White House (@WhiteHouse)",
            "url": "https://www.youtube.com/watch?v=FTh-FX25Eps",
        },
        {
            "yt": "y3du2GiOoJg",
            "title": "Fraud Task Force Press Conference",
            "date": "October 21, 2026",
            "channel": "The White House (@WhiteHouse)",
            "url": "https://www.youtube.com/watch?v=y3du2GiOoJg",
        },
        {
            "yt": "R_BILWX5md0",
            "title": "Press Briefing with Karoline Leavitt and the Vice President",
            "date": "January 8, 2026",
            "channel": "The White House (@WhiteHouse)",
            "url": "https://www.youtube.com/watch?v=R_BILWX5md0",
        },
    ]
    video_cards = []
    for v in videos:
        video_cards.append(
            """<div class="video-card">
              <div class="video-wrap">
                <iframe src="https://www.youtube-nocookie.com/embed/%s" title="%s" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
              </div>
              <div class="video-cap">
                <h3>%s</h3>
                <p>%s · Official channel: <a href="%s">%s</a></p>
              </div>
            </div>"""
            % (esc(v["yt"]), esc(v["title"]), esc(v["title"]), esc(v["date"]), esc(v["url"]), esc(v["channel"]))
        )

    body = """
  <div class="hero-disclaimer">
    <div class="wrap">
      <p>Unofficial supporter site. Independently created by supporters of JD Vance. Not affiliated with, authorized, or endorsed by JD Vance, his office, any campaign, committee, or the White House. No funds are solicited or accepted.</p>
    </div>
  </div>
  <article class="wrap">
    <header class="page-hero">
      <p class="kicker">Media gallery</p>
      <h1>Photos, official videos &amp; memes</h1>
      <p>A curated gallery of JD Vance from his Senate and Marine Corps service through the vice presidency, paired with official White House YouTube speeches and embeds from his official X accounts.</p>
      <p class="fine">Last updated __UPDATED__. <strong>Reuse &amp; licensing note:</strong> Images on this page are used under their stated licenses — U.S. federal government public-domain works (17 U.S.C. § 105) or Creative Commons–licensed works on Wikimedia Commons with attribution. Videos and social posts are embedded directly from official White House and JD Vance channels, never reposted from copyrighted news outlets. <a href="images/CREDITS.md">Full credits list</a></p>
    </header>

    <section class="block" id="photos">
      <h2>Permitted photographs (15)</h2>
      <p class="lede">Every photograph below is stored in the repository with its author, date, license, and source link. Eleven are public-domain U.S. government works and four carry Creative Commons attribution licenses.</p>
      <div class="media-grid">
        __PHOTOS__
      </div>
    </section>

    <section class="block" id="videos">
      <h2>Official White House videos &amp; X clips</h2>
      <p class="lede">Speeches, press briefings, and official trip video embedded from The White House YouTube channel and Vice President Vance’s official X accounts.</p>
      <div class="video-grid">
        __VIDEOS__
      </div>
      <div class="embed-grid">
        <div class="embed-card">
          <h3>Thanksgiving meal with troops at Wright-Patterson AFB</h3>
          <p class="embed-credit">Posted by Vice President JD Vance (<code>@VP</code>) · Nov. 25, 2026 · <a href="https://x.com/VP/status/2125644133377441813">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Vice President JD Vance and the Second Family serve food to our troops at Wright Patterson Air Force Base ahead of Thanksgiving. <a href="https://t.co/XMCp81mgio">pic.twitter.com/XMCp81mgio</a></p>&mdash; Vice President JD Vance (@VP) <a href="https://x.com/VP/status/2125644133377441813?ref_src=twsrc%5Etfw">November 25, 2026</a></blockquote>
        </div>
        <div class="embed-card">
          <h3>Nvidia CEO reinstatement (“Welcome back Jensen”)</h3>
          <p class="embed-credit">Posted by JD Vance (<code>@JDVance</code>) · Nov. 23, 2026 PT · <a href="https://x.com/JDVance/status/2125065305504272838">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Welcome back Jensen <a href="https://t.co/HqpDeIz0dz">https://t.co/HqpDeIz0dz</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/2125065305504272838?ref_src=twsrc%5Etfw">November 24, 2026</a></blockquote>
        </div>
      </div>
    </section>

    <section class="block" id="memes">
      <h2>Official memes &amp; lighter moments</h2>
      <p class="lede">Only memes posted directly by JD Vance on his official <code>@JDVance</code> account, embedded via X’s official embed and linked back to each original post.</p>
      <div class="embed-grid">
        <div class="embed-card">
          <h3>Kenny Powers lookalike pose</h3>
          <p class="embed-credit">Credit: JD Vance (<code>@JDVance</code>) · Nov. 23, 2026 · 8,280 likes, 839K views · <a href="https://x.com/JDVance/status/2125007337433838065">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="zxx" dir="ltr"><a href="https://t.co/dHqnOzNGrG">pic.twitter.com/dHqnOzNGrG</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/2125007337433838065?ref_src=twsrc%5Etfw">November 23, 2026</a></blockquote>
        </div>
        <div class="embed-card">
          <h3>Halloween costume with baby Yoda hat</h3>
          <p class="embed-credit">Credit: JD Vance (<code>@JDVance</code>) · Oct. 31, 2026 · 85.6K likes, 7.3M views · <a href="https://x.com/JDVance/status/2116654367952519597">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Happy Halloween everyone! <a href="https://t.co/RkEgQiT9xM">pic.twitter.com/RkEgQiT9xM</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/2116654367952519597?ref_src=twsrc%5Etfw">October 31, 2026</a></blockquote>
        </div>
        <div class="embed-card">
          <h3>Self-parody Halloween wig meme</h3>
          <p class="embed-credit">Credit: JD Vance (<code>@JDVance</code>) · Oct. 31, 2025 · 300.6K likes, 25.1M views · <a href="https://x.com/JDVance/status/1984339141694493023">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="en" dir="ltr">Happy Halloween! <a href="https://t.co/0JOOwlCn8J">pic.twitter.com/0JOOwlCn8J</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/1984339141694493023?ref_src=twsrc%5Etfw">October 31, 2025</a></blockquote>
        </div>
        <div class="embed-card">
          <h3>Pointing meme face edit</h3>
          <p class="embed-credit">Credit: JD Vance (<code>@JDVance</code>) · Mar. 8, 2025 · 502.5K likes, 154M views · <a href="https://x.com/JDVance/status/1898372454235451694">Original X post</a></p>
          <blockquote class="twitter-tweet" data-dnt="true"><p lang="zxx" dir="ltr"><a href="https://t.co/rPloNGHLej">pic.twitter.com/rPloNGHLej</a></p>&mdash; JD Vance (@JDVance) <a href="https://x.com/JDVance/status/1898372454235451694?ref_src=twsrc%5Etfw">March 8, 2025</a></blockquote>
        </div>
      </div>
    </section>
  </article>
  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
""".replace("__UPDATED__", esc(updated)).replace("__PHOTOS__", "".join(photo_cards)).replace("__VIDEOS__", "".join(video_cards))
    return page_shell(
        "Media — JD Vance Tracker",
        "Permitted public-domain and Creative Commons photographs of JD Vance, official White House videos, and official X memes with full credits.",
        "media",
        body,
    )


def write_pages(updated: str) -> None:
    (ROOT / "bio.html").write_text(bio_page(updated), encoding="utf-8")
    (ROOT / "myths.html").write_text(myths_page(updated), encoding="utf-8")
    (ROOT / "media.html").write_text(media_page(updated), encoding="utf-8")
    (ROOT / "opposition.html").write_text(opposition_page(updated), encoding="utf-8")
    myths_dir = ROOT / "myths"
    myths_dir.mkdir(exist_ok=True)
    for m in _myths():
        (myths_dir / f"{m['slug']}.html").write_text(myth_detail_page(updated, m), encoding="utf-8")
    print("Wrote bio.html, myths.html, media.html, opposition.html, and myths detail pages")
