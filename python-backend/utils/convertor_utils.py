import os
import json

from models.audio_info import AudioInfo
from models.xls_info import XlsInfo
from models.audio_collection import AudioCollection
from utils import config

def dict_to_xls_info(d):
    print(d['filePath'], d['createTime'], d['place'])
    return XlsInfo(d['filePath'], int(d['createTime']), d['place'])

def dict_to_audio_info(d):
    return AudioInfo(d['filePath'], int(d['createTime']), d['place'])

def dict_to_audio_collection(d):
    return AudioCollection(d['collections'])

def xls_info_to_dict(xls_info):
    return {
        'filePath': xls_info.file_path,
        'createTime': xls_info.create_time,
        'place': xls_info.place
    }

def audio_info_to_dict(audio_info):
    return {
        'filePath': audio_info.file_path,
        'createTime': audio_info.create_time,
        'place': audio_info.place
    }

def audio_collection_to_dict(audio_collection):
    return {
        'collections': audio_collection.collections
    }

def pct_sub_result_to_dict(pct_sub_result):
    return {
        'fileName': pct_sub_result.file_name,
        'pctn': pct_sub_result.pctn,
        'pctu': pct_sub_result.pctu,
        'pctm': pct_sub_result.pctm,
        'place': pct_sub_result.place,
        'createTime': pct_sub_result.create_time
    }

def pctn_result_to_dict(pctn_result):
    return {
        'fileName': pctn_result.file_name,
        'value': pctn_result.value,
        'place': pctn_result.place,
        'createTime': pctn_result.create_time
    }

def soundtype_result_to_dict(soundtype_result):
    return {
        'fileName': soundtype_result.file_name,
        'value': soundtype_result.value,
        'place': soundtype_result.place,
        'createTime': soundtype_result.create_time
    }

def convert_to_object_wrapper(msg, type):
    obj = None
    if (type == 'xls_info'):
        obj = json.loads(msg, object_hook=dict_to_xls_info)
    elif (type == 'audio_info'):
        obj = json.loads(msg, object_hook=dict_to_audio_info)
    elif (type == 'audio_collection'):
        obj = json.loads(msg, object_hook=audio_collection_to_dict)

def parse_output_file_path(input_fp):
    input_dir = os.path.dirname(input_fp)
    basename = os.path.basename(input_fp)
    input_dir = input_dir[:input_dir.find("wav")]
    output_dir = config.SPECTROGRAM_OUTPUT_FOLDER.replace("{input}", input_dir)
    basename = basename.replace("wav", "png")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    return os.path.join(output_dir, basename)
