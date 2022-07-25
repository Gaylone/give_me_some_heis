import traceback

from hoshino.typing import MessageSegment
from hoshino import Service, priv

from .main_func import *

sv = Service('give_me_some_heis')
def render_forward_msg(msg_list: list, uid=1916714922, name='小加加(VC装甲钢36D版)'):
    forward_msg = []
    for msg in msg_list:
        forward_msg.append({
            "type": "node",
            "data": {
                "name": str(name),
                "uin": str(uid),
                "content": msg
            }
        })
    return forward_msg



@sv.on_prefix('来点')
async def quick_search_skin(bot, ev):
    try:
        args = ev.message.extract_plain_text().split()
        msg_list = []
        if len(args) == 1:
            if args[0] == '黑丝':
                heis_set = give_me_some_heis(2)
                msg_list.append(MessageSegment.image(file=heis_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=heis_set[1]) + "\n")
            if args[0] == '白丝':
                bais_set = give_me_some_bais(2)
                msg_list.append(MessageSegment.image(file=bais_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=bais_set[1]) + "\n")
            if args[0] == '足控':
                zuk_set = give_me_some_zuk(2)
                msg_list.append(MessageSegment.image(file=zuk_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=zuk_set[1]) + "\n")
            if args[0] == '巨乳':
                jur_set = give_me_some_jur(2)
                msg_list.append(MessageSegment.image(file=jur_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=jur_set[1]) + "\n")
            if args[0] == '网红':
                mcn_set = give_me_some_mcn(2)
                msg_list.append(MessageSegment.image(file=mcn_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=mcn_set[1]) + "\n")
            if args[0] == 'jk':
                jk_set = give_me_some_jk(2)
                msg_list.append(MessageSegment.image(file=jk_set[0]) + "\n")
                msg_list.append(MessageSegment.image(file=jk_set[1]) + "\n")
        else:
            return
        if len(msg_list)==0 :
            return
        forward_msg = render_forward_msg(msg_list)
        await bot.send_group_forward_msg(group_id=ev.group_id, messages=forward_msg)
        return

    except:
        msg = '载图出错.请看日志'
        traceback.print_exc()
        await bot.send(ev, str(msg)+str(traceback.print_exc()), at_sender=True)
        return