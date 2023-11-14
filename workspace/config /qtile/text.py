
# from libqtile.command.client import CommandClient
from libqtile.command.client import InteractiveCommandClient

# cc = CommandClient()
# print(cc.call("status"))
# axeced at group info

icc = InteractiveCommandClient()
#print(icc.group.info())

icc.group[""].to_screen(2)
