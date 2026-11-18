"""Shared copy for compact myth cards and full-story pages. Do not invent facts."""

from extra_pages import esc, page_shell


def myths():
    return [
        {
            "slug": "couch",
            "n": 1,
            "title_html": "That <cite>Hillbilly Elegy</cite> describes a sexual encounter with a couch",
            "title_plain": "That Hillbilly Elegy describes a sexual encounter with a couch",
            "desc": "The full record of the false claim that JD Vance wrote in Hillbilly Elegy about a sexual encounter with a couch, with fact-checks from Snopes and PolitiFact and a reading of the book.",
            "said_short": "On July 15, 2024, an X user claimed that <cite>Hillbilly Elegy</cite>, pages 179–181, described a sexual act with “an inside-out latex glove shoved between two couch cushions.” Illinois Gov. JB Pritzker later repeated the “obsession with couches” line on television.",
            "verdict": "False: the passage isn’t in the book.",
            "bullets": [
                "Snopes rated the original rumor false. PolitiFact, reviewing Pritzker’s repetition, rated it Pants on Fire.",
                "PolitiFact read pages 179–181 of a 2016 paperback: they describe Vance’s arrival at Ohio State, not a couch. A digital search found ten uses of “couch,” none matching the rumor.",
                "The original poster followed the claim with a “Just Go On the Internet and Tell Lies” meme. A later “first edition” page was a faked e-book edit.",
                "The Associated Press published a fact-check, then removed it for editing-process reasons — not because the rumor was true.",
            ],
            "sources_html": (
                'Fact-checks: <a href="https://www.snopes.com/fact-check/jd-vance-couch-cushions/">Snopes, July 23, 2024 (updated July 26)</a> · '
                '<a href="https://www.politifact.com/factchecks/2024/jul/31/jb-pritzker/pritzker-repeats-a-baseless-claim-about-jd-vance-a/">PolitiFact, July 31, 2024 (Pants on Fire)</a> · related: '
                '<a href="https://www.snopes.com/fact-check/jd-vance-hillbilly-elegy-first-edition-couch-erotica/">Snopes on the fake first-edition page, July 26, 2024</a>. '
                "Primary evidence: PolitiFact’s reading of the 2016 paperback, pages 179–181, and its search of the digital edition. "
                "Pritzker’s remarks are quoted from PolitiFact’s review of ABC’s <cite>This Week</cite>, July 28, 2024."
            ),
            "said_full": (
                "<blockquote>On July 15, 2024 — the day Donald Trump named Vance as his running mate — an X user, "
                "@rickrudescalves, claimed that Vance’s 2016 memoir admitted, on pages 179–181, to a sexual act involving "
                "“an inside-out latex glove shoved between two couch cushions.”</blockquote>\n"
                '            <p class="who">Who spread it: the original X post, then other users who repeated it as if it were in the book. '
                "Illinois Gov. JB Pritzker amplified it on television, telling ABC’s <cite>This Week</cite> on July 28, 2024, "
                "that Trump’s running mate was “getting known for his obsession with couches.” He also joked about a "
                "“Couches Against Trump” Zoom at a July 29 fundraiser. A later variant circulated a fake page said to be from a first edition or galley proof.</p>"
            ),
            "true_full": (
                "<p>The passage does not exist, in the 2016 edition or in the first edition. Snopes rated the original rumor false. "
                "PolitiFact, reviewing Pritzker’s repetition, rated it Pants on Fire and said the claim “surfaced on social media in a satirical post.”</p>\n"
                "            <p>PolitiFact searched a digital copy of the 2016 book and found ten uses of the word “couch,” none in the sense of the rumor, "
                "and no uses of “sofa,” “lounge,” “settee,” or “love seat.” It then read pages 179–181 in a 2016 paperback. Those pages describe Vance’s arrival "
                "at Ohio State, orientation, Columbus’s proximity to Middletown, roommates, financial-aid forms, an interest in law school, and a job at the Ohio Statehouse "
                "— and they do not mention a couch.</p>\n"
                "            <p>The original poster later followed the claim with the “Just Go On the Internet and Tell Lies” meme, which Snopes, citing Know Your Meme, "
                "treated as a signal that he was joking. NewsGuard, cited by PolitiFact, also traced the claim to a satirical post.</p>\n"
                "            <p>A later image, passed off as a first-edition or galley page about the “eroticism” of couch cushions, was fake. Snopes reported that an X user "
                "who circulated scans later described them as “a simple edit of an e-book copy.” The book still contains no such passage.</p>\n"
                "            <p>The Associated Press published a fact-check of the rumor on July 24, 2024, then removed it. The notice on the page, as reported by Snopes, "
                "said the story “did not go through our standard editing process and has been removed.” That withdrawal was about AP’s editing process, not a finding that the rumor was true.</p>"
            ),
            "timeline": [
                (
                    "July 15, 2024",
                    "X user @rickrudescalves posts the claim, citing pages 179–181 of <cite>Hillbilly Elegy</cite>, on the day Donald Trump named Vance as his running mate.",
                ),
                (
                    "Shortly after",
                    "The same poster follows the claim with the “Just Go On the Internet and Tell Lies” meme, which Snopes, citing Know Your Meme, treated as a signal that he was joking.",
                ),
                ("July 23, 2024", "Snopes rates the rumor false (updated July 26)."),
                (
                    "July 24, 2024",
                    "The Associated Press publishes a fact-check, then later removes it. The notice, as reported by Snopes, said the story “did not go through our standard editing process and has been removed.”",
                ),
                (
                    "July 26, 2024",
                    "Snopes publishes a related check on a fake “first edition” or galley page; an X user who circulated scans later described them as “a simple edit of an e-book copy.”",
                ),
                (
                    "July 28, 2024",
                    "Illinois Gov. JB Pritzker tells ABC’s <cite>This Week</cite> that Vance was “getting known for his obsession with couches.”",
                ),
                ("July 29, 2024", "Pritzker jokes about a “Couches Against Trump” Zoom at a fundraiser."),
                (
                    "July 31, 2024",
                    "PolitiFact, reviewing Pritzker’s repetition, rates the claim Pants on Fire and reports that pages 179–181 of a 2016 paperback describe Vance’s arrival at Ohio State and do not mention a couch.",
                ),
            ],
            "evidence": (
                "Primary evidence is the book itself, as opened by the fact-checkers: PolitiFact searched a digital copy of the 2016 edition "
                "(ten uses of “couch,” none in the sense of the rumor; no uses of “sofa,” “lounge,” “settee,” or “love seat”) and read pages 179–181 "
                "in a 2016 paperback. Those pages describe Vance’s arrival at Ohio State, orientation, Columbus’s proximity to Middletown, roommates, "
                "financial-aid forms, an interest in law school, and a job at the Ohio Statehouse. Snopes likewise found no such passage in the 2016 edition "
                "or the first edition. Pritzker’s televised remarks are quoted from PolitiFact’s review of ABC’s <cite>This Week</cite>, July 28, 2024."
            ),
        },
        {
            "slug": "name",
            "n": 2,
            "title_html": "That he changed his name three times to hide who he is",
            "title_plain": "That he changed his name three times to hide who he is",
            "desc": "The full record of the 2024 meme claiming JD Vance changed his name three times to hide who he is, with Snopes, the Associated Press, and official records.",
            "said_short": "A 2024 meme said he was “born as James Donald Bowman,” became “Jimmy Hamel,” and became JD Vance “when he married his wife,” as if he were hiding something.",
            "verdict": "Mixture: he was born James Donald Bowman, but he did not officially change his name three times, or when he married.",
            "bullets": [
                "He was born James Donald Bowman on Aug. 2, 1984, in Middletown, Ohio, named in part for his biological father.",
                "The first official change came when his stepfather, Robert Hamel, adopted him; he became James David Hamel in 1990, the year he started kindergarten, and used that name through high school.",
                "The second official change, to Vance — his grandmother’s family name — became legal in April 2013, a year before he married. “Jimmy Hamel” is not in the record. Dropping the periods in “J.D.” was stylistic, not a third legal change.",
                "Snopes rated the meme a mixture. The Associated Press, using Ohio vital records and documents from his school, the Marine Corps, Ohio State, and Yale, reported the same timeline.",
            ],
            "sources_html": (
                'Fact-check and reporting: <a href="https://www.snopes.com/fact-check/jd-vance-born-james-donald-bowman/">Snopes, Aug. 16, 2024</a> · '
                '<a href="https://apnews.com/article/election-2024-republicans-vice-president-vance-name-359c3d1361c94f5d2d1e9798b7854477">Associated Press, July 26, 2024</a> '
                '(opened via a <a href="https://web.archive.org/web/20240727041018/https://apnews.com/article/election-2024-republicans-vice-president-vance-name-359c3d1361c94f5d2d1e9798b7854477">July 27, 2024 archived copy</a>). '
                "Primary evidence: Ohio vital-records finding and campaign confirmation reported by the AP; Vance’s own account in <cite>Hillbilly Elegy</cite>, as quoted by Snopes and the AP; and "
                '<a href="https://www.middletowncityschools.com/middletown-high-school-news/entry/jd-vance-middletown-high-school-graduate-elected-vice-president/">Middletown City Schools</a>, Nov. 6, 2024. '
                'Additional reporting: <a href="https://www.nytimes.com/2024/07/15/us/politics/jd-vance-name.html">The New York Times, July 15, 2024</a> '
                '(opened via a <a href="https://web.archive.org/web/20240719203813/https://www.nytimes.com/2024/07/15/us/politics/jd-vance-name.html">July 19, 2024 archived copy</a>).'
            ),
            "said_full": (
                "<blockquote>A 2024 social-media meme said Vance was “born as James Donald Bowman,” then “changed middle name to David,” "
                "“changed name again to Jimmy Hamel,” and “changed name to JD Vance 10 years ago when he married his wife.” One version was titled "
                "“WHO ARE YOU?” and asked whether he was “hiding” something.</blockquote>\n"
                '            <p class="who">Who spread it: widely shared image macros on X and similar posts in the summer of 2024, after Vance became the Republican vice-presidential nominee. '
                "Snopes examined a post that had more than 51,000 views when it was reviewed, and readers sent in close variants of the same meme.</p>"
            ),
            "true_full": (
                "<p>He was born James Donald Bowman, in Middletown, Ohio, on Aug. 2, 1984, named in part for his biological father. That much of the meme is true. The rest mixes up the legal record and invents a motive.</p>\n"
                "            <p>There were two official name changes, not three, and neither was a disguise. The first came when his stepfather, Robert Hamel, adopted him. His mother changed his name to James David Hamel — keeping the initials “J.D.,” which were already his nickname. Middletown City Schools, his hometown district, says that change happened in 1990, the year he started kindergarten, and that James David Hamel is the name he used throughout school. He graduated from Middletown High School in 2003. The Associated Press, which reviewed documentation and Ohio vital records, reported that the only birth certificate on file for him at the state’s vital-statistics office reads James David Hamel, because the adoption removed the Bowman name from the public record.</p>\n"
                "            <p>The meme’s “Jimmy Hamel” is not a name in that record. The second official change, to Vance — his grandmother Bonnie Blanton Vance’s family name — became legal in April 2013, as he was about to graduate from Yale Law School, a year before he married. His spokesperson, Taylor Van Kirk, told the AP that it “didn’t happen on his wedding day in 2014, as the book implies.” Dropping the periods in “J.D.” later on was a stylistic preference, not a third legal change. His legal name is James David Vance.</p>\n"
                "            <p>Snopes rated the meme a mixture: true that he was born James Donald Bowman; false that he officially changed his name three times, or that the last change came “when he married.” The AP’s reporting, built on state records and documents from his school, the Marine Corps, Ohio State, and Yale, matches that timeline.</p>"
            ),
            "timeline": [
                ("Aug. 2, 1984", "Born James Donald Bowman in Middletown, Ohio, named in part for his biological father, according to the Associated Press."),
                ("1990", "Middletown City Schools says that, the year he started kindergarten, his mother renamed him James David Hamel, the name he used throughout school. He graduated from Middletown High School in 2003."),
                ("April 2013", "The second official change, to Vance — his grandmother Bonnie Blanton Vance’s family name — became legal as he was about to graduate from Yale Law School, a year before he married, his spokesperson Taylor Van Kirk told the AP."),
                ("Later", "Dropping the periods in “J.D.” was a stylistic preference, not a third legal change. His legal name is James David Vance."),
                ("Summer 2024", "A meme claiming three name changes, including “Jimmy Hamel” and a change “when he married his wife,” spreads after Vance becomes the Republican vice-presidential nominee. Snopes reviewed a post with more than 51,000 views, and close variants."),
                ("July 15, 2024", "The New York Times reports the name history (opened via a July 19, 2024 archived copy)."),
                ("July 26, 2024", "The Associated Press publishes its records-based account (opened via a July 27, 2024 archived copy), including the Ohio vital-records finding that the only birth certificate on file reads James David Hamel."),
                ("Aug. 16, 2024", "Snopes rates the meme a mixture: true that he was born James Donald Bowman; false that he officially changed his name three times, or that the last change came “when he married.”"),
                ("Nov. 6, 2024", "Middletown City Schools publishes a graduate profile restating the 1984 birth name and the 1990 change to James David Hamel."),
            ],
            "evidence": (
                "Primary evidence, as opened or reported in the sources above: the Associated Press reviewed documentation and Ohio vital records and reported that the only birth certificate on file at the state’s vital-statistics office reads James David Hamel, because the adoption removed the Bowman name from the public record. Campaign spokesperson Taylor Van Kirk told the AP the change to Vance became official in April 2013, not on his wedding day in 2014. Vance’s own account in <cite>Hillbilly Elegy</cite> is quoted by Snopes and the AP. Middletown City Schools, his hometown district, says he was born James Donald Bowman in 1984, was renamed James David Hamel in 1990, and used that name throughout school, graduating in 2003."
            ),
        },
        {
            "slug": "dog",
            "n": 3,
            "title_html": "That he admitted his dog Atlas was a campaign “rent-a-dog”",
            "title_plain": "That he admitted his dog Atlas was a campaign “rent-a-dog”",
            "desc": "The full record of the claim that JD Vance admitted his dog Atlas was a campaign rent-a-dog, with fact-checks from PolitiFact and FactCheck.org and quotes from the interview.",
            "said_short": "In mid-September 2024, short clips of Vance’s interview with Tucker Carlson were posted as if he had admitted that his German shepherd, Atlas, was “a rent-a-dog that was given to me by the campaign.”",
            "verdict": "False: the clip was cut to hide a joke about an online rumor.",
            "bullets": [
                "In the full interview, Vance said he “found out on the internet” that Atlas was supposedly a rent-a-dog, then that the family “got him when he was an 8-week-old puppy.”",
                "PolitiFact rated the claim False and wrote that “the video was deceptively edited.”",
                "FactCheck.org reached the same conclusion: the posts “misrepresent” his comments.",
                "A Vance spokesman told PolitiFact the family got Atlas as an 8-week-old puppy in January 2024 — before Vance became the vice-presidential nominee.",
            ],
            "sources_html": (
                'Fact-checks: <a href="https://www.politifact.com/factchecks/2024/sep/22/social-media/jd-vances-german-shepherd-atlas-is-his-actual-dog/">PolitiFact, Sept. 22, 2024 (False)</a> · '
                '<a href="https://www.factcheck.org/2024/09/posts-misrepresent-vances-comments-about-his-pet-dog/">FactCheck.org, Sept. 24, 2024</a>. '
                "Primary evidence: the Sept. 18, 2024 Carlson interview, as quoted in full by both fact-checks. This item does not rely on Snopes."
            ),
            "said_full": (
                "<blockquote>In mid-September 2024, short clips of Vance’s interview with Tucker Carlson were posted as if Vance had admitted that his German shepherd, Atlas, was “a rent-a-dog that was given to me by the campaign to make me seem like I’m a dog fan.”</blockquote>\n"
                '            <p class="who">Who spread it: videos and captions on TikTok, Threads, and X around Sept. 21, 2024, cut from a Sept. 18 interview on Carlson’s Rumble show. One Threads caption said, “The campaign got JD a dog to make him appear more human.” Another said, “JD Vance admits he has a ‘rent-a-dog.’”</p>'
            ),
            "true_full": (
                "<p>The clips were cut in a way that hid the setup. In the full interview, Vance was mocking an online rumor, not confessing to it. He introduced the dog by saying, “this is Atlas, which I found out on the internet a few weeks ago that he’s actually a rent-a-dog that was given to me by the campaign to make me seem like I’m a dog fan.” He then said, “Of course, we got him when he was an 8-week-old puppy,” and that it was “shocking” anyone would think otherwise.</p>\n"
                "            <p>PolitiFact rated the claim False and wrote that “the video was deceptively edited.” FactCheck.org reached the same conclusion: the posts “misrepresent” the comments. A Vance spokesman told PolitiFact the family got Atlas as an 8-week-old puppy in January 2024 — before Vance became the vice-presidential nominee.</p>"
            ),
            "timeline": [
                ("January 2024", "A Vance spokesman told PolitiFact the family got Atlas as an 8-week-old puppy, before Vance became the vice-presidential nominee."),
                ("Sept. 18, 2024", "Vance appears with Atlas in an interview with Tucker Carlson on Carlson’s Rumble show and jokes about the online rumor, then says the family got the dog as an 8-week-old puppy."),
                ("Around Sept. 21, 2024", "Short clips and captions circulate on TikTok, Threads, and X as if Vance had admitted the dog was a campaign “rent-a-dog.” One Threads caption said, “The campaign got JD a dog to make him appear more human.”"),
                ("Sept. 22, 2024", "PolitiFact rates the claim False and writes that “the video was deceptively edited.”"),
                ("Sept. 24, 2024", "FactCheck.org concludes that the posts “misrepresent” Vance’s comments. This item does not rely on Snopes."),
            ],
            "evidence": (
                "Primary evidence is the Sept. 18, 2024 Carlson interview, as quoted in full by both fact-checks. Vance introduced the dog by saying, “this is Atlas, which I found out on the internet a few weeks ago that he’s actually a rent-a-dog that was given to me by the campaign to make me seem like I’m a dog fan.” He then said, “Of course, we got him when he was an 8-week-old puppy,” and that it was “shocking” anyone would think otherwise. A Vance spokesman told PolitiFact the family got Atlas as an 8-week-old puppy in January 2024."
            ),
        },
    ]


def myths_page(updated: str) -> str:
    cards = []
    for m in myths():
        bullets = "".join("<li>%s</li>" % b for b in m["bullets"])
        cards.append(
            """
      <article class="myth-card">
        <header class="myth-card-top">
          <p class="kicker">Myth %s</p>
          <h2>%s</h2>
        </header>
        <div class="myth-grid">
          <div class="myth-col said">
            <h3>What they said</h3>
            <p>%s</p>
          </div>
          <div class="myth-col true">
            <h3>What is true</h3>
            <p class="verdict">%s</p>
            <ul>%s</ul>
            <a class="btn-more" href="myths/%s.html">Read more <span aria-hidden="true">→</span></a>
          </div>
        </div>
        <div class="myth-foot">
          <p class="sources">%s</p>
        </div>
      </article>"""
            % (
                m["n"],
                m["title_html"],
                m["said_short"],
                esc(m["verdict"]),
                bullets,
                m["slug"],
                m["sources_html"],
            )
        )

    body = """
  <article class="wrap">
    <header class="page-hero">
      <p class="kicker">Fact checks</p>
      <h1>Myths vs. facts</h1>
      <p>Viral smears about JD Vance, set out as they were told and as the record stands. Each card has two columns: <strong>What they said</strong> and <strong>What is true</strong>. Open <strong>Read more</strong> for the full story, the timeline, and the primary evidence. We cite at least two independent fact-checkers or a fact-checker plus a major news organization for every item, and we link the primary evidence those checks used — the book, the interview, or the official record — whenever we opened it.</p>
      <p class="fine">Last updated %s. This page includes only claims that fact-checkers examined as stories about Vance, not fact-checks of statements he made about policy or other people. Snopes appears only where it debunks a smear against him, never as the sole source and never as the referee of a criticism of his record.</p>
    </header>

    <section class="block">
      %s
    </section>

    <section class="block">
      <h2>What this page does not do</h2>
      <p>It does not collect every harsh joke, policy dispute, or campaign attack. It also does not use fact-checks of <em>Vance’s own claims</em> — for example, statements he made about the 2024 campaign, or claims he repeated about Springfield, Ohio — as “myths about him.” Those are a different question, and they belong in political reporting, not on a list of fabrications about his life.</p>
    </section>
  </article>
""" % (esc(updated), "".join(cards))
    return page_shell(
        "Myths vs. facts — JD Vance Tracker",
        "Side-by-side fact-checks of viral claims about JD Vance, including the fabricated couch rumor, claims about his name, and the rent-a-dog hoax, with links to Snopes, PolitiFact, the Associated Press, and FactCheck.org.",
        "myths",
        body,
    )


def myth_detail_page(updated: str, m: dict) -> str:
    steps = "".join(
        '<div class="tl"><p class="when">%s</p><p>%s</p></div>' % (when, what)
        for when, what in m["timeline"]
    )
    body = """
  <article class="wrap">
    <header class="page-hero">
      <p class="crumb"><a href="../myths.html">← Myths vs. facts</a></p>
      <p class="kicker">Myth %s · The whole story</p>
      <h1>%s</h1>
      <p class="verdict">%s</p>
      <p class="fine">Last updated %s. This page keeps the full record behind the short card on the Myths vs. facts page: what was claimed, what the fact-checks found, a timeline, and the primary evidence.</p>
    </header>

    <section class="block">
      <div class="myth-grid myth-detail-grid">
        <div class="myth-col said">
          <h3>What they said</h3>
          %s
        </div>
        <div class="myth-col true">
          <h3>What is true</h3>
          %s
        </div>
      </div>
    </section>

    <section class="block">
      <h2>Timeline</h2>
      <div class="timeline">
        %s
      </div>
    </section>

    <section class="block">
      <h2>Primary evidence</h2>
      <p>%s</p>
    </section>

    <section class="block">
      <h2>Sources</h2>
      <p class="sources">%s</p>
      <p><a class="btn-more" href="../myths.html">← Back to Myths vs. facts</a></p>
    </section>
  </article>
""" % (
        m["n"],
        m["title_html"],
        esc(m["verdict"]),
        esc(updated),
        m["said_full"],
        m["true_full"],
        steps,
        m["evidence"],
        m["sources_html"],
    )
    return page_shell(
        "%s — Myths vs. facts — JD Vance Tracker" % m["title_plain"],
        m["desc"],
        "myths",
        body,
        root="../",
    )
