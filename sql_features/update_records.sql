-- example of how to update a table to add a column
ALTER TABLE workout_names ADD COLUMN workout_description TEXT NULL;

-- adding to the workout_names table to utilize the column
UPDATE workout_names
SET workout_description = 'Breathing-focused yoga workout'
WHERE workout_name = 'Yoga Flow';

UPDATE workout_names
SET workout_description = 'Part of the PPL Split'
WHERE workout_name IN ('Push', 'Pull', 'Legs');

-- setting up some averages & sums later on
ALTER TABLE workout_events ADD COLUMN workout_duration_mins NUMBER DEFAULT 0;

UPDATE workout_events
SET workout_duration_mins = '40'
WHERE workout_name = 'Yoga Flow';

UPDATE workout_events
SET workout_duration_mins = '60'
WHERE workout_name = 'Full Body Strength Training';

UPDATE workout_events
SET workout_duration_mins = '25'
WHERE workout_name IN ('HIIT Circuit', 'Interval Running');

UPDATE workout_events
SET workout_duration_mins = '45'
WHERE workout_name LIKE '%Body%';

UPDATE workout_events
SET workout_duration_mins = '35'
WHERE workout_id = '9';

