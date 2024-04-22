from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_content = toml.loads(content)
        print(toml_content)
        print("\n")

        tool_info = toml_content.get("tool", {})
        poetry_info = tool_info.get("poetry", {})
        group_info = poetry_info.get("group", {})
        dev_info = group_info.get("dev", {})

        name = poetry_info.get("name")
        desc = poetry_info.get("description")
        depe = poetry_info.get("dependencies")
        devp = dev_info.get("dependencies")
        lices = poetry_info.get("license")
        authors = poetry_info.get("authors")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, lices, authors, depe, devp)
