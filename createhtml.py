import os
import re

kHomeFolderPath = 'S:/localSite'
kTemplateFilePath = 'template.html'
kTxtExtension = ".txt"
kFirstColumnMacro = "{FIRST_COLUMN}"
kSecondColumnMacro = "{SECOND_COLUMN}"
kTwoColumnsLayout = "<div class=\"row\"><div class=\"column\">" + kFirstColumnMacro + "</div><div class=\"column\">" + kSecondColumnMacro + "</div></div>"
kMaxLinksForOneColumn = 15


def create(path):
    fullpath = os.path.join(kHomeFolderPath, path)
    txtpath = fullpath + kTxtExtension

    if os.path.isfile(txtpath):
        content = createInfoPage(txtpath)
    elif os.path.isdir(fullpath):
        content = createLinksPage(fullpath)
    else:
        content = create404Page()

    return content


def createInfoPage(path):
    f = open(path, 'r')
    content = f.read()
    content = re.sub(r"(<img[^>]*>)", "</pre>\\1<pre>", content)

    return htmlWrap(content, getTitle(path))


def htmlWrap(content, title):
    templateFile = open(kTemplateFilePath, 'r')
    template = templateFile.read()

    template = template.replace("{CONTENT}", content)
    template = template.replace("{TITLE}", title)
    template = template.replace("{LINE}", "<hr><br>" if title else "")

    return template


def getTitle(path):
    return os.path.splitext(os.path.basename(path))[0]


def createLinksPage(path):
    filesList = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path,f)) or os.path.splitext(f)[1] == kTxtExtension]
    filesList = sorted(filesList)
    numOfLinksInColumn =  len(filesList) / 2 if len(filesList) > kMaxLinksForOneColumn * 2 else kMaxLinksForOneColumn

    links = ""
    firstColumn = ""

    for i in range(len(filesList)):
        url = createUrl(path, filesList[i])
        title = getTitle(filesList[i])
        links = links + "<p><a href=\"" + url + "\">" + title + "</a>"

        if i > numOfLinksInColumn and firstColumn == "":
            firstColumn = links
            links = ""

    layout = ""

    if firstColumn != "":
        layout = kTwoColumnsLayout.replace(kFirstColumnMacro, firstColumn).replace(kSecondColumnMacro, links)
    else:
        layout = links

    return htmlWrap(layout, getTitle(path))


def createUrl(path, relativePath):
    url = os.path.join(path, os.path.splitext(relativePath)[0])

    return url.replace(kHomeFolderPath, "")


def create404Page():
    return htmlWrap("Page not found", "404")