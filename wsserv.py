#!/usr/bin/env python

import json
from json import JSONDecodeError
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from utils.base.dict import MyDict

clients = []


class MyWsServer(WebSocket):
    channel = None
    client_id = None

    @staticmethod
    def send(client, action, category, payload):
        message = json.dumps({'action': action, 'category': category, 'payload': payload})
        client.sendMessage(message)

    def handleMessage(self):
        try:
            message = json.loads(self.data)
            print(message)
            payload = MyDict.get(message, 'payload', {})
            action = MyDict.get(message, 'action', 'unknown')
            category = MyDict.get(message, 'category', 'unknown')
            for client in clients:
                # 不再向消息来源发送
                if client == self:
                    continue
                # 向相同 channel 的所有客户端，广播接收到的消息载荷
                # 或：向所有客户端，广播接收到的消息载荷
                if (action == 'broadcast_channel' and client.channel == self.channel) or action == 'broadcast_all':
                    MyWsServer.send(client, action, category, payload)
        except JSONDecodeError as decode_err:
            print(decode_err)
        except AttributeError as attr_err:
            print(attr_err)

    def handleConnected(self):
        # 从连接请求中解析 channel 和 客户端 ID
        # 'GET /asset_info/2ed45cad-79de-07fb-309f-d56a4af6a97f HTTP/1.1'
        try:
            req = self.request.requestline.split(' ')
            client_addr = req[1].split('/')
            self.channel = client_addr[1]
            # 'GET / HTTP/1.1] 是客户端没有设置 channel 和客户端 ID 时的请求
            # client_addr[2] 会抛出 IndexError 异常，从而关闭该客户端的连接
            self.client_id = client_addr[2]
            print(self.address, self.channel, '/', self.client_id, ': connected')

            for client in clients:
                if client.channel == self.channel:
                    # 向相同 channel 的所有客户端广播新的客户端连接消息
                    payload = {'addr': self.address, 'channel': self.channel, 'client': self.client_id}
                    MyWsServer.send(client, 'open', 'general', payload)

            clients.append(self)

        except AttributeError as attr_err:
            print(attr_err)
        except Exception as e:
            print(e)

    def handleClose(self):
        clients.remove(self)
        print(self.address, self.channel, '/', self.client_id, ': closed')
        for client in clients:
            if client.channel == self.channel:
                # 向相同 channel 的所有客户端，广播客户端断开消息
                payload = {'addr': self.address, 'channel': self.channel, 'client': self.client_id}
                MyWsServer.send(client, 'close', 'general', payload)


server = SimpleWebSocketServer('', 6789, MyWsServer)
server.serveforever()
