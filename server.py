from concurrent import futures
import grpc
import euromil_pb2
import euromil_pb2_grpc


class EuromilService(euromil_pb2_grpc.EuromilServicer):
    def RegisterEuroMil(self, request, context):
        # Simple business logic for registration
        if request.key and request.checkid:
            message = f"Bet registered with key: {request.key} and check ID: {request.checkid}."
            return euromil_pb2.RegisterReply(message=message)
        else:
            #Invalid input no key or/and check id
            return euromil_pb2.RegisterReply(message="Invalid input. Both key and check ID are required.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    euromil_pb2_grpc.add_EuromilServicer_to_server(EuromilService(), server)
    server.add_insecure_port("[::]:50051")
    print("Server is running on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
