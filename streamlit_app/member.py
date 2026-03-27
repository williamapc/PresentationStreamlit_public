class Member:
    def __init__(
        self, name: str, linkedin_url: str = None, github_url: str = None
    ) -> None:
        self.name = name
        self.linkedin_url = linkedin_url
        self.github_url = github_url

    def sidebar_markdown(self):


        markdown = ('<b style=\"display: inline-block; vertical-align: middle; height: 100%\">{0}</b></br>'.format(self.name))

        #if self.linkedin_url is not None:
        #markdown += f'<a href= {self.linkedin_url} target="_blank"><img src="https://dst-studio-template.s3.eu-west-3.amazonaws.com/linkedin-logo-black.png" alt="linkedin" width="25" style="vertical-align: middle; margin-left: 5px"/></a> '

        #if self.github_url is not None:
        #markdown += (
            #  "<a href={0}<img src=\'https://dst-studio-template.s3.eu-west-3.amazonaws.com/github-logo.png\' alt=\'github\' width=\'20\' style=\'vertical-align: middle; margin-left: 5px\'/></a>".format(
             #      self.github_url))

        return markdown


