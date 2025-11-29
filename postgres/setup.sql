DROP DATABASE IF EXISTS ssdatabase;
DROP USER IF EXISTS ssadmin;
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
CREATE DATABASE ssdatabase;
CREATE USER ssadmin WITH PASSWORD 'ssadmin';
ALTER ROLE ssadmin SET client_encoding TO 'utf8';
ALTER ROLE ssadmin SET default_transaction_isolation TO 'read committed';
ALTER ROLE ssadmin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE ssdatabase TO ssadmin;

-- Switch to the database
\c ssdatabase;

-- Give schema permissions
GRANT ALL ON SCHEMA public TO ssadmin;
ALTER SCHEMA public OWNER TO ssadmin;

-- Allow the user to create tables/functions/etc.
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ssadmin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ssadmin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO ssadmin;