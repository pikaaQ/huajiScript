#   --------------------------------注释区--------------------------------
#   资金盘 谁充钱谁是傻逼
#   资金盘 谁充钱谁是傻逼
#   资金盘 谁充钱谁是傻逼
#
#   入口&教程:
#   先在微信打开http://qq.ylilp.cn?masterid=oUmo76x4Eer1Do4wYRnYR9zko4a4
#   然后在网页登录 领取首页的BNU小狗零号 并且绑定支付宝完成提现一次
#   抓取qq.ylilp.cn域名下unionid和token的值

#   格式: unionid的值#token的值
#   变量:yuanshen_bnudog
#   多号分割方式 [ @ 或 换行 或 新建同名变量 ]
#   corn: 一天一次即可
#   --------------------------------一般不动区--------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))