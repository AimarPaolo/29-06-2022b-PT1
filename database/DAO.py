from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodi(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.*, sum(t.Milliseconds) as durata
from track t , album a 
where a.AlbumId = t.AlbumId
group by a.AlbumId 
having sum(t.Milliseconds) > %s * 1000 
"""
        cursor.execute(query, (durata, ))
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllArchiPesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
from (select a.AlbumId as a1, sum(t.Milliseconds) as milli1
from album a, track t 
where a.AlbumId = t.AlbumId 
group by a.AlbumId 
having sum(t.Milliseconds) > %s * 1000
) as t1,
(select a.AlbumId as a2, sum(t.Milliseconds) as milli2
from album a, track t 
where a.AlbumId = t.AlbumId 
group by a.AlbumId 
having sum(t.Milliseconds) > %s* 1000
) as t2
where t1.a1 > t2.a2 and t1.milli1 <> t2.milli2 
and 4*%s*1000 < t1.milli1 + t2.milli2"""
        cursor.execute(query, ())
        for row in cursor:
            result.append((row["a1"], row["a2"], row["milli1"], row["milli2"]))
            # Prodotto(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query, )

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result