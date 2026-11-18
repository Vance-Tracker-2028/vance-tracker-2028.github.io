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
      <p>Viral smears about JD Vance, set out as they were told and as the record stands. Each card has two columns: <strong>What they said</strong> and <strong>What is true</strong>. We cite at least two independent fact-checkers or a fact-checker plus a major news organization for every item, and we link the primary evidence those checks used — the book, the interview, or the official record — whenever we opened it.</p>
      <p class="fine">Last updated {esc(updated)}. This page includes only claims that fact-checkers examined as stories about Vance, not fact-checks of statements he made about policy or other people. Snopes appears only where it debunks a smear against him, never as the sole source and never as the referee of a criticism of his record.</p>
    </header>

    <section class="block">
      <article class="myth-card">
        <header class="myth-card-top">
          <p class="kicker">Myth 1</p>
          <h2>That <cite>Hillbilly Elegy</cite> describes a sexual encounter with a couch</h2>
        </header>
        <div class="myth-grid">
          <div class="myth-col said">
            <h3>What they said</h3>
            <blockquote>On July 15, 2024 — the day Donald Trump named Vance as his running mate — an X user, @rickrudescalves, claimed that Vance’s 2016 memoir admitted, on pages 179–181, to a sexual act involving “an inside-out latex glove shoved between two couch cushions.”</blockquote>
            <p class="who">Who spread it: the original X post, then other users who repeated it as if it were in the book. Illinois Gov. JB Pritzker amplified it on television, telling ABC’s <cite>This Week</cite> on July 28, 2024, that Trump’s running mate was “getting known for his obsession with couches.” He also joked about a “Couches Against Trump” Zoom at a July 29 fundraiser. A later variant circulated a fake page said to be from a first edition or galley proof.</p>
          </div>
          <div class="myth-col true">
            <h3>What is true</h3>
            <p>The passage does not exist, in the 2016 edition or in the first edition. Snopes rated the original rumor false. PolitiFact, reviewing Pritzker’s repetition, rated it Pants on Fire and said the claim “surfaced on social media in a satirical post.”</p>
            <p>PolitiFact searched a digital copy of the 2016 book and found ten uses of the word “couch,” none in the sense of the rumor, and no uses of “sofa,” “lounge,” “settee,” or “love seat.” It then read pages 179–181 in a 2016 paperback. Those pages describe Vance’s arrival at Ohio State, orientation, Columbus’s proximity to Middletown, roommates, financial-aid forms, an interest in law school, and a job at the Ohio Statehouse — and they do not mention a couch.</p>
            <p>The original poster later followed the claim with the “Just Go On the Internet and Tell Lies” meme, which Snopes, citing Know Your Meme, treated as a signal that he was joking. NewsGuard, cited by PolitiFact, also traced the claim to a satirical post.</p>
            <p>A later image, passed off as a first-edition or galley page about the “eroticism” of couch cushions, was fake. Snopes reported that an X user who circulated scans later described them as “a simple edit of an e-book copy.” The book still contains no such passage.</p>
            <p>The Associated Press published a fact-check of the rumor on July 24, 2024, then removed it. The notice on the page, as reported by Snopes, said the story “did not go through our standard editing process and has been removed.” That withdrawal was about AP’s editing process, not a finding that the rumor was true.</p>
          </div>
        </div>
        <div class="myth-foot">
          <p class="sources">Fact-checks: <a href="https://www.snopes.com/fact-check/jd-vance-couch-cushions/">Snopes, July 23, 2024 (updated July 26)</a> · <a href="https://www.politifact.com/factchecks/2024/jul/31/jb-pritzker/pritzker-repeats-a-baseless-claim-about-jd-vance-a/">PolitiFact, July 31, 2024 (Pants on Fire)</a> · related: <a href="https://www.snopes.com/fact-check/jd-vance-hillbilly-elegy-first-edition-couch-erotica/">Snopes on the fake first-edition page, July 26, 2024</a>. Primary evidence: PolitiFact’s reading of the 2016 paperback, pages 179–181, and its search of the digital edition. Pritzker’s remarks are quoted from PolitiFact’s review of ABC’s <cite>This Week</cite>, July 28, 2024.</p>
        </div>
      </article>

      <article class="myth-card">
        <header class="myth-card-top">
          <p class="kicker">Myth 2</p>
          <h2>That he changed his name three times to hide who he is</h2>
        </header>
        <div class="myth-grid">
          <div class="myth-col said">
            <h3>What they said</h3>
            <blockquote>A 2024 social-media meme said Vance was “born as James Donald Bowman,” then “changed middle name to David,” “changed name again to Jimmy Hamel,” and “changed name to JD Vance 10 years ago when he married his wife.” One version was titled “WHO ARE YOU?” and asked whether he was “hiding” something.</blockquote>
            <p class="who">Who spread it: widely shared image macros on X and similar posts in the summer of 2024, after Vance became the Republican vice-presidential nominee. Snopes examined a post that had more than 51,000 views when it was reviewed, and readers sent in close variants of the same meme.</p>
          </div>
          <div class="myth-col true">
            <h3>What is true</h3>
            <p>He was born James Donald Bowman, in Middletown, Ohio, on Aug. 2, 1984, named in part for his biological father. That much of the meme is true. The rest mixes up the legal record and invents a motive.</p>
            <p>There were two official name changes, not three, and neither was a disguise. The first came when his stepfather, Robert Hamel, adopted him. His mother changed his name to James David Hamel — keeping the initials “J.D.,” which were already his nickname. Middletown City Schools, his hometown district, says that change happened in 1990, the year he started kindergarten, and that James David Hamel is the name he used throughout school. He graduated from Middletown High School in 2003. The Associated Press, which reviewed documentation and Ohio vital records, reported that the only birth certificate on file for him at the state’s vital-statistics office reads James David Hamel, because the adoption removed the Bowman name from the public record.</p>
            <p>The meme’s “Jimmy Hamel” is not a name in that record. The second official change, to Vance — his grandmother Bonnie Blanton Vance’s family name — became legal in April 2013, as he was about to graduate from Yale Law School, a year before he married. His spokesperson, Taylor Van Kirk, told the AP that it “didn’t happen on his wedding day in 2014, as the book implies.” Dropping the periods in “J.D.” later on was a stylistic preference, not a third legal change. His legal name is James David Vance.</p>
            <p>Snopes rated the meme a mixture: true that he was born James Donald Bowman; false that he officially changed his name three times, or that the last change came “when he married.” The AP’s reporting, built on state records and documents from his school, the Marine Corps, Ohio State, and Yale, matches that timeline.</p>
          </div>
        </div>
        <div class="myth-foot">
          <p class="sources">Fact-check and reporting: <a href="https://www.snopes.com/fact-check/jd-vance-born-james-donald-bowman/">Snopes, Aug. 16, 2024</a> · <a href="https://apnews.com/article/election-2024-republicans-vice-president-vance-name-359c3d1361c94f5d2d1e9798b7854477">Associated Press, July 26, 2024</a> (opened via a <a href="https://web.archive.org/web/20240727041018/https://apnews.com/article/election-2024-republicans-vice-president-vance-name-359c3d1361c94f5d2d1e9798b7854477">July 27, 2024 archived copy</a>). Primary evidence: Ohio vital-records finding and campaign confirmation reported by the AP; Vance’s own account in <cite>Hillbilly Elegy</cite>, as quoted by Snopes and the AP; and <a href="https://www.middletowncityschools.com/middletown-high-school-news/entry/jd-vance-middletown-high-school-graduate-elected-vice-president/">Middletown City Schools</a>, Nov. 6, 2024. Additional reporting: <a href="https://www.nytimes.com/2024/07/15/us/politics/jd-vance-name.html">The New York Times, July 15, 2024</a> (opened via a <a href="https://web.archive.org/web/20240719203813/https://www.nytimes.com/2024/07/15/us/politics/jd-vance-name.html">July 19, 2024 archived copy</a>).</p>
        </div>
      </article>

      <article class="myth-card">
        <header class="myth-card-top">
          <p class="kicker">Myth 3</p>
          <h2>That he admitted his dog Atlas was a campaign “rent-a-dog”</h2>
        </header>
        <div class="myth-grid">
          <div class="myth-col said">
            <h3>What they said</h3>
            <blockquote>In mid-September 2024, short clips of Vance’s interview with Tucker Carlson were posted as if Vance had admitted that his German shepherd, Atlas, was “a rent-a-dog that was given to me by the campaign to make me seem like I’m a dog fan.”</blockquote>
            <p class="who">Who spread it: videos and captions on TikTok, Threads, and X around Sept. 21, 2024, cut from a Sept. 18 interview on Carlson’s Rumble show. One Threads caption said, “The campaign got JD a dog to make him appear more human.” Another said, “JD Vance admits he has a ‘rent-a-dog.’”</p>
          </div>
          <div class="myth-col true">
            <h3>What is true</h3>
            <p>The clips were cut in a way that hid the setup. In the full interview, Vance was mocking an online rumor, not confessing to it. He introduced the dog by saying, “this is Atlas, which I found out on the internet a few weeks ago that he’s actually a rent-a-dog that was given to me by the campaign to make me seem like I’m a dog fan.” He then said, “Of course, we got him when he was an 8-week-old puppy,” and that it was “shocking” anyone would think otherwise.</p>
            <p>PolitiFact rated the claim False and wrote that “the video was deceptively edited.” FactCheck.org reached the same conclusion: the posts “misrepresent” the comments. A Vance spokesman told PolitiFact the family got Atlas as an 8-week-old puppy in January 2024 — before Vance became the vice-presidential nominee.</p>
          </div>
        </div>
        <div class="myth-foot">
          <p class="sources">Fact-checks: <a href="https://www.politifact.com/factchecks/2024/sep/22/social-media/jd-vances-german-shepherd-atlas-is-his-actual-dog/">PolitiFact, Sept. 22, 2024 (False)</a> · <a href="https://www.factcheck.org/2024/09/posts-misrepresent-vances-comments-about-his-pet-dog/">FactCheck.org, Sept. 24, 2024</a>. Primary evidence: the Sept. 18, 2024 Carlson interview, as quoted in full by both fact-checks. This item does not rely on Snopes.</p>
        </div>
      </article>
    </section>

    <section class="block">
      <h2>What this page does not do</h2>
      <p>It does not collect every harsh joke, policy dispute, or campaign attack. It also does not use fact-checks of <em>Vance’s own claims</em> — for example, statements he made about the 2024 campaign, or claims he repeated about Springfield, Ohio — as “myths about him.” Those are a different question, and they belong in political reporting, not on a list of fabrications about his life.</p>
    </section>
  </article>
"""
    return page_shell(
        "Myths vs. facts — JD Vance Tracker",
        "Side-by-side fact-checks of viral claims about JD Vance, including the fabricated couch rumor, claims about his name, and the rent-a-dog hoax, with links to Snopes, PolitiFact, the Associated Press, and FactCheck.org.",
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
