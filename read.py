import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

cond  = input("請輸入您要查詢的課程關鍵字:")
aond  = input("請輸入您要查詢的老師：")

db = firestore.client()
collection_ref = db.collection("靜宜資管")
docs = collection_ref.get()
result = ""
for doc in docs:
	dict = doc.to_dict()
	if cond in dict["Course"]:
		#print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
		result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
		result += dict["Time"] + "於" + dict["Room"] + "上課\n"

	if aond in dict["Leacture"]:
		#print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
		result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
		result += dict["Time"] + "於" + dict["Room"] + "上課\n"
print(result)