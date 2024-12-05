# Vibe Check

### _Analyzing the Political Pulse: A Journey through YouTube's Election Discussions_

2024 has been the year of democratic elections around the world – a whopping [70 countries went to the polls](https://www.cnn.com/2024/07/08/world/global-elections-2024-maps-charts-dg/index.html) to exercise their fundamental rights to vote. Among these, the U.S. presidential elections have captured global attention due to their far-reaching implications.

Naturally, the 2024 presidential elections and their debates have spurred millions of conversations around the world, both online and offline. With Internet being the most widespread form of communication, Our project, **Vibe Check**, capitalizes on this by exploring the rich terrain of YouTube comments to gauge public opinion and unearth trends related to political biases.

## Why does this matter?
Public sentiment plays a pivotal role in shaping political landscapes, particularly during significant events like the U.S. Presidential elections. In today’s digital age where freedom of speech proliferates online, engaging platforms such as YouTube provide a goldmine of real-time public discourse.

While there are conventional methods of gauging public reactions like polls and surveys, we at Vibe Check rely on already available rich discourse in the form of YouTube comments to generate data-backed insights.

By employing sophisticated data science techniques, Vibe Check efficiently processes and categorizes large volumes of textual data. This enables us to deliver insights into political biases and voter tendencies rapidly, providing a fresh and immediate snapshot of the political pulse. It also brings to light a spectrum of diverse views that might be overlooked in traditional methods.

Such insights are crucial as they help us understand the nuances of voter behavior and sentiment. Potentially, this would encourage informed decision-making in several use cases - policies and campaign management, nuanced journalism, marketing and content creation, forming educational material - the list goes on.

## Data, Data, and Data

Our journey started in the middle of August 2024, when one presidential debate ([Biden vs Trump](https://en.wikipedia.org/wiki/2024_Joe_Biden%E2%80%93Donald_Trump_presidential_debate)) had already taken place and a new Democrat candidate had stepped up. Using the [YouTube API](https://developers.google.com/youtube/v3/getting-started), we pulled comments from debates posted by several networks on different sides of the political spectrum.

Now, how did we identify a network’s media bias? This information, thankfully, has been made available to us by the folks over at [AllSides](https://www.allsides.com/media-bias/media-bias-chart). This not only enriched our analysis but ensured a balanced perspective in our dataset.

Simultaneously, we revisited the [first 2020 presidential debate](https://en.wikipedia.org/wiki/2020_United_States_presidential_debates#September_29:_First_presidential_debate_(Case_Western_Reserve_University)). By comparing comments from both election cycles, pulled from a diversity of news outlets labeled as left, center, and right, we sought to illuminate shifts in public opinion and discourse.

### Live Chats

Entering September, we had to prepare for 2 upcoming debates: the [2nd presidential debate (Harris vs Trump)](https://en.wikipedia.org/wiki/2024_United_States_presidential_debates#September_10:_Second_presidential_debate_(ABC,_Philadelphia)) and the [Vice-presidential debate (Vance vs Walz)](https://en.wikipedia.org/wiki/2024_United_States_presidential_debates#October_1:_Vice_presidential_debate_(CBS,_New_York_City)), most likely to scrape comments as the debates aired live. But why? This is to capture YouTube Live chats.

[YouTube Live chats](https://support.google.com/youtube/answer/2524549?hl=en) differ from YouTube comments – you would see Live chats in live videos as floating comments as opposed to actual YouTube comments that stay in the video. They exist temporarily during live broadcasts, showcasing raw, knee-jerk viewer reactions. Live chats typically can be sent by any user and stay for as long as the livestream lasts (but can take up to 24 hours after the live video posting for all chats to come in). They can also be replayed.

Therefore, we had to set up a unique data scraper tailored for Live chats using the  [`pytchat`](https://github.com/taizan-hokuto/pytchat) library. This ran a scraper through a live video and dumped the scraped chats into JSON files.

Now, do Live chats always come up on live videos? [Unfortunately, no]( https://support.google.com/youtube/answer/9826490?hl=en#zippy=%2Caccess-channel-activity-from-live-chat-feed). YouTube, being the flexible platform it is, does allow channel owners to ban Live chats or restrict them to a small group of users. And to our surprise (and chagrin), we found most giant media networks to prefer these options. Despite these hurdles, we managed to survey and track down several networks that still supported them, albeit a few of them with restrictions, and adapted our scraping strategies accordingly.

An intriguing case involved NBC, which uniquely allowed only its channel to post live chats, primarily for fact-checking the candidates' statements during the debate. This posed both a challenge and an opportunity to further enhance the authenticity and depth of our analysis.

Through these meticulous efforts, we effectively mapped the evolving dialogues surrounding these high-stakes political events, providing a unique lens through which to view the public's political engagement and sentiment.

### YouTube's Election Policy

A small detour: the election content policies and moderation techniques [that YouTube follows](https://www.youtube.com/howyoutubeworks/our-commitments/supporting-political-integrity/) helped us understand the platform's policies and adapt our strategies.
















 

