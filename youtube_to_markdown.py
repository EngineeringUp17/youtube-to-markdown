
import sys, re
# From https://webapps.stackexchange.com/a/101153
VIDEO_ID_REGEX = re.compile(r"watch\?v=([0-9A-Za-z_-]{10}[048AEIMQUYcgkosw])")

video_url = input("Enter Video Url> ").strip()
match = VIDEO_ID_REGEX.search(video_url)
if not match:
    print("Please enter a valid youtube url!")
    sys.exit(1)
else:
    video_id = match.group(1)

alt_text = "Video 1"
if (input_alt_text := input("Enter Alt Text> ").strip()) != "":
    alt_text = input_alt_text

print()

# The video id in a normal youtube url: https://www.youtube.com/watch?v=<VIDEO_ID>
# The video id in a shortened youtube url: https://youtu.be/<VIDEO_ID>

# Taken from https://stackoverflow.com/a/47649414
# Template for thumbnail url: https://img.youtube.com/v1/<VIDEO_ID_HERE>/maxresdefault.jpg
print(f"[![{alt_text}](https://img.youtube.com/vi/{video_id}/maxresdefault.jpg)](https://www.youtube.com/watch?v={video_id})")
