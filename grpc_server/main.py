import os
import argparse
from concurrent import futures
from pprint import pprint
from datetime import datetime
import asyncio

import grpc
from grpc_server.proto import get_image_encode_pb2_grpc as giep_grpc

from grpc_server.model import MobileClip
import base_config as config_manager


def parse_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-mc", "--model_cfg", type=str, default="")
    parser.add_argument("-mw", "--model_weight", type=str, default="")
    parser.add_argument("-c", "--cfg", type=str, default="")
    args = parser.parse_args()
    return args

async def main(grpc_args,model):
    server = grpc.aio.server(
        futures.ThreadPoolExecutor(max_workers=grpc_args['max_workers']),
        options=[('grpc.max_send_message_length',
                  grpc_args['max_send_message_length']),
                 ('grpc.max_receive_message_length',
                  grpc_args['max_receive_message_length'])])
    giep_grpc.add_AiServiceServicer_to_server(model, server)

    server.add_insecure_port("{}:{}".format(grpc_args['host'],
                                            grpc_args['port']))
    await server.start()
    print('modileclip image decode gprc server init done')
    await server.wait_for_termination()

def run():
    args = parse_args()
    if os.path.exists(args.cfg):
        config_manager.merge_param(args.cfg)
    args_dict: dict = config_manager.param
    detector_params = args_dict['detector_params']
    if os.path.exists(args.model_cfg) and os.path.exists(args.model_weight):
        detector_params['cfg_path'] = args.model_cfg
        detector_params['ckpt_path'] = args.model_weight
    model = MobileClip(**detector_params)
    print("model init done!")
    grpc_args = args_dict['grpc_args']
    asyncio.run(main(grpc_args,model))

if __name__ == "__main__":
    run()
