
import pymysql


db_conn = pymysql.connect(
    host='47.100.138.122',
    port=33006,
    user='message_center',
    passwd='a9U911VU2Ggz',
    db='message_center',
    # connect_timeout=self.EXT_PONY_DB['connect_timeout'],
    # read_timeout=self.EXT_PONY_DB['read_timeout']
)