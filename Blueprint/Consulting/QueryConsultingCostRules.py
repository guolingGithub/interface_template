#coding:utf-8

__author__ = "guoling"

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import config
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

import logging.config
logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('default')

from flask import jsonify
from Common.MessageUtils import standarlize_response
from Tool.AsyncQueryTools import AsyncQueryTools




def query_consulting_cost_rules(xspid):
    """
    param xspid: 0000000055C09D6B9A376E98E053433210AC47CA
    :return:
    """
    in_param_list = [["V_SELLID",xspid]]
    out_param_type_list = ["CURSOR"]
    result = async_query_tool.async_query("P_IF_GET_GOODS_INFO_EXT",
                                          in_param_list=in_param_list,
                                          out_param_type_list=out_param_type_list)
    logger.debug("返回P_IF_GET_GOODS_INFO_EXT的结果集 result:%s",result)