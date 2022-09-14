from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_xpath("//*[@type='submit'][@value='Create New Project']")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def change_project_value(self, proj_field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(proj_field_name).click()
            wd.find_element_by_name(proj_field_name).clear()
            wd.find_element_by_name(proj_field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_project_value("name", project.projectName)
        self.change_project_value("description", project.description)

    def add(self, new_project_data):
        wd = self.app.wd
        self.project_page()
        # init proj creation
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        # fill proj form
        self.fill_project_form(new_project_data)
        # submit proj creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.project_page()
        return len(wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_page()
            self.project_cache = []
            for row in wd.find_elements_by_xpath("//table[@class='width100'][@cellspacing='1']"
                                                     "//tr[contains(@class,'row-')]"):
                    cells = row.find_elements_by_tag_name("td")
                    text = cells[0].text
                    description = cells[4].text
                    self.project_cache.append(Project(projectName=text, description=description))
            self.project_cache.pop(0)
            return list(self.project_cache)
