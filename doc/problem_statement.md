Overview and Motivation
******************

While soccer is one of the most popular sports in the world, its analytics is lackluster in comparison to other popular sports such as baseball, American football, hockey, and basketball. This is particularly evident for the FIFA World Cup. The amount of analytics done on the FIFA World Cup is just miniscule in comparison to its scale, given that it is one of the most popular and highly televised sporting events in the world! This can be attributed to the general resistance of the sport (or FIFA) towards technology. Even though numerous other sports already use video technology to review plays while on the pitch, FIFA World Cup 2018 was the first time Video Assistant Referee (VAR) was used in a major soccer tournament. 

<div class="center">

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Putin right now! 😅 <a href="https://twitter.com/hashtag/WorldCup?src=hash&amp;ref_src=twsrc%5Etfw">#WorldCup</a> <a href="https://t.co/7r67cWsuNm">pic.twitter.com/7r67cWsuNm</a></p>&mdash; Football Memes (@FootballMemesCo) <a href="https://twitter.com/FootballMemesCo/status/1015695929222090752?ref_src=twsrc%5Etfw">July 7, 2018</a></blockquote> 
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

</div>

Another possible explanation is it's uniqueness as a sporting event of a global scale. The only other comparison is the Olympics. As a result, it is just logistically difficult for international teams to play each other very frequently! In fact, soccer clubs are often very resistant to allowing their players leave for international friendlies, especially if it is in the middle of their sporting season. 

<div class="center">

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">The international break summed up. <a href="http://t.co/slY4KLGqtz">pic.twitter.com/slY4KLGqtz</a></p>&mdash; Soccer Memes (@SoccerMemes) <a href="https://twitter.com/SoccerMemes/status/653329315283795968?ref_src=twsrc%5Etfw">October 11, 2015</a></blockquote> 

<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

</div>

As countries just do not compete against each other at the highest level frequently, there is a lack of high quality data that can be immediately fed into models to perform predictions. This is one of the biggest limitations on our project. While we would have liked to construct a model based on historical match based statistics, such as the possesion rate, the number of shots on target, etc., these data are just not readily available (free). Most of these statistics for international matches seem to have been calculated only since the start of the 2010s. Even then, only matches at the highest level, during tournaments or featuring top teams, have these statistics available. As such, we rely on a mix of simple match based statistics, and team and individual data from the popular FIFA games for our World Cup predictions.

The World Cup is composed of 64 matches in total - 48 matches in group stages and 16 matches in knockout (15 + 1 for third place). We plan to predict the outcome of each of the 64 matches independently instead of predicting which teams proceed in each round. This strategy allows our results to be comparable across models. By framing the problem in this way, we plan to approach this problem as a classification problem. Each game can be treated as a multi-class classification problem, where there are three outcomes: win for the home team (or team 1, indicated with 1), win for the away team (or team 2, indicated with -1), or a draw (indicated with 0). In the knockout rounds, we limit the outcome to: win for the home team (or team 1), win for the away team (or team 2), as draws are not allowed. Note that while we refer to teams as 'home' or 'away', we are merely abusing the terminology to distinguish between teams. There is only one true 'home' team for World Cups. 

To validate how accurate FIFA rankings are, we aim to use a baseline model that leverages FIFA rankings and some other simple team predictors to predict the World Cup results. We plan to create a more advanced model without relying on FIFA rankings. Instead, our advanced model is based on features that we self collected and engineered. The feature engineering process is a follow up to our initial EDA, where we identified features that could possibly impact match results. Ultimately, our analysis attempts to create a model that can predict the World Cup results as accurately as possible, while offering an insight into the features helpful in soccer analytics.