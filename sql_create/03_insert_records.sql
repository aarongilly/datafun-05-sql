INSERT INTO workout_names (workout_name, workout_type) VALUES
        ('Full Body Strength Training', 'strength'),
        ('Yoga Flow', 'mobility'),
        ('Interval Running', 'cardio'),
        ('Mobility and Flexibility', 'mobility'),
        ('Upper Body Strength', 'strength'),
        ('Lower Body Strength', 'strength'),
        ('HIIT Circuit', 'cardio'),
        ('Pilates', 'mobility');


INSERT INTO workout_events (workout_name, workout_note) VALUES
        ('Full Body Strength Training', 'Focused on compound exercises.'),
        ('Yoga Flow', 'Beginner level class.'),
        ('Interval Running', '30 seconds sprint, 60 seconds rest, repeated 8 times.'),
        ('Mobility and Flexibility', 'Stretching and foam rolling.'),
        ('Upper Body Strength', 'Bench press, overhead press, rows.'),
        ('Lower Body Strength', 'Squats, deadlifts, lunges.'),
        ('HIIT Circuit', 'Burpees, mountain climbers, jump squats.'),
        ('Full Body Strength Training', 'Increased weight on deadlifts.'), -- Example of the same workout name used again
        ('Pilates', 'Core strengthening and stability work.'),
        ('Interval Running', 'Ran a new personal best time!'); -- Another example of the same workout name used again


-- example including a specified timestamp
INSERT INTO workout_events (timestamp, workout_name, workout_note) VALUES ('2025-02-03 13:40:42', 'Yoga Flow', 'FLOWED LIKE LAVA');
