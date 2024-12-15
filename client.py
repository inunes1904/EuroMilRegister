import grpc
import euromil_pb2
import euromil_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = euromil_pb2_grpc.EuromilStub(channel)
        response = stub.RegisterEuroMil(euromil_pb2.RegisterRequest(key="12345", checkid="abcde"))
        print(f"Response from server: {response.message}")


if __name__ == "__main__":
    run()
