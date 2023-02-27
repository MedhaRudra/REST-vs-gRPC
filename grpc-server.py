import lab6_pb2_grpc
import lab6_pb2
import grpc
from concurrent import futures
from PIL import Image
import io
import json
import base64
class lab6Servicer(lab6_pb2_grpc.lab6Servicer):
  
  def add(self, request, context):
    return lab6_pb2.addReply(sum=request.a+request.b)
  
  def rawImage(self, request, context):
    try:
      ioBuffer = io.BytesIO(request.img)
      img = Image.open(ioBuffer)
      return lab6_pb2.imageReply(width = img.size[0], height = img.size[1])
    except :
        return lab6_pb2.imageReply(width = 0, height = 0)

  def dotProduct(self, request, context):
    s =0
    l1=request.a
    l2=request.b
    for i in range(len(l1)):
        s = s + l1[i] * l2[i]
    return lab6_pb2.dotProductReply(dotproduct=s)
      

  def jsonImage(self, request, context):
    d = json.loads(request.img)
    
    ioBuffer = io.BytesIO(base64.b64decode(d['image']))
    img = Image.open(ioBuffer)
    #
    return lab6_pb2.imageReply(width = img.size[0], height = img.size[1])
    


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  lab6_pb2_grpc.add_lab6Servicer_to_server(
      lab6Servicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

serve()