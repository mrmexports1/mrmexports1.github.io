# Project root directory
PROJ_ROOT = '/Users/jayabal/git/exports/'
TEMPLATES = PROJ_ROOT + 'automation/templates/'
CONTENTS = PROJ_ROOT + 'automation/contents/'
PROJ_TITLE = 'MRM Exports'

# =================
# Site wide Common sections
# Content files
SITE_HEAD_FILE = CONTENTS + 'site_head.content'
#SITE_NAVIGATION_FILE = CONTENTS + 'site_navigation.content'
SITE_NAVIGATION_FILE = CONTENTS + 'site_navigation.content'
SITE_FOOTER_FILE = CONTENTS + 'site_footer.content'
GOOGLE_ANLYTICS_FILE = CONTENTS + 'google_analytics_init.content'

# =================
# Menu Navigation - generated for each page
# Default Nav menu schema
SITE_NAVIGATION_MENU_SCHEMA = 'site_nav_menu.schema'

# Nav menu templates
NAV_TMPLT_FILE = TEMPLATES + 'site_nav_menu.template'
NAV_MENU_DROPDN_TMPLT_FILE = TEMPLATES + 'site_nav_menu_dropdn.template'
NAV_MENU_DROPDN_ITEMS_TMPLT_FILE = TEMPLATES + 'site_nav_menu_dropdn_items.template'



# Nav menu content generated file
#SITE_NAVIGATION_FILE_GEN = SITE_NAVIGATION_FILE

# =================
# Product page specific

# Content files
PRODUCT_JSCRIPT_FILE = CONTENTS + 'prod_jscripts.content'

# Product page templates
PROD_HTML_TMPLT_FILE = TEMPLATES + 'prod.html.template'
SUBPROD_W_SIDEMENU_TMPLT_FILE = TEMPLATES + 'sub_prod_w_sidemenu.html.template'
SUBPROD_TMPLT_FILE = TEMPLATES + 'sub_prod.html.template'
SIDEPROD_MENU_TMPLT_FILE = TEMPLATES + 'sideprod_menu.html.template'

# =================
# Home page
# Content files
HOMEPAGE_CONTENT_FILE = CONTENTS + 'index.html.content'
HOMEPAGE_JSCRIPT_FILE =  CONTENTS + 'index_jscript.content'

# template files
HOMEPAGE_TEMPLATE = TEMPLATES + 'index.html.template'

# =================
# Contact us page
# Content files
CONTACT_CONTENT_FILE = CONTENTS + 'contact.html.content'
CONTACT_JSCRIPT_FILE =  CONTENTS + 'contact_jscript.content'

# template files
CONTACTPAGE_TEMPLATE = TEMPLATES + 'contact.html.template'
