SELECT
    we.workout_id,
    we.timestamp,
    wn.workout_name,
    wn.workout_type,
    we.workout_note,
    we.workout_duration_mins  -- Include this if you've added the column
FROM
    workout_events AS we
INNER JOIN
    workout_names AS wn
ON
    we.workout_name = wn.workout_name;

-- Alternative using a LEFT JOIN (includes all workout_events, even if they don't have a match in workout_names):
SELECT
    we.workout_id,
    we.timestamp,
    wn.workout_name,
    wn.workout_type,
    we.workout_note,
    we.workout_duration_mins
FROM
    workout_events AS we
LEFT JOIN
    workout_names AS wn
ON
    we.workout_name = wn.workout_name;

-- Another alternative using a RIGHT JOIN (includes all workout_names, even if they don't have a match in workout_events):
SELECT
    we.workout_id,
    we.timestamp,
    wn.workout_name,
    wn.workout_type,
    we.workout_note,
    we.workout_duration_mins
FROM
    workout_events AS we
RIGHT JOIN
    workout_names AS wn
ON
    we.workout_name = wn.workout_name;

-- You can also add a WHERE clause to filter the results:
SELECT
    we.workout_id,
    we.timestamp,
    wn.workout_name,
    we.workout_duration_mins
FROM
    workout_events AS we
INNER JOIN
    workout_names AS wn
ON
    we.workout_name = wn.workout_name
WHERE
    wn.workout_type = 'strength';  -- Example: show only strength workouts