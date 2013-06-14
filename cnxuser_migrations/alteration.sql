-- # ###
-- # Copyright (c) 2013, Rice University
-- # This software is subject to the provisions of the GNU Affero General
-- # Public License version 3 (AGPLv3).
-- # See LICENCE.txt for details.
-- # ###
BEGIN;
CREATE EXTENSION "uuid-ossp";
ALTER TABLE users
ALTER COLUMN id SET DEFAULT uuid_generate_v4();
COMMIT;
