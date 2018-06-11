#coding:utf-8

__author__ = "guoling"

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import config
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
__author__ = 'guoling'
import logging.config
logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger('default')

from flask import Blueprint,jsonify,request
from Common.MessageUtils import standarlize_response

import QueryConsultingCostRules as ConsultingRules

consulting = Blueprint('consult',__name__)


@consulting.route('/bp/consulting/cost/rules',methods=['GET'])
def query_consulting_cost_rules():
    """

    :return:
    """
    logger.debug("[查询副卡销售品额外信息接口  start]")
    xspid = request.args.get("xspid",None).strip()

    if not xspid:
        logger.debug('没有获取到手机号')
        return jsonify(standarlize_response(1,'[失败]没有获取到手机号'))

        result = ConsultingRules.query_consulting_cost_rules(xspid)
        logger.debug('获取到结果集result:%s',result)
        return result