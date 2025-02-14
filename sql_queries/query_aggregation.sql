
-- Averaging
SELECT
	avg(workout_duration_mins)
FROM
	workout_events;

-- Summing
SELECT
    sum(workout_duration_mins)
FROM
    workout_events;

-- Counting
SELECT
    count(workout_name)
FROM    
    workout_events;
