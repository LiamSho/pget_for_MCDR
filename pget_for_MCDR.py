# -*- coding: utf-8 -*-
#version v1.1.1
import requests

HelpMessage ='''------MCDR pget插件------
§7!!pget [url] -下载[url]插件
--------------------------------'''

reload_msg=' [{"text":"§a请输入!!MCDR reload plugin或点击这条消息来重载插件§r","insertion":"!!MCDR reload plugin","clickEvent":{"action":"run_command","value":"!!MCDR reload plugin"}}]'

def on_load(server, old):
        server.add_help_message('!!pget', '下载插件')


def on_info(server, info):
    content = info.content.rstrip(' ')
    content = content.split(' ')
    if content[0] == '!!pget':
        if server.get_permission_level(info) == 3:
            if len(content) == 1:
                server.reply(info, HelpMessage)
            elif len(content) == 2:
                name = content[1].split('/')
                python_file_check = name[-1].split('.')
                if python_file_check[-1] == 'py':
                    file = requests.get(content[1])
                    if file.status_code == 200:
                        with open('./plugins/' + name[-1], 'wb') as write:
                            write.write(file.content)
                        if info.is_player:
                            server.tell(info.player, '§a下载成功!§r')
                            server.execute('tellraw ' + info.player + reload_msg)
                        else:
                            print('下载成功！')
                            print('请手动输入!!MCDR reload plugin重载插件')
                    else:
                        server.reply(info, '§c下载失败§r')
                else:
                    server.reply(info, '§c您下载的不是python文件§r')
            else:
                server.reply(info, '§c命令格式错误！请使用!!pget查看帮助§r§r')
        else:
            server.reply(info, '§c权限不足！§r')