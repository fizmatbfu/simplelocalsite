# simplelocalsite
Tool for creating simple text site in local network.

Requirements: Python 3.5+, Flask

Run: python server.py

Site will be available on your local network on port 5000 (can be changed in server.py).

Adding info: in createhtml.py specify folder for data (kHomeFolderPath). In this folder you can create .txt
 documents and folders (recursively). All documents and folders will be showed as links on main page. On click on link to text document will be showed page with info from this file (can use html tags in .txt  for formatting). On click on link to folder will be showed page with links to all documents and folders, which contain this folder.
Home folder can be shared (on network disk)
