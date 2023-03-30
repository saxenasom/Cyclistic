SELECT trip_date,rental,rideable,COUNT(*),SUM(duration)
FROM
(
	SELECT rental,rideable,date_part('epoch',time_end)-date_part('epoch',time_start) AS duration, CAST(time_start AS date) AS trip_date
	FROM cyc
)t1
WHERE duration>0 AND duration<=86400
GROUP BY trip_date,rental,rideable