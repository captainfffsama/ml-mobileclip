import torch
import mobileclip
import datetime
from grpc_server.proto import get_image_encode_pb2_grpc
from grpc_server.utils import load_image_from_base64, np2tensor_proto


class MobileClip(get_image_encode_pb2_grpc.AiServiceServicer):
    def __init__(self, model_type: str, ckpt_path: str, device: str = "cuda"):
        self.model, _, self.preprocess = mobileclip.create_model_and_transforms(
            model_type,
            pretrained=ckpt_path,
            device=device,
        )
        self.device = device

        self.tokenizer = mobileclip.get_tokenizer(model_type)

    def DlEmbeddingGet(self, request, context):
        with torch.no_grad(), torch.amp.autocast(self.device):
            image = load_image_from_base64(request.imdata)
            image = self.preprocess(image.convert("RGB")).unsqueeze(0).to(self.device)
            image_features: torch.Tensor = self.model.encode_image(image)
            image_features /= image_features.norm(dim=-1, keepdim=True).squeeze()

        image_features = image_features.detach().cpu().numpy()
        print(
            "{} embedding size: ".format(datetime.datetime.now()), image_features.shape
        )
        torch.cuda.empty_cache()
        return np2tensor_proto(image_features)
