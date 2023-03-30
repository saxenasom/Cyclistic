CREATE TABLE cyc(
	ride_id varchar(20),
	rideable varchar(15),
	time_start timestamp,
	time_end timestamp,
	start_station text,
	start_station_id text,
	end_station text,
	end_station_id text,
	start_lat real,
	start_lng real,	
	end_lat real,
	end_lng real,
	rental varchar(6)
);
COPY cyc
FROM 'D:\Cyclistic\out.csv'
WITH (FORMAT CSV, HEADER);