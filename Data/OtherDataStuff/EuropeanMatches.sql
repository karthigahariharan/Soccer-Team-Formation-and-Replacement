-- League id : 1729

-- Arsenal

-- fifa api id : 1
-- team api id : 9825

-- matches for a team

select team_api_id from team where team_long_name like "arsenal";

-- input is teamname and season

select home_player_1, home_player_2, home_player_3, home_player_4, home_player_5, home_player_6, home_player_7, home_player_8, home_player_9, home_player_10, home_player_11 from match where home_team_api_id in (select team_api_id from team where team_long_name like "leicester city") and season = "2015/2016";

select away_player_1, away_player_2, away_player_3, away_player_4, away_player_5, away_player_6, away_player_7, away_player_8, away_player_9, away_player_10, away_player_11 from match where away_team_api_id in (select team_api_id from team where team_long_name like "leicester city") and season = "2015/2016";

select * from match where away_team_api_id in (select team_api_id from team where team_long_name like "leicester city") and season = "2015/2016";

-- given two players, number of matches that he played. input is two player ids

select player_api_id from player where player_name like "John terry"; --30627
select player_api_id from player where player_name like "Frank lampard"; --30631

-- home matches that player 1 and 2 played together. ip : player 1 and 2

select count(*) from match where (home_player_1 = 30627 or home_player_2 = 30627 or home_player_3 = 30627 or home_player_4 = 30627 or home_player_5 = 30627  or home_player_6 = 30627 or home_player_7 = 30627 or home_player_8 = 30627 or home_player_9 = 30627 or home_player_10 = 30627 or home_player_11 = 30627)
and (home_player_1 = 30631 or home_player_2 = 30631 or home_player_3 = 30631 or home_player_4 = 30631 or home_player_5 = 30631  or home_player_6 = 30631 or home_player_7 = 30631 or home_player_8 = 30631 or home_player_9 = 30631 or home_player_10 = 30631 or home_player_11 = 30631);

-- away matches only

select count(*) from match where (away_player_1 = 30627 or away_player_2 = 30627 or away_player_3 = 30627 or away_player_4 = 30627 or away_player_5 = 30627  or away_player_6 = 30627 or away_player_7 = 30627 or away_player_8 = 30627 or away_player_9 = 30627 or away_player_10 = 30627 or away_player_11 = 30627)
and (away_player_1 = 30631 or away_player_2 = 30631 or away_player_3 = 30631 or away_player_4 = 30631 or away_player_5 = 30631  or away_player_6 = 30631 or away_player_7 = 30631 or away_player_8 = 30631 or away_player_9 = 30631 or away_player_10 = 30631 or away_player_11 = 30631);

-- total no of matches

select count(*) from match where ((home_player_1 = 30627 or home_player_2 = 30627 or home_player_3 = 30627 or home_player_4 = 30627 or home_player_5 = 30627  or home_player_6 = 30627 or home_player_7 = 30627 or home_player_8 = 30627 or home_player_9 = 30627 or home_player_10 = 30627 or home_player_11 = 30627)
and (home_player_1 = 30631 or home_player_2 = 30631 or home_player_3 = 30631 or home_player_4 = 30631 or home_player_5 = 30631  or home_player_6 = 30631 or home_player_7 = 30631 or home_player_8 = 30631 or home_player_9 = 30631 or home_player_10 = 30631 or home_player_11 = 30631)) or ((away_player_1 = 30627 or away_player_2 = 30627 or away_player_3 = 30627 or away_player_4 = 30627 or away_player_5 = 30627  or away_player_6 = 30627 or away_player_7 = 30627 or away_player_8 = 30627 or away_player_9 = 30627 or away_player_10 = 30627 or away_player_11 = 30627)
and (away_player_1 = 30631 or away_player_2 = 30631 or away_player_3 = 30631 or away_player_4 = 30631 or away_player_5 = 30631  or away_player_6 = 30631 or away_player_7 = 30631 or away_player_8 = 30631 or away_player_9 = 30631 or away_player_10 = 30631 or away_player_11 = 30631));

-- win percentage
-- home

select count(*) from match where (home_player_1 = 30627 or home_player_2 = 30627 or home_player_3 = 30627 or home_player_4 = 30627 or home_player_5 = 30627  or home_player_6 = 30627 or home_player_7 = 30627 or home_player_8 = 30627 or home_player_9 = 30627 or home_player_10 = 30627 or home_player_11 = 30627)
and (home_player_1 = 30631 or home_player_2 = 30631 or home_player_3 = 30631 or home_player_4 = 30631 or home_player_5 = 30631  or home_player_6 = 30631 or home_player_7 = 30631 or home_player_8 = 30631 or home_player_9 = 30631 or home_player_10 = 30631 or home_player_11 = 30631) and home_team_goal > away_team_goal;

--away

select count(*) from match where (away_player_1 = 30627 or away_player_2 = 30627 or away_player_3 = 30627 or away_player_4 = 30627 or away_player_5 = 30627  or away_player_6 = 30627 or away_player_7 = 30627 or away_player_8 = 30627 or away_player_9 = 30627 or away_player_10 = 30627 or away_player_11 = 30627)
and (away_player_1 = 30631 or away_player_2 = 30631 or away_player_3 = 30631 or away_player_4 = 30631 or away_player_5 = 30631  or away_player_6 = 30631 or away_player_7 = 30631 or away_player_8 = 30631 or away_player_9 = 30631 or away_player_10 = 30631 or away_player_11 = 30631) and away_team_goal > home_team_goal;

-- all wins


select count(*) from match where ((home_player_1 = 30627 or home_player_2 = 30627 or home_player_3 = 30627 or home_player_4 = 30627 or home_player_5 = 30627  or home_player_6 = 30627 or home_player_7 = 30627 or home_player_8 = 30627 or home_player_9 = 30627 or home_player_10 = 30627 or home_player_11 = 30627)
and (home_player_1 = 30631 or home_player_2 = 30631 or home_player_3 = 30631 or home_player_4 = 30631 or home_player_5 = 30631  or home_player_6 = 30631 or home_player_7 = 30631 or home_player_8 = 30631 or home_player_9 = 30631 or home_player_10 = 30631 or home_player_11 = 30631) and home_team_goal > away_team_goal) or ((away_player_1 = 30627 or away_player_2 = 30627 or away_player_3 = 30627 or away_player_4 = 30627 or away_player_5 = 30627  or away_player_6 = 30627 or away_player_7 = 30627 or away_player_8 = 30627 or away_player_9 = 30627 or away_player_10 = 30627 or away_player_11 = 30627)
and (away_player_1 = 30631 or away_player_2 = 30631 or away_player_3 = 30631 or away_player_4 = 30631 or away_player_5 = 30631  or away_player_6 = 30631 or away_player_7 = 30631 or away_player_8 = 30631 or away_player_9 = 30631 or away_player_10 = 30631 or away_player_11 = 30631) and away_team_goal > home_team_goal);