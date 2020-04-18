import os

kHomeFolderPath = 'S:/localSite'
kTemplateFilePath = 'template.html'
kTxtExtension = ".txt"


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
    content = replaceLineBreaks(content)

    return htmlWrap(content, getTitle(path))


def replaceLineBreaks(content):
    return content.replace("\n", "<p>\n")


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
    filesList = [f for f in os.listdir(path)]
    links = ""

    for f in filesList:
        if os.path.isdir(os.path.join(path,f)) or os.path.splitext(f)[1] == kTxtExtension:
            url = createUrl(path, f)
            title = getTitle(f)
            links = links + "<p><a href=\"" + url + "\">"+ title + "</a>"

    return htmlWrap(links, getTitle(path))


def createUrl(path, relativePath):
    url = os.path.join(path, os.path.splitext(relativePath)[0])

    return url.replace(kHomeFolderPath, "")


def create404Page():
    return htmlWrap("Page not found", "404")