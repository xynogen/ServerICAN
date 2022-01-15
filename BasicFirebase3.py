from firebase_admin import credentials, db, initialize_app, delete_app, storage
import requests
import cv2
import imutils
import time

cred = credentials.Certificate("./icansdk.json")
app = initialize_app(cred, {"storageBucket": "icanpolsri-a0d38.appspot.com"})
url = "https://icanpolsri-a0d38-default-rtdb.asia-southeast1.firebasedatabase.app/"
ref = db.reference("/", app, url)
filename = "Kolam.jpeg"

def captureImage(rotasi = "0"):
	rotasi = int(rotasi)
	trig = requests.get("http://192.168.0.102/capture")
	time.sleep(4)
	req = requests.get("http://192.168.0.102/saved-photo")
	
	if trig.status_code == 200 and req.status_code == 200:
		with open(filename, "wb") as file:
			file.write(req.content)

	img = cv2.imread(filename)
	img = imutils.rotate(img, rotasi)
	cv2.imwrite(filename, img)

def sendImage():
	ref = db.reference("/", app, url)
	bucket = storage.bucket(app=app)
	blob = bucket.blob(filename)
	blob.upload_from_filename(filename)

def main(Data):
	if (Data.path == "/snap/trig"):
		if Data.data[0] == "1":
			rotasi = ref.child("snap").child("rotasi").get()
			captureImage(rotasi)
			sendImage()
			ref.child("snap").child("trig").set("0")

if __name__ == '__main__':
	ref.listen(main)

