import lab6_pb2_grpc
import lab6_pb2
import grpc
from concurrent import futures
import random
import json
import base64
import sys,time

host = sys.argv[1]
cmd = sys.argv[2]
reps = int(sys.argv[3])
channel = grpc.insecure_channel(host+':50051')
stub = lab6_pb2_grpc.lab6Stub(channel)


def doAdd(debug=False):
 data=lab6_pb2.addMsg(a=random.randrange(0,100),b=random.randrange(0,100))
 response = stub.add(data)
 if debug:
   print(response.sum)

def doRawImage(debug=False):
  data = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
  t = lab6_pb2.rawImageMsg(img=data)
  response = stub.rawImage(t)
  if debug:
    print(response.height,response.width)

def doDotProduct(debug=False):
  l1=[random.random() for _ in range(100)]
  l2=[random.random() for _ in range(100)]
  data=lab6_pb2.dotProductMsg(a=l1,b=l2)
  response=stub.dotProduct(data)
  if debug:
    print(response.dotproduct)

def doJsonImage(debug=False):
  with open("Flatirons_Winter_Sunrise_edit_2.jpg", "rb") as image2string:
          converted_string = base64.b64encode(image2string.read()).decode("utf-8")
  t = {'image' : converted_string}

  data = lab6_pb2.jsonImageMsg(img=json.dumps(t))
  response = stub.jsonImage(data)
  if debug:
    print(response.height,response.width)

if cmd == 'rawImage':
    start = time.perf_counter()
    for i in range(reps):
        doRawImage()
    t = ((time.perf_counter() - start)/reps)*1000
    print("Took", t, "ms per operation")
elif cmd == 'add':
    start = time.perf_counter()
    for j in range(reps):
        doAdd()
    t = ((time.perf_counter() - start)/reps)*1000
    print("Took", t, "ms per operation")
elif cmd == 'jsonImage':
    start = time.perf_counter()
    for i in range(reps):
        doJsonImage(debug=True)
    t = ((time.perf_counter() - start)/reps)*1000
    print("Took", t, "ms per operation")
elif cmd == 'dotProduct':
    start = time.perf_counter()
    for j in range(reps):
        doDotProduct(debug=True)
    t = ((time.perf_counter() - start)/reps)*1000
    print("Took", t, "ms per operation")
else:
    print("Unknown option", cmd)