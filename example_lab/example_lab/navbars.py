from edc_navbar import NavbarItem, site_navbars, Navbar

lab = Navbar(name='lab')

lab.append_item(
    NavbarItem(name='lab',
               title='Lab',
               label='lab',
               fa_icon='fa-flask',
               url_name=f'edc_lab_dashboard:home_url'))

site_navbars.register(lab)
