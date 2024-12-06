# Vibe Check

### _Analyzing the Political Pulse: A Journey through YouTube's Election Discussions_

2024 has been the year of democratic elections around the world – a whopping [70 countries went to the polls](https://www.cnn.com/2024/07/08/world/global-elections-2024-maps-charts-dg/index.html) to exercise their fundamental rights to vote. Among these, the U.S. presidential elections have captured global attention due to their far-reaching implications.

Naturally, the 2024 presidential elections and their debates have spurred millions of conversations around the world, both online and offline. With Internet being the most widespread form of communication, Our project, **Vibe Check**, capitalizes on this by exploring the rich terrain of YouTube comments to gauge public opinion and unearth trends related to political biases.

## Why does this matter?
Public sentiment is a heavyweight in the political arena, especially during pivotal events like the U.S. Presidential elections. In today's era of ubiquitous online expression, platforms like YouTube are treasure troves of spontaneous public discourse.

Traditional methods like polls and surveys do their part, but at Vibe Check, we mine the rich seam of YouTube comments for real-time, data-driven insights.

Using advanced data science techniques, Vibe Check swiftly sifts through and categorizes heaps of textual data. This not only provides a real-time pulse on political biases and voter sentiment but also reveals a rainbow spectrum of opinions that might slip through the cracks with conventional approaches.

These insights are incredibly valuable—they peel back the layers of voter behavior and sentiment, fostering informed decision-making across various domains, including policy-making, campaign strategy, journalism, marketing, and educational content.

## Data, Data, and Data

Our journey started in the middle of August 2024, when one presidential debate ([Biden vs Trump](https://en.wikipedia.org/wiki/2024_Joe_Biden%E2%80%93Donald_Trump_presidential_debate)) had already taken place and a new Democrat candidate had stepped up. Using the [YouTube API](https://developers.google.com/youtube/v3/getting-started), we pulled comments from debates posted by several networks on different sides of the political spectrum.

Now, how did we identify a network’s media bias? This information, thankfully, has been made available to us by the folks over at [AllSides](https://www.allsides.com/media-bias/media-bias-chart). This not only enriched our analysis but ensured a balanced perspective in our dataset.

Simultaneously, we revisited the [first 2020 presidential debate](https://en.wikipedia.org/wiki/2020_United_States_presidential_debates#September_29:_First_presidential_debate_(Case_Western_Reserve_University)). By comparing comments from both election cycles, pulled from a diversity of news outlets labeled as left, center, and right, we sought to illuminate shifts in public opinion and discourse.

### Live chats

Entering September, we had to prepare for 2 upcoming debates: the [2nd presidential debate (Harris vs Trump)](https://en.wikipedia.org/wiki/2024_United_States_presidential_debates#September_10:_Second_presidential_debate_(ABC,_Philadelphia)) and the [Vice-presidential debate (Vance vs Walz)](https://en.wikipedia.org/wiki/2024_United_States_presidential_debates#October_1:_Vice_presidential_debate_(CBS,_New_York_City)), most likely to scrape comments as the debates aired live. But why? This is to capture YouTube Live chats.

[YouTube Live chats](https://support.google.com/youtube/answer/2524549?hl=en) differ from YouTube comments – you would see Live chats in live videos as floating comments as opposed to actual YouTube comments that stay in the video. They exist temporarily during live broadcasts, showcasing raw, knee-jerk viewer reactions. Live chats typically can be sent by any user and stay for as long as the livestream lasts (but can take up to 24 hours after the live video posting for all chats to come in). They can also be replayed.

Therefore, we had to set up a unique data scraper tailored for Live chats using the  [`pytchat`](https://github.com/taizan-hokuto/pytchat) library. This ran a scraper through a live video and dumped the scraped chats into JSON files.

Now, do Live chats always come up on live videos? [Unfortunately, no]( https://support.google.com/youtube/answer/9826490?hl=en#zippy=%2Caccess-channel-activity-from-live-chat-feed). YouTube, being the flexible platform it is, does allow channel owners to ban Live chats or restrict them to a small group of users. And to our surprise (and chagrin), we found most giant media networks to prefer these options. Despite these hurdles, we managed to survey and track down several networks that still supported them, albeit a few of them with restrictions, and adapted our scraping strategies accordingly.

An intriguing case involved those channels which uniquely allowed only itself to post Live chats, such as NBC and Associated Press. Done primarily to fact-check the candidates' statements during the debate, this posed both a challenge and an opportunity to further enhance the authenticity and depth of our analysis.

**_A summary of the networks we surveyed and scraped:_**

| **Network**                     | **Media Bias** |
|---------------------------------|----------------|
| Wall Street Journal             | Lean Right     |      
| C-SPAN                          | Center         |
| Fox News                        | Lean Left      |
| Sky News                        | Lean Left      |
| MSNBC                           | Left           |
| News Max                        | Right          |
| CBS                             | Lean Left      |
| NBC                             | Lean Left      |
| USA Today                       | Lean Left      |
| CNN TV-18                       | Center         |
| WFLA                            | Center         |
| Kamala Harris's YouTube Channel | Left           |
| Tim Walz's YouTube Channel      | Left           |
| Washington Post                 | Lean Left      |
| News Max                        | Right          |
| CNBC TV-18                      | Center         |
| WFAA                            | Left           |
| Associated Press                | Left           |

Through these meticulous efforts, we effectively consolidated, processed, and cleaned the scraped data to form a **dataset with over 190,000 entries**.

### YouTube's Election Policy

A side note on [YouTube's election-specific policies](https://www.youtube.com/howyoutubeworks/our-commitments/supporting-political-integrity/) — understanding how the platform handles election content was essential for adapting our strategies.

## Unpacking Data: How We Analyze Political Sentiments

### Simplifying Complexity: Text Summarization in Action

In Vibe Check, we employed text summarization to condense extended discussions into digestible, concise summaries that highlight the core sentiments and prevailing opinions about the presidential debates. Here's a snapshot of the output:

![Text Summaries of the 4 debates](./images/text%20summaries.png)

Across 2020 and 2024, the repetitive emphasis on and endorsement of President-Elect Trump is present. The text summaries underscore a fascinating trend: overwhelming support for the Republican candidates, even within debates aired on more left-leaning networks. This was particularly interesting during the second 2024 presidential debate, where such a pattern wasn’t just evident; it dominated the summarized discourse.

Along with chant-like support for the candidates, we see a quirky inclusion of a phrase related to "Russian bot homies," which might reflect the notorious issue of bot involvement in online discussions. The vice-presidential debate reflects a deeply polarized viewer base and a mixed bag of views, with some comments highly praising Vance’s performance.

### Thematic Analysis of Debates Using Latent Dirichlet Allocation

We dove into our dataset using a technique called [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) to really dig into the themes hidden in the comments. LDA is a statistical model that identifies topics in a collection of documents by grouping together frequently co-occurring words.

We hit optimal results with **10 topics**, landing a coherence score of **0.552**. A [coherence score](https://towardsdatascience.com/understanding-topic-coherence-measures-4aa41339634c) is a rating for how relevant or how much sense the words in each topic make together – the closer to 1, the clearer and more distinct the topic.

With a score of 0.552, our topics are moderately interpretable. While not exceptionally high, this score indicates that there is a reasonable degree of thematic relevance and distinction within the derived topics, making the model useful for exploring and understanding the main themes in the debates. Here's a summary of interesting findings of each topic when LDA was performed for the entire dataset:

![Full Dataset - LDA summary](./images/topic%20modeling_full%20dataset_summary.png)

We've also performed analysis per debate, whose key observations are as follows:
- The 2020 Presidential Debate had mentions of COVID-19 + vaccines, and there was significant
talk about moderators (biased, interrupting)
- The 2024 Presidential Debate 1 had mentions of the candidates themselves, their age, and
emphasis on America + voting.
- The 2024 Presidential Debate 2 sees mentions of Kamala Harris (new Democrat candidate) and
a significant rise in policies (war, abortion, tax, inflation even the pandemic). There is still talk
about the debate itself, moderators, and fact-checking.
- The 2024 Vice presidential debate mentions the candidates (J D Vance, Tim Walz), the
presidential candidates, support and polling, not to mention smug nicknames.


We've jazzed up our findings with some incredible visualizations using the [`pyLDAvis`](https://pypi.org/project/pyLDAvis/) library – it’s a fantastic way to see what each of the 10 topics is all about.

Each visualization dashboard allows the exploring of different topics that our LDA model has identified from the YouTube comments. By hovering over the various bubbles, we can see the top keywords that are driving the topics. To see how specific terms play a role in political discussions, we can click on a topic to highlight its associated terms and get a clearer view of how often they appear and their relevance within that topic. Adjusting the relevance metric will help us view less frequent but more exclusive terms to each topic or broad terms that are common across multiple topics.

Follow these links to interact with the HTML dashboards we created, and have fun exploring the visual maps of our analysis!
- [Full Dataset](https://html-preview.github.io/?url=https://github.com/deeptika/vibe-check-blog/blob/24b1daa276750a610a0750e600ee184134304a54/static/vis_full_dataset_initial_model.html)
- [2020 Presidential Debate 1: Biden vs Trump](https://html-preview.github.io/?url=https://github.com/deeptika/vibe-check-blog/blob/24b1daa276750a610a0750e600ee184134304a54/static/vis_2020%20Presidential%20Debate_%20Biden%20vs%20Trump_initial_model.html)
- [2024 Presidential Debate 1: Biden vs Trump](https://html-preview.github.io/?url=https://github.com/deeptika/vibe-check-blog/blob/24b1daa276750a610a0750e600ee184134304a54/static/vis_2024%20Presidential%20Debate%201_%20Biden%20vs%20Trump_initial_model.html)
- [2024 Presidential Debate 2: Harris vs Trump](https://html-preview.github.io/?url=https://github.com/deeptika/vibe-check-blog/blob/24b1daa276750a610a0750e600ee184134304a54/static/vis_2024%20Presidential%20Debate%202_%20Harris%20vs%20Trump_initial_model.html)
- [2024 Vice-presidential Debate: Vance vs Walz](https://html-preview.github.io/?url=https://github.com/deeptika/vibe-check-blog/blob/24b1daa276750a610a0750e600ee184134304a54/static/vis_2024%20Vice%20Presidential%20Debate_%20Vance%20vs%20Walz_initial_model.html)

### Exploring Political Bias: Insights from YouTube Comments

To uncover political leanings in YouTube discussions, we conducted a detailed analysis by looking into the political orientation of various news networks. We used a scale from -2 for strongly left-leaning to +2 for strongly right-leaning networks, based on the Allsides media bias chart. Instead of manually reading thousands of comments, we transformed them into numerical values using [TF-IDF vectorization](https://scikit-learn.org/1.5/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to highlight the most prominent words and phrases. This allowed us to handle the data more effectively.

Next, we simplified this complex information to understand broader trends, which we then illustrated in an easy-to-read graph. This graph helped us spot patterns, showing us how the political tilt of a news channel might influence the types of comments it receives. These visual findings not only confirmed some of our expectations about media bias but also provided a clear, tangible way to see how political discussion varies across different media channels. Here's the scatter plot that visualizes the bias of each comment (each point on the scatter plot represents a comment):

![Visualization: t-SNE scatter plot](./images/media%20bias%20t-sne.png)

The [t-SNE visualization](https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding) of YouTube comments by political bias provides a fascinating snapshot of online political discussions. In this scatter plot, comments from left-leaning sources are marked in blue, center-leaning in green, and right-leaning in orange.

Noticeably, there is a significant blending of blue and orange dots, indicating that topics discussed by left and right commenters often overlap, suggesting similarities in language usage or shared concerns across these groups. The green dots, representing centrist comments, are less frequent and scattered throughout, hinting at a lower presence or less distinctive linguistic patterns among moderate views.

This visual mingling emphasizes the complex nature of online political discourse, where diverse opinions often intersect, reflecting a vibrant, engaged community across the spectrum. The plot underscores the importance of considering how we categorize and understand these interactions, hinting at underlying commonalities that might bridge divides or reveal shared priorities among seemingly disparate groups.

## Media Bias: The Great Debate Shift
The shift in public discourse between 2020 and 2024 tells a compelling story. While 2020's conversations were dominated by COVID-19 and vaccine discussions, 2024 has seen a dramatic pivot toward policy-focused debates. The public's attention has turned to pressing issues like abortion rights, economic concerns, and detailed policy proposals, showing a marked evolution in political engagement.

Perhaps our most surprising discovery challenges conventional wisdom about media polarization. Contrary to popular belief, we found that comment content is primarily shaped by debate topics rather than network bias. Viewers across different networks, from Fox News to MSNBC, engage with content in remarkably similar ways, suggesting that the walls between political echo chambers might be more permeable than we thought.

The 2024 Vice Presidential debate saw a surge in policy talk and candidate chatter. Looks like the understudies are stealing some of the spotlight!

## What's Next on the Vibe Check Agenda?

As we approach the 2024 election, our work continues to evolve. We're enhancing our analysis tools, developing more sophisticated visualization techniques, and expanding our understanding of how media influences public opinion. The insights we've gained don't just represent academic findings – they offer a window into the changing nature of political discourse in the digital age.

Through Vibe Check, we're not just analyzing comments; we're mapping the landscape of modern political dialogue, one comment at a time. Our findings suggest that despite the apparent polarization in American politics, there might be more common ground in how we engage with political content than previously thought.
















 

