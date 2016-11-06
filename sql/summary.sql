INSERT INTO summary
  SELECT DISTINCT
    COALESCE(c.player_name, '路人')            AS 'player_name',
    COALESCE(c.player_country, 'unknown')    AS 'player_country',
    COALESCE(c.player_team_short_name, '路人') AS 'player_team_short_name',
    COALESCE(c.player_team_league, '路人')     AS 'player_team_league',
    COALESCE(c.player_place, '路人')           AS 'player_place',
    a.*
  FROM gameidinfo a
    LEFT JOIN idmapping b
      ON a.game_id = b.game_id
    LEFT JOIN
    (
      SELECT *
      FROM player
      WHERE player_name IN
            (
              SELECT player_name
              FROM player
              GROUP BY player_name
              HAVING count(*) = 1
            )
    ) c
      ON b.player_name = c.player_name;

update summary set player_team_short_name='' WHERE player_team_short_name='路人';
update summary set player_country='' where player_country='unknown';
