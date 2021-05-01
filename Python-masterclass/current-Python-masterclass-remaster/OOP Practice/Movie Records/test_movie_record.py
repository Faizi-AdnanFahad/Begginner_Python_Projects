import unittest
from model import Zone, Store, MovieRecord

# Problem:
#
# You are required to build classes for managing a store,
# 	 where records of available movies are stored in different zones.
#
# A store has up to 100 zones.
#
# Each zone stores a collection of movie records.
# When first created, a zone is set with a capacity
# (i.e., maximum total number of movie DVDs).
#
# Each movie record is characterized by its name, number of available DVDs, and located zone.
# You can assume that within a zone, there are no two movie records with the same name.
#
# A zone's status is a summary of its stored movie records.
# 	However, if the last invoked mutator resulted in an error (e.g., due to insufficient space in the zone),
# 	then the zone's status should be updated to the corresponding error message.
#
# For other functionalities, details, and examples, see below for the test methods and in-line comments.
#


class MyTestCase(unittest.TestCase):
    
    def test_case_1(self):
        # Create empty zones which can store
        # up to the specified maximum numbers of movie DVDs.
        #
        z1 = Zone(10)
        z2 = Zone(9)
        z3 = Zone(7)
        z4 = Zone(11)

        # The id of each has the form "Zone-?",
        # where ? is an integer. The integer part of all id's should form
        # the following arithmetic sequence (with a common difference): 23, 34, 45, 56, 67, ...
        #
        self.assertEqual("Zone-23", z1.getID())
        self.assertEqual("Zone-34", z2.getID())
        self.assertEqual("Zone-45", z3.getID())
        self.assertEqual("Zone-56", z4.getID())

        # The id of a zone, once assigned, never changes. #
        self.assertEqual("Zone-23", z1.getID())
        self.assertEqual("Zone-34", z2.getID())
        self.assertEqual("Zone-45", z3.getID())
        self.assertEqual("Zone-56", z4.getID())

        # Create a movie record with the specified name, number of DVDs, and located zone.
        #
        # Assumption: The passed argument values for name, number of DVDs, and object
        # are always valid (i.e., no error checking is needed).
        #
        r1 = MovieRecord("La La Land", 4, z1)
        r2 = MovieRecord("Mission Impossible", 3, z2)
        r3 = MovieRecord("Groundhog Day", 2, z3)
        r4 = MovieRecord("Toy Story", 1, z4)

        # Get the name of each movie. #
        self.assertEqual("La La Land", r1.getName())
        self.assertEqual("Mission Impossible", r2.getName())
        self.assertEqual("Groundhog Day", r3.getName())
        self.assertEqual("Toy Story", r4.getName())

        # Get the number of available DVDs of each movie. #
        self.assertEqual(4, r1.getNumberOfDVDs())
        self.assertEqual(3, r2.getNumberOfDVDs())
        self.assertEqual(2, r3.getNumberOfDVDs())
        self.assertEqual(1, r4.getNumberOfDVDs())

        # Get the located of each movie. #
        r1_zone = r1.getZone()
        self.assertTrue(r1_zone == z1)
        self.assertTrue(r2.getZone() == z2)
        self.assertTrue(r3.getZone() == z3)
        self.assertTrue(r4.getZone() == z4)

        # The id of each movie record consists of three parts (separated by dashes):
        # 1. The id of its located (assumed to be non-null)
        # 2. The name of the movie
        # 3. An integer indicating the chronological order in which the movie record was created.
        # 	  e.g., 1 for the first created movie record, 2 for the second created movie record, etc.
        #
        self.assertEqual("Zone-23-La La Land-1", r1.getID())
        self.assertEqual("Zone-34-Mission Impossible-2", r2.getID())
        self.assertEqual("Zone-45-Groundhog Day-3", r3.getID())
        self.assertEqual("Zone-56-Toy Story-4", r4.getID())

        # The id of a movie record, once assigned, never changes. #
        self.assertEqual("Zone-23-La La Land-1", r1.getID())
        self.assertEqual("Zone-34-Mission Impossible-2", r2.getID())
        self.assertEqual("Zone-45-Groundhog Day-3", r3.getID())
        self.assertEqual("Zone-56-Toy Story-4", r4.getID())

    def test_case_2(self):
        # Create an an empty zone that can store up to
        # the specified number of movie DVDs.
        #
        z1 = Zone(10)

        # Note the distinction between movie records and movie DVDs:
        # 	- A zone stores a collection of movie ###records###.
        # 	- Each movie record indicates the number of ###DVDs### available for that movie.
        #
        self.assertEqual(0, z1.getNumberOfMovieRecords())
        self.assertEqual(0, z1.getNumberOfMovieDVDs())

        # When there was no error resulted from the last mutator call,
        # 	a zone's status is a summary of its stored
        # 		- number of movie records
        # 		- number of available movie DVDs
        # 		- a list (surrounded by curly braces) of movie names (indicated with their numbers of available DVDs).
        #
        # Note. Always spell `records` and `DVDs` in the plural form.
        # There is no need to say, e.g., 0 record, 1 record, 0 DVD, 1 DVD.
        #
        self.assertEqual("0 records and 0 DVDs: {}", z1.getStatus())

        r1 = MovieRecord("Toy Story", 1, z1)

        # Case 1 of adding a movie record:
        # 	Add a movie record (with a non-existing name) to its located zone.
        #
        # Again: A zone stores a collection of movie records.
        # 		  Each movie record indicates the number of DVDs available for that movie.
        #
        # In the previous line, r1 was created with its located being set to z1.
        # In the next line, add r1 to z1's collection of movie records.
        #
        # Assume: a movie record is always added to its located zone.
        # e.g., r1's located was already set to z1 when it was created,
        # 			and the following line adds r1 to z1.
        #
        z1.addMovieRecord(r1)

        # Note again the distinction between movie records and movie DVDs:
        # 	- A stores a collection of movie ###records###.
        # 	- Each movie record indicates the number of ###DVDs### available for that movie.
        #
        self.assertEqual(1, z1.getNumberOfMovieRecords())  # 1 movie record: r1 #
        self.assertEqual(1, z1.getNumberOfMovieDVDs())  # 1 movie DVD, calculated from what r1 indicates #

        # In the list {...}, each movie name is indicated with its number of available DVDs. #
        self.assertEqual("1 records and 1 DVDs: {Toy Story (1)}", z1.getStatus())

        # Note: r2 is 1 movie record indicating 4 DVDs available for that movie. #
        r2 = MovieRecord("La La Land", 4, z1)
        z1.addMovieRecord(r2)
        self.assertEqual(2, z1.getNumberOfMovieRecords())  # 2 movie records: r1 and r2 #
        self.assertEqual(5, z1.getNumberOfMovieDVDs())  # 5 movie DVDs, calculated from what r1 and r2 indicate #

        # Note the spaces after the colon and comma, and the spaces before the opening parentheses. #
        self.assertEqual("2 records and 5 DVDs: {Toy Story (1), La La Land (4)}", z1.getStatus())

    def test_Case_3(self):
        # Create an empty which can store
        # up to the specified maximum number of movie DVDs.
        #
        z1 = Zone(10)

        r1 = MovieRecord("Mission Impossible", 7, z1)
        r2 = MovieRecord("Toy Story", 3, z1)
        z1.addMovieRecord(r1)
        z1.addMovieRecord(r2)
        self.assertEqual(2, z1.getNumberOfMovieRecords())
        self.assertEqual(10, z1.getNumberOfMovieDVDs())
        self.assertEqual("2 records and 10 DVDs: {Mission Impossible (7), Toy Story (3)}", z1.getStatus())

        # The movie is full (i.e., the maximum 10 movie DVDs reached). #

        r3 = MovieRecord("La La Land", 1, z1)

        # Case 2 of adding a movie record:
        # 	An error will be resulted from the following mutator call
        # 	(due to the being already full).
        # The corresponding error message should then be set to the zone's status.
        #
        z1.addMovieRecord(r3)
        # Note: `10` in the error message corresponds to the specified maximum number when z1 was created. #
        self.assertEqual("Error: maximum number of movie DVDs (10) reached", z1.getStatus())

        # An error occurring does not modify the existing records and DVDs in zone. #
        self.assertEqual(2, z1.getNumberOfMovieRecords())
        self.assertEqual(10, z1.getNumberOfMovieDVDs())
        # Note. You need not worry if in your implementation,
        # 	after the last mutator call where r3 could not be added to the full z1,
        # 	the located of r3 is still linked to z1.
        #
        # That is, there is no need to assign the located of r3 to null upon an error like above.
        #

    def test_case_4(self):
        # Create an empty which can store
        # up to the specified maximum number of movie DVDs.
        #
        z1 = Zone(10)

        r1 = MovieRecord("Mission Impossible", 5, z1)
        r2 = MovieRecord("Toy Story", 2, z1)
        z1.addMovieRecord(r1)
        z1.addMovieRecord(r2)
        self.assertEqual(2, z1.getNumberOfMovieRecords())
        self.assertEqual(7, z1.getNumberOfMovieDVDs())
        self.assertEqual("2 records and 7 DVDs: {Mission Impossible (5), Toy Story (2)}", z1.getStatus())

        # The movie is now 3 DVDs away from being full. #

        r3 = MovieRecord("La La Land", 4, z1)

        # Case 3 of adding a movie record:
        # 	An error will be resulted from the following mutator call
        # 	(due to the zone's remaining space cannot accommodate r3's movie DVDs).
        #
        # The corresponding error message should then be set to the zone's status.
        # The error message should also display how much space (in terms of movie DVDs)
        # the is short of.
        # e.g., current has space for 3 DVDs, which is 1 DVD short of the intended 4 DVDs of r3.
        #
        # Of course, "short of 0" is not an error, as it means the would just become full.
        #
        # Note. Always spell `DVDs` in the plural form.
        # There is no need to say, e.g., 1 DVD.
        #
        z1.addMovieRecord(r3)
        self.assertEqual("Error: insufficient space left in the (1 DVDs short)", z1.getStatus())

        # An error occurring does not modify the existing records and DVDs in zone. #
        self.assertEqual(2, z1.getNumberOfMovieRecords())
        self.assertEqual(7, z1.getNumberOfMovieDVDs())

        # Note. When the is already full, an attempt to add more movie DVDs always results in
        # the error message as shown in test_03, not an error message showing insufficient space.
        #

    def test_case_5(self):
        z1 = Zone(10)

        r1 = MovieRecord("Mission Impossible", 5, z1)
        r2 = MovieRecord("Toy Story", 2, z1)
        z1.addMovieRecord(r1)
        z1.addMovieRecord(r2)
        self.assertEqual("2 records and 7 DVDs: {Mission Impossible (5), Toy Story (2)}", z1.getStatus())

        # The movie is now 3 DVDs away from being full. #

        r3 = MovieRecord("Toy Story", 2, z1)

        # Case 4 of adding a movie record:
        # 	When adding a movie record with some existing name,
        # 	update the movie DVDs of the existing stored movie record only.
        # e.g., The following mutator call will increase the number of movie DVDs for "Toy Story" by 2.
        #
        z1.addMovieRecord(r3)

        self.assertEqual(2, z1.getNumberOfMovieRecords())
        self.assertEqual(9, z1.getNumberOfMovieDVDs())
        self.assertEqual("2 records and 9 DVDs: {Mission Impossible (5), Toy Story (4)}", z1.getStatus())

    def test_Case_06(self):
        z1 = Zone(10)
        z2 = Zone(10)
        z3 = Zone(10)

        # Recall the assumption from test_02: a movie record is always added to its located zone.
        # e.g., in the line below, the anonymous movie record object's located is set to z1,
        # 			and that anonymous object is added to z1's collection.
        #
        z1.addMovieRecord(MovieRecord("La La Land", 4, z1))

        # DVDs of a movie may be distributed over multiple zones. #
        z1.addMovieRecord(MovieRecord("Mission Impossible", 3, z1))
        z2.addMovieRecord(MovieRecord("Mission Impossible", 6, z2))

        z2.addMovieRecord(MovieRecord("Groundhog Day", 2, z2))
        z3.addMovieRecord(MovieRecord("Toy Story", 5, z3))

        # Create an empty Store which can up to 100 zones. #
        lib = Store()

        # Add an array of zones to a store.
        #
        # Assume:
        # 	- Each element of the input array is a valid object.
        # 	- Length of the input array will not result in the store's capacity (100) being exceeded.
        # 	- IDs in the input array do not clash with each other,
        # 		and neither do they clash with IDs of zones already stored in the store.
        #
        input1 = {z1, z2}
        lib.addZones(input1)
        zones1 = lib.getZones()
        self.assertTrue(
            zones1.length == 2
            and zones1[0] == z1
            and zones1[1] == z2
        )

        input2 = {z3}
        lib.addZones(input2)
        zones2 = lib.getZones()
        self.assertTrue(
            zones2.length == 3
            and zones2[0] == z1
            and zones2[1] == z2
            and zones2[2] == z3
        )

        input3 = {}
        lib.addZones(input3)  # Adding an empty array of zones should cause no change. #
        zones3 = lib.getZones()
        self.assertTrue(
            zones3.length == 3
            and zones3[0] == z1
            and zones3[1] == z2
            and zones3[2] == z3)

    def test_case_07(self):
        z1 = Zone(10)
        z2 = Zone(10)
        z3 = Zone(10)

        z1.addMovieRecord(MovieRecord("La La Land", 4, z1))

        # DVDs of a movie may be distributed over multiple zones. #
        z1.addMovieRecord(MovieRecord("Mission Impossible", 3, z1))
        z2.addMovieRecord(MovieRecord("Mission Impossible", 6, z2))

        z2.addMovieRecord(MovieRecord("Groundhog Day", 2, z2))
        z3.addMovieRecord(MovieRecord("Toy Story", 5, z3))

        # Create an empty which can hold up to 100 zones. #
        lib = Store()

        input_list = {z1, z2, z3}
        lib.addZones(input_list)
        zones = lib.getZones()
        self.assertEqual(3, zones.length)
        self.assertEqual("2 records and 7 DVDs: {La La Land (4), Mission Impossible (3)}", zones[0].getStatus())
        self.assertEqual("2 records and 8 DVDs: {Mission Impossible (6), Groundhog Day (2)}", zones[1].getStatus())
        self.assertEqual("1 records and 5 DVDs: {Toy Story (5)}", zones[2].getStatus())

        # Return the stats information of the as an array of length 2:
        # 	- Index 0 stores the total number of movie records, across all zones, with the input movie name.
        # 		e.g., two movie records with name "Mission Impossible" can be located: from z1 and z2.
        # 	- Index 1 stores the total number of available movie DVDs, across all zones, with the input movie name.
        # 		e.g., movie records with name "Mission Impossible" can be located in z1 (3 DVDs) and z2 (6 DVDs).
        #
        stats = lib.getStats("Mission Impossible")  # list of integers
        self.assertEqual(2, stats.length)
        self.assertEqual(2, stats[0])
        self.assertEqual(3 + 6, stats[1])

        # If none of the zones stores a movie record with the specified name,
        # then both stats information should be 0.
        #
        stats = lib.getStats("Life of Pi")
        self.assertEqual(2, stats.length)
        self.assertEqual(0, stats[0])
        self.assertEqual(0, stats[1])

    def test_case_8(self):
        z1 = Zone(10)
        z2 = Zone(10)
        z3 = Zone(10)

        z1.addMovieRecord(MovieRecord("La La Land", 4, z1))

        # DVDs of a movie may be distributed over multiple zones. #
        z1.addMovieRecord(MovieRecord("Mission Impossible", 3, z1))
        z2.addMovieRecord(MovieRecord("Mission Impossible", 6, z2))

        z2.addMovieRecord(MovieRecord("Groundhog Day", 2, z2))
        z3.addMovieRecord(MovieRecord("Toy Story", 5, z3))

        # Create an empty which can up to 100 zones. #
        lib = Store()

        input_list = {z1, z2, z3}
        lib.addZones(input_list)
        zonez1 = lib.getZones()
        self.assertEqual(3, zonez1.length)
        self.assertEqual("2 records and 7 DVDs: {La La Land (4), Mission Impossible (3)}", zonez1[0].getStatus())
        self.assertEqual("2 records and 8 DVDs: {Mission Impossible (6), Groundhog Day (2)}", zonez1[1].getStatus())
        self.assertEqual("1 records and 5 DVDs: {Toy Story (5)}", zonez1[2].getStatus())

        # z1 is now 3 DVDs away from being full.
        # z2 is now 2 DVDs away from being full.
        # z3 is now 5 DVDs away from being full.
        #

        # Across all zones, return those zones whose remaining space is within the specified number of available
        # movie DVDs. e.g., the remaining space of zones z1 (3 DVDs remaining) and z2 (2 DVDs remaining) is less than
        # or equal to 3 movie DVDs.
        #
        # objects in the returned array should be arranged according to
        # the order in which they were added to the store.
        #
        zonez2 = lib.getZones(3)
        self.assertEqual(2, zonez2.length)
        self.assertTrue(z1 == zonez2[0])
        self.assertTrue(z2 == zonez2[1])


if __name__ == '__main__':
    unittest.main()
