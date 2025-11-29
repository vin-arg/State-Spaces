CREATE TABLE building(
	building_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000', 
	building_name VARCHAR(255) NOT NULL,
	address VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL
);

CREATE TABLE agent(
	agent_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000',
	agent_name VARCHAR(255) NOT NULL,
	building_id VARCHAR(8),
	FOREIGN KEY (building_id) REFERENCES building(building_id) ON DELETE CASCADE
);

CREATE TABLE venue(
	venue_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000',
	venue_name VARCHAR(255) NOT NULL,
	capacity INT NOT NULL CHECK (capacity >= 0),
	type VARCHAR(100) NOT NULL,
	floor_area INT NOT NULL CHECK (floor_area >= 0),
	building_id VARCHAR(8),
	floor VARCHAR(20) NOT NULL,
	under_renovation BOOLEAN,
	agent_id VARCHAR(8),
	FOREIGN KEY (building_id) REFERENCES building(building_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES agent(agent_id) ON DELETE SET NULL
);

CREATE TABLE customer(
	customer_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000',
	customer_name VARCHAR(255) NOT NULL,
	birth_date DATE NOT NULL,
	location VARCHAR(255) NOT NULL
);

CREATE TABLE reservation(
	reservation_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000',
	venue_id VARCHAR(8),
	customer_id VARCHAR(8),
	participant_qty INT NOT NULL check (participant_qty > 0),
	start_date_time TIMESTAMP NOT NULL,
	end_date_time TIMESTAMP NOT NULL,
	FOREIGN KEY (venue_id) REFERENCES venue(venue_id) ON DELETE CASCADE,
	FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

CREATE TABLE amenity(
	amenity_id VARCHAR(8) NOT NULL UNIQUE PRIMARY KEY DEFAULT '0000',
	type VARCHAR(255) NOT NULL,
	description TEXT
);

CREATE TABLE venueamenity(
	venue_id VARCHAR(8),
	amenity_id VARCHAR(8),
	count INT NOT NULL DEFAULT 1 CHECK (count > 0),
	PRIMARY KEY(venue_id, amenity_id),
	FOREIGN KEY (venue_id) REFERENCES venue(venue_id) ON DELETE CASCADE,
	FOREIGN KEY (amenity_id) REFERENCES amenity(amenity_id) ON DELETE CASCADE
);

CREATE TABLE renovation(
	renovation_id VARCHAR(8) NOT NULL PRIMARY KEY DEFAULT '0000',
	start_date_time TIMESTAMP NOT NULL,
	end_date_time TIMESTAMP NOT NULL,
	venue_id VARCHAR(8),
	FOREIGN KEY (venue_id) REFERENCES venue(venue_id) ON DELETE CASCADE
);

CREATE TABLE team(
	agent_id VARCHAR(8),
	team_name VARCHAR(255) NOT NULL,
	job VARCHAR(255) NOT NULL,
	PRIMARY KEY(agent_id, team_name),
	FOREIGN KEY (agent_id) REFERENCES agent(agent_id) ON DELETE CASCADE
);
