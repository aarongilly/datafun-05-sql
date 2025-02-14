
-- Create the workout_names table 
-- Note that the workout_names table has no foreign keys, so it is a standalone table

CREATE TABLE workout_names (
    workout_name TEXT PRIMARY KEY,
    workout_type TEXT CHECK (workout_type IN ('strength', 'mobility', 'cardio'))
);

-- Create the workout_events table
-- Note that the workout_events table has a foreign key to the workout_names table
-- This means that the workout_events table is dependent on the workout_names table
-- Be sure to create the standalone authors table BEFORE creating the books table.

CREATE TABLE workout_events (
    workout_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    workout_name TEXT NOT NULL REFERENCES workout_names(workout_name) ON DELETE CASCADE,
    workout_note TEXT NULL
);