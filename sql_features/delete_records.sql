-- basic deletion code, picking workout 4 arbitrarily
DELETE FROM workout_events
WHERE workout_id = 4;

DELETE FROM workout_names
WHERE workout_name = "HIIT Circuit"