# oggify.plugins.flac - FLAC decoder plugin for Oggify
# Copyright (c) 2008 Scott Paul Robertson (spr@scottr.org)
#
# This is part of Oggify (http://scottr.org/oggify/)
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from oggify import plugins
from tag_wrapper import tag
from subprocess import Popen, STDOUT
import os

class Codec(object):
    """Oggify FLAC Source Plugin. (default)
Using this plugin will scan the source directory tree for files ending in
.flac.  These files are then converted to the specified output format.

Requires "flac" to be on you $PATH. http://flac.sf.net"""

    extension = property(lambda s: "flac", doc="flac")

    def decode(self, source, dest, nice, stdout):
        os.unlink(dest)
        args = ["nice", "-n", str(nice), "flac", "--totally-silent", "-d",
                "-o", dest, source]
        p = Popen(args, stdout=stdout, stderr=STDOUT)
        return p

    def encode(self, dest, source, quality, nice, stdout):
        os.unlink(dest)
        args = ["nice", "-n", str(nice), "flac", "--totally-silent", "-o",
                dest, source]
        p = Popen(args, stdout=stdout, stderr=STDOUT)
        return p

    def set_tags(self, file, tags):
        flac_tag = tag(file)
        flac_tag.update(tags)
        flac_tag.save()

    def get_tags(self, file):
        return tag(file)
