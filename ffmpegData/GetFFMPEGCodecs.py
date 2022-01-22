"""
Get the codecs from FFMPEG and write them to a file.
"""
import json
import os
import subprocess


def GetFFMPEGCodecs():
    process = subprocess.Popen(["ffmpeg", "-codecs"], stdout=subprocess.PIPE)
    firstSplit = str(process.communicate()[0]).split("\\r\\n")
    out = []
    for spl in range(10, len(firstSplit)):
        out.append(firstSplit[spl])
    return out


def GetPixelFormats():
    process = subprocess.Popen(["ffmpeg", "-pix_fmts"], stdout=subprocess.PIPE)
    firstSplit = str(process.communicate()[0]).split("\\r\\n")
    out = []
    for spl in range(8, len(firstSplit)):
        out.append(firstSplit[spl])
    return ProcessFFMPEGOutput(out)


def ProcessFFMPEGOutput(ffmpegCodecOutput):
    data = ffmpegCodecOutput
    extensions = []
    for line in data:
        spl = line.lstrip(' ').split(' ')
        v = 0
        try:
            ext = spl[1]
            extensions.append(ext)
        except:
            pass
    return extensions


def GetVideoCodecs():
    codecs = ProcessFFMPEGOutput(GetFFMPEGCodecs())
    finished = False
    ext = []
    for codec in codecs:
        if codec == '4gv':
            finished = True
        if finished:
            pass
        else:
            ext.append(codec)
    return ext


def GetAudioCodecs():
    codecs = ProcessFFMPEGOutput(GetFFMPEGCodecs())
    finished = False
    started = False
    ext = []
    for codec in codecs:
        if codec == 'ass':
            finished = True
        if codec == '4gv':
            started = True
        if not finished:
            if not started:
                pass
            else:
                ext.append(codec)
        else:
            pass
    return ext


def GetSubtitilesCodecs():
    codecs = ProcessFFMPEGOutput(GetFFMPEGCodecs())
    finished = False
    started = False
    ext = []
    for codec in codecs:
        # if codec == 'ass':
        #     finished = True
        if codec == 'ass':
            started = True
        if not finished:
            if not started:
                pass
            else:
                ext.append(codec)
        else:
            pass
    return ext


def GetCodecs():
    return ProcessFFMPEGOutput(GetFFMPEGCodecs())


def WriteCodecFile(filepath='ffmpegCodecs.csv'):
    file = open(filepath, 'w')
    if 'json' in os.path.splitext(filepath)[1].lower():
        codecJs = {"Codecs": GetCodecs()}
        file.write(json.dumps(codecJs))
    else:
        file.write('\n'.join(GetCodecs()))
    file.close()


def main():
    WriteCodecFile(filepath='ffmpegData/ffmpegCodecs.json')
    WriteCodecFile(filepath='ffmpegData/ffmpegCodecs.csv')


if __name__ == '__main__':
    main()
