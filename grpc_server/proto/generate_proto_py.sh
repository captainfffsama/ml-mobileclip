python -m grpc_tools.protoc -I ./ --proto_path=./get_image_encode.proto --python_out=. --grpc_python_out=./ get_image_encode.proto
