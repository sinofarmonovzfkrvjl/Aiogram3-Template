from aiogram import types, F
from utils.downloader import YouTubeVideoDownloader, InstagramDownloader
from os import remove
import glob
import requests

from loader import dp, bot

@dp.message()
async def echo_handler(message: types.Message):
    if message.text.startswith(("https://youtube.com/", "https://www.youtube.com/", "https://youtu.be/", "https://tiktok.com/", "https://www.tiktok.com/", "https://www.facebook.com/", "https://www.facebook.com")):
        await message.answer("Video yuklanmoqda...")
        video = YouTubeVideoDownloader(message.text)
        try:
            if video:
                video_file = types.FSInputFile(glob.glob("*.mp4")[0])
                await message.answer_video(
                    video=video_file,
                    caption=f"Video nomi: {video.get('title')}\n"
                            f"Video yuklagan shaxs: {video.get('uploader')}\n"
                            f"Layklar soni: {video.get('like_count')}\n"
                            f"Dislayklar soni: {video.get('dislike_count')}\n"
                            f"Ko'rishlar soni: {video.get('view_count')}\n"
                            f"Video yuklangan sana: {video.get('upload_date')}"
                )
                await message.answer(f"Video izohi: {video.get('description')}")
            else:
                await message.answer("Video yuklayolmadim")
        except:
            pass
        remove(glob.glob("*.mp4")[0])
    elif message.text.startswith(("https://www.instagram.com/", "https://instagram.com/")):
        await message.answer("Video yuklanmoqda")
        downloaded = InstagramDownloader(message.text)
        response = requests.get(downloaded['url'])
        if message.text.startswith("https://www.instagram.com/p/"):
            with open("image.png", "wb") as f:
                f.write(response.content)
            try:
                await message.answer_photo(types.FSInputFile("image.png"))
                await message.answer(str(downloaded['description']))
            except Exception as e:
                await message.answer(e)
            remove("image.png")
        elif message.text.startswith("https://www.instagram.com/reel/"):
            with open('video.mp4', 'wb') as f:
                f.write(response.content)
            try:
                await message.answer_video(types.types.FSInputFile("video.mp4"))
                await message.answer(str(downloaded['description']))
            except Exception as e:
                await message.answer("Videoni yuklab bo'lmadi")
            remove("video.mp4")
