# -*- coding: utf-8 -*-
# v1.4.0
import requests
import json
from utils import constant


HelpMessage ="""------MCDR pget插件------
§7!!pget [url] -下载这个插件
--------------------------------"""



def on_load(server, old):
    server.add_help_message("!!pget", "下载插件")


def on_info(server, info):
    content = info.content.rstrip(" ")
    content = content.split(" ")
    if content[0] == "!!pget":
        if server.get_permission_level(info) == 3:
            if len(content) == 1:
                server.reply(info, HelpMessage)
            elif len(content) == 2:
                download(server, info, content)
            else:
                server.reply(info, "§c命令格式错误！请使用!!pget查看帮助§r")
        else:
            server.reply(info, "§c权限不足！§r")


def download(server, info, content):
    name = content[1].split("/")
    if name[-1].split(".")[-1] == "py":
        file = requests.get(content[1])
        if file.status_code == 200:
            with open("./plugins/" + name[-1], "wb") as write:
                write.write(file.content)
            finish_download_msg(server, info, name)
        else:
            server.reply(info, "§c下载失败§r")
    else:
        server.reply(info, "§c您下载的不是python文件§r")


def finish_download_msg(server, info, name):
    version = constant.VERSION.split("-")
    version = version[0].split(".")
    version = ".".join(version[0:2])
    version = float(version)
    if version >= 0.8:
        server.refresh_changed_plugins()
        server.reply(info, "§a已自动重载插件！§r")
    else:
        if info.is_player:
            server.tell(info.player, "§a下载成功!§r")
            server.execute("tellraw " + info.player + " " + reload_msg())
        else:
            print("下载成功！")
            print("请手动输入!!MCDR reload plugin重载插件")
    if info.is_player:
        server.logger.info("管理员" + info.player + "下载了插件" + name[-1])
    else:
        server.logger.info("有人通过控制台下载了插件" + name[-1])


def reload_msg():
    return json.dumps(
        [
            {
                "text": "§a请输入!!MCDR reload plugin或点击这条消息来重载插件§r",
                "clickEvent":
                    {
                        "action": "run_command",
                        "value": "!!MCDR reload plugin"
                    }
            }
        ]
    )