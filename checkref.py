# -*- coding: UTF-8 -*-
import requests
import time
import urllib.parse

def line():
    print(str())
    print(str())
    print(str())
    print(str())
    print(str())
    print(str())

def read(datalist,laststr):
    looped = 0
    people = 0
    for item in datalist:
        print(item[0],end="")
        space(29-(len(item[0])*2))
        print(item[1],end="")
        print()
        if looped != 0:
            people = people + 1
        else:
            print("-----------------------------†-----------------------------†------------------------------")
        looped = 1
    print("Total: " + str(people) + " " + str(laststr))

def space(times):
    for a in ['a']*times:
        print(" ",end="")
    print("|",end="")
times = int(input("How many times do you want to do? "))
if 4*times >= 1800:
    print("this will use over " + str(4*times) + " second(" + str(4*times//60) + " minute).")
    wait = input("Do you really want to start?(y/n) ")
    if wait != "y":
        print("Give up")
        exit(1)
times_list = ["x"]*times
main_list=[["Pagename","WebLink"]]
time_count = 0
for x in times_list :
    time_count = time_count + 1
    pagedata = requests.get("http://zh.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=1&format=json").json()
    pagetitle = pagedata["query"]["random"][0]["title"]
    print("Get No. " + str(time_count))
    print("pagetitle: " + pagetitle)
    PARAMS_GET = {
        "action":"query",
        "prop":"revisions",
        "titles":pagetitle,
        "rvslots":"*",
        "rvprop":"content",
        "formatversion":"2",
        "format":"json"
    }
    pagedatamain = requests.get("http://zh.wikipedia.org/w/api.php", params=PARAMS_GET).json()
    pagedatamaintext = pagedatamain["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
    if pagedatamaintext.find("</ref>") != -1 or pagedatamaintext.find("{{#tag:ref") != -1:
        print("finded ref")
    else:
        if pagedatamaintext.find("{{unreferenced") != -1 or pagedatamaintext.find("{{noref") != -1 or pagedatamaintext.find("{{Unreferenced") != -1 or pagedatamaintext.find("{{缺乏來源") != -1 or pagedatamaintext.find("{{No references") != -1 or pagedatamaintext.find("{{Noref") != -1 or pagedatamaintext.find("{{Unref") != -1 or pagedatamaintext.find("{{unref") != -1 or pagedatamaintext.find("{{unsourced") != -1 or pagedatamaintext.find("{{Unsorced") != -1 or pagedatamaintext.find("{{缺乏来源") != -1:
            print("finded noref template")
        else:
            if pagedatamaintext.find("{{disambig") != -1 or pagedatamaintext.find("{{Disambig") != -1 or pagedatamaintext.find("{{Disambiguation") != -1 or pagedatamaintext.find("{{disambiguation") != -1 or pagedatamaintext.find("{{disamb") != -1 or pagedatamaintext.find("{{Disamb") != -1 or pagedatamaintext.find("{{dab") != -1 or pagedatamaintext.find("{{dab") != -1 or pagedatamaintext.find("{{消歧義") != -1 or pagedatamaintext.find("{{消歧义") != -1:
                print("This is a dismbig page. ")
            else:
                if pagedatamaintext.find("{{BLP unsourced") != -1 or pagedatamaintext.find("{{bLP unsourced") != -1 or pagedatamaintext.find("{{生者傳記來源") != -1 or pagedatamaintext.find("{{BLP_unsourced") != -1 or pagedatamaintext.find("{{bLP_unsourced") != -1 or pagedatamaintext.find("{{生者传记来源") != -1:
                    print("finded noref template(BLP)")
                else:
                    if pagedatamaintext.find("{{No footnotes") != -1 or pagedatamaintext.find("{{no footnotes") != -1 or pagedatamaintext.find("{{No_footnotes") != -1 or pagedatamaintext.find("{{no_footnotes") != -1 or pagedatamaintext.find("{{Nofootnotes") != -1 or pagedatamaintext.find("{{nofootnotes") != -1 or pagedatamaintext.find("{{inline") != -1 or pagedatamaintext.find("{{Inline") != -1 or pagedatamaintext.find("{{缺乏腳註") != -1 or pagedatamaintext.find("{{缺乏註腳") != -1 or pagedatamaintext.find("{{缺乏脚注") != -1 or pagedatamaintext.find("{{缺乏注脚") != -1:
                        print("No footnote")
                    else:
                        if pagedatamaintext.find("{{Citation style") != -1 or pagedatamaintext.find("{{citation style") != -1 or pagedatamaintext.find("{{Citation_style") != -1 or pagedatamaintext.find("{{citation_style") != -1 or pagedatamaintext.find("{{citationstyle") != -1 or pagedatamaintext.find("{{Citationstyle") != -1 or pagedatamaintext.find("{{Citation-style") != -1 or pagedatamaintext.find("{{citation-style") != -1 or pagedatamaintext.find("{{Reference style") != -1 or pagedatamaintext.find("{{reference style") != -1 or pagedatamaintext.find("{{Reference_style") != -1 or pagedatamaintext.find("{{reference_style") != -1 or pagedatamaintext.find("{{來源清理") != -1 or pagedatamaintext.find("{{清理來源") != -1 or pagedatamaintext.find("{{来源清理") != -1 or pagedatamaintext.find("{{清理来源") != -1:
                            print("reference style clean")
                        else:
                            if pagedatamaintext.find("{{cite") != -1 or pagedatamaintext.find("{{Cite") != -1:
                                print("Not useing <ref> tag to tag the ref")
                            elif pagedatamaintext.find("{{FishBase") != -1 or pagedatamaintext.find("{{fishBase") != -1:
                                print("Not useing <ref> tag to tag the ref (Fishbase)")
                            elif pagedatamaintext.find("{{IUCN") != -1 or pagedatamaintext.find("{{iUCN") != -1:
                                print("Not useing <ref> tag to tag the ref (IUCN)")
                            elif pagedatamaintext.find("{{efn") != -1 or pagedatamaintext.find("{{Efn") != -1:
                                print("Not useing <ref> tag to tag the ref (Efn)")
                            elif pagedatamaintext.find("{{Citation") != -1 or pagedatamaintext.find("{{citation") != -1:
                                print("Not useing <ref> tag to tag the ref (Citation)")
                            else:
                                print("https://zhwp.org/" + pagetitle)
                                main_list = main_list + [[pagetitle,"https://zhwp.org/" + urllib.parse.quote(pagetitle)]]
    print("sleep for three second")
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        print()
        print("Paused by user")
        break
    print()
line()
print("List for founded noref page:")
read(main_list,"noref article")
