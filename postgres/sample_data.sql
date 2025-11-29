-- ----------------------------
-- Buildings
-- ----------------------------
INSERT INTO building (building_id, building_name, address, city) VALUES
('BLDG001','Sunrise Plaza','123 Main St','Metro City'),
('BLDG002','Oceanview Tower','456 Ocean Ave','Coastal City'),
('BLDG003','Greenwood Center','789 Green Rd','Metro City');

-- ----------------------------
-- Agents
-- ----------------------------
INSERT INTO agent (agent_id, agent_name, building_id) VALUES
('AGNT001','Alice Smith','BLDG001'),
('AGNT002','Bob Johnson','BLDG002'),
('AGNT003','Carol White','BLDG003');

-- ----------------------------
-- Venues
-- ----------------------------
INSERT INTO venue (venue_id, venue_name, capacity, type, floor_area, building_id, floor, under_renovation, agent_id) VALUES
('V001','Grand Hall',200,'Conference',500,'BLDG001','1',FALSE,'AGNT001'),
('V002','Sky Lounge',100,'Banquet',300,'BLDG002','10',TRUE,'AGNT002'),
('V003','Maple Room',150,'Conference',400,'BLDG003','2',FALSE,'AGNT003');

-- ----------------------------
-- Customers
-- ----------------------------
INSERT INTO customer (customer_id, customer_name, birth_date, location) VALUES
('CSTM001','John Doe','1985-06-15','Metro City'),
('CSTM002','Jane Roe','1990-11-20','Coastal City'),
('CSTM003','Michael Scott','1975-03-12','Hilltown');

-- ----------------------------
-- Reservations
-- ----------------------------
INSERT INTO reservation (reservation_id, venue_id, customer_id, participant_qty, start_date_time, end_date_time) VALUES
('RSVT001','V001','CSTM001',50,'2025-12-10 10:00','2025-12-10 14:00'),
('RSVT002','V002','CSTM002',80,'2025-12-12 18:00','2025-12-12 22:00'),
('RSVT003','V003','CSTM003',30,'2025-12-15 09:00','2025-12-15 12:00');

-- ----------------------------
-- Amenities
-- ----------------------------
INSERT INTO amenity (amenity_id, type, description) VALUES
('AMNT001','Projector','High-definition projector'),
('AMNT002','Sound System','Professional sound system for events'),
('AMNT003','Wi-Fi','High-speed wireless internet');

-- ----------------------------
-- Venue Amenities
-- ----------------------------
INSERT INTO venueamenity (venue_id, amenity_id, count) VALUES
('V001','AMNT001',2),
('V001','AMNT002',1),
('V002','AMNT002',1),
('V002','AMNT003',1);

-- ----------------------------
-- Renovations
-- ----------------------------
INSERT INTO renovation (renovation_id, start_date_time, end_date_time, venue_id) VALUES
('RNVT001','2025-11-01 08:00','2025-11-15 18:00','V002'),
('RNVT002','2025-11-10 09:00','2025-11-25 17:00','V003');

-- ----------------------------
-- Teams
-- ----------------------------
INSERT INTO team (agent_id, team_name, job) VALUES
('AGNT001','Maintenance Crew','Facility Maintenance'),
('AGNT002','Event Staff','Event Coordination'),
('AGNT003','Cleaning Team','Housekeeping');
