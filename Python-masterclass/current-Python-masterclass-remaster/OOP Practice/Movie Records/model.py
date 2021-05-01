class Zone:
    id_num = 23

    def __init__(self, numZones):
        self.numZones = numZones
        self.list_of_movie_records = [None] * self.numZones
        self.noz = 0
        self.id = 'Zone-' + str(Zone.id_num)
        Zone.id_num += 11
        self.errorExist = False

    def getID(self):
        return self.id

    def getNumberOfMovieRecords(self):
        return self.noz

    def getNumberOfMovieDVDs(self):
        total = 0
        for i in range(self.noz):
            total += self.list_of_movie_records[i].getNumberOfDVDs()
        return total

    def addMovieRecord(self, movieRecordObj=None):
        if self.getNumberOfMovieDVDs() < self.numZones:
            self.list_of_movie_records[self.noz] = movieRecordObj
            self.noz += 1
        else:
            self.errorExist = True

    def getStatus(self):
        result = ''
        seq = '{'
        if not self.errorExist:
            if self.noz == 0:
                result = "0 records and 0 DVDs: {}"
            else:
                for i in range(self.noz):
                    if i == self.noz - 1:
                        seq += f'{self.list_of_movie_records[i].movieName} ({self.list_of_movie_records[i].numDvd})'
                    elif i < self.noz - 1:
                        seq += f'{self.list_of_movie_records[i].movieName} ({self.list_of_movie_records[i].numDvd}), '
                seq += '}'
                result = f"{self.getNumberOfMovieRecords()} records and {self.getNumberOfMovieDVDs()} DVDs: {seq}"
        else:
            result = f"Error: maximum number of movie DVDs ({self.getNumberOfMovieDVDs()}) reached"

        return result


class MovieRecord:
    id = 1

    # Each zone stores a collection of movie records.
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
    # A store has up to 100 zones.
    def __init__(self):
        pass

    def addZones(self, listOfZoneObj):
        pass

    def getZones(self, zone=None):
        pass

    def getStats(self, movieName):
        pass
