How to do setup

Install requirements via requirements.txt
log in as postgres postgres
run setup.sql
log out
log in as postgres ssadmin
    password: ssadmin
run create_table.sql

open another command prompt for django
make migrations
migrate
create superuser
runserver
login to admin
    login: ssadmin
    pass: ssadmin
            *unrelated to ssadmin of postgres


in the previous command prompt, run \dt to display tables, it should display the updated tables

    it also generates the prefixed tables, but django still uses the original ones so its okay?

test it