from angel import angel

CLIENT_ID = 'f4bc189150f55e3a4e04d7dd47d6f60d5d0101b7c16c9719'
CLIENT_SECRET = '45e8cf40afa601846ea9af9dcf4d101aef2d183514690433'
ACCESS_TOKEN = '7b2f970c65843c003f29faab3cd089d9a2fe65fb738a1f69'
al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

location = al.get_tags(1654)
print location['statistics']['all']['followers']

