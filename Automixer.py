#####
'''
Program: Sparta Remix Auto Mixer
Desc: Accepts subclips and pattern type and mixes an mp3 of resulting mix
'''
#####

from pydub import AudioSegment


cur_pos = 0  # millisecond position
bases = AudioSegment.from_mp3("Sparta_Remix_Base.mp3")
space = ""
multiple = "m"
subclip1 = AudioSegment.from_mp3("subclip1.mp3")
subclip2 = AudioSegment.from_mp3("subclip2.mp3")
subclip3 = AudioSegment.from_mp3("subclip3.mp3")
pat_dict = {'_': space, 'x': multiple, '1': subclip1, '2': subclip2, '3': subclip3}

def write_media(media_type):
    global cur_pos
    global bases
    global pat_dict
    if media_type == space:
        cur_pos += 100
    elif media_type[0] == "m":
        for x in range(int(media_type[2:4])):
            if pat_dict[media_type[1]] == space:
                cur_pos += 100
                print(cur_pos)
            else:
                bases = bases.overlay(pat_dict[media_type[1]], position = cur_pos)
                cur_pos += 100
                print(cur_pos)
    else:
        try:
            bases = bases.overlay(media_type, position=cur_pos)
            cur_pos += 100
            print(cur_pos)
        except Exception:
            warn("Invalid Character Detected! Skipping over...")
            cur_pos += 100
            print(cur_pos)


def read_pattern_file():
    f = open('pattern_template.textpat', 'r')
    pattern = str(f.read())
    print pattern
    f.close()
    return pattern


def main():
    pattern = read_pattern_file()
    skip_buffer = 0
    for num in range(len(pattern)):
        if skip_buffer > 0:
            skip_buffer -= 1
        elif pattern[num] == 'x':
            write_media("m" + pattern[num + 1:num + 4])
            skip_buffer += 3
        else:
            write_media(pat_dict[pattern[num]])
    bases.export("Sparta_Remix_Export.mp3", format="mp3")

main()
