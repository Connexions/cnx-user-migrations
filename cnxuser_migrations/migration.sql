-- # ###
-- # Copyright (c) 2013, Rice University
-- # This software is subject to the provisions of the GNU Affero General
-- # Public License version 3 (AGPLv3).
-- # See LICENCE.txt for details.
-- # ###
BEGIN;
INSERT INTO users (email, firstname, othername, surname, _legacy_id)
	SELECT email, firstname, othername, surname, personid FROM persons
		WHERE NOT EXISTS (SELECT 1 FROM users WHERE users._legacy_id = persons.personid);
COMMIT;
