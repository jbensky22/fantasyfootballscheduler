# fantasyfootballscheduler

My friends and I take part in a dynsatsy fantasy football league. The league uses the ESPN fantasy football API. ESPN provides a schedule each year, where each team plays every other team at least once, and possibly twice. For this year, however, we implmented two rivalry weeks into the schedule. So in week 7 and 14, every matchup should be the same. ESPN's scheduling proved to be diffcult to customize, so I took it upon myself to write a quick script that ensures a couple of important criteria
1) Every team plays every week
2) Every team plays every other team at least once and no more than twice
3) No two matchups are the same two weeks in a row
4) Every team play's there rival in weeks 7 and 14
