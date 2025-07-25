import ffmpeg
import os
import uuid

async def compress_video(input_file):
    output_file = f"compressed_{uuid.uuid4().hex}.mp4"
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec='libx264', crf=28, preset='fast')
            .run(overwrite_output=True)
        )
        if os.path.exists(output_file):
            return output_file
    except ffmpeg.Error as e:
        print("FFmpeg error:", e.stderr.decode())
    return None
