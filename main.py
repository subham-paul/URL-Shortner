#import the necessary package
import pyshorteners as sh

link = ""  #enter URL here

s = sh.Shortener()

print(s.tinyurl.short(link))