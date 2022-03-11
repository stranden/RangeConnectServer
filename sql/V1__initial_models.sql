BEGIN

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE firing_type AS ENUM ('SIGHTERS', 'MATCH', 'SINGLE_SHOT', 'RAPID_FIRE', 'FINISHED')

CREATE TABLE country (
        sys_id SERIAL NOT NULL,
        name VARCHAR NOT NULL,
        shortname VARCHAR NOT NULL,
        PRIMARY KEY (sys_id)
)

CREATE TABLE shootingclub (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
        sys_id SERIAL NOT NULL,
        country_id INTEGER,
        club_id uuid DEFAULT uuid_generate_v4 (),
        name VARCHAR NOT NULL,
        shortname VARCHAR NOT NULL,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (country_id) REFERENCES country (sys_id)
)

CREATE TABLE shootingrange (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
        sys_id SERIAL NOT NULL,
        club_id INTEGER,
        range_id uuid DEFAULT uuid_generate_v4 (),
        name VARCHAR NOT NULL,
        lanes INTEGER NOT NULL,
        first_lane INTEGER NOT NULL,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (club_id) REFERENCES shootingclub (sys_id)
)

CREATE TABLE range_event_shooter (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER,
        shooter_id INTEGER NOT NULL,
        lane_id INTEGER NOT NULL,
        name VARCHAR,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id)
)

CREATE TABLE range_event_team (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER,
        shooter_id INTEGER,
        team VARCHAR,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id),
        FOREIGN KEY (shooter_id) REFERENCES range_event_shooter (sys_id)
)

CREATE TABLE range_event_class (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER,
        shooter_id INTEGER,
        class VARCHAR,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id),
        FOREIGN KEY (shooter_id) REFERENCES range_event_shooter (sys_id)
)

CREATE TABLE range_event_practice (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER NOT NULL,
        shooter_id INTEGER,
        sequence_number INTEGER NOT NULL,
        timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        event_type INTEGER NOT NULL,
        practice_sequence_number INTEGER NOT NULL,
        shoot_code INTEGER NOT NULL,
        practice_code INTEGER NOT NULL,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id),
        FOREIGN KEY (shooter_id) REFERENCES range_event_shooter (sys_id)
)

CREATE TABLE range_event_group (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER NOT NULL,
        shooter_id INTEGER,
        sequence_number INTEGER NOT NULL,
        timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        event_type INTEGER NOT NULL,
        group_ordinal INTEGER NOT NULL,
        state firing_type INTEGER NOT NULL,
        expected_number_of_shots INTEGER NOT NULL,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id),
        FOREIGN KEY (shooter_id) REFERENCES range_event_shooter (sys_id)
)

CREATE TABLE range_event_shot (
        created_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        modified_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(),
        sys_id SERIAL NOT NULL,
        shootingrange_id INTEGER NOT NULL,
        shooter_id INTEGER,
        sequence_number INTEGER NOT NULL,
        timestamp TIMESTAMP WITHOUT TIME ZONE NOT NULL,
        shot_id INTEGER NOT NULL,
        shot_value INTEGER NOT NULL,
        shot_value_decimal INTEGER NOT NULL,
        x_coord FLOAT NOT NULL,
        y_coord FLOAT NOT NULL,
        shot_timestamp INTEGER NOT NULL,
        caliber INTEGER NOT NULL,
        event_type INTEGER NOT NULL,
        shot_attr INTEGER NOT NULL,
        PRIMARY KEY (sys_id),
        FOREIGN KEY (shootingrange_id) REFERENCES shootingrange (sys_id),
        FOREIGN KEY (shooter_id) REFERENCES range_event_shooter (sys_id)
)