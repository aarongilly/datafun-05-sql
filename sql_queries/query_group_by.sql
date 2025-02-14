-- Grouping
SELECT
    workout_name,
    count(workout_name)
FROM
    workout_events
GROUP BY
    workout_name