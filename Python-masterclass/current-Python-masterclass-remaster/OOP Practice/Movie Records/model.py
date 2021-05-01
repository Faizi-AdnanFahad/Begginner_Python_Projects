class Zone:
    """ Stores the a list of zones, where each zone have movieR"""
    id_num = 23

    def __init__(self, numZones):
        self.numZones = numZones
        self.list_of_movie_records = [None] * self.numZones
        self.noz = 0  # counts the number of different movies added to the self.list_of_movies_records list
        self.id = 'Zone-' + str(Zone.id_num)
        Zone.id_num += 11
        self.errorExist = False
        self.errorMsg = ''
        self.numMovieDVD = 0
        self.DvdDict = {}  # keys: movie name, values: number of dvds
        self.counter = 0  # used to index form left position

    def getID(self):
        """ Returns the ID of each zone"""
        return self.id

    def getNumberOfMovieRecords(self):
        """ Getter to get the number of different movies in the self.list_of_movies_records list"""
        return self.noz

    def getNumberOfMovieDVDs(self):
        """ Getter to get the total number of Dvds """
        return self.numMovieDVD

    def addMovieRecord(self, movieRecordObj=None):
        """
        Adds a MovieRecord object to the list of zones if there's space in the zones list.

        The items don't get added due to the following two reasons:
            1. If list was already full and a request to add a new movieRecord was invoked, get the specified error
                message below.
            2. If there's partial space to add some movieRecords but not all of them, the relevant error message appears
        """
        remaining_space_in_the_list = self.numZones - self.counter
        if remaining_space_in_the_list == 0:
            self.errorExist = True
            self.errorMsg = f"Error: maximum number of movie DVDs ({self.numZones}) reached"
        elif remaining_space_in_the_list >= movieRecordObj.getNumberOfDVDs():
            for i in range(0, movieRecordObj.getNumberOfDVDs()):
                self.list_of_movie_records[self.counter] = movieRecordObj
                self.counter += 1
            self.numMovieDVD += movieRecordObj.getNumberOfDVDs()
            if movieRecordObj.getName() not in self.DvdDict:
                self.DvdDict[movieRecordObj.getName()] = movieRecordObj.getNumberOfDVDs()
                self.noz += 1
            else:
                self.DvdDict[movieRecordObj.getName()] += movieRecordObj.getNumberOfDVDs()
        else:
            dvd_short = movieRecordObj.getNumberOfDVDs() - remaining_space_in_the_list
            self.errorMsg = f"Error: insufficient space left in the ({dvd_short} DVDs short)"
            self.errorExist = True

    def getStatus(self):
        """ Returns the relevant status change of error message."""
        seq = '{'
        if not self.errorExist:
            if self.noz == 0:
                result = "0 records and 0 DVDs: {}"
            else:
                total = 0
                for movies in self.DvdDict:
                    total += self.DvdDict[movies]
                    if total == self.numMovieDVD:
                        seq += f'{movies} ({self.DvdDict[movies]})'
                    elif total < self.numMovieDVD:
                        seq += f'{movies} ({self.DvdDict[movies]}), '
                seq += '}'
                result = f"{self.getNumberOfMovieRecords()} records and {self.getNumberOfMovieDVDs()} DVDs: {seq}"
        else:
            result = self.errorMsg

        return result


class MovieRecord:
    """ Creates a movie with a name and the number of DvDs into a particular zone. """
    id = 1

    def __init__(self, movieName, numDvd, zoneObj):
        self.movieName = movieName
        self.numDvd = numDvd
        self.zoneObj = zoneObj
        self.idd = ''
        self.id_num = MovieRecord.id
        MovieRecord.id += 1

    def getName(self):
        return self.movieName

    def getNumberOfDVDs(self):
        return self.numDvd

    def getZone(self):
        return self.zoneObj

    def getID(self):
        self.idd = f"{self.zoneObj.getID()}-{self.movieName}-{self.id_num}"

        return self.idd


class Store:
    """ Stores a list of zones"""
    # A store has up to 100 zones.
    def __init__(self):
        self.list_of_zones = []
        self.info = [0, 0]

    def addZones(self, listOfZoneObj):
        """ Adds zones to the store form the list of zones. """
        if len(listOfZoneObj) <= 100:
            for zone in listOfZoneObj:
                self.list_of_zones.append(zone)

    def getZones(self, zoneRange=None):
        """ Returns the list of zones in the store which includes all zones if no range is specified.
        Otherwise, returns the list of zones which has less number of zones than the given rangeZone argument.
        """
        temp = []
        if zoneRange is None:
            return self.list_of_zones
        else:
            for zone in self.list_of_zones:
                if (zone.numZones - zone.getNumberOfMovieDVDs()) <= zoneRange:
                    temp.append(zone)
            return temp

    def getStats(self, movieName):
        """ returns a list size 2 for each zone.
        The first index includes the number of different movies in the zone matching the name of the argument.
        The second index includes the number dvds in the zone matching the name of the argument.
        """
        index0 = 0
        index1 = 0
        for zone in self.list_of_zones:
            for movies in zone.DvdDict:
                if movieName == movies:
                    index0 = len(zone.DvdDict.keys())
                    index1 += zone.DvdDict[movies]
                    break
        self.info[0] = index0
        self.info[1] = index1

        return self.info
