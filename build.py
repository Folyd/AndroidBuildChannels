#!/bin/python
import shutil,zipfile
import sys,os

emptyFile = "empty_file"

def write_channel_to_apk(apkfile, channel):
    zipped = zipfile.ZipFile(apkfile, 'a', zipfile.ZIP_DEFLATED)
    zipped.write(emptyFile, 'META-INF/channel_%s' % channel)
    zipped.close()

def build():
    if len(sys.argv) < 2:
        raise SystemError("must specify a apk file")

    if len(sys.argv) < 3:
        raise SystemError("must specify a channel list file")

    apk = sys.argv[1]
    channels = sys.argv[2]
    print '----apk name is %s ----' % apk
    version = raw_input('please input current version code:')
    print '----start build channels----'

    if not os.path.exists(emptyFile):
        os.system('touch %s' % emptyFile)
        # os.mknod(emptyFile)

    dest = 'channels-%s-%s' % (apk,version)
    if not os.path.exists(dest):
        os.mkdir(dest)

    file=open("channel.txt")
    count = 0
    for channel in file:
	    channel = channel.strip('\n')
	    print '----build channel [%s]' % channel
	    apkfile = '%s/%s-%s-%s.apk' % (dest,apk[:-4],channel,version)
	    shutil.copyfile(apk, apkfile)
            write_channel_to_apk(apkfile, channel)
            count += 1

    print '----finish build channels, channel count=%d----' % count

if __name__ == "__main__":
    build()
