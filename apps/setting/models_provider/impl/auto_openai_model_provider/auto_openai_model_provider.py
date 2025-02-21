# coding=utf-8
import os
from urllib.parse import urlparse, ParseResult

import requests

from common.util.file_util import get_file_content
from setting.models_provider.base_model_provider import IModelProvider, ModelProvideInfo, ModelInfo, ModelTypeConst, \
    ModelInfoManage
from setting.models_provider.impl.auto_openai_model_provider.credential.llm import AutoOpenaiModelCredential
from setting.models_provider.impl.auto_openai_model_provider.model.llm import VllmChatModel
from smartdoc.conf import PROJECT_DIR

auto_openai_model_credential = AutoOpenaiModelCredential()

# DEFAULT_AUTO_OPENAI_MODELS = os.environ.get("DEFAULT_AUTO_OPENAI_MODELS", "Qwen-三小文本大模型")
# DEFAULT_AUTO_OPENAI_MODELS = DEFAULT_AUTO_OPENAI_MODELS.split(",")

# model_info_list = [ModelInfo(name, name, ModelTypeConst.LLM, auto_openai_model_credential, VllmChatModel) for name in DEFAULT_AUTO_OPENAI_MODELS]

# model_info_manage = (ModelInfoManage.builder().append_model_info_list(model_info_list).append_default_model_info(
#     ModelInfo(DEFAULT_AUTO_OPENAI_MODELS[0], DEFAULT_AUTO_OPENAI_MODELS[0], ModelTypeConst.LLM, auto_openai_model_credential, VllmChatModel)
#     ).build())


def get_base_url(url: str):
    parse = urlparse(url)
    result_url = ParseResult(scheme=parse.scheme, netloc=parse.netloc, path=parse.path, params='',
                             query='',
                             fragment='').geturl()
    return result_url[:-1] if result_url.endswith("/") else result_url


class AutoOpenaiModelProvider(IModelProvider):
    def get_model_info_manage(self):
        return ()

    def get_model_provide_info(self):
        return ModelProvideInfo(provider='model_auto_openai_provider', name='Auto Openai', icon=get_file_content(
            os.path.join(PROJECT_DIR, "apps", "setting", 'models_provider', 'impl', 'auto_openai_model_provider', 'icon',
                         'vllm_icon_svg')))

    @staticmethod
    def get_base_model_list(api_base):
        base_url = get_base_url(api_base)
        base_url = base_url if base_url.endswith('/v1') else (base_url + '/v1')
        r = requests.request(method="GET", url=f"{base_url}/models", timeout=5)
        r.raise_for_status()
        return r.json().get('data')

    @staticmethod
    def get_model_info_by_name(model_list, model_name):
        if model_list is None:
            return []
        return [model for model in model_list if model.get('id') == model_name]
