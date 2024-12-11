import base64
import io

import numpy as np
from PIL import Image

from grpc_server.proto import get_image_encode_pb2


def load_image_from_base64(base64_string):
    image_data = base64.b64decode(base64_string)
    image_file = io.BytesIO(image_data)
    image = Image.open(image_file)
    return image


def np2tensor_proto(np_ndarray: np.ndarray):
    shape = list(np_ndarray.shape)
    data = np_ndarray.flatten().tolist()
    tensor_pb = get_image_encode_pb2.Tensor()
    tensor_pb.shape.extend(shape)
    tensor_pb.data.extend(data)
    return tensor_pb


def tensor_proto2np(tensor_pb):
    np_matrix = np.array(tensor_pb.data, dtype=np.float).reshape(tensor_pb.shape)
    return np_matrix
