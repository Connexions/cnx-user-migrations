cnx-user migrations
===================

A set of logic used to migrate the legacy user database to ``cnx-user``.

Getting started
---------------

To install the package, run the typical python installation procedure::

    $ python setup.py install

This will have installed the script(s) to do the migration. The scripts
are prefixed with ``cnx-user-`` so that they don't pollute you scripts
namespace.

Migration
---------

The migration script is used to migrate the legacy ``persons`` table to
the cnx-user ``users`` table. The script needs to be supplied with a few
pieces of information, but the gist of it's usage is this::

    $ cnx-user-migrate --username cnxuser --password cnxuser \
      --database cnxuser

Note, the above a defaults, which closely match with the defaults in
the ``cnx-user`` package itself. Also, this depends on Postgres and
the user should have abilities to alter tables.

Also note, the above example assumes you have setup the ``cnx-user``
database and a copy of the legacy ``persons`` table in the same database.
Information about initializing the ``cnx-user`` database can be found
in that packages documentation. See Ross Reedstrom for access to the
``persons`` table data.

Tests
-----

There aren't any... But if you would like to verify the scripts ability to
be run more than once. Run the following statements and compare the
row count after each.
::

    $ psql -c "SELECT count(*) FROM users;" cnxuser cnxuser
    $ psql -c "DELETE FROM users WHERE surname LIKE '%iller%';" cnxuser cnxuser
    $ psql -c "SELECT count(*) FROM users;" cnxuser cnxuser
    $ cnx-user-migrate
    $ psql -c "SELECT count(*) FROM users;" cnxuser cnxuser
