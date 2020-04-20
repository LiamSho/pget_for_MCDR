# -*- coding: utf-8 -*-
#version v1.0.0
import requests

HelpMessage ='''------MCDR pget插件------
§7!!pget [url] -下载这个插件
--------------------------------'''


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
                        server.reply(info, '§a下载成功!§r')
                        server.reply(info, '§a由于fallen大佬偷懒，无法自动重载插件\n§a请手动输入!!MCDR reload plugin重载插件§r')
                    else:
                        server.reply(info, '§c下载失败§r')
                else:
                    server.reply(info, '§c您下载的不是python文件§r')
            else:
                server.reply(info, '§c命令格式错误！请使用!!pget查看帮助§r§r')
        else:
            server.reply(info, '§c权限不足！§r')