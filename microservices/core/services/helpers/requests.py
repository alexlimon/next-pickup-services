import aiohttp 
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'Connection': "keep-alive",
    'Content-Type':"application/json"
}

async def get_async(url):
    async with aiohttp.ClientSession() as async_session:
        async with async_session.get(url, headers = headers) as response:
            content = await response.read()

            if response.status >= 400:
                raise aiohttp.ClientError(json.loads(content))
            
            return json.loads(content)

async def post_async(url, payload):
    async with aiohttp.ClientSession() as async_session:
        async with async_session.post(url, headers = headers, data = payload) as response:
            content = await response.read()

            if response.status >= 400:
                raise aiohttp.ClientError(json.loads(content))
            
            return json.loads(content)
